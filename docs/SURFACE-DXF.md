# SURFACE (DXF)

Surface entity definitions consist of group codes that are common to all surface types, followed by codes specific to the
type.

| Common Surface group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbModelerGeometry) |
| 70 | Modeler format version number (currently = 1) |
| 1 | Proprietary data (multiple lines < 255 characters each) |
| 3 | Additional lines of proprietary data (if previous group 1 string is greater than 255 characters) (optional) |
| 100 | Subclass markar (AcDbSurface) |
| 71 | Number of U isolines |
| 72 | Number of V isolines |

#### Topics in this section

* [Extruded Surface (DXF)](Extruded-Surface-DXF.md)
* [Lofted Surface (DXF)](Lofted-Surface-DXF.md)
* [Revolved Surface (DXF)](Revolved-Surface-DXF.md)
* [Swept Surface (DXF)](Swept-Surface-DXF.md)

#### Related References

* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)
* [Extruded Surface (DXF)](Extruded-Surface-DXF.md)
* [Lofted Surface (DXF)](Lofted-Surface-DXF.md)
* [Revolved Surface (DXF)](Revolved-Surface-DXF.md)
* [Swept Surface (DXF)](Swept-Surface-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*