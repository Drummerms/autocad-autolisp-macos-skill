# TRACE (DXF)

The following group codes apply to trace entities.

NOTE:This entity isn't related to the Trace feature introduced in
AutoCAD 2022-based products, but rather the

* TRACE command in AutoCAD 2011-based products and earlier
* APIs available to create and modify
  AcDbTrace entities

| Trace group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbTrace) |
| 10 | First corner (in OCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of first corner (in OCS) |
| 11 | Second corner (in OCS)  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of second corner (in OCS) |
| 12 | Third corner (in OCS)  DXF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of third corner (in OCS) |
| 13 | Fourth corner (in OCS)  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of fourth corner (in OCS) |
| 39 | Thickness (optional; default = 0) |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*