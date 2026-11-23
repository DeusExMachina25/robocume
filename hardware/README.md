# Hardware

Our own designs, licensed CERN-OHL-S-2.0 (see [ADR 0003](../docs/decisions/0003-licensing.md)).

| Folder | What goes here |
|---|---|
| `mothership/` | Chassis CAD (source + STEP + printable STL/3MF), bumper, brush and fan mounts, scout bay |
| `scout/` | Low-profile scout chassis, mini fan duct, bin, pogo-contact mount |
| `dock/` | Mothership charging dock (later: head rack for auto-swap) |
| `heads/` | Swappable cleaning heads and the standard head mount |
| [`BOM.md`](BOM.md) | Parts list and rough prices |

## Rules for CAD files
- Commit the **source** file (FreeCAD `.FCStd` or Onshape export link) and a
  **STEP** export, so anyone can edit it without your CAD tool.
- Put printable files in a `print/` subfolder with the print settings in a README
  (material, layer height, infill, supports).
- Name files `<part>-v<version>.<ext>`, e.g. `scout-shell-v0.2.step`.
- Big binary files: use Git LFS once we have them (`git lfs track "*.stl"`).
