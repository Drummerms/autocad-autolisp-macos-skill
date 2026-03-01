# Object Snap Tab (Drafting Settings Dialog Box)

Controls running object snap settings.

DSETTINGS (Command)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Drafting Settings.

![](../images/GUID-AD197814-7ADA-4740-94B0-0D12912C1751-low.png)

NOTE:The 3D Object Snap tab is not available in AutoCAD LT.

## Summary

With running object snap settings, also called Osnap, you can specify a snap point at an exact location on an object. When
more than one option is selected, the selected snap modes are applied to return a point closest to the center of the aperture
box. Press TAB to cycle through the options.

## List of Options

Object Snap On

With running object snaps, the object snaps selected under Object Snap Modes are active while specifying points on objects
when a command is in progress. (OSMODE system variable)

Object Snap Tracking On

With object snap tracking, the cursor can track along alignment paths based on current object snap modes when specifying points
in a command. (AUTOSNAP system variable)

Object Snap Modes

Lists object snaps that you can turn on as running object snaps.

Endpoint
:   Snaps to the closest endpoint or corner of a geometric object.

    ![](../images/GUID-819DE911-46D7-4662-9740-45EB83CA0624-low.png)

Midpoint
:   Snaps to the midpoint of a geometric object.

    ![](../images/GUID-CF8F741F-CD1E-4F4D-A61F-28CD4D59CAA3-low.png)

Center
:   Snaps to the center of an arc, circle, ellipse, or elliptical arc.

    ![](../images/GUID-A2124187-41E2-4F0D-890A-88E1301DCA04-low.png)

Geometric-Center
:   Snaps to the centroid of any closed polylines and splines.

    ![](../images/GUID-383CDE17-DA49-4125-8747-80F992469F08-low.png)

Node
:   Snaps to a point object, dimension definition point, or dimension text origin.

    ![](../images/GUID-33EB783E-76AE-4DB0-9D7F-15757E29EA75-low.png)

Quadrant
:   Snaps to a quadrant point of an arc, circle, ellipse, or elliptical arc.

    ![](../images/GUID-A0E327B3-EA78-4336-B754-39270B013717-low.png)

Intersection
:   Snaps to the intersection of geometric objects.

    Extended intersections as shown below are available only as overrides during a command, not as a running object snap.

    ![](../images/GUID-FB1FCA27-A38E-4CE8-A770-72C1B45E6EF7-low.png)

    Intersections and extended intersections do not work with edges or corners of 3D solids.

    NOTE: Results may vary if both the Intersection and Apparent Intersection running object snaps are turned on.

Extension
:   Causes a temporary extension line or arc to be displayed when you pass the cursor over the endpoint of objects, so you can
    specify points on the extension.

    NOTE: When working in perspective view, you cannot track along the extension line of an arc or elliptical arc.

Insertion
:   Snaps to the insertion point of objects such as an attribute, a block, or text.

Perpendicular
:   Snaps to a point perpendicular to the selected geometric object.

    Deferred Perpendicular snap mode is automatically turned on when the object you are drawing requires that you complete more
    than one perpendicular snap. You can use an object such as a line, arc, circle, polyline, ray, xline, multiline, or 3D solid
    edge as an object from which to draw a perpendicular line. You can use Deferred Perpendicular to draw perpendicular lines
    between such objects. When your cursor passes over a Deferred Perpendicular snap point, an AutoSnap™ tooltip and marker are displayed.

    ![](../images/GUID-46E577BB-C6B0-4C25-8910-0EB557164BE7-low.png)

Tangent
:   Snaps to the tangent of an arc, circle, ellipse, elliptical arc, polyline arc, or spline.

    Deferred Tangent snap mode is automatically turned on when the object you are drawing requires that you complete more than
    one tangent snap. You can use it to draw a line or xline that is tangent to arcs, polyline arcs, or circles. When your cursor
    passes over a Deferred Tangent snap point, a marker and an AutoSnap tooltip are displayed.

    ![](../images/GUID-9CEB48AF-ED26-4C19-A8B6-B812A403E687-low.png)

    NOTE: When you use the From option in conjunction with the Tangent snap mode to draw objects other than lines from arcs or circles,
    the first point drawn is tangent to the arc or circle in relation to the last point selected in the drawing area.

Nearest
:   Snaps to the nearest point on an object such as an arc, circle, ellipse, elliptical arc, line, point, polyline, ray, spline,
    or xline.

Apparent Intersection
:   Snaps to the visual intersection of two objects that do not intersect in 3D space but may appear to intersect in the current
    view.

    Extended Apparent Intersection snaps to the imaginary intersection of objects that would appear to intersect if the objects
    were extended along their natural paths. Apparent and Extended Apparent Intersection do not work with edges or corners of
    3D solids.

    NOTE: Results may vary if both the Intersection and Apparent Intersection running object snaps are turned on.

Parallel
:   Constrains a new line segment, polyline segment, ray or xline to be parallel to an existing linear object that you identify
    by hovering your cursor.

    After you specify the first point of a linear object, specify the parallel object snap. Unlike other object snap modes, you
    move the cursor and
    *hover* over another linear object until the angle is acquired. Then, move the cursor back toward the object that you are creating.
    When the path of the object is parallel to the previous linear object, an alignment path is displayed, which you can use to
    create the parallel object.

    NOTE: Turn off ORTHO mode before using the parallel object snap. Object snap tracking and polar snap are turned off automatically
    during a parallel object snap operation. You must specify the first point of a linear object before using the parallel object
    snap.

Select All
:   Turns on all running object snap modes.

Clear All
:   Turns off all running object snap modes.

#### Related Tasks

* [To Snap to a Geometric Location on an Object](To-Snap-to-a-Geometric-Location-on-an-Object.md)
* [To Display the Object Snap Menu](To-Display-the-Object-Snap-Menu.md)
* [To Set Running Object Snaps](To-Set-Running-Object-Snaps.md)
* [To Turn on and Turn off Running Object Snaps](To-Turn-on-and-Turn-off-Running-Object-Snaps.md)

#### Related References

* [Drafting Settings Dialog Box](Drafting-Settings-Dialog-Box.md)
* [DSETTINGS (Command)](DSETTINGS-Command.md)

#### Related Concepts

* [About Using Object Snaps](About-Using-Object-Snaps.md)
* [About Suppressing Running Object Snaps](About-Suppressing-Running-Object-Snaps.md)
* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*