# VSSILHEDGES (System Variable)

Controls display of silhouette edges of solid objects in the visual style applied to the current viewport.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

| 0 | Off |
| 1 | On |

![](../images/GUID-CCB25B51-8856-4E38-B520-7DCEDF415DAA-low.gif)

The initial value of VSSILHEDGES depends on the current visual style.

| Visual Style (VSCURRENT) | Initial Value |
| 2D Wireframe | 0 |
| Conceptual | 1 |
| Hidden | 1 |
| Shaded | 0 |
| Shaded with Edges | 1 |
| Shades of Gray | 1 |
| Sketchy | 1 |
| Wireframe | 0 |
| X-ray | 0 |
| Realistic | 0 |

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [About Controlling the Display of Edges](About-Controlling-the-Display-of-Edges.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*