# Handoff notes

Read this first if you're picking up the work (human or AI agent).

_Last updated: 2026-11-23_

## What Robocume is
An original open-source modular robot vacuum: a LiDAR **mothership** that carries
a small detachable **scout** for low, tight spaces. Goals: a portfolio piece and a
product to sell worldwide at low cost. Inspired by, but not copied from,
[makerspet/oomwoo](https://github.com/makerspet/oomwoo) (see ADR 0001).

## Where things stand
- Phase 0 (foundations) nearly done. See `docs/ROADMAP.md`.
- Only working code: `software/robocume_link` (tested message format).
- Hardware, firmware, ROS2 and web folders are placeholders with plans.

## Decisions made
- Fresh repo, own design (ADR 0001).
- Mothership + 1 scout (ADR 0002, still **proposed**: waiting for the owner's pick).
- Licenses (ADR 0003).
- Owner has a 3D printer, a reasonable budget, and an 8 GB RAM laptop.

## Open questions
- Owner's laptop OS (decides Docker vs native vs WSL2 setup).
- Confirm the modular design option (ADR 0002).

## Next steps
1. Docker dev image with ROS2 Jazzy + Gazebo Harmonic that fits 8 GB.
2. `robocume_description`: URDF for mothership and scout.
3. Gazebo world with a low bed and sofa.
4. In parallel, the owner can print and wire scout v0 (see `hardware/BOM.md`).

## How to work here
Branch, small commits, PR, CI green, update this file and `CHANGELOG.md`.
See `CONTRIBUTING.md`.
