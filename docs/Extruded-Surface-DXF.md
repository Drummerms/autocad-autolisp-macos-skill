# Extruded Surface (DXF)

The following group codes apply to extruded surfaces.

| Extruded Surface group codes | |
| Group code | Description |
| 100 | Subclass markar (AcDbExtrudedSurface) |
| 90 | Class ID |
| 90 | Size of binary data |
| 310 | Binary data |
| 10, 20, 30 | Sweep vector |
| 40 | Transform matrix of extruded entity (16 reals; row major format; default = identity matrix) |
| 42 | Draft angle (in radians) |
| 43 | Draft start distance |
| 44 | Draft end distance |
| 45 | Twist angle |
| 48 | Scale factor |
| 49 | Align angle (in radians) |
| 46 | Transform matrix of sweep entity (16 reals; row major format; default = identity matrix) |
| 47 | Transform matrix of path entity (16 reals; row major format; default = identity matrix) |
| 290 | Solid flag |
| 70 | Sweep alignment option  0 = No alignment  1 = Align sweep entity to path  2 = Translate sweep entity to path  3 = Translate path to sweep entity |
| 292 | Align start flag |
| 293 | Bank flag |
| 294 | Base point set flag |
| 295 | Sweep entity transform computed flag |
| 296 | Path entity transform computed flag |
| 11, 21, 31 | Reference vector for controlling twist |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [SURFACE (DXF)](SURFACE-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*