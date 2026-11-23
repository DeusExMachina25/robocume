# robocume_link

How the mothership and the scout talk to each other. Pure Python, no
dependencies, so it runs on the Pi, on a laptop, and in tests. The firmware
versions (C++) must produce the same bytes.

## Frame layout (all numbers little-endian)

| Bytes | Field | Notes |
|---|---|---|
| 2 | start `A5 5A` | marks the beginning of a frame |
| 1 | version | protocol version, currently `1` |
| 1 | type | which message (see below) |
| 1 | seq | counter 0–255, used to match ACKs |
| 1 | length | payload size, 0–255 |
| n | payload | message body |
| 2 | CRC-16/CCITT-FALSE | over version..payload, catches corrupted bytes |

## Messages (v1)

| Type | Name | Payload |
|---|---|---|
| `0x01` | Heartbeat | `uptime_ms: u32` |
| `0x02` | Status | `battery_mv: u16, state: u8, flags: u8` (bit0 bin full, bit1 docked) |
| `0x10` | Command | `command: u8, zone_id: u16` |
| `0x7F` | Ack | `acked_seq: u8, ok: u8` |

## Use it

```python
from robocume_link import Command, CommandCode, StreamDecoder, encode

data = encode(Command(CommandCode.CLEAN_ZONE, zone_id=3), seq=7)
decoder = StreamDecoder()
for frame in decoder.feed(data):
    print(frame.seq, frame.message)
```

## Develop

```bash
cd software/robocume_link
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest && ruff check .
```
