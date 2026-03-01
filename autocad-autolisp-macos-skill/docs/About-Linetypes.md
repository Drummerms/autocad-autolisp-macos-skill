# About Linetypes

A linetype is a repeating pattern of dashes, dots, and blank spaces displayed in a line or a curve. You assign linetypes
to objects either by layer or by specifying the linetype explicitly, independent of layers.

All objects created using the *current linetype* is displayed in the Properties inspector.

* If the current linetype is set to ByLayer, objects are created with the linetype assigned to the current layer.
* If the current linetype is set to ByBlock, objects are created using the Continuous linetype, a solid linetype without embedded
  spaces, until the objects are combined into a block definition. When the block is inserted into the drawing, it displays the
  current linetype for those objects.
* If the current linetype is set explicitly, for example to ACAD\_ISO02W100, objects are created with that linetype regardless
  of the current layer.
* The CONTINUOUS linetype displays an unbroken line.

Some linetype definitions include text and symbols.

![](../images/GUID-4A42C287-365D-4D21-AE6F-753872079252-low.png)

## Load Linetypes

Before you can use different linetypes, you must load them from a linetype definition (LIN) file using the Linetype Manager
(LINETYPE command) or through the Layer Properties Manager, Linetype column. Once a linetype is loaded and the drawing is
saved, the linetype definition is stored in the drawing.

Two linetype definition files are available: *acad.lin* for imperial units, and *acadiso.lin* for metric units. ACAD\_ISO linetypes can be plotted with the ISO pen-width option.

You can remove unreferenced linetype definitions from a drawing with the PURGE command, or by deleting unreferenced linetypes
from the Linetype Manager. The BYBLOCK, BYLAYER, and CONTINUOUS linetypes cannot be removed.

## Control the Linetype Scale

You can control the linetype scale both globally for all objects, and explicitly for each object.

* The *global scale factor*controls the linetype scale globally for both new and existing objects. It is accessible from the Linetype Manager,Show Details
  button.
* The *current object scale*, also called the *linetype scale*, controls the linetype scale for new objects, and it can be set explicitly for existing objects. It accessible from the Properties
  palette as well as the Linetype Manager.

The *current object scale* is multiplied by the *global scale factor* to get the displayed linetype scale.

In a layout, by default, the linetype scale in different layout viewports is automatically based on paper space units, regardless
of the magnification of the objects. If you create a new layout viewport, use REGENALL to update the display of the linetype
scale.

NOTE:

* By default, both global and individual linetype scales are set to 1.00. The smaller the scale factor, the more repetitions
  of the pattern are generated per drawing unit. For example, with a setting of 0.5, two repetitions of the pattern in the linetype
  definition are displayed for each drawing unit.
* In most cases, you should leave the global scale factor set to 1.00
* These linetypes should not be confused with the hardware linetypes provided by some plotters. The two types of dashed lines
  produce similar results. Do not use both types at the same time, however, because the results can be unpredictable.

## Display Linetypes on Short Segments and Polylines

You can center the pattern of a linetype on each segment of a polyline, and you can control how the linetype is displayed
on short segments. If a line is too short to hold even one dash sequence, the result is a continuous line between the endpoints,
as shown below.

![](../images/GUID-EDDD5661-2220-413A-A47B-B1A8619D18DB-low.png)

You can accommodate short segments by using a smaller value for their individual linetype scales.

For polylines, you can specify whether a linetype pattern is centered on each segment or is continuous across vertices throughout
the entire length of the polyline. You do this by setting the PLINEGEN system variable.

![](../images/GUID-06FDE310-0A2F-4E12-9CD2-AE02C6412B75-low.png)

#### Related Tasks

* [To Set the Plotted Linetype](To-Set-the-Plotted-Linetype.md)
* [To Change the Linetype Scale for All Objects](To-Change-the-Linetype-Scale-for-All-Objects.md)
* [To Set the Linetype Display Style for All New 2D Polylines](To-Set-the-Linetype-Display-Style-for-All-New-2D-Polylines.md)

#### Related Concepts

* [About Custom Linetypes and Linetype Definitions](About-Custom-Linetypes-and-Linetype-Definitions.md)
* [Overview of Object Properties](Overview-of-Object-Properties.md)

#### Related Information

* [To Load a Linetype](To-Load-a-Linetype.md)
* [To Set the Linetype for All New Objects](To-Set-the-Linetype-for-All-New-Objects.md)
* [To Change the Linetype of Selected Objects](To-Change-the-Linetype-of-Selected-Objects.md)
* [To Set the Linetype Scale for New Objects](To-Set-the-Linetype-Scale-for-New-Objects.md)
* [To Change the Linetype Scale of Selected Objects](To-Change-the-Linetype-Scale-of-Selected-Objects.md)
* [To Change the Linetype Display Style of Existing 2D Polylines](To-Change-the-Linetype-Display-Style-of-Existing-2D-Polylines.md)
* [To Unload an Unused Linetype](To-Unload-an-Unused-Linetype.md)
* [To List the Linetypes in a Linetype Definition File](To-List-the-Linetypes-in-a-Linetype-Definition-File.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*