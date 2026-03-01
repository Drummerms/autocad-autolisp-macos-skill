# Object Coordinate Systems (OCS) in DXF

To save space in the drawing database (and in the DXF file), the points associated with each entity are expressed in terms
of the entity's own object coordinate system (OCS). With OCS, the only additional information needed to describe the entity's
position in 3D space are the 3D vector describing the
*Z* axis of the OCS and the elevation value.

For a given
*Z* axis (or extrusion) direction, there are an infinite number of coordinate systems, defined by translating the origin in 3D
space and by rotating the
*X* and
*Y* axes around the
*Z* axis. However, for the same
*Z* axis direction, there is only one OCS. It has the following properties:

* Its origin coincides with the WCS origin.
* The orientation of the
  *X* and
  *Y* axes within the
  *XY* plane is calculated in an arbitrary but consistent manner. The
  AutoCAD program performs this calculation using the arbitrary axis algorithm (see Arbitrary Axis Algorithm).

For some entities, the OCS is equivalent to the WCS, and all points (DXF groups 10-37) are expressed in world coordinates.
See the following table.

| Coordinate systems associated with an entity type | |
| Entities | Notes |
| 3D entities such as line, point, 3dface, 3D polyline, 3D vertex, 3D mesh, 3D mesh vertex | These entities do not lie in a particular plane. All points are expressed in world coordinates. Of these entities, only lines and points can be extruded. Their extrusion direction can differ from the world *Z* axis |
| 2D entities such as circle, arc, solid, trace, text, attrib, attdef, shape, insert, 2D polyline, 2D vertex, lwpolyline, hatch, image | These entities are planar in nature. All points are expressed in object coordinates. These entities can be extruded. Their extrusion direction can differ from the world *Z* axis |
| Dimension | Some of a dimension's points are expressed in WCS and some in OCS |
| Viewport | Expressed in world coordinates |

Once the
AutoCAD program has established the OCS for a given entity, the OCS works as follows: The elevation value stored with an entity indicates
how far to shift the
*XY* plane along the
*Z* axis (from the WCS origin) to make it coincide with the plane that contains the entity. How much of this is the user-defined
elevation is unimportant.

Any 2D points entered through the UCS are transformed into the corresponding 2D points in the OCS, which is shifted and rotated
with respect to the UCS.

These are a few ramifications of this process:

* You cannot reliably find out what UCS was in effect when an entity was acquired.
* When you enter the
  *XY* coordinates of an entity in a given UCS and then do a SAVEAS, you probably won't recognize those
  *XY* coordinates in the DXF file. You must know the method by which the
  AutoCAD program calculates the
  *X* and
  *Y* axes in order to work with these values.
* The elevation value stored with an entity and output in DXF files is a sum of the
  *Z*-coordinate difference between the UCS
  *XY* plane and the OCS
  *XY* plane, and the elevation value that the user specified at the time the entity was drawn.

#### Related References

* [About Arbitrary Axis Algorithm (DXF)](About-Arbitrary-Axis-Algorithm-DXF.md)
* [About Advanced DXF Issues (DXF)](About-Advanced-DXF-Issues-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*