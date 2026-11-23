# ADR 0001: Start fresh instead of forking oomwoo

- Date: 2026-11-23
- Status: accepted

## Context
[makerspet/oomwoo](https://github.com/makerspet/oomwoo) is an open-source DIY
robot vacuum (Apache-2.0 code, hardware license not decided yet). It's early:
simulation only, no buildable hardware. Its makers plan to sell their own kits.

## Decision
Robocume is a new repository with its own design. We study oomwoo as prior art
but do not copy its CAD, PCB or branding. If we ever reuse Apache-2.0 code from
it, we keep its license header and credit it in `NOTICE`.

## Consequences
- The product is clearly ours to brand and sell.
- We don't get oomwoo's updates for free; we can still read them.
- More design work, but it's the work that makes Robocume different.
