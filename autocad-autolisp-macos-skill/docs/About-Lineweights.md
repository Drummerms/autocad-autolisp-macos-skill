# About Lineweights

Lineweight is a property assigned to graphical objects, hatches, leader lines, and dimension geometry that results in thicker,
darker lines.

The *current* lineweight is assigned to all new objects until you make another lineweight current. In addition to setting an explicit value
for the lineweight, you can set lineweight to ByLayer or ByBlock.

* If the current lineweight is set to ByLayer, objects are created with the lineweight assigned to the current layer.
* If the current lineweight is set to ByBlock, objects are created using the default lineweight setting until the objects are
  grouped into a block. When the block is inserted into the drawing, it acquires the current lineweight setting.

## Display Lineweights

Lineweights can be turned on and off in a drawing, and are displayed differently in model space than in a paper space layout.

* In model space, a lineweight of 0 is displayed as one pixel wide, and other lineweights use a proportional pixel width. Lineweight
  display in model space does not change with the zoom factor. For example, a lineweight value that is represented by a width
  of four pixels is always displayed using four pixels regardless of how far you zoom in.
* In a paper space layout, lineweights are displayed using real-world units, and lineweight display changes with the zoom factor.
* By default, lineweights are plotted with the exact width of the assigned lineweight value.

NOTE:

* Regeneration time increases with lineweights that are represented by more than one pixel. To optimize performance, turn off
  the display of lineweights on the status bar. This setting does not affect plotting lineweights.
* The lineweight of dimension lines and extension lines can also be controlled separately with the Dimension Style Manager.
* If you need fixed-width lines such as would be used for a printed circuit board, use wide polylines instead of lineweights.

## Plot Lineweights

You can control lineweight plotting and scaling in your drawing in the Plot or the Page Setup dialog boxes. You can also plot
objects in your drawing with custom lineweight values: use the Plot Style Table Editor to adjust the fixed lineweight values
to plot at a new value.

You can use *plot styles* (STYLESMANAGER) to apply different line join and line end styles to objects with lineweights. These styles are displayed
only in a full preview using PREVIEW or PLOT.

#### Related Tasks

* [To Display or Hide Lineweights](To-Display-or-Hide-Lineweights.md)

#### Related Information

* [To Set the Current Lineweight](To-Set-the-Current-Lineweight.md)
* [To Set the Plotted Lineweight](To-Set-the-Plotted-Lineweight.md)
* [Overview of Object Properties](Overview-of-Object-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*