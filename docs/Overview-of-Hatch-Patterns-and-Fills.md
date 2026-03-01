# Overview of Hatch Patterns and Fills

A hatch object displays a standard pattern of lines and dots used to highlight an area, or to identify a material, such as
steel or concrete. Hatch objects can also display a solid fill or a gradient fill.

Create hatches and fills with the HATCH command. The following illustration includes a solid fill, a gradient fill, and a
hatch pattern. The hatch pattern has a hatch background color assigned to it.

![](../images/GUID-7E8F8E81-279C-4206-9222-CE67C3C4CD2A-low.png)

Hatches and fills do not have to be bounded. In the following illustration, the concrete hatches are *bounded*, while the earth hatches are *unbounded*.

![](../images/GUID-F5508F7B-3F4E-4868-8514-53C4976FDF95-low.png)

By default, bounded hatches are *associative*, which means that the hatch object is associated with the hatch boundary objects, and changes to the boundary objects are
automatically applied to the hatch.

![](../images/GUID-D8AFC8A7-4E75-4182-9C6E-0FCFBFA20C1F-low.png)

To maintain associativity, the boundary objects must continue to completely enclose the hatch.

The alignment and orientation of a hatch pattern is determined by the current location and orientation of the user coordinate
system, in addition to controls in the user interface.

![](../images/GUID-99E146E9-8979-4942-B297-8988E4E18A85-low.png)

Moving or rotating the UCS is an alternate method for controlling hatch patterns.

NOTE:By default, a preview of the hatch displays as you move the cursor over enclosed areas. To improve the response time in large
drawings, turn off the hatch preview feature with the HPQUICKPREVIEW system variable, or decrease the time before the preview
is temporarily canceled with the HPQUICKPREVTIMEOUT system variable.

Alternatively, solid-filled areas can be created using

* 2D solids (SOLID)
* Wide polylines (PLINE)
* Donuts (DONUT)

#### Related Tasks

* [To Create an Unbounded Hatch](To-Create-an-Unbounded-Hatch.md)

#### Related Information

* [To Set Property Overrides for New Hatch Objects](To-Set-Property-Overrides-for-New-Hatch-Objects.md)
* [To Hatch or Fill Objects or Areas](To-Hatch-or-Fill-Objects-or-Areas.md)
* [To Simplify Hatching in a Complex Drawing by Defining a Boundary Set](To-Simplify-Hatching-in-a-Complex-Drawing-by-Defining-a-Boundary-Set.md)
* [To Specify Hatch Pattern Alignment and Origin](To-Specify-Hatch-Pattern-Alignment-and-Origin.md)
* [About Hatch Islands](About-Hatch-Islands.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*