"""Encode and decode robocume_link frames.

Frame: A5 5A | version | type | seq | length | payload | crc16 (little-endian).
The CRC (CRC-16/CCITT-FALSE) covers version through the end of the payload.
"""

from __future__ import annotations

import struct
from collections.abc import Iterator
from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar

PROTOCOL_VERSION = 1
START = b"\xa5\x5a"
HEADER_LEN = 6  # start(2) + version + type + seq + length
CRC_LEN = 2
MAX_PAYLOAD = 255


def crc16_ccitt(data: bytes, crc: int = 0xFFFF) -> int:
    """CRC-16/CCITT-FALSE: poly 0x1021, init 0xFFFF, no reflection, no final XOR."""
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) if crc & 0x8000 else (crc << 1)
            crc &= 0xFFFF
    return crc


class CommandCode(IntEnum):
    STOP = 0
    UNDOCK = 1
    CLEAN_ZONE = 2
    RETURN_HOME = 3


class ScoutState(IntEnum):
    DOCKED = 0
    UNDOCKING = 1
    CLEANING = 2
    RETURNING = 3
    STOPPED = 4
    ERROR = 5


@dataclass(frozen=True)
class Heartbeat:
    TYPE: ClassVar[int] = 0x01
    FORMAT: ClassVar[str] = "<I"
    uptime_ms: int

    def pack(self) -> bytes:
        return struct.pack(self.FORMAT, self.uptime_ms)

    @classmethod
    def unpack(cls, payload: bytes) -> Heartbeat:
        return cls(*struct.unpack(cls.FORMAT, payload))


@dataclass(frozen=True)
class Status:
    TYPE: ClassVar[int] = 0x02
    FORMAT: ClassVar[str] = "<HBB"
    battery_mv: int
    state: ScoutState
    bin_full: bool = False
    docked: bool = False

    def pack(self) -> bytes:
        flags = (1 if self.bin_full else 0) | (2 if self.docked else 0)
        return struct.pack(self.FORMAT, self.battery_mv, int(self.state), flags)

    @classmethod
    def unpack(cls, payload: bytes) -> Status:
        battery_mv, state, flags = struct.unpack(cls.FORMAT, payload)
        return cls(battery_mv, ScoutState(state), bool(flags & 1), bool(flags & 2))


@dataclass(frozen=True)
class Command:
    TYPE: ClassVar[int] = 0x10
    FORMAT: ClassVar[str] = "<BH"
    command: CommandCode
    zone_id: int = 0

    def pack(self) -> bytes:
        return struct.pack(self.FORMAT, int(self.command), self.zone_id)

    @classmethod
    def unpack(cls, payload: bytes) -> Command:
        command, zone_id = struct.unpack(cls.FORMAT, payload)
        return cls(CommandCode(command), zone_id)


@dataclass(frozen=True)
class Ack:
    TYPE: ClassVar[int] = 0x7F
    FORMAT: ClassVar[str] = "<BB"
    acked_seq: int
    ok: bool = True

    def pack(self) -> bytes:
        return struct.pack(self.FORMAT, self.acked_seq, 1 if self.ok else 0)

    @classmethod
    def unpack(cls, payload: bytes) -> Ack:
        acked_seq, ok = struct.unpack(cls.FORMAT, payload)
        return cls(acked_seq, bool(ok))


Message = Heartbeat | Status | Command | Ack
MESSAGE_TYPES: dict[int, type[Message]] = {m.TYPE: m for m in (Heartbeat, Status, Command, Ack)}


@dataclass(frozen=True)
class Frame:
    seq: int
    message: Message
    version: int = PROTOCOL_VERSION


class FrameError(ValueError):
    """Raised when a frame is malformed."""


def encode(message: Message, seq: int) -> bytes:
    """Turn a message into the bytes sent over the wire."""
    if not 0 <= seq <= 255:
        raise ValueError("seq must be 0-255")
    payload = message.pack()
    if len(payload) > MAX_PAYLOAD:
        raise ValueError("payload too long")
    body = bytes([PROTOCOL_VERSION, message.TYPE, seq, len(payload)]) + payload
    return START + body + struct.pack("<H", crc16_ccitt(body))


def decode(data: bytes) -> Frame:
    """Decode exactly one complete frame. Raises FrameError if it's invalid."""
    if len(data) < HEADER_LEN + CRC_LEN or data[:2] != START:
        raise FrameError("missing start bytes or too short")
    version, msg_type, seq, length = data[2:6]
    if len(data) != HEADER_LEN + length + CRC_LEN:
        raise FrameError("length mismatch")
    body = data[2 : HEADER_LEN + length]
    (crc,) = struct.unpack("<H", data[HEADER_LEN + length :])
    if crc != crc16_ccitt(body):
        raise FrameError("bad CRC")
    if version != PROTOCOL_VERSION:
        raise FrameError(f"unsupported protocol version {version}")
    cls = MESSAGE_TYPES.get(msg_type)
    if cls is None:
        raise FrameError(f"unknown message type 0x{msg_type:02x}")
    try:
        message = cls.unpack(data[HEADER_LEN : HEADER_LEN + length])
    except (struct.error, ValueError) as exc:
        raise FrameError(f"bad payload: {exc}") from exc
    return Frame(seq=seq, message=message, version=version)


class StreamDecoder:
    """Pulls frames out of a byte stream that may be split up or contain noise."""

    def __init__(self) -> None:
        self._buf = bytearray()
        self.errors = 0

    def feed(self, chunk: bytes) -> Iterator[Frame]:
        self._buf.extend(chunk)
        while True:
            start = self._buf.find(START)
            if start < 0:
                # Keep a trailing 0xA5 in case the next chunk starts with 0x5A.
                del self._buf[: max(0, len(self._buf) - 1)]
                return
            del self._buf[:start]
            if len(self._buf) < HEADER_LEN:
                return
            total = HEADER_LEN + self._buf[5] + CRC_LEN
            if len(self._buf) < total:
                return
            candidate = bytes(self._buf[:total])
            try:
                frame = decode(candidate)
            except FrameError:
                self.errors += 1
                del self._buf[:1]  # skip this start byte and search again
                continue
            del self._buf[:total]
            yield frame
