# PSLTSCALE (System Variable)

Controls the linetype scaling of objects displayed in paper space viewports.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 1 |

| 0 | No special linetype scaling. Linetype dash lengths are based on the drawing units of the space (model or paper) in which the objects were created. Scaled by the global [LTSCALE](LTSCALE-Command.md) factor. |
| 1 | Viewport scaling governs linetype scaling. If  [TILEMODE](TILEMODE-System-Variable.md) is set to 0, dash lengths are based on paper space drawing units, even for objects in model space. In this mode, viewports can have varying magnifications, yet display linetypes identically. For a specific linetype, the dash lengths of a line in a viewport are the same as the dash lengths of a line in paper space. You can still control the dash lengths with LTSCALE |

When you change PSLTSCALE or use a command such as [ZOOM](ZOOM-Command.md) with PSLTSCALE set to 1, objects in viewports are not automatically regenerated with the new linetype scale. Use the [REGEN](REGEN-Command.md) or [REGENALL](REGENALL-Command.md) command to update the linetype scales in each viewport.

#### Related Concepts

* [To Scale Linetypes in Layout Viewports](To-Scale-Linetypes-in-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*