# ADR 0002: Modular design: mothership plus a detachable scout

- Date: 2026-11-23
- Status: accepted (owner chose option 1 on 2026-11-23)

## Context
The owner wants modular units that split apart to reach hard-to-reach spaces.
Most robot vacuums are about 9.5–10 cm tall and can't clean under low beds and
sofas, or between tight chair legs.

## Options considered
1. Mothership + 1 scout (recommended)
2. Mothership + 2 scouts
3. A swarm of identical small bots that join up
4. One robot with hand-swappable tool heads

## Decision
Option 1. A full mothership (LiDAR, big fan, big bin) carries one scout at most
6 cm tall that detaches for low and tight zones and docks back to charge.

## Consequences
- A signature feature that's easy to show in a video.
- Two firmwares and a link protocol to maintain (`software/robocume_link`).
- The scout can't see the LiDAR map under furniture, so it estimates its own
  position (encoders, IMU, optical flow). That needs testing in sim early.
