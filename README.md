# Robocume

**An open-source modular cleaning robot that splits up to reach where others can't.**

Robocume is two robots that work as one. A full-size **mothership** vacuum maps your
home with LiDAR and cleans the open floor. It carries a small **scout** (at most 6 cm
tall) that detaches to clean under beds, sofas and other tight spots, then drives
back to recharge.

> **Status:** planning and foundations (Phase 0). Not buildable yet.
> See the [roadmap](docs/ROADMAP.md).

## Highlights (planned)
- Mothership + detachable scout, coordinated automatically
- 2D LiDAR mapping and navigation (ROS2 Jazzy, Nav2, slam_toolbox)
- 3D-printable bodies, parts you can buy in India and worldwide
- Works fully offline; Home Assistant integration; web dashboard
- Raspberry Pi 5 + RP2350 on the mothership, ESP32-S3 on the scout

## Repository map
| Folder | What's inside |
|---|---|
| [`docs/`](docs) | Architecture, roadmap, decisions, handoff notes, changelog |
| [`hardware/`](hardware) | CAD and print files, [bill of materials](hardware/BOM.md) |
| [`firmware/`](firmware) | Microcontroller code for mothership I/O and scout |
| [`ros2_ws/`](ros2_ws/src) | ROS2 packages: models, sim, navigation, coordinator |
| [`software/robocume_link`](software/robocume_link) | Mothership-to-scout message format (tested) |
| [`web/`](web) | Dashboard |

## Get started
- Developers: [docs/DEV_SETUP.md](docs/DEV_SETUP.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- Where things stand: [docs/HANDOFF.md](docs/HANDOFF.md)

## License
Code and firmware: [Apache-2.0](LICENSE). Hardware: CERN-OHL-S-2.0. Docs: CC BY-SA 4.0.
The Robocume name and logo are not covered by these licenses.
See [ADR 0003](docs/decisions/0003-licensing.md) and [NOTICE](NOTICE).
