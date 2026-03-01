# About Adding 3D Thickness to 2D Objects

Use the thickness property to give objects a 3D appearance.

The 3D thickness of an object is the distance that the object is extended above or below its location in 3D. Positive thickness
extends upward in the positive *Z* direction; negative thickness extends downward (negative *Z*).

![](../images/GUID-1090EE11-09EA-4632-A105-6FA1A56B639C-low.png)

The orientation of the UCS when the object was created determines the *Z* direction. Objects with a non-zero thickness can be shaded and can hide other objects behind them.

The thickness property changes the appearance of the following types of objects:

* 2D solids
* Arcs
* Circles
* Lines
* Polylines (including spline-fit polylines, rectangles, polygons, boundaries, and donuts)
* Text (only if created as a single-line text object using an SHX text font)
* Points

Modifying the thickness property of other types of objects does not affect their appearance.

You can set the default thickness property for new objects you create by setting the THICKNESS system variable. For existing
objects, change the thickness property on the Properties Inspector palette.

The 3D thickness is applied uniformly to an object; a single object cannot have different thicknesses.

You might need to change the 3D viewpoint to see the effect of thickness on an object.

NOTE:Although the THICKNESS variable sets an extruded thickness for new 2D objects, those objects continue to be 2D objects. The
THICKEN command adds volume to a surface object, converting it to a 3D solid.

#### Related Tasks

* [To Drop a Perpendicular Line From a 3D Point to the XY Plane](To-Drop-a-Perpendicular-Line-From-a-3D-Point-to-the-XY-Plane.md)
* [To Create Wireframe Geometry Based on Other Objects](To-Create-Wireframe-Geometry-Based-on-Other-Objects.md)

#### Related Concepts

* [About Creating 3D Wireframe Models](About-Creating-3D-Wireframe-Models.md)

#### Related Information

* [To Set the Thickness of New Objects](To-Set-the-Thickness-of-New-Objects.md)
* [To Change the Thickness of Existing Objects](To-Change-the-Thickness-of-Existing-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*