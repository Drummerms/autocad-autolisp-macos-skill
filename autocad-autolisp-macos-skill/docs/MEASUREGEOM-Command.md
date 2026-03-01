# MEASUREGEOM (Command)

Measures the distance, radius, angle, area, and volume of selected objects, a sequence of points, or dynamically.

## Access Methods

*Menu*:
Tools
![](../images/ac.menuaro.gif) Inquiry

*Toolbar*:

* ![](../images/GUID-24B7A5AE-6824-45C5-B10C-D39BF37BF553-low.png) Measure Distance
* ![](../images/GUID-2C4B509D-50A1-48E3-9AD9-E8A49C6BE13E-low.png) Measure Area
* ![](../images/GUID-E95C1F3B-DE79-490D-949C-DB1C49CE4E73-low.png) Measure Radius
* ![](../images/GUID-FBA22FBA-6E80-4E1C-904A-60638DB3741F-low.png) Measure Angle
* ![](../images/GUID-6678CEC4-1E4F-4C0B-BDD3-49EE71997719-low.png) Quick Measure

NOTE:Hidden by default. Right-click the toolbar and select Customize Toolbar to display.

## Summary

The MEASUREGEOM command performs many of the same calculations as the following commands:

* [AREA](AREA-Command.md)
* [DIST](DIST-Command.md)
* [MASSPROP](MASSPROP-Command.md)

Information displays at the Command prompt and in the tooltip in the current units format.

The following prompts are displayed.

## Quick

Displays dimensions, distances, and angles within a drawing dynamically as you move your mouse over and between objects.

With this option, you can quickly review the dimensions, distances, and angles in a plan view within a drawing. As you move
your cursor between and over objects, dimensions, distances, and angles display dynamically. The orange squares displayed
at the left side of the illustration represent angles at precisely 90 degrees.

![](../images/GUID-C975C356-013A-425A-83D1-5A27D0FD4687-low.png)

Clicking within a space enclosed by geometric objects highlights it in green and displays the calculated values in the Command
window and in a dynamic tooltip. If you use Shift-click to select several areas, the cumulative area and perimeters are calculated.
The perimeters of enclosed islands as shown in the following illustration are also included.

![](../images/GUID-5AFEB32A-EECD-44B6-B294-A5A8A8272ECC-low.png)

Shift-click also deselects areas. To clear the selected area, simply move the mouse a small distance.

NOTE:The Quick option is designed to work primarily on 2D geometry in a plan view with the UCS set to World and the visual style
set to 2D Wireframe. Objects that aren't measured include annotations such as dimensions and hatches, and custom objects.

## Distance

Measures the distance between specified points along with the
*X*,
*Y*, and
*Z* component distances and the angle relative to the UCS.

Multiple points
:   Displays a running total of the distance between successive points.

    If you enter the Arc, Length, or Undo options, additional options similar to those for creating a polyline are displayed.

## Radius

Measures the radius and diameter of a specified arc, circle, or polyline arc.

## Angle

Measures the angle associated with selected arc, circle, polyline segments, and line objects.

Arc
:   Measures the angle formed between the two endpoints of an arc using the center of the arc as the vertex.

Circle
:   Measures the acute angle formed between where the circle was originally selected and a second point, using the center of the
    circle as the vertex.

Line
:   Measures the acute angle between two selected lines. The lines do not need to intersect.

Vertex
:   Measures the acute angle formed by specifying a point to act as a vertex and two other points.

## Area

Measures the area and perimeter of an object or defined area.

Specify corner points
:   Calculates the area and perimeter defined by specified points.

    ![](../images/GUID-BDCE4A60-E257-4A13-9132-9DC55FCF6C54-low.png)

    If you enter the Arc, Length, or Undo options, additional options similar to those for creating a polyline are displayed.

Add area
:   Turns on Add mode and keeps a running total of area as you define areas.

    ![](../images/GUID-34E0513C-4E72-418E-84AA-B987C0AF6520-low.png)

Subtract area
:   Subtracts a specified area from the total area. The total area and perimeter displays at the Command prompt and in the tooltip.

    ![](../images/GUID-AEBD11B9-6651-4389-A36B-BB79156F78F3-low.png)

## Volume

Measures the volume of an object or a defined area.

Object
:   Measures the volume of an object or defined area.

    You can select 3D solids or 2D objects. If you select a 2D object you must specify a height for that object.

    If you define an object by specifying points, you must specify at least three points to define a polygon. All must lie on
    a plane parallel to the
    *XY* plane of the UCS. If you do not close the polygon, an area will be calculated as if a line existed between the first and
    last points entered.

    If you enter the Arc, Length, or Undo options, additional options similar to those for creating a polyline are displayed.

Add volume
:   Turns on Add mode and keeps a running total of the volume as you define areas.

Subtract volume
:   Turns on Subtract mode and subtracts a specified volume from the total volume.

## Distance, Area, and Volume Options

You can specify options similar to those used in creating polylines when you use the Distance, Area, and Volume options.

Arc
:   Adds arc segments to the total length.

Endpoint of arc
:   Completes the arc segment, which is tangent to the previous segment.

Angle
:   Specifies the included angle of the arc segment from the start point.

    Entering a positive number creates counterclockwise arc segments. Entering a negative number creates clockwise arc segments.

Radius
:   Specifies the radius of the arc segment.

Center
:   Specifies the center of the arc segment.

Length
:   Specifies the chord length of the arc segment. If the previous segment is an arc, the new arc segment is drawn tangent to
    the previous arc segment.

Close
:   Draws an arc segment from the last point specified to the starting point, creating a closed polyline. At least two points
    must be specified to use this option.

Direction
:   Specifies a starting direction for the arc segment.

Radius
:   Specifies the radius of the arc segment.

Second pt
:   Specifies the second point and endpoint of a three-point arc.

Length
:   Draws a line segment of a specified length at the same angle as the previous segment. If the previous segment is an arc, the
    new line segment is drawn tangent to that arc segment.

Undo
:   Removes the most recent arc segment added to the polyline.

Close
:   Draws an arc segment from the last point specified to the starting point, creating a closed polyline. At least two points
    must be specified to use this option.

## Mode

Determines whether the command always defaults to the Quick option. Otherwise, the last option used is the default.

#### Related Concepts

* [About Finding Distances, Angles, and Point Locations](About-Finding-Distances,-Angles,-and-Point-Locations.md)

#### Related Information

* [About Finding Area and Mass Properties Information](About-Finding-Area-and-Mass-Properties-Information.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*