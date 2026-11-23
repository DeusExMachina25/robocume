# Bill of materials (first rough estimate)

Rough Indian retail prices in ₹, 2026-11, for one unit. **These are guesses to check
before buying**, not quotes. Sources: Robu.in, Robocraze, Amazon.in, AliExpress.

## Scout (build first)
| Part | Qty | ~₹ | Notes |
|---|---|---|---|
| ESP32-S3 dev board (small) | 1 | 700 | Wi-Fi + enough pins |
| N20 gear motor with encoder | 2 | 800 | Drive wheels |
| DRV8833 motor driver | 1 | 150 | |
| VL53L1X ToF distance sensor | 3 | 1,200 | Front, left, right |
| PMW3901 optical-flow sensor | 1 | 1,200 | Position under furniture |
| IMU (e.g. BMI270 / MPU6050) | 1 | 300 | |
| Mini fan (coreless / 7.4 V) | 1 | 600 | Suction |
| 2S Li-ion (2× 18650) + BMS | 1 | 800 | |
| Pogo pins + magnets | 1 set | 300 | Charging contacts |
| Cliff IR sensors (TCRT5000) | 2 | 100 | |
| Filament (PETG) | ~150 g | 300 | |
| **Scout total** | | **~6,450** | |

## Mothership
| Part | Qty | ~₹ | Notes |
|---|---|---|---|
| Raspberry Pi 5 (4 GB) | 1 | 6,500 | Main computer |
| Raspberry Pi Pico 2 (RP2350) | 1 | 600 | I/O and safety |
| 2D LiDAR (used vacuum LDS or LD19) | 1 | 2,500–7,000 | Used vacuum LiDARs are cheapest |
| Roborock-compatible drive wheel pair | 1 | 3,000 | Motor, encoder, suspension, wheel-drop switch |
| Motor drivers (TB6612 / DRV8871) | 2 | 400 | |
| Suction fan (spare part) | 1 | 1,500 | |
| Main brush + motor | 1 | 1,500 | |
| 4S Li-ion pack + BMS | 1 | 3,000 | |
| Bumper switches, cliff sensors, IMU | 1 set | 800 | |
| IR LEDs for scout homing beacon | 1 set | 200 | |
| Filament (PETG) | ~1 kg | 1,500 | |
| Wiring, connectors, screws | | 1,500 | |
| **Mothership total** | | **~23,000–27,500** | |

**Both robots: roughly ₹30,000–34,000** for the first prototype. Kit prices drop with
batches of 10 and PCBs instead of breadboards.
