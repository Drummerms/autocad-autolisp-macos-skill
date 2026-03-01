# VIEWMODE (System Variable)

Stores the view settings for the current viewport.

(Read-only)

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

The setting is stored as a bitcode using the sum of the following values:

| Value | Description |
| 0 | Off |
| 1 | Perspective view |
| 2 | Front clipping |
| 4 | Back clipping |
| 8 | UCS Follow mode |
| 16 | Front clipping not at the camera (not available in AutoCAD LT)  If turned on, FRONTZ determines the front clipping plane.  If turned off, FRONTZ is ignored, and the front clipping plane passes through the camera point. This setting is ignored if the front-clipping bit 2 is turned off. |

#### Related Concepts

* [About Saving and Restoring Views](About-Saving-and-Restoring-Views.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*