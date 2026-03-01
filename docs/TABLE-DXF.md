# TABLE (DXF)

The following group codes apply to table entities.

| Table group codes | |
| Group code | Description |
| 0 | Entity name (ACAD\_TABLE) |
| 5 | Entity handle |
| 330 | Soft-pointer ID to the owner dictionary |
| 100 | Subclass marker. (AcDbEntity) |
| 92 | Number of bytes in the proxy entity graphics |
| 310 | Data for proxy entity graphics (multiple lines; 256-character maximum per line) |
| 100 | Subclass marker. (AcDbBlockReference) |
| 2 | Block name; an anonymous block begins with a \*T value |
| 10,20,30 | Insertion point |
| 100 | Subclass marker. (AcDbTable) |
| 280 | Table data version number:  0 = 2010 |
| 342 | Hard pointer ID of the TABLESTYLE object |
| 343 | Hard pointer ID of the owning BLOCK record |
| 11,21,31 | Horizontal direction vector |
| 90 | Flag for table value (unsigned integer) |
| 91 | Number of rows |
| 92 | Number of columns |
| 93 | Flag for an override |
| 94 | Flag for an override of border color |
| 95 | Flag for an override of border lineweight |
| 96 | Flag for an override of border visibility |
| 141 | Row height; this value is repeated, 1 value per row |
| 142 | Column height; this value is repeated, 1 value per column |
| 171 | Cell type; this value is repeated, 1 value per cell:  1 = text type  2 = block type |
| 172 | Cell flag value; this value is repeated, 1 value per cell |
| 173 | Cell merged value; this value is repeated, 1 value per cell |
| 174 | Boolean flag indicating if the autofit option is set for the cell; this value is repeated, 1 value per cell |
| 175 | Cell border width (applicable only for merged cells); this value is repeated, 1 value per cell |
| 176 | Cell border height ( applicable for merged cells); this value is repeated, 1 value per cell |
| 91 | Cell override flag; this value is repeated, 1 value per cell (from AutoCAD 2007) |
| 178 | Flag value for a virtual edge |
| 145 | Rotation value (real; applicable for a block-type cell and a text-type cell) |
| 344 | Hard pointer ID of the FIELD object. This applies only to a text-type cell. If the text in the cell contains one or more fields, only the ID of the FIELD object is saved. The text string (group codes 1 and 3) is ignored |
| 1 | Text string in a cell. If the string is shorter than 250 characters, all characters appear in code 1. If the string is longer than 250 characters, it is divided into chunks of 250 characters. The chunks are contained in one or more code 2 codes. If code 2 codes are used, the last group is a code 1 and is shorter than 250 characters. This value applies only to text-type cells and is repeated, 1 value per cell |
| 2 | Text string in a cell, in 250-character chunks; optional. This value applies only to text-type cells and is repeated, 1 value per cell |
| 340 | Hard-pointer ID of the block table record. This value applies only to block-type cells and is repeated, 1 value per cell |
| 144 | Block scale (real). This value applies only to block-type cells and is repeated, 1 value per cell |
| 179 | Number of attribute definitions in the block table record (applicable only to a block-type cell) |
| 331 | Soft pointer ID of the attribute definition in the block table record, referenced by group code 179 (applicable only for a block-type cell). This value is repeated once per attribute definition |
| 300 | Text string value for an attribute definition, repeated once per attribute definition and applicable only for a block-type cell |
| 7 | Text style name (string); override applied at the cell level |
| 140 | Text height value; override applied at the cell level |
| 170 | Cell alignment value; override applied at the cell level |
| 64 | Value for the color of cell content; override applied at the cell level |
| 63 | Value for the background (fill) color of cell content; override applied at the cell level |
| 69 | True color value for the top border of the cell; override applied at the cell level |
| 65 | True color value for the right border of the cell; override applied at the cell level |
| 66 | True color value for the bottom border of the cell; override applied at the cell level |
| 68 | True color value for the left border of the cell; override applied at the cell level |
| 279 | Lineweight for the top border of the cell; override applied at the cell level |
| 275 | Lineweight for the right border of the cell; override applied at the cell level |
| 276 | Lineweight for the bottom border of the cell; override applied at the cell level |
| 278 | Lineweight for the left border of the cell; override applied at the cell level |
| 283 | Boolean flag for whether the fill color is on; override applied at the cell level |
| 289 | Boolean flag for the visibility of the top border of the cell; override applied at the cell level |
| 285 | Boolean flag for the visibility of the right border of the cell; override applied at the cell level |
| 286 | Boolean flag for the visibility of the bottom border of the cell; override applied at the cell level |
| 288 | Boolean flag for the visibility of the left border of the cell; override applied at the cell level |
| 70 | Flow direction; override applied at the table entity level |
| 40 | Horizontal cell margin; override applied at the table entity level |
| 41 | Vertical cell margin; override applied at the table entity level |
| 280 | Flag for whether the title is suppressed; override applied at the table entity level |
| 281 | Flag for whether the header row is suppressed; override applied at the table entity level |
| 7 | Text style name (string); override applied at the table entity level. There may be one entry for each cell type |
| 140 | Text height (real); override applied at the table entity level. There may be one entry for each cell type |
| 170 | Cell alignment (integer); override applied at the table entity level. There may be one entry for each cell type |
| 63 | Color value for cell background or for the vertical, left border of the table; override applied at the table entity level. There may be one entry for each cell type |
| 64 | Color value for cell content or for the horizontal, top border of the table; override applied at the table entity level. There may be one entry for each cell type |
| 65 | Color value for the horizontal, inside border lines; override applied at the table entity level |
| 66 | Color value for the horizontal, bottom border lines; override applied at the table entity level |
| 68 | Color value for the vertical, inside border lines; override applied at the table entity level |
| 69 | Color value for the vertical, right border lines; override applied at the table entity level |
| 283 | Flag for whether background color is enabled (default = 0); override applied at the table entity level. There may be one entry for each cell type:  0 = Disabled  1 = Enabled |
| 274-279 | Lineweight for each border type of the cell (default = kLnWtByBlock); override applied at the table entity level. There may be one group for each cell type |
| 284-289 | Flag for visibility of each border type of the cell (default = 1); override applied at the table entity level. There may be one group for each cell type:  0 = Invisible  1 = Visible |
| 97 | Standard/title/header row data type |
| 98 | Standard/title/header row unit type |
| 4 | Standard/title/header row format string |
| 177 | Cell override flag value (before AutoCAD 2007) |
| 92 | Extended cell flags (from AutoCAD 2007) |
| 301 | Cell value block begin (from AutoCAD 2007) |
| 302 | Text string in a cell. If the string is shorter than 250 characters, all characters appear in code 302. If the string is longer than 250 characters, it is divided into chunks of 250 characters. The chunks are contained in one or more code 303 codes. If code 393 codes are used, the last group is a code 1 and is shorter than 250 characters. This value applies only to text-type cells and is repeated, 1 value per cell (from AutoCAD 2007) |
| 303 | Text string in a cell, in 250-character chunks; optional. This value applies only to text-type cells and is repeated, 302 value per cell (from AutoCAD 2007) |

Group code 178 is a flag value for a virtual edge. A virtual edge is used when a grid line is shared by two cells. For example,
if a table contains one row and two columns and it contains cell A and cell B, the central grid line contains the right edge
of cell A and the left edge of cell B. One edge is real, and the other edge is virtual. The virtual edge points to the real
edge; both edges have the same set of properties, including color, lineweight, and visibility.

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*