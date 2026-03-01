# UNDERLAY (DXF)

The following group codes apply to underlays.

Please note that UNDERLAY group codes are common to DGNUNDERLAY, DWFUNDERLAY, and PDFUNDERLAY. The differentiation between
DGNUNDERLAY, DWFUNDERLAY, and PDFUNDERLAY occurs in group code 0, defining the object name.

| Underlay group codes | |
| Group code | Description |
| 0 | Object name.   * DGNUNDERLAY - Attached DGN file * DWFUNDERLAY - Attached DWF file * PDFUNDERLAY - Attached PDF file |
| 100 | Subclass marker (AcDbUnderlayReference) |
| 340 | The ID of the AcDbUnderlayDefinition object |
| 10,20,30 | The *X*,*Y*, and *Z* coordinates of the insertion point of the underlay. These are OCS/ECS coordinates |
| 41,42,43 | DXF: *X*, *Y*, and *Z* scale factors |
| 50 | Rotation Angle (in OCS/ECS. CCW from the coordinate system *X* axis and around the *Z* axis) |
| 210,220,230 | Normal vector (in WCS) |
| 280 | Flags  1 = Clipping is on  2 = Underlay is on  4 = Monochrome  8 = Adjust for background  16 = Clip is inside mode |
| 281 | Contrast (value between 20 and 100) |
| 282 | Fade (value between 0 and 80) |
| 11, 21 | Repeating: 2d points in OCS/ECS. If only two, then they are the lower left and upper right corner points of a clip rectangle. If more than two, then they are the vertices of a clipping polygon |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*