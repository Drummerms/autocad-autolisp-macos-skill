# About Entering 2D Polar Coordinates

You can use absolute or relative polar coordinates (distance and angle) to locate points when creating objects.

To use polar coordinates to specify a point, enter a distance and an angle separated by an angle bracket (<).

By default, angles increase in the counterclockwise direction and decrease in the clockwise direction. To specify a clockwise
direction, enter a negative value for the angle. For example, entering *1<315* locates the same point as entering *1<-45*. You can change the angle conventions for the current drawing with the UNITS command.

![](../images/GUID-1DCF3DCD-4E4B-4C12-AF8A-05C618E62B57-low.png)

### Absolute Polar Coordinates

Absolute polar coordinates are measured from the UCS origin (0,0), which is the intersection of the *X* and *Y* axes. Use absolute polar coordinates when you know the precise distance and angle coordinates of the point.

With dynamic input, you can specify absolute coordinates with the *#* prefix. If you enter coordinates on the command line instead of in the tooltip, the *#* prefix is not used. For example, entering *#3<45* specifies a point 3 units from the origin at an angle of 45 degrees from the *X* axis.

The following example shows two lines drawn with absolute polar coordinates using the default angle direction setting. Enter
the following in the tooltip:

Command: *line*

From point: *#0,0*

To point: *#4<120*

To point: *#5<30*

![](../images/GUID-BF289670-2D6E-4FDA-9CA3-F65CC489AA80-low.png)

### Relative Polar Coordinates

Relative coordinates are based on the last point entered. Use relative coordinates when you know the location of a point in
relation to the previous point.

To specify relative coordinates, precede the coordinate values with an @ sign. For example, entering *@1<45* specifies a point at a distance of 1 unit from the last point specified at an angle of 45 degrees from the *X* axis.

The following example shows two lines drawn with relative polar coordinates. In each illustration, the line begins at the
location labeled as the previous point.

Command: *line*

From point: *@3<45*

To point: *@5<285*

![](../images/GUID-F13D12DA-5498-401E-B310-470E0431D729-low.png)

#### Related Tasks

* [To Enter Relative 2D Polar Coordinates](To-Enter-Relative-2D-Polar-Coordinates.md)
* [To Enter Absolute 2D Polar Coordinates](To-Enter-Absolute-2D-Polar-Coordinates.md)

#### Related References

* [Commands for Displaying Coordinates](Commands-for-Displaying-Coordinates.md)

#### Related Concepts

* [About Coordinate Entry](About-Coordinate-Entry.md)
* [About Using Dynamic Input Tooltips](About-Using-Dynamic-Input-Tooltips.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*