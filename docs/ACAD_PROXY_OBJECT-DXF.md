# ACAD\_PROXY\_OBJECT (DXF)

The following group codes apply to ACAD\_PROXY\_OBJECT objects.

| ACAD\_PROXY\_OBJECT group codes | |
| Group code | Description |
| 100 | DXF: Subclass marker (AcDbProxyObject) |
| 90 | DXF: Proxy object class ID (always 499) |
| 91 | DXF: Application object's class ID. Class IDs are based on the order of the class in the CLASSES section. The first class is given the ID of 500, the next is 501, and so on |
| 93 | DXF: Size of object data in bits |
| 310 | DXF: Binary object data (multiple entries can appear) (optional) |
| 330 or 340 or 350 or 360 | DXF: An object ID (multiple entries can appear) (optional) |
| 94 | DXF: 0 (indicates end of object ID section) |
| 95 | DXF: Object drawing format when it becomes a proxy (a 32-bit unsigned integer):  Low word is AcDbDwgVersion  High word is MaintenanceReleaseVersion |
| 70 | DXF: Original custom object data format:  0 = DWG format  1 = DXF format |

The 92 field is not used for AcDbProxyObject. Objects of this class never have graphics.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*