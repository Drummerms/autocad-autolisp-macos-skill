# About Entering 2D Cartesian Coordinates

You can use absolute or relative Cartesian (rectangular) coordinates to locate points when creating objects.

To use Cartesian coordinates to specify a point, enter an *X* value and a *Y* value separated by a comma. The *X* value is the positive or negative distance, in units, along the horizontal axis. The *Y* value is the positive or negative distance, in units, along the vertical axis.

### Absolute Coordinates

Absolute coordinates are based on the UCS origin (0,0), which is the intersection of the *X* and *Y* axes. Use absolute coordinates when you know the precise *X* and *Y* values of the point.

With dynamic input, you specify absolute coordinates with the *#* prefix. If you enter coordinates on the command line instead of in the tooltip, the *#* prefix is not used. For example, entering *#3,4* specifies a point 3 units along the *X* axis and 4 units along the *Y* axis from the UCS origin.

The following example draws a line beginning at an *X* value of -2, a *Y* value of 1, and an endpoint at 3,4. Enter the following in the tooltip:

Command: *line*

From point: *#-2,1*

To point: *#3,4*

The line is located as follows:

![](../images/GUID-DDE88650-E614-4972-803B-9F3AF0482D82-low.png)

### Relative Coordinates

Relative coordinates are based on the last point entered. Use relative coordinates when you know the location of a point in
relation to the previous point.

To specify relative coordinates, precede the coordinate values with an @ sign. For example, entering *@3,4* specifies a point 3 units along the *X* axis and 4 units along the *Y* axis from the last point specified.

The following example draws the sides of a triangle. The first side is a line starting at the absolute coordinates -2,1 and
ending at a point 5 units in the *X* direction and 0 units in the *Y* direction. The second side is a line starting at the endpoint of the first line and ending at a point 0 units in the *X* direction and 3 units in the *Y* direction. The final line segment uses relative coordinates to return to the starting point.

Command: *line*

From point: *#-2,1*

To point: *@5,0*

To point: *@0,3*

To point: *@-5,-3*

![](../images/GUID-57D93C5F-10E6-48B1-9DA8-AA8CDCAE7912-low.png)

#### Related Tasks

* [To Enter Relative 2D Cartesian Coordinates](To-Enter-Relative-2D-Cartesian-Coordinates.md)
* [To Enter Absolute 2D Cartesian Coordinates](To-Enter-Absolute-2D-Cartesian-Coordinates.md)

#### Related References

* [Commands for Displaying Coordinates](Commands-for-Displaying-Coordinates.md)

#### Related Concepts

* [About Coordinate Entry](About-Coordinate-Entry.md)
* [About Using Dynamic Input Tooltips](About-Using-Dynamic-Input-Tooltips.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*