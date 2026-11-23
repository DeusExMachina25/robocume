# ADR 0003: Licenses

- Date: 2026-11-23
- Status: accepted (can change before the first public release)

## Decision
| What | License | Why |
|---|---|---|
| Software and firmware | Apache-2.0 | Permissive, allows selling, protects against patent claims, works with ROS2 |
| Hardware (CAD, PCB) | CERN-OHL-S-2.0 | Anyone who sells a modified copy must share their changes, which makes closed clones less attractive |
| Docs, images, videos | CC BY-SA 4.0 | Credit required, changes shared alike |
| Name and logo | Not licensed | "Robocume" is the brand; plan to register the trademark |

The full CERN-OHL-S and CC BY-SA texts are added to `hardware/` and `docs/` with
the first design files.
