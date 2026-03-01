# HATCH (DXF)

The following group codes apply to hatch and MPolygon entities.

| Hatch group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbHatch) |
| 10 | Elevation point (in OCS)  DXF: *X* value = 0; APP: 3D point (*X* and *Y* always equal 0, *Z* represents the elevation) |
| 20, 30 | DXF: *Y* and *Z* values of elevation point (in OCS)  *Y* value = 0, *Z* represents the elevation |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction |
| 2 | Hatch pattern name |
| 70 | Solid fill flag (0 = pattern fill; 1 = solid fill); for MPolygon, the version of MPolygon |
| 63 | For MPolygon, pattern fill color as the ACI |
| 71 | Associativity flag (0 = non-associative; 1 = associative); for MPolygon, solid-fill flag (0 = lacks solid fill; 1 = has solid fill) |
| 91 | Number of boundary paths (loops) |
| *varies* | Boundary path data. Repeats number of times specified by code 91. See Boundary Path Data |
| 75 | Hatch style:  0 = Hatch “odd parity” area (Normal style)  1 = Hatch outermost area only (Outer style)  2 = Hatch through entire area (Ignore style) |
| 76 | Hatch pattern type:  0 = User-defined  1 = Predefined  2 = Custom |
| 52 | Hatch pattern angle (pattern fill only) |
| 41 | Hatch pattern scale or spacing (pattern fill only) |
| 73 | For MPolygon, boundary annotation flag:  0 = boundary is not an annotated boundary  1 = boundary is an annotated boundary |
| 77 | Hatch pattern double flag (pattern fill only):  0 = not double  1 = double |
| 78 | Number of pattern definition lines |
| *varies* | Pattern line data. Repeats number of times specified by code 78. See Pattern Data |
| 47 | Pixel size used to determine the density to perform various intersection and ray casting operations in hatch pattern computation for associative hatches and hatches created with the Flood method of hatching |
| 98 | Number of seed points |
| 11 | For MPolygon, offset vector |
| 99 | For MPolygon, number of degenerate boundary paths (loops), where a degenerate boundary path is a border that is ignored by the hatch |
| 10 | Seed point (in OCS)  DXF: *X* value; APP: 2D point (multiple entries) |
| 20 | DXF: *Y* value of seed point (in OCS); (multiple entries) |
| 450 | Indicates solid hatch or gradient; if solid hatch, the values for the remaining codes are ignored but must be present. Optional; if code 450 is in the file, then the following codes must be in the file: 451, 452, 453, 460, 461, 462, and 470. If code 450 is not in the file, then the following codes must not be in the file: 451, 452, 453, 460, 461, 462, and 470  0 = Solid hatch  1 = Gradient |
| 451 | Zero is reserved for future use |
| 452 | Records how colors were defined and is used only by dialog code:  0 = Two-color gradient  1 = Single-color gradient |
| 453 | Number of colors:  0 = Solid hatch  2 = Gradient |
| 460 | Rotation angle in radians for gradients (default = 0, 0) |
| 461 | Gradient definition; corresponds to the Centered option on the Gradient Tab of the Boundary Hatch and Fill dialog box. Each gradient has two definitions, shifted and non-shifted. A Shift value describes the blend of the two definitions that should be used. A value of 0.0 means only the non-shifted version should be used, and a value of 1.0 means that only the shifted version should be used. |
| 462 | Color tint value used by dialog code (default = 0, 0; range is 0.0 to 1.0). The color tint value is a gradient color and controls the degree of tint in the dialog when the Hatch group code 452 is set to 1. |
| 463 | Reserved for future use:  0 = First value  1 = Second value |
| 470 | String (default = LINEAR) |

#### Topics in this section

* [Boundary Path Data (DXF)](Boundary-Path-Data-DXF.md)
* [Pattern Data (DXF)](Pattern-Data-DXF.md)

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [Boundary Path Data (DXF)](Boundary-Path-Data-DXF.md)
* [Pattern Data (DXF)](Pattern-Data-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*