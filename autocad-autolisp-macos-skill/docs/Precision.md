# Precision

Ensure the precision required for your models.

There are several precision features available, including

* *Polar tracking*. Snap to the closest preset angle and specify a distance along that angle.
* *Locking angles*. Lock to a single, specified angle and specify a distance along that angle.
* *Object snaps*. Snap to precise locations on existing objects, such as an endpoint of a polyline, the midpoint of a line, or the center
  point of a circle.
* *Grid snaps*. Snap to increments in a rectangular grid.
* *Coordinate entry*. Specify a location by its Cartesian or polar coordinates, either absolute or relative.

The most commonly used precision features are polar tracking, locking angles, and object snaps.

## Polar Tracking

When you need to specify a point, such as when you create a line, you can use polar tracking to guide the movement of your
cursor in certain directions.

For example, after you specify the first point of the line below, move your cursor to the right, and then enter a distance
in the Command window to specify a precise horizontal length for the line.

![](../images/GUID-70729858-0332-4D21-9912-7555AE39457F-low.png)

By default, polar tracking is turned on and guides your cursor in a horizontal or vertical direction (0 or 90 degrees).

To turn polar tracking on and off, press F10 or
![](../images/GUID-D32C1929-DF71-46A8-B5AD-D0D46289A3FC-low.png) on the touch bar.

## Locking Angles

If you need to draw a line at a specified angle, you can lock the angle for the next point. For example, if the second point
of a line needs to be created at a 45 degree angle, you would enter <45 in the Command window.

![](../images/GUID-49C345D2-11FA-4A91-A59F-CF503C7123A0-low.png)

After you move your cursor in the desired direction along the 45-degree angle, you can enter the length of the line.

## Object Snaps

By far, the most important way for you to specify precise locations on objects is to use object snaps. In the following illustration,
several different kinds of object snaps are represented by markers.

![](../images/GUID-4FDEB8A0-C795-4B88-8FCE-64955BAFEB2A-low.png)

Object snaps become available during a command whenever AutoCAD prompts you to specify a point. For example, if you start
a new line and move your cursor near the endpoint of an existing line, the cursor will automatically snap to it.

![](../images/GUID-898ACCA4-82BC-4259-8EA2-20E07BBFA5D6-low.png)

To turn object snaps on and off, press F3 or
![](../images/GUID-DEAF1244-966F-460B-AA47-3CF33E3E4148-low.png) on the touch bar.

## Set Default Object Snaps

Enter the OSNAP command to set the default object snaps, which are also called "running" object snaps. For example, you might
find it useful to turn on the Midpoint object snap by default.

![](../images/GUID-2E724EED-CE6C-4FA6-8105-6F33631113DC-low.png)

## Recommendations

* At any prompt for a point, you can specify a single object snap that overrides all other object snap settings. You hold down
  Shift, right-click in the drawing area, and choose an object snap from the Object Snap menu. Then move the cursor to select
  a location on an object.
* Make sure that you zoom in close enough to avoid mistakes. In a densely populated model, snapping to the wrong object will
  result in an error that can propagate throughout your model.

## Object Snap Tracking

During a command, you can align points both horizontally and vertically from object snap locations. In the following illustration,
you first hover over endpoint 1 and then hover over endpoint 2. When you move your cursor near location 3, the cursor locks
into the horizontal and vertical location shown.

![](../images/GUID-D6DACC9B-B58C-4CE7-8B72-F04C0B55F617-low.png)

You can now finish creating the line, circle, or other object that you were creating from that location.

To turn object snap tracking on and off, press F11 or
![](../images/GUID-9A63943B-D8CE-40DA-B4C7-487DE42335F9-low.png) on the touch bar.

## Verify Your Work

Recheck your geometry to catch mistakes early. Enter the DIST command (or just DI) to measure the distance between any two
points in your model.

For example, you might need to find the clearance between two points shown, which might represent the corner of a wall and
a small table, or perhaps a 2D section of a plastic part and a wire.

After you enter DIST, click the endpoint on the corner (1). Next, hold down Shift as you right-click, and then choose Perpendicular
from the object snap menu. Finally, click the circle (2).

![](../images/GUID-99A6F948-E756-442A-893E-71B6AA1645B0-low.png)

The number of decimal places and unit style displayed in the result is controlled by the UNITS command.

## Handy Function Key Reference

The keyboard function keys all have assignments in AutoCAD. For computers with the touch bar, the function keys are replaced
with icons. The icons shown are on the touch bar by default.

NOTE:If you have a touch bar, you can press
*fn* to revert to the standard F1-F12 function keys.

| Function Key | Icon | Feature | Description |
| F1 | ![](../images/GUID-7C9407BB-CA9C-4A1C-B08D-85C448693909-low.png) | Help | Displays Help for the active tooltip, command, palette, or dialog box. |
| F2 | ![](../images/GUID-AFC1C102-0167-43DB-AB98-6A562F708082-low.png) | Expanded command line | Displays an expanded command history in the Command window. |
| F3 | ![](../images/GUID-DEAF1244-966F-460B-AA47-3CF33E3E4148-low.png) | Object snap | Turns object snap on and off. |
| F4 |  | 3D Object Snap | Turns on additional object snaps for 3D elements. |
| F5 |  | Isoplane | Cycles through 2-1/2D isoplane settings |
| F6 | ![](../images/GUID-331A1EC3-12FA-4D18-840B-CAFD4E7234CC-low.png) | Dynamic UCS (AutoCAD only) | Turns automatic UCS alignment with planar surfaces on and off. |
| F7 | ![](../images/GUID-CD7987DD-AB67-4027-AD87-149DA630BFFB-low.png) | Grid display | Turns the grid display on and off. |
| F8 | ![](../images/GUID-62FC01CB-D303-45C4-8D59-589FD9828446-low.png) | Ortho mode | Locks cursor movement to horizontal or vertical. |
| F9 | ![](../images/GUID-BEBC9838-A4E4-4AEC-8612-5FE13E3058BC-low.png) | Grid snap | Restricts cursor movement to specified grid intervals. |
| F10 | ![](../images/GUID-D32C1929-DF71-46A8-B5AD-D0D46289A3FC-low.png) | Polar tracking | Guides cursor movement to specified angles. |
| F11 | ![](../images/GUID-9A63943B-D8CE-40DA-B4C7-487DE42335F9-low.png) | Object snap tracking | Tracks the cursor horizontally and vertically from object snap locations. |
| F12 | ![](../images/GUID-598052FD-166B-48E0-9A64-DBB598CD8039-low.png) | Dynamic input | Displays distances and angles near the cursor and accepts input as you use Tab between fields. |

NOTE:Ortho mode (F8) and Polar tracking (F10) are mutually exclusive—turning either one on will turn the other one off.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Geometry](GUID-AC292B8E-6E28-42DD-BC90-2BC15EE86199.htm " Create basic geometric objects such as lines, circles, and hatched areas.
")

**Next topic:** [Layers](GUID-3C0294C1-4659-42FF-96E7-A5501CCE7046.htm " Organize your drawing by assigning objects to layers.
")

#### Related References

* [DIST (Command)](DIST-Command.md)
* [OSNAP (Command)](OSNAP-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*