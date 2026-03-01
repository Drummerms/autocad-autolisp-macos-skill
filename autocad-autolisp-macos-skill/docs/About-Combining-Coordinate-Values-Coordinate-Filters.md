# About Combining Coordinate Values (Coordinate Filters)

You can use coordinate filters to extract one coordinate value at a time from locations on existing objects.

Coordinate filters specify a new coordinate location by using the *X* value from one location, the *Y* value of a second location, and, for 3D coordinates, the *Z* value of a third location. When used with object snaps, coordinate filters extract coordinate values from an existing object.

Coordinate filters are commonly used to locate the center of a rectangle and to locate the projection of a 3D point on the
*XY* plane of the UCS.

To specify a filter at the Command prompt, enter a period and one or more of the letters *X*, *Y*, and *Z*. The next entry is limited to a specific coordinate value.

## Example: Use of Coordinate Filters in 2D

In the following illustration, the hole in the holding plate was centered in the rectangle by extracting the *X,Y* coordinates from the midpoints of the plate's horizontal and vertical line segments.

![](../images/GUID-883277AD-FB5C-4F76-851F-E759463BC785-low.png)

Here is the Command prompt sequence:

Command: *circle*

Specify center point for circle or [3P/2P/Ttr (tangent tangent radius)]: .*x*

of: *mid*

of: *Select the horizontal line on the lower edge of the holding plate*

of: (need YZ): *mid*

of: *Select the vertical line on the left side of the holding plate*

of: Diameter/<Radius> *Specify the radius of the hole*

Coordinate filters work only when the program prompts you for a point. If you try to use a coordinate filter at the Command
prompt, you see an error message.

## Example: Use of Coordinate Filters in 3D

This example shows how to use coordinate filters to create a point object at the center (centroid) of a 3D object. Hidden
lines have been removed for clarity. The *X* value of the new point is extracted from the first location specified, the *Y* value from the second location, and the *Z* value from the third. The three values are combined to form the coordinate values of the new point.

Command: *point*

Point: *.x*

of mid

of select object (*1*)

(need YZ): *.y*

*of mid*

of select object (*2)*

(need Z): *mid*

of select object (*3)*

![](../images/GUID-A9652014-1B94-4CA4-B1B0-F0F92D9861C6-low.png)

#### Related Tasks

* [To Use Coordinate Filters to Specify a Point in 2D](To-Use-Coordinate-Filters-to-Specify-a-Point-in-2D.md)
* [To Use Coordinate Filters to Specify a Point in 3D](To-Use-Coordinate-Filters-to-Specify-a-Point-in-3D.md)
* [To Specify a Point From a Temporary Reference Point](To-Specify-a-Point-From-a-Temporary-Reference-Point.md)

#### Related References

* [Coordinate Filters (Command Modifier)](Coordinate-Filters-Command-Modifier.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*