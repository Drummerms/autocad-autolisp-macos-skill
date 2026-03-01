# About Fillets and Rounds

A fillet or round connects two objects with a tangent arc in 2D, or creates a rounded transition between the adjacent faces
of a 3D solid.

An inside corner is called a *fillet* and an outside corner is called a *round*; you can create both using the FILLET command.

![](../images/GUID-56284202-200C-4AEB-B7F8-68223BCFF6A2-low.png)

These object types can be selected to define a fillet or round:

* 2D polylines
* 3D solids and surfaces (not available in AutoCAD LT)
* Arcs
* Circles
* Ellipses and elliptical arcs
* Lines
* Rays
* Splines
* Xlines

![](../images/GUID-1BA80782-088C-4080-88EF-46C3F2A175FC-low.png)

NOTE:As an alternative to inserting an arc, the BLEND command can be used to connect two objects with a tangent spline.

## Add Fillets or Rounds to 2D Polylines

A fillet or round can be inserted at a single vertex or all the vertices of a 2D polyline using a single command. Use the
Polyline option add a fillet or round to each vertex of a polyline.

![](../images/GUID-8EF70416-51BE-44AD-A661-317EF591C164-low.png)

NOTE:The Multiple option can also be used to fillet or round more than one set of objects without exiting the command.

You add a fillet or round to a polyline by setting the current fillet radius to a nonzero value and selecting two line segments
that intersect. The distance between the selected line segments must be long enough to accommodate the fillet radius, otherwise
the arc will not be inserted. If the selected line segments are separated by an arc segment, the arc segment is removed and
replaced with the new arc segment.

When the current fillet radius is set to 0 and the two line segments selected are separated by an arc segment, the arc segment
is removed and the two line segments are extended until they intersect.

NOTE:Filleting the start and end segments of an open polyline results in a closed polyline.

## Round Parallel Lines

A round can be created tangent to two parallel lines, rays, or xlines. The current fillet radius is ignored and adjusted to
the distance that is between the two selected objects. The selected objects must be located on the same plane.

The first selected object must be a line or ray, while the second object can be a line, a ray, or an xline.

![](../images/GUID-DBEAB0E1-C374-42B4-A610-FBE9676953AE-low.png)

## Trim and Extend Objects

By default, the objects selected to define a fillet or round are trimmed or extended to the resulting arc. You can use the
Trim option to specify whether the selected objects are changed or left unchanged.

![](../images/GUID-A7527DE9-2DD7-4386-836C-88E3EB450DE4-low.png)

If the Trim option is enabled and two line segments of a polyline are selected, the fillet or round added is joined with the
polyline as an arc segment.

#### Related Concepts

* [About Chamfers and Bevels](About-Chamfers-and-Bevels.md)

#### Related Information

* [To Work With 2D Fillets and Rounds](To-Work-With-2D-Fillets-and-Rounds.md)
* [To Work With 2D Chamfers and Bevels](To-Work-With-2D-Chamfers-and-Bevels.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*