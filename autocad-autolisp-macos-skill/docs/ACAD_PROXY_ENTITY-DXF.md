# ACAD\_PROXY\_ENTITY (DXF)

The following group codes apply to proxy entities. In addition to the group codes described here, see Common Group Codes
for Entities.

| Acad\_proxy\_entity group codes | |
| Group code | Description |
| 100 | DXF: AcDbProxyEntity |
| 90 | DXF: Proxy entity class ID (always 498) |
| 91 | DXF: Application entity's class ID. Class IDs are based on the order of the class in the CLASSES section. The first class is given the ID of 500, the next is 501, and so on |
| 92 | DXF: Size of graphics data in bytes |
| 310 | DXF: Binary graphics data (multiple entries can appear) (optional) |
| 93 | DXF: Size of entity data in bits |
| 310 | DXF: Binary entity data (multiple entries can appear) (optional) |
| 330 or 340  or 350 or 360 | DXF: An object ID (multiple entries can appear) (optional) |
| 94 | DXF: 0 (indicates end of object ID section) |
| 95 | DXF: Object drawing format when it becomes a proxy (a 32-bit unsigned integer):  Low word is AcDbDwgVersion  High word is MaintenanceReleaseVersion |
| 70 | DXF: Original custom object data format:  0 = DWG format  1 = DXF format |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*