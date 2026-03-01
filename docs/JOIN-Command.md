# JOIN (Command)

Joins the endpoints of linear and curved objects to create a single object.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Join.
![](../images/GUID-38F47CB9-9733-4D1D-BADA-90F06D37CAC1-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Join.

Combines a series of finite linear and open curved objects at their common endpoints to create a single 2D or 3D object.
The type of object that results depends on the types of objects selected, the type of object selected first, and whether the
objects are coplanar.

![](../images/GUID-FC746C89-1BCE-483D-BAF1-49A2AE954139-low.gif)

NOTE: Construction lines, rays, and closed objects cannot be joined.

The following prompts are displayed.

Select source object or multiple objects to join at once:
:   Select lines, polylines, 3D polylines, arcs, elliptical arcs, helixes, or splines.

## Source object

Specifies a single source object to which you can join other objects. Press Enter after selecting the source object to begin
selecting the objects to join. The following rules apply for each type of source object:

Line
:   Only line objects can be joined to the source line. The line objects must all be collinear, but can have gaps between them.

Polyline
:   Lines, polylines, and arcs can be joined to the source polyline. All objects must be contiguous and coplanar. The resulting
    object is a single polyline.

3D Polyline
:   Any linear or curved object can be joined to the source 3D polyline. All the objects must be contiguous, but can be noncoplanar.
    The resulting object is either a single 3D polyline or a single spline, depending on whether you are joining to a linear or
    a curved object respectively.

Arc
:   Only arcs can be joined to the source arc. All the arc objects must have the same radius and center point, but can have gaps
    between them. The arcs are joined in a counterclockwise direction starting from the source arc.

    The Close option converts the source arc into a circle.

Elliptical Arc
:   Only elliptical arcs can be joined to the source elliptical arc. The elliptical arcs must be coplanar and have the same major
    and minor axes, but can have gaps between them. The elliptical arcs are joined counterclockwise starting from the source elliptical
    arc.

    The Close option converts the source elliptical arc into an ellipse.

Helix
:   Any linear or curved object can be joined to the source helix. All objects must be contiguous, but can be noncoplanar. The
    resulting object is a single spline.

Spline
:   Any linear or curved object can be joined to the source spline. All objects must be contiguous, but can be noncoplanar. The
    resulting object is a single spline.

## Multiple objects to join at once

Joins multiple objects without specifying a source object. The rules and resulting object types are as follows:

* A line object results from joining collinear lines. The lines can have gaps between their endpoints.
* An arc or circle object results from joining coplanar arcs with the same center point and radius. The arcs can have gaps between
  their endpoints. Lengthening occurs in a counterclockwise direction. A circle object results if the joined arcs form a complete
  circle.
* A spline object results from joining splines, elliptical arcs, or helixes together, or to other objects. The objects can be
  noncoplanar.
* A polyline object results from joining coplanar lines, arcs, polylines, or 3D polylines.
* A 3D polyline results from joining noncoplanar objects other than curved objects.

#### Related Information

* [About Breaking and Joining Objects](About-Breaking-and-Joining-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*