# WIPEOUT (DXF)

The following group codes apply to wipeout entities.

| Wipeout group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbRasterImage) |
| 90 | Class version |
| 10 | Insertion point (in WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of insertion point (in WCS) |
| 11 | U-vector of a single pixel (points along the visual bottom of the image, starting at the insertion point) (in WCS)  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values U-vector (in WCS) |
| 12 | V-vector of a single pixel (points along the visual left side of the image, starting at the insertion point) (in WCS)  DXF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of V-vector (in WCS) |
| 13 | Image size in pixels  DXF: *U* value; APP: 2D point (*U* and *V* values) |
| 23 | DXF: *V* value of image size in pixels |
| 340 | Hard reference to imagedef object |
| 70 | Image display properties:  1 = Show image  2 = Show image when not aligned with screen  4 = Use clipping boundary  8 = Transparency is on |
| 280 | Clipping state: 0 = Off; 1 = On |
| 281 | Brightness value (0-100; default = 50) |
| 282 | Contrast value (0-100; default = 50) |
| 283 | Fade value (0-100; default = 0) |
| 360 | Hard reference to imagedef\_reactor object |
| 71 | Clipping boundary type. 1 = Rectangular; 2 = Polygonal |
| 91 | Number of clip boundary vertices that follow |
| 14 | Clip boundary vertex (in OCS)  DXF: *X* value; APP: 2D point (multiple entries)  NOTE 1) For rectangular clip boundary type, two opposite corners must be specified. Default is (-0.5,-0.5), (size.x-0.5, size.y-0.5). 2) For polygonal clip boundary type, three or more vertices must be specified. Polygonal vertices must be listed sequentially |
| 24 | DXF: *Y* value of clip boundary vertex (in OCS) (multiple entries) |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*