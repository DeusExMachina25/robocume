import pytest

from robocume_link import (
    Ack,
    Command,
    CommandCode,
    Heartbeat,
    ScoutState,
    Status,
    StreamDecoder,
    crc16_ccitt,
    decode,
    encode,
)
from robocume_link.frames import FrameError

MESSAGES = [
    Heartbeat(uptime_ms=123_456),
    Status(battery_mv=7_400, state=ScoutState.CLEANING, bin_full=True, docked=False),
    Command(CommandCode.CLEAN_ZONE, zone_id=3),
    Ack(acked_seq=9, ok=False),
]


def test_crc_known_value():
    # Standard check value for CRC-16/CCITT-FALSE.
    assert crc16_ccitt(b"123456789") == 0x29B1


@pytest.mark.parametrize("message", MESSAGES)
def test_round_trip(message):
    frame = decode(encode(message, seq=42))
    assert frame.seq == 42
    assert frame.message == message


def test_golden_bytes():
    # Firmware ports must produce exactly these bytes.
    assert encode(Command(CommandCode.UNDOCK, zone_id=0), seq=1).hex() == ("a55a011001030100009655")


def test_corrupted_byte_is_rejected():
    data = bytearray(encode(Heartbeat(1), seq=0))
    data[7] ^= 0xFF
    with pytest.raises(FrameError):
        decode(bytes(data))


def test_unknown_type_is_rejected():
    body = bytes([1, 0x55, 0, 0])
    data = b"\xa5\x5a" + body + crc16_ccitt(body).to_bytes(2, "little")
    with pytest.raises(FrameError):
        decode(data)


def test_seq_out_of_range():
    with pytest.raises(ValueError):
        encode(Heartbeat(1), seq=256)


def test_stream_decoder_handles_noise_and_split_chunks():
    stream = b"\x00\xa5\xff" + b"".join(encode(m, seq=i) for i, m in enumerate(MESSAGES))
    decoder = StreamDecoder()
    frames = []
    for i in range(0, len(stream), 3):  # feed 3 bytes at a time
        frames.extend(decoder.feed(stream[i : i + 3]))
    assert [f.message for f in frames] == MESSAGES
    assert [f.seq for f in frames] == [0, 1, 2, 3]


def test_stream_decoder_recovers_after_bad_frame():
    bad = bytearray(encode(Heartbeat(5), seq=0))
    bad[-1] ^= 0xFF
    good = encode(Heartbeat(6), seq=1)
    frames = list(StreamDecoder().feed(bytes(bad) + good))
    assert [f.message for f in frames] == [Heartbeat(6)]


def test_crc_matches_python_stdlib():
    # binascii.crc_hqx with init 0xFFFF is an independent CRC-16/CCITT-FALSE.
    import binascii

    data = bytes(range(64))
    assert crc16_ccitt(data) == binascii.crc_hqx(data, 0xFFFF)
