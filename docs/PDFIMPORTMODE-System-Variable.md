# PDFIMPORTMODE (System Variable)

Controls the default processing when importing objects from a PDF file.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 6 |

| Value | Description |
| 0 | Does not process objects after they are imported. This includes converting Bezier curves to arcs, and paths into polylines. |
| 1 | Combines imported objects into a block. |
| 2 | Applies lineweight properties. |
| 4 | Joins contiguous line and arc segments into polylines, when possible. |
| 8 | Converts fills into solid-filled hatches rather than 2D solids. |
| 16 | Combines sets of collinear segments into polyline segments. |

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*