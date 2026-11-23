# Robocume roadmap

Phases are in order. Each one ends with something you can show (a demo video,
a release tag), which doubles as marketing content (see [BUSINESS.md](BUSINESS.md)).

## Phase 0: Foundations (now)
- [x] Repo, licenses, docs, CI, contribution workflow
- [x] Architecture and key decisions written down
- [x] `robocume_link` mother–scout message format with tests
- [ ] Dev environment that fits an 8 GB laptop (Docker + headless Gazebo)

## Phase 1: MVP in simulation
- [ ] `robocume_description`: URDF models of mothership and scout
- [ ] Gazebo world with a bed and sofa the mothership can't fit under
- [ ] Mothership maps the room (slam_toolbox) and navigates (Nav2)
- [ ] Coverage cleaning of open floor
- [ ] Low-zone detection on the map
- [ ] Scout mission: undock, clean low zone, return, dock (the signature demo)
- [ ] Web dashboard: live map, start/stop/home, scout status

## Phase 2: MVP hardware (first real robots)
- [ ] Scout v1 printed and driving (cheapest part, build it first)
- [ ] Mothership v1 chassis with Roborock spare wheels, brush, fan
- [ ] RP2350 I/O board on a breadboard, then a custom PCB
- [ ] Scout bay with ramp and pogo-pin charging
- [ ] Same software from Phase 1 running on the real robots
- [ ] Home Assistant integration (start, stop, battery, status)

## After the MVP
- Auto-empty the scout's bin into the mothership
- Charging dock for the mothership, with auto-empty
- Room and zone cleaning, schedules, no-go zones
- Phone app (PWA first: one web codebase, no app-store fees)
- Camera obstacle avoidance (cables, socks, pet mess)
- Mopping module
- Second scout, or a corner/edge scout
- Optional cloud dashboard for fleets (schools, offices, rentals)
- Voice control through Home Assistant
