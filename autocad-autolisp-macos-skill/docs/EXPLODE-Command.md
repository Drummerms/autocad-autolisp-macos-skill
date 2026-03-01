# EXPLODE (Command)

Breaks a compound object into its component objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Explode.
![](../images/GUID-28962630-A678-4897-B2D0-D4B92429177D-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Explode.

Explodes a compound object when you want to modify its components separately. Objects that can be exploded include blocks,
polylines, and regions, among others.

![](../images/GUID-392D0FA5-6ADE-4EC4-B0C8-E81E3DAD870B-low.gif)

The color, linetype, and lineweight of any exploded object might change. Other results differ depending on the type of compound
object you're exploding. See the following list of objects that can be exploded and the results for each.

To explode objects and change their properties at the same time, use XPLODE.

NOTE:If you're using a script or an ObjectARX® function, you can explode only one object at a time. (Not applicable to AutoCAD LT.)

Here are the results of EXPLODE for each of the following types of objects:

2D Polyline
:   Discards any associated width or tangent information. For wide polylines, the resulting lines and arcs are placed along the
    center of the polyline.

    ![](../images/GUID-DC4FEF1D-0B1C-40AC-BC0B-3397F2552CEC-low.png)

3D Polyline
:   Explodes into line segments. Any linetype assigned to the 3D polyline is applied to each resulting line segment.

3D Solid
:   Explodes planar faces into regions.

    Nonplanar faces explode into surfaces. (Not applicable to AutoCAD LT.)

Annotative Objects
:   Explodes the current scale representation into its constituent parts which are no longer annotative. Other scale representations
    are removed.

Arc
:   If within a nonuniformly scaled block, explodes into elliptical arcs.

Array
:   Explodes an associative array into copies of the original objects.

Block
:   Removes one grouping level at a time. If a block contains a polyline or a nested block, exploding the block exposes the polyline
    or nested block object, which must then be exploded to expose its individual objects.

    Blocks with equal
    *X*,
    *Y*, and
    *Z* scales explode into their component objects. Blocks with unequal
    *X*,
    *Y*, and
    *Z* scales (nonuniformly scaled blocks) might explode into unexpected objects.

    When nonuniformly scaled blocks contain objects that cannot be exploded, they are collected into an anonymous block (named
    with a “\*E” prefix) and referenced with the nonuniform scaling. If all the objects in such a block cannot be exploded, the
    selected block reference will not be exploded. Body, 3D Solid, and Region entities in a nonuniformly scaled block cannot be
    exploded. (Not available in AutoCAD LT.)

    Exploding a block that contains attributes deletes the attribute values and redisplays the attribute definitions.

    Blocks inserted with external references (xrefs) and their dependent blocks cannot be exploded.

    Blocks inserted with MINSERT cannot be exploded. (MINSERT is not available in AutoCAD LT.)

Body
:   Explodes into a single-surface body (nonplanar surfaces), regions, or curves.

Circle
:   If within a nonuniformly scaled block, explodes into ellipses.

Leaders
:   Explodes into lines, splines, solids (arrow heads), block inserts (arrow heads, annotation blocks), multiline text, or tolerance
    objects, depending on the leader.

Mesh Objects
:   Explodes each face into a separate 3D face object. Color and materials assignments are retained. (Not available in AutoCAD
    LT.)

Multiline Text
:   Explodes into text objects.

Multiline
:   Explodes into lines and arcs.

Polyface Mesh
:   Explodes one-vertex meshes into a point object. Two-vertex meshes explode into a line. Three-vertex meshes explode into 3D
    faces.

Region
:   Explodes into lines, arcs, or splines.

#### Related Tasks

* [To Explode an Object](To-Explode-an-Object.md)

#### Related Concepts

* [About Breaking and Joining Objects](About-Breaking-and-Joining-Objects.md)
* [About Exploding Compound Objects](About-Exploding-Compound-Objects.md)
* [About Modifying Block References](About-Modifying-Block-References.md)

#### Related Information

* [About Polylines](About-Polylines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*