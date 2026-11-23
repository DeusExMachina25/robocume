# ADR 0004: Interchangeable cleaning heads, swapped at the dock

- Date: 2026-11-23
- Status: accepted

## Context
The owner wants interchangeable heads that swap at the dock. Different floors
and jobs need different tools: a bristle brush for carpet, a rubber roller for
pet hair, a mop pad for hard floors.

## Decision
Build it in two steps.

**MVP: one standard head mount, swapped by hand.**
- Every head clicks into the same slot under the mothership (guide rails + magnets
  or a spring latch, no screws).
- An electrical connector of pogo pins gives the head motor power and an **ID**:
  each head carries a resistor of a different value (later a tiny EEPROM chip), so
  the RP2350 knows which head is fitted and picks the right motor speed and suction.
- MVP heads: bristle brush roll, rubber roller.

**After the MVP: automatic swapping at the dock.**
- The dock gets a head rack with slots.
- The mothership reverses into a free slot, a latch in the dock releases the
  current head, the robot moves to the next slot and picks up the new head.
- The coordinator chooses heads per room (carpet vs tile, from the map) or per job.
- More heads: mop pad module (with water tank), deep-carpet brush, edge/corner brush.

## Consequences
- Designing the mount now means auto-swap later doesn't need a new chassis.
- The head slot must stay in the same place and shape across versions: it's an
  interface, like a software API. Changes bump a "head mount version".
- Extra money angle: sell heads separately (cheap to print, repeat purchases).
- The scout keeps a fixed head for now; a scout head mount is a later option.
