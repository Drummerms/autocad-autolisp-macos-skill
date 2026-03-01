# About Purging Unreferenced Layers, Blocks, and Style Definitions

You can clean up your drawing by removing unused items in your drawing such as unreferenced layers, blocks, and style definitions.

The term,
*purge*, is used to describe removing a definition rather than erasing an object. For example, erasing all objects that use a dashed
linetype still leaves the linetype definition in the drawing. Similarly, erasing all block
*references* to a fixture still leaves the block
*definition* of that fixture block in the drawing.

A drawing that has the minimum number of unreferenced definitions open, save, and perform faster, and use less memory. In
addition, purging a drawing provides the following specific benefits:

* Removing unreferenced block definitions can reduce the size of a drawing file substantially.
* Removing unreferenced layers reduces the clutter in the Layer Properties Manager.
* Removing unreferenced style definitions such as text styles and dimension styles also reduces clutter in their dialog boxes
  and palettes.

You might want to consider exceptions to purging to maintain standardized definitions for future work.

## Determine Why an Item Cannot be Purged

In some cases, it might seem that you should be able to purge an item, but you can't determine exactly why the Purge dialog
box doesn't allow it. Here's a list of the most common reasons why an item can't be purged:

* Permanent definitions, such as layer 0 and all definitions named Standard
* Styles or definitions set to Current, such as the current layer
* Referenced by another style or definition, such as a text style used by a dimension style
* Used by or nested within a block or an anonymous block, such as a linetype used in a block definition or a block within another
  block
* Located on a frozen layer and not visible, or on a locked layer
* Referenced by an attached xref
* Referenced in paper space on a different layout tab

The Purge dialog box provides you with all the details about an item and why you cannot purge it from your drawing. Specifically,
you can click Non-Purgeable Items and examine the Details section to find the key information you need. You can click Select
Objects
![](../images/GUID-69842A20-AFC0-446A-9228-CF95528A80B3-low.png) to navigate to the non-purgeable object and take appropriate action to make it purgeable.

The Purge dialog box also provides you with a thumbnail preview of the item selected in the tree view pane for a visual representation
of the item.

#### Related Tasks

* [To Purge Unused Items](To-Purge-Unused-Items.md)
* [To Find Non-Purgeable Blocks](To-Find-Non-Purgeable-Blocks.md)

#### Related References

* [PURGE (Command)](PURGE-Command.md)
* [Purge Dialog Box](Purge-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*