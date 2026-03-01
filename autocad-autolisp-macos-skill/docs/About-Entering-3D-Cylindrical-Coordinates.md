# About Entering 3D Cylindrical Coordinates

3D cylindrical coordinates specify a location by a distance from the UCS origin in the *XY* plane, an angle from the *X* axis in the *XY* plane, and a *Z* value.

For cylindrical coordinate entry, you specify a point using the following syntax:

*X* *<* *angle* *,* *Z*

In the illustration below, dynamic input is turned off, so 5<30,8 specifies a point 5 units from the UCS origin in the *XY* plane, 30 degrees from the positive*X* axis in the *XY* plane, and 8 units along the positive *Z* axis.

![](../images/GUID-D8D66A27-5F18-4D3B-935D-09987EF9CAF7-low.png)

## Absolute and Relative Cylindrical Coordinates

You can enter absolute coordinates, which are based on the UCS origin, or you can enter relative coordinates, which are based
on the last point entered.

* By default, when you enter coordinates in the cursor tooltip with dynamic input turned on (F12), you specify relative coordinates
  with no prefix, and absolute coordinates with the *#* prefix. For example, 5<30,8 specifies a point relative to the previous point.
* If you turn off dynamic input, you specify relative coordinates with the @ sign as a prefix and no prefix to enter absolute
  coordinates. In this case, @5<30,8 specifies a point relative to the previous point.

#### Related Tasks

* [To Enter Relative 3D Cylindrical Coordinates](To-Enter-Relative-3D-Cylindrical-Coordinates.md)

#### Related References

* [Commands for Displaying Coordinates](Commands-for-Displaying-Coordinates.md)

#### Related Concepts

* [About Coordinate Entry](About-Coordinate-Entry.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*