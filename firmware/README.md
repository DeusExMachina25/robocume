# Firmware

| Folder | Chip | Language / toolchain |
|---|---|---|
| `mothership-io/` | RP2350 (Raspberry Pi Pico 2) | C++ with the Pico SDK, or Arduino via PlatformIO |
| `scout/` | ESP32-S3 | C++ with PlatformIO (Arduino or ESP-IDF framework) |

Both speak the frame format in [`software/robocume_link`](../software/robocume_link).
The Python version there is the reference: firmware ports must pass the same test
vectors.

Safety stops (bumper, cliff, wheel drop, link timeout) live here, not in ROS2.
