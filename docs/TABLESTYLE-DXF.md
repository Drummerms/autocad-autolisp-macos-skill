# TABLESTYLE (DXF)

The following group codes are used by TABLESTYLE objects.

| TABLESTYLE group codes | |
| Group code | Description |
| 0 | Object name (TABLESTYLE) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” (The persistent reactors group appears in all dictionaries except the main dictionary.) |
| 330 | Soft-pointer ID/handle to owner dictionary. For TABLESTYLE objects, this code is always the ACAD\_TABLESTYLE entry of the named object dictionary |
| 102 | End of persistent reactors group, always “}” |
| 100 | Subclass marker (AcDbTableStyle) |
| 280 | Version number:  0 = 2010 |
| 3 | Table style description (string; 255 characters maximum) |
| 70 | FlowDirection (integer):  0 = Down  1 = Up |
| 71 | Flags (bit-coded) |
| 40 | Horizontal cell margin (real; default = 0.06) |
| 41 | Vertical cell margin (real; default = 0.06) |
| 280 | Flag for whether the title is suppressed:  0 = Not suppressed  1 = Suppressed |
| 281 | Flag for whether the column heading is suppressed:  0 = Not suppressed  1 = Suppressed |
|  | *The following group codes are repeated for every cell in the table* |
| 7 | Text style name (string; default = STANDARD) |
| 140 | Text height (real) |
| 170 | Cell alignment (integer) |
| 62 | Text color (integer; default = BYBLOCK) |
| 63 | Cell fill color (integer; default = 7) |
| 283 | Flag for whether background color is enabled (default = 0):  0 = Disabled  1 = Enabled |
| 90 | Cell data type |
| 91 | Cell unit type |
| 274-279 | Lineweight associated with each border type of the cell (default = kLnWtByBlock) |
| 284-289 | Flag for visibility associated with each border type of the cell (default = 1):  0 = Invisible  1 = Visible |
| 64-69 | Color value associated with each border type of the cell (default = BYBLOCK) |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*