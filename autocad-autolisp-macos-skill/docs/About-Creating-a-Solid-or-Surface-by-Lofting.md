# About Creating a Solid or Surface by Lofting

Create a 3D solid or surface by lofting a profile through a set of two or more cross-section profiles.

The cross-section profiles define the shape of the resulting solid object.

Cross-section profiles can be open or closed curves. Open curves create surfaces and closed curves create solids or surfaces.

![](../images/GUID-E2D83829-190C-4536-84E9-C0DD7E3BEA55-low.png)

## Options for Lofting

* *Mode.* Sets whether the loft creates a surface or a solid.
* *Cross-section profiles.* Select a series of cross-section profiles to define the shape of the new 3D object.

  ![](../images/GUID-8247198F-1EFF-4803-AD60-E9116F5B6A48-low.png)

  lofted objects with different cross-section settings

  As you create a lofted object, you can adjust its shape by specifying how the profile passes through the cross sections (for
  example, a sharp or smooth curve). You can also modify the settings later in the Properties palette.
* *Paths.* Specify a path for the loft operation to obtain more control over the shape of the lofted object. For best results, start
  the path curve on the plane of the first cross section and end it on the plane of the last cross section.

  ![](../images/GUID-2200E8C9-B3DD-48D4-AA95-E1C2C5814467-low.png)
* *Guide curves.* Specify guide curves to match points on corresponding cross sections. This method prevents undesired results, such as wrinkles
  in the resulting 3D object.

  ![](../images/GUID-F3258BB6-3305-44C2-B5AF-3789F13716D4-low.png)

  Each guide curve must meet the following criteria:

  + Intersects each cross section
  + Starts on the first cross section
  + Ends on the last cross section

#### Related Tasks

* [To Create a Solid by Lofting Through a Set of Cross-section Profiles](To-Create-a-Solid-by-Lofting-Through-a-Set-of-Cross-section-Profiles.md)
* [To Modify a Lofted Solid or Surface by Changing the Surface Normal Settings](To-Modify-a-Lofted-Solid-or-Surface-by-Changing-the-Surface-Normal-Settings.md)

#### Related Concepts

* [About Constructing Solids and Surfaces From 2D Geometry](About-Constructing-Solids-and-Surfaces-From-2D-Geometry.md)

#### Related Information

* [To Create a NURBS Surface by Conversion and Lofting](To-Create-a-NURBS-Surface-by-Conversion-and-Lofting.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*