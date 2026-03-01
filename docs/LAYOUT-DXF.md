# LAYOUT (DXF)

The following group codes are used by LAYOUT objects.

| LAYOUT group codes | |
| Group code | Description |
| 0 | Object name (LAYOUT) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group, always “}” |
| 330 | Soft-pointer ID/handle to owner object |
| 100 | Subclass marker (AcDbPlotSettings) |
| *plotsettings object group codes* | For group codes and descriptions following the AcDbPlotSettings marker, see PLOTSETTINGS |
| 100 | Subclass marker (AcDbLayout) |
| 1 | Layout name |
| 70 | Flag (bit-coded) to control the following:  1 = Indicates the PSLTSCALE value for this layout when this layout is current  2 = Indicates the LIMCHECK value for this layout when this layout is current |
| 71 | Tab order. This number is an ordinal indicating this layout's ordering in the tab control that is attached to the drawing window. Note that the “Model” tab always appears as the first tab regardless of its tab order |
| 10 | Minimum limits for this layout (defined by LIMMIN while this layout is current)  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of minimum limits |
| 11 | Maximum limits for this layout (defined by LIMMAX while this layout is current):  DXF: *X* value; APP: 2D point |
| 21 | DXF: *Y* value of maximum limits |
| 12 | Insertion base point for this layout (defined by INSBASE while this layout is current):  DXF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of the insertion base point |
| 14 | Minimum extents for this layout (defined by EXTMIN while this layout is current):  DXF: *X* value; APP: 3D point |
| 24, 34 | DXF: *Y* and *Z* values of the minimum extents |
| 15 | Maximum extents for this layout (defined by EXTMAX while this layout is current):  DXF: *X* value; APP: 3D point |
| 25, 35 | DXF: *Y* and *Z* values of the maximum extents |
| 146 | Elevation |
| 13 | UCS origin  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z*values of UCS origin |
| 16 | UCS *X*-axis  DXF: *X* value; APP: 3D vector |
| 26, 36 | DXF: *Y* and *Z*values of UCS *X*-axis |
| 17 | UCS *Y* axis  DXF: *X* value; APP: 3D vector |
| 27, 37 | DXF: *Y* and *Z*values of UCS *Y* axis |
| 76 | Orthographic type of UCS  0 = UCS is not orthographic  1 = Top; 2 = Bottom  3 = Front; 4 = Back  5 = Left; 6 = Right |
| 330 | ID/handle to this layout's associated paper space block table record |
| 331 | ID/handle to the viewport that was last active in this layout when the layout was current |
| 345 | ID/handle of AcDbUCSTableRecord if UCS is a named UCS. If not present, then UCS is unnamed |
| 346 | ID/handle of AcDbUCSTableRecord of base UCS if UCS is orthographic (76 code is non-zero). If not present and 76 code is non-zero, then base UCS is taken to be WORLD |
| 333 | Shade plot ID |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [PLOTSETTINGS (DXF)](PLOTSETTINGS-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*