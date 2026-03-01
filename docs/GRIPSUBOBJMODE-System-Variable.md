# GRIPSUBOBJMODE (System Variable)

Controls whether grips are automatically selected (made “hot”) when subobjects are selected.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 1 |

| 0 | Does not turn grips hot when subobjects are selected. |
| 1 | Turns the face, edge, or vertex grips hot when subobjects of 3D objects (solid, surface, or mesh) are selected. |
| 2 | Turns the grips hot when subobjects of 2D polyline objects (line or arc segments) are selected. |
| 3 | Turns the grips hot when subobjects of   * 3D objects (faces, edges, or vertices) are selected * 2D polyline objects (line or arc segments) are selected |

Setting this system variable to 1 is especially helpful for quickly modifying groups of faces, edges, and vertices on mesh
objects.

#### Related Concepts

* [About Using 3D Gizmos](About-Using-3D-Gizmos.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*