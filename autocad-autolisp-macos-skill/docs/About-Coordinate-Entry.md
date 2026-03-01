# About Coordinate Entry

When a command prompts you for a point, you can use the pointing device to specify the point, or you can enter its coordinates.
When dynamic input is turned on, you can enter the coordinate values in a tooltip near the cursor.

## Cartesian and Polar Coordinates

A Cartesian coordinate system has three axes, *X*, *Y*, and *Z*. When you enter coordinate values, you indicate a point's distance and its direction (+ or -) along the *X*, *Y*, and *Z* axes relative to the coordinate system origin (0,0,0).

In 2D, you specify points on the *XY* plane, also called the *work plane*. The work plane is similar to a flat sheet of grid paper. The *X* value of a Cartesian coordinate specifies horizontal distance, and the *Y* value specifies vertical distance. The origin point (0,0) indicates where the two axes intersect.

Polar coordinates use a distance and an angle to locate a point. With both Cartesian and polar coordinates, you can enter
absolute coordinates based on the origin (0,0) or relative coordinates based on the last point specified.

Another method of specifying a point is by moving the cursor to indicate a direction, and then entering a distance. This
method is called *direct distance entry*.

You can enter coordinates in scientific, decimal, engineering, architectural, or fractional notation. You can enter angles
in grads, radians, surveyor's units, or degrees, minutes, and seconds. The UNITS command controls the unit *format*.

NOTE:

* Coordinates and distances are always measured in units, which do not represent any specific type of units such as millimeters
  or inches. Before you start, you decide what distance one unit will represent in the drawing.
* Coordinates normally reference a moveable user coordinate system (UCS) rather than the fixed World Coordinate System (WCS).
  By default, the UCS and WCS are coincident.

## Enter Coordinates Using Dynamic Input Tooltips

You can also enter coordinates in dynamic input tooltips. After you type a coordinate value in an input field and press Tab,
the field displays a lock icon, and the cursor is constrained by the value that you entered. You can then enter a value for
the second input field. Alternately, if you type a value and press Enter, the second input field is ignored and the value
is interpreted as direct distance entry.

## Display Coordinates on the Status Bar

The current cursor location is displayed as a coordinates on the status bar.

![](../images/GUID-44FB590E-5C3C-4CB5-BDCF-E48927891449-low.png)

NOTE:Coordinates are not displayed on the status bar by default. Click Customize on the status bar, and select Coordinates to display
it.

There are three types of coordinate display: static, dynamic, and distance and angle.

* *Static display*. Updates only when you specify a point.
* *Dynamic display.* Updates as you move the cursor.
* *Distance and angle display.* Updates the relative distance *(distance<angle)* as you move the cursor. This option is available only when you draw lines or other objects that prompt you for more than
  one point.

#### Related Tasks

* [To Change the Coordinate Display on the Status Bar](To-Change-the-Coordinate-Display-on-the-Status-Bar.md)

#### Related References

* [Direct Distance Entry (Command Modifier)](Direct-Distance-Entry-Command-Modifier.md)
* [Commands for Displaying Coordinates](Commands-for-Displaying-Coordinates.md)

#### Related Concepts

* [About Entering 2D Cartesian Coordinates](About-Entering-2D-Cartesian-Coordinates.md)
* [About Entering 2D Polar Coordinates](About-Entering-2D-Polar-Coordinates.md)
* [About Entering 3D Cartesian Coordinates](About-Entering-3D-Cartesian-Coordinates.md)
* [About Entering 3D Cylindrical Coordinates](About-Entering-3D-Cylindrical-Coordinates.md)
* [About Entering 3D Spherical Coordinates](About-Entering-3D-Spherical-Coordinates.md)
* [About Using Dynamic Input Tooltips](About-Using-Dynamic-Input-Tooltips.md)

#### Related Information

* [To Display the Coordinates of a Point](To-Display-the-Coordinates-of-a-Point.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*