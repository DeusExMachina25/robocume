# Robocume architecture

> Status: draft v0.1 (2026-11-23). This is the contract every module agrees to.
> Anything marked **TBD** is an open decision, tracked in `docs/decisions/`.

## 1. The idea in one paragraph

Robocume is two robots that work as one. The **mothership** is a full-size robot
vacuum: it maps the home with a LiDAR, does the open-floor cleaning, and carries
a small **scout** in a bay at its back. When the map shows a space too low or too
tight for the mothership (under a bed, a sofa, between chair legs), the mothership
parks at the edge, the scout drives out, cleans that pocket, and comes back to
recharge and empty its tiny bin. See [ADR 0002](decisions/0002-mothership-and-scout.md).

## 2. Design principles

- **Ours, from scratch.** Our own CAD, PCBs and firmware. We use open-source
  libraries (ROS2, Nav2, slam_toolbox) as dependencies, and credit any reused
  code in `NOTICE`.
- **Simulation first.** Every behaviour runs in Gazebo before it runs on hardware,
  so work can continue without parts.
- **Cheap parts that are easy to buy in India and worldwide.** Raspberry Pi,
  RP2350 (Pico 2), ESP32-S3, common motor drivers and Roborock spare parts.
- **Safety in the microcontroller.** Bumper, cliff and wheel-drop stops run on
  the small chips, never only in Linux, so a crashed Pi can't drive off stairs.
- **Swappable modules.** Each part talks through a published interface (§5), so
  any part can be redesigned without breaking the others.
- **Local first.** Works without the cloud. Cloud features are optional add-ons.

## 3. System overview

```
                       ┌───────────────────────────── MOTHERSHIP ─────────────────────────────┐
  Web dashboard  ◀──▶  │  Raspberry Pi 5 (Ubuntu 24.04, ROS2 Jazzy)                           │
  Home Assistant ◀──▶  │   SLAM (slam_toolbox) · Nav2 · coverage planner · mission coordinator │
                       │        │ USB serial                      │ Wi-Fi (UDP, robocume_link) │
                       │  RP2350 I/O board                        │                            │
                       │   wheels · brush · fan · bumper · cliff  │                            │
                       │   battery · SAFETY STOPS                 │                            │
                       │  Scout bay: ramp · pogo charging pins · IR homing beacon · empty port │
                       └──────────────────────────────────────────┼────────────────────────────┘
                                                                  │
                       ┌──────────────────────── SCOUT (≤ 6 cm tall) ──────────────────────────┐
                       │  ESP32-S3: 2 N20 encoder motors · 3 ToF sensors · optical-flow sensor │
                       │  IMU · mini fan + bin · 2S battery · cliff sensors · SAFETY STOPS     │
                       └───────────────────────────────────────────────────────────────────────┘
```

## 4. Modules

| Module | Folder | Runs on | Job |
|---|---|---|---|
| Mothership chassis + mechanics | `hardware/mothership` | 3D printed | Body, bumper, brush, fan, bin, scout bay |
| Scout chassis + mechanics | `hardware/scout` | 3D printed | Low-profile body, mini fan, bin, pogo contacts |
| Charging dock | `hardware/dock` | 3D printed + PCB | Charges the mothership (scout charges inside it) |
| Mothership I/O firmware | `firmware/mothership-io` | RP2350 | Motors, sensors, safety, battery |
| Scout firmware | `firmware/scout` | ESP32-S3 | Drive, sensing, safety, `robocume_link` client |
| ROS2 packages | `ros2_ws/src` | Pi 5 / laptop | Description, sim, bringup, navigation, coordinator |
| Mother–scout link | `software/robocume_link` | Pi + ESP32 | Message format between the two robots |
| Web dashboard | `web` | Browser | Map, start/stop, scout status |

## 5. Interfaces (the contracts)

1. **Mother ↔ scout:** `robocume_link` frames over Wi-Fi UDP (ESP-NOW is a later
   option). Defined and tested in `software/robocume_link`. Versioned: any breaking
   change bumps the protocol version byte.
2. **Pi ↔ RP2350 I/O board:** serial frames using the same framing as
   `robocume_link` (one parser to learn). **TBD:** message list.
3. **ROS2 topics:** standard where possible (`/cmd_vel`, `/scan`, `/odom`, `/map`,
   `/battery_state`). Scout topics live under `/scout/...`. **TBD:** full list in
   `ros2_ws/src/README.md`.
4. **Dashboard ↔ robot:** rosbridge WebSocket in the MVP. **TBD:** REST API later.

## 6. How a scout mission works

1. The mothership finishes mapping and marks "low zones" (places the LiDAR sees
   but its body can't enter).
2. The coordinator picks a zone, drives the mothership to its edge and faces it.
3. The scout undocks down the ramp and gets the zone's outline and a start pose.
4. Under furniture the scout can't use the mothership's LiDAR, so it estimates its
   position from wheel encoders, IMU and the optical-flow sensor, and uses ToF
   sensors to avoid legs and walls. It cleans in a boustrophedon (back-and-forth) pattern.
5. When the zone is done, its battery is low, or the link is lost for too long,
   it drives back toward the mothership's IR beacon and climbs into the bay.
6. While docked it charges through pogo pins. (Later: the mothership's fan
   empties the scout's bin through an aligned port.)

## 7. Safety rules

- Each robot's microcontroller stops its motors on bumper, cliff or wheel drop,
  with no help from the Pi.
- The scout stops if it hears nothing from the mothership for 2 s while
  driving, then starts its return-home routine.
- Battery packs have a BMS with over-current, over-discharge and temperature
  protection. Charging circuits get a safety review before anyone builds them.

## 8. Open decisions

- Mothership I/O chip: RP2350 (current pick, cheap and easy) vs STM32.
- Scout position tracking accuracy under furniture: needs testing in sim.
- Auto-emptying the scout into the mothership: post-MVP.
