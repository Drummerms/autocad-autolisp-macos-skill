# FRAME (System Variable)

Controls the display of frames for all images, PDF underlays, clipped xrefs, and wipeout objects.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 3 |

The FRAME setting overrides the individual [IMAGEFRAME](IMAGEFRAME-System-Variable.md), [PDFFRAME](PDFFRAME-System-Variable.md), [XCLIPFRAME](XCLIPFRAME-System-Variable.md), and [WIPEOUTFRAME](WIPEOUTFRAME-System-Variable.md) settings.

| 0 | The frame is not visible and it is not plotted. The frame temporarily reappears during selection preview or object selection. |
| 1 | Displays and plots the frame. |
| 2 | Displays but does not plot the frame. |
| 3 | The individual setting varies for all external references in the current drawing (raster images, underlays, clipped xrefs, and wipeout objects all have different frame settings). |

#### Related Tasks

* [To Hide and Show PDF Underlay Frames](To-Hide-and-Show-PDF-Underlay-Frames.md)

#### Related Concepts

* [Hide and Show PDF Underlay Frames](Hide-and-Show-PDF-Underlay-Frames.md)
* [About Showing and Hiding Raster Image Boundaries](About-Showing-and-Hiding-Raster-Image-Boundaries.md)
* [About Clipping External References and Blocks](About-Clipping-External-References-and-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*