# About Entering 3D Spherical Coordinates

3D spherical coordinates specify a location by a distance from the UCS origin, an angle from the *X* axis in the *XY* plane, and an angle from the *XY* plane.

You specify a point using the following syntax:

**X**  *<* *angle from X axis* *<* *angle from XY plane*

In the illustration below, dynamic input is turned off, so 5<45<15 indicates a point 5 units from the UCS origin in the *XY* plane, 45 degrees from the positive *X* axis in the *XY* plane, and 15 degrees up from the *XY* plane.

![](../images/GUID-A9CC4B17-C28B-4D3B-B62C-C43BD5CF5762-low.png)

## Absolute and Relative Spherical Coordinates

You can enter absolute coordinates, which are based on the UCS origin, or you can enter relative coordinates, which are based
on the last point entered.

* By default, when you enter coordinates in the cursor tooltip with dynamic input turned on (F12), you specify relative coordinates
  with no prefix, and absolute coordinates with the *#* prefix. For example, 5<45<15 specifies a point relative to the previous point.
* If you turn off dynamic input, you specify relative coordinates with the @ sign as a prefix and no prefix to enter absolute
  coordinates. In this case, @5<45<15 specifies a point relative to the previous point.

#### Related Tasks

* [To Enter Relative 3D Spherical Coordinates](To-Enter-Relative-3D-Spherical-Coordinates.md)

#### Related References

* [Commands for Displaying Coordinates](Commands-for-Displaying-Coordinates.md)

#### Related Concepts

* [About Coordinate Entry](About-Coordinate-Entry.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*