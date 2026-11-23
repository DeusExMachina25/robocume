# Changelog

All notable changes are listed here. Format: [Keep a Changelog](https://keepachangelog.com/),
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Project foundation: README, licenses (Apache-2.0 code, CERN-OHL-S-2.0 hardware), NOTICE.
- Architecture for the mothership + detachable scout design (`docs/ARCHITECTURE.md`).
- Roadmap with MVP and later features (`docs/ROADMAP.md`).
- Money-making plan (`docs/BUSINESS.md`).
- Decision records 0001 (fresh repo), 0002 (mothership + scout), 0003 (licenses).
- Rough bill of materials in ₹ (`hardware/BOM.md`).
- Folder layout for hardware, firmware, ROS2 and web, with READMEs.
- `robocume_link` v0.1.0: mothership–scout frame format with CRC, stream
  decoder and 12 tests.
- Interchangeable cleaning heads (ADR 0004): standard head mount with head ID in the
  MVP, automatic swapping at the dock after the MVP. Architecture, roadmap and
  business plan updated.
- CI (ruff + pytest on Python 3.10 and 3.12, required docs check), PR and issue templates.
