# FAQ: What is the Difference Between Lightweight Polylines and "Legacy" Polylines? (AutoLISP)

A lightweight polyline (LWPOLYLINE) is defined in the drawing database as a single graphic entity unlike the "legacy" polyline
(POLYLINE), which is defined as a group of subentities. A "legacy" polyline can be either a 2D or 3D polyline, while a lightweight
polyline can only be a 2D polyline.

Lightweight polylines display faster and consume less disk space and RAM than "legacy" 2D polylines. As of AutoCAD Release
14 and later, 3D polylines are always created as "legacy" polyline entities, and 2D polylines are created as lightweight polylines,
unless they are curved or fitted with the AutoCAD PEDIT command. When a drawing from an earlier release is opened in AutoCAD
Release 14 or a later release, all 2D polylines are convert to lightweight polylines automatically, unless they have been
curved or fitted or contain extended data (xdata).

#### Related Concepts

* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [FAQ: How Do I Process Curve-Fit and Spline-Fit Polylines? (AutoLISP)](FAQ-How-Do-I-Process-Curve-Fit-and-Spline-Fit-Polylines-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*