# About Exporting a Layout to Model Space in a New Drawing

You can export all visible objects from the current layout to model space in a new drawing with the EXPORTLAYOUT command.

Objects that are outside the boundaries of “paper” in the layout are also exported.

Some objects are not exported to the model space drawing. The objects are:

* Objects on layers that are turned off or frozen
* Objects in Model space that are not visible in a layout viewport
* Named views
* Materials
* Lights

## Changes to Exported Objects

When exported, some objects become a different object type, or are modified in order to maximize the visual fidelity of the
layout.

| Object Type | Representation in Exported Drawing |
| Dimensions | Dimensions that exceed the boundaries of the layout viewport are exploded. |
| Constraints | Dimensional constraints are removed. |
| Standard or dynamic block (with or without attributes) | Standard or dynamic blocks, with or without attributes, that exceed the boundaries of the layout viewport will be converted to a new, anonymous block. Attributes are converted to text objects in the block. NOTE: The “Allow Exploding” setting (a setting on the block definition) is ignored if the block exceeds the boundaries of the layout viewport. |
| Annotative objects | Objects become non-annotative. |
| External reference (xref) | An xref with nested objects that exceed the boundaries of the layout viewport is converted to a block reference and exploded. |
| Layout viewport | Layout viewports are represented either by a polyline or the clipped viewport object. |
| Custom objects | Custom objects are exploded and converted to anonymous blocks. |
| Xref clipped with the XCLIP command | Xrefs clipped with the XCLIP command are converted to a clipped block reference. |
| Visual Styles | The 2D wireframe visual style is used. |
| Perspective viewports | Objects in a viewport with Perspective turned on will change to a parallel projection. |

NOTE:Objects that can be trimmed without changing their object types are not listed in the table.

## Visual Changes to Objects

Not all objects displayed in a layout will display identically in the Model tab of the exported drawing. This includes the
following cases:

* The same object displayed in multiple viewports becomes multiple objects in the exported drawing. In addition, objects are
  transformed and often scaled. These changes can affect data extraction of blocks.
* Some objects are converted or exploded before being trimmed.
* Layout viewports can each have a different visual style; only a single visual style can be used in model space.
* Polylines with a non-zero width that are clipped by the layout viewport boundary might not be accurately trimmed in the exported
  drawing.

#### Related Tasks

* [To Export a Layout to Model Space in a New Drawing](To-Export-a-Layout-to-Model-Space-in-a-New-Drawing.md)
* [To Work With Layout Tabs](To-Work-With-Layout-Tabs.md)

#### Related Concepts

* [About Layouts](About-Layouts.md)

#### Related Information

* [EXPORTLAYOUT (Command)](EXPORTLAYOUT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*