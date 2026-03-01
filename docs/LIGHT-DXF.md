# LIGHT (DXF)

The following group codes apply to light entities.

| Light group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbLight) |
| 90 | Version number |
| 1 | Light name |
| 70 | Light type:  1 = Distant  2 = Point  3 = Spot |
| 290 | Status |
| 291 | Plot glyph |
| 40 | Intensity |
| 10 | Light Position  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *X*, *Y*, and *Z* values of the light position |
| 11 | Target location  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *X*, *Y*, and *Z* values of the target location |
| 72 | Attenuation type:  0 = None  1 = Inverse Linear  2 = Inverse Square |
| 292 | Use attenuation limits |
| 41 | Attenuation start limit |
| 42 | Attenuation end limit |
| 50 | Hotspot angle |
| 51 | Falloff angle |
| 293 | Cast shadows |
| 73 | Shadow Type  0 = Ray traced shadows  1 = Shadow maps |
| 91 | Shadow map size |
| 280 | Shadow map softness |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*