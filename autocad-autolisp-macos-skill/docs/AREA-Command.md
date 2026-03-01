# AREA (Command)

Calculates the area and perimeter of objects or of defined areas.

## Summary

Several commands are available to provide area information including AREA,
[MEASUREGEOM](MEASUREGEOM-Command.md), and
[MASSPROP](MASSPROP-Command.md). Alternatively, use
[BOUNDARY](BOUNDARY-Command.md) to create a closed polyline or region. Then use
[LIST](LIST-Command.md) or the
[Properties Inspector](Properties-Inspector.md) to find the area.

## List of Prompts

The following prompts are displayed.

[Specify first corner point](AREA-Command.md) or [[Object](AREA-Command.md)/[Add Area](AREA-Command.md)/[Subtract Area](AREA-Command.md)] <Object>:
*Select an option*

The area and perimeter of the specified object displays at the Command prompt and in the tooltip.

Specify Corner Points

Calculates the area and perimeter defined by specified points. All points must lie in a plane parallel to the
*XY* plane of the current user coordinate system (UCS).

A rubberband line from the first specified point to the cursor is displayed. Once the second point is specified, a line segment
and a polygon with green fill are displayed.

Continue to specify points to define a polygon and then press Enter to complete the definition of the perimeter. The area
to be calculated is highlighted in green.

If you do not close the polygon, the area is calculated as if a line were drawn from the last point entered to the first.
When the perimeter is calculated, that line length is added.

![](../images/GUID-D9AD4DC8-0E1E-44DF-AE7A-07C4ECCC0E35-low.png)

![](../images/GUID-290FEE04-F871-4E60-AE44-66F420906322-low.png)

Object

Calculates the area and perimeter of a selected object. You can calculate the area of circles, ellipses, splines, polylines,
polygons, regions, and 3D solids.

NOTE:2D solids (created with the
[SOLID](SOLID-Command.md) command) do not have an area reported.

Select object:

If you select an open polyline, the area is calculated as if a line were drawn from the last point entered to the first. When
the perimeter is calculated that line length is ignored.

The centerline of a wide polyline is used to make area and perimeter calculations.

![](../images/GUID-57AB2635-6FC6-4CBC-8EFA-D271352C8079-low.png)

The centerline of a wide polyline is used to make area and perimeter (or length) calculations.

![](../images/GUID-939E436B-F2E2-4329-B4D6-C2F5F014FE74-low.png)

Add Area

Turns on Add mode and keeps a running balance of the total area as you continue to define areas. You can use the Add Area
option to calculate individual areas and perimeters of defined areas and objects and the total area of all defined areas and
objects.

You can also select to specify the points. A rubberband line from the first specified point to the cursor is displayed

![](../images/GUID-7ED321D9-9843-467E-8D3C-DF7CEB1A3615-low.png)

![](../images/GUID-725CE20F-EB55-4D5C-BFAC-E0591F1E40A9-low.png)

Specify points to define a polygon (3). The area to be added is highlighted in green. Press Enter. AREA calculates the area
and perimeter and returns the total area of all the areas defined by selecting points or objects since Add mode was turned
on.

If you do not close the polygon, the area is calculated as if a line were drawn from the last point entered to the first.
When the perimeter is calculated, that line length is added.

Subtract Area

Similar to the Add Area option, but subtracts areas and perimeters. You can use the Subtract Area option to subtract a specified
area from a total area.

You can also specify the area to be subtracted with points. A rubberband line from the first specified point to the cursor
is displayed.

![](../images/GUID-1CE4B3BF-84C9-4D1C-A0E3-C6CC436C7D83-low.png)

The specified area to be subtracted is highlighted in red.

The total area and perimeter displays at the Command prompt and in the tooltip.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*