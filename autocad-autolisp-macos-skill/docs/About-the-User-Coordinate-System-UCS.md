# About the User Coordinate System (UCS)

The User Coordinate System (UCS) is a movable coordinate system, which is a fundamental tool both for 2D drawing and 3D modeling.

The UCS is the active coordinate system that establishes the XY plane (work plane) and Z -axis direction for drawing and
modeling. You can set the UCS origin and its X, Y, and Z axes to suit your needs. The UCS is useful in 2D design and essential
in 3D design because it controls features that include

* The *XY* plane, also called the *work plane*, on which objects are created and modified
* The horizontal and vertical directions used for features like Ortho mode, polar tracking, and object snap tracking
* The alignment and angle of the grid, hatch patterns, text, and dimension objects
* The origin and orientation for coordinate entry and absolute reference angles
* For 3D operations, the orientation of work planes, projection planes, and the *Z* axis for vertical direction and axis of rotation

You can change the location and orientation of the current UCS by clicking the UCS icon and using its grips, or with the UCS
command. Display options for the UCS icon are available with the UCSICON command.

## Understand the UCS in 3D

When you create or modify objects in a 3D environment, you can move and reorient the UCS anywhere in 3D space to simplify
your work. The UCS is useful for entering coordinates, creating 3D objects on 2D work planes, and rotating objects in 3D.

NOTE: The UCS icon follows the traditional right-hand rule in determining positive axis directions and rotation directions.

![](../images/GUID-3BF28E8C-A4A4-4DDE-A3A3-99851A4C1AA5-low.png)

## The UCS in Paper Space

You can define a new UCS in paper space just as you can in model space; however, the UCS in paper space is restricted to 2D
manipulation. Although you can enter 3D coordinates in paper space, you cannot use 3D viewing commands such as PLAN and VPOINT.

## Understand the World Coordinate System (WCS)

The WCS is a fixed Cartesian coordinate system. Internally, all objects are defined by their WCS coordinates, and the WCS
and the UCS are coincident in a new drawing. However, it is usually more convenient to create and edit objects based on the
UCS, which can be customized to suit your needs.

#### Related Tasks

* [To Move the UCS Origin Using the Origin Grip](To-Move-the-UCS-Origin-Using-the-Origin-Grip.md)
* [To Rotate the UCS About the X , Y , or Z Axis](To-Rotate-the-UCS-About-the-X-,-Y-,-or-Z-Axis.md)
* [To Specify a New UCS Orientation With Three Points](To-Specify-a-New-UCS-Orientation-With-Three-Points.md)
* [To Change the Orientation of the Z Axis of the UCS](To-Change-the-Orientation-of-the-Z-Axis-of-the-UCS.md)
* [To Align the UCS With an Existing 3D Object](To-Align-the-UCS-With-an-Existing-3D-Object.md)
* [To Restore the Previous UCS](To-Restore-the-Previous-UCS.md)
* [To Restore the UCS to the WCS Orientation](To-Restore-the-UCS-to-the-WCS-Orientation.md)

#### Related Concepts

* [About Controlling the User Coordinate System (UCS)](About-Controlling-the-User-Coordinate-System-UCS.md)

#### Related Information

* [About Assigning UCS Definitions to Viewports](About-Assigning-UCS-Definitions-to-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*