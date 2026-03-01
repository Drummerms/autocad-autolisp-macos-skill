# About Controlling the Display of the User Coordinate System Icon

The user coordinate system icon (UCS icon) helps you visualize the current orientation of the UCS with respect to your current
viewing direction. Several versions of this icon are available, and you can change its size, location, and color.

To indicate the location and orientation of the UCS, the UCS icon is displayed either at the UCS origin point or in the lower-left
corner of the current viewport.

You can choose a 2D or 3D style of the icon to represent the UCS when working in 2D environment. Shaded style of icon is
displayed to represent the UCS in the 3D environment.

![](../images/GUID-28F1059C-F5EC-4A42-90F4-5F6BB821F8ED-low.png)

You can also use the UCSICON command to change its appearance, including its size and color.

* The UCS icon can be displayed either at the UCS origin point or in the lower-left corner of the viewport.
* When you display multiple viewports, each viewport displays its own UCS icon.
* The shaded UCS icon is displayed when using 3D visual styles.
* The UCSICON command also lets you turn off the UCS icon.

### The UCS Icon and Multiple Viewports

If you have multiple viewports, each viewport displays its own UCS icon.

### Variations in UCS Icon Types

The UCS icon is displayed in various ways to help you visualize the orientation of the work plane. The following figure shows
some of the possible icon displays.

You can use the UCSICON command to switch between the 2D UCS icon and the 3D UCS icon. You can also use the command to change
the size, color, and icon line width of the 3D UCS icon.

The UCS broken pencil icon replaces the 2D UCS icon when the viewing direction is in a plane parallel to the UCS XY plane.
The broken pencil icon indicates that the edge of the XY plane is almost perpendicular to your viewing direction. This icon
warns you not to use your pointing device to specify coordinates.

When you use the pointing device to locate a point, it's normally placed on the XY plane. If the UCS is rotated so that the
Z axis lies in a plane parallel to the viewing plane-that is, if the XY plane is edge-on to the viewer-it may be difficult
to visualize where the point will be located. In this case, the point will be located on a plane parallel to your viewing
plane that also contains the UCS origin point. For example, if the viewing direction is along the X axis, coordinates specified
with a pointing device will be located on the YZ plane, which contains the UCS origin point.

Use the 3D UCS icon to help you visualize which plane these coordinates will be projected on; the 3D UCS icon does not use
a broken pencil icon.

#### Related Tasks

* [To Change the Appearance of the UCS Icon](To-Change-the-Appearance-of-the-UCS-Icon.md)
* [To Display the UCS Icon at the UCS Origin](To-Display-the-UCS-Icon-at-the-UCS-Origin.md)

#### Related Concepts

* [About the User Coordinate System (UCS)](About-the-User-Coordinate-System-UCS.md)
* [About the User Coordinate System (UCS) Icon](About-the-User-Coordinate-System-UCSIcon.md)

#### Related Information

* [To Turn the Display of the UCS Icon On and Off](To-Turn-the-Display-of-the-UCS-Icon-On-and-Off.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*