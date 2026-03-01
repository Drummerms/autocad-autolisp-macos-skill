# LAYOUTREGENCTL (System Variable)

Specifies how the display list is updated in the Model layout and named layouts.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

For each layout, the display list is updated either by regenerating the drawing when you switch to that layout or by saving
the display list to memory and regenerating only the modified objects when you switch to that layout. Changing the LAYOUTREGENCTL
setting can improve performance.

| 0 | The drawing is regenerated each time you switch tabs. |
| 1 | For the Model layout and the last named layout made current, the display list is saved to memory and regenerations are suppressed when you switch between layouts. For all other layouts, regenerations still occur when you switch to that layout. |
| 2 | The drawing is regenerated the first time you switch to each layout. For the remainder of the drawing session, the display list is saved to memory and regenerations are suppressed when you switch to those layouts |

The performance gain achieved by changing the LAYOUTREGENCTL setting is dependent on several factors, including the drawing
size and type, the objects contained in the drawing, the amount of available memory, and the effect of other open drawings
or applications. When LAYOUTREGENCTL is set to 1 or 2, the amount of additional memory used is the size of the Model layout's
display list multiplied by the number of viewports in each layout for which the display list is saved.

If LAYOUTREGENCTL is set to 1 or 2 and performance seems slow in general or when you switch between layouts for which the
display list is saved, consider changing to a setting of 0 or 1 to find the optimal balance for your work environment.

Regardless of the LAYOUTREGENCTL setting, if you redefine a block or undo a layout switch, the drawing is regenerated the
first time you switch to any layout that contains saved viewports.

#### Related Concepts

* [About Layout Viewports](About-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*