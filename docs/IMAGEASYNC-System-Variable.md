# IMAGEASYNC (System Variable)

Controls whether images are asynchronous loaded in the background during the opening of a drawing file.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

| Value | Description |
| 0 | Images are loaded synchronously (legacy behavior) |
| 1 | Images are loaded asynchronously and can improve the performance of opening drawing files |

NOTE:AutoCAD 2025 and earlier loaded images synchronously during file open which is the same as setting IMAGEASYNC to 0.

#### Related Information

* [About Raster Images in Drawings](About-Raster-Images-in-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*