# Revised VPORT Header Variables (DXF)

The following header variables existed before AutoCAD ®  Release 11 but now have independent settings for each active viewport. OPEN honors these variables when read from DXF™ files.
If a VPORT symbol table with \*ACTIVE entries is present (as is true for any DXF file produced by Release 11 or later), the
values in the VPORT table entries override the values of these header variables.

| Revised VPORT header variables | | |
| Variable | Group code | Description |
| $FASTZOOM | 70 | Fast zoom enabled if nonzero |
| $GRIDMODE | 70 | Grid mode on if nonzero |
| $GRIDUNIT | 10, 20 | Grid X and Y spacing |
| $SNAPANG | 50 | Snap grid rotation angle |
| $SNAPBASE | 10, 20 | Snap/grid base point (in UCS) |
| $SNAPISOPAIR | 70 | Isometric plane: 0 = Left; 1 = Top; 2 = Right |
| $SNAPMODE | 70 | Snap mode on if nonzero |
| $SNAPSTYLE | 70 | Snap style: 0 = Standard; 1 = Isometric |
| $SNAPUNIT | 10, 20 | Snap grid X and Y spacing |
| $VIEWCTR | 10, 20 | XY center of current view on screen |
| $VIEWDIR | 10, 20, 30 | Viewing direction (direction from target in WCS) |
| $VIEWSIZE | 40 | Height of view |

#### Related References

* [About the DXF HEADER Section](About-the-DXF-HEADER-Section.md)
* [HEADER Section Group Codes (DXF)](HEADER-Section-Group-Codes-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*