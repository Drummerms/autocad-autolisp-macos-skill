# MESHEXTRUDE (Command)

Extends a mesh face into 3D space.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Extrude Face.
![](../images/GUID-F47953AC-6298-46BA-8C8F-9F9E3C551507-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) Mesh Editing
![](../images/ac.menuaro.gif) Extrude Face.

## Summary

When you extrude, or extend, a mesh face, you can specify several options to determine the shape of the extrusion. You can
also determine whether extruding multiple mesh faces results in joined or separate extrusions.

![](../images/GUID-DB7C965B-EBF7-44A2-807B-C51B208A7C3A-low.gif)

## List of Prompts

The following prompts are displayed.

Mesh face(s) to extrude
:   Specifies the mesh faces to extrude. Click one or more faces to select them.

    * [Height of extrusion](MESHEXTRUDE-Command.md)
    * [Direction](MESHEXTRUDE-Command.md)
    * [Path](MESHEXTRUDE-Command.md)
    * [Taper angle](MESHEXTRUDE-Command.md)

Setting
:   (Available only when you start the command before selecting faces) Sets the style for extruding multiple adjacent mesh faces.

    * *Join adjacent mesh faces when extruding* Specifies whether adjacent mesh faces are extruded singly or as a unit. (The difference between the two options is not always
      apparent on a mesh that has not been smoothed.)
      + *Yes.* Extrudes all adjacent faces as a unit.

        ![](../images/GUID-0FA21183-59A6-4EFE-AFE0-6088965A304F-low.png)
      + *No.* Extrudes each adjacent face separately.

        ![](../images/GUID-EC4782A8-73A8-4BDD-A021-61E30B0EA77B-low.png)

Height of extrusion
:   Extrudes mesh faces along the
    *Z* axis. Enter a positive value to extrude the face along the positive
    *Z* axis. Enter a negative value to extrude along the negative
    *Z* axis. Multiple mesh faces do not need to be parallel to the same plane.

Direction
:   Specifies the length and direction of the extrusion. (The direction cannot be parallel to the plane of the sweep curve created
    by the extrusion.)

    * *Start point of direction.*Specifies the first point in the direction vector.
    * *End point of direction.* Specifies the second point in the direction vector.

Path
:   Specifies an object, such as a line or spline, that determines the path and length of the extrusion. The outline of the mesh
    face is swept along the path. The new orientation of the swept mesh face is perpendicular to the endpoint of the path.

    ![](../images/GUID-11B62E38-21FE-459A-AA4B-057411865181-low.png)

    The path should not lie on the same plane as the mesh face or have areas of high curvature. For extrusions that adhere closely
    to the curved path, use a spline, not an arced polyline, as the path.

Taper angle
:   Sets an angle of taper for an extrusion.

    ![](../images/GUID-059624B3-C30F-4592-88E7-950E95A66E1E-low.png)

    Positive angles taper inward from the base mesh face. Negative angles taper outward. The default angle, 0, extrudes the face
    perpendicular to the plane of the mesh.

    If the adjacent faces are not set to be joined, the faces that are selected for extrusion are tapered to the same value. However,
    for joined extrusions, the taper is applied only to the portion of the extrusion that is not adjacent to another extruded
    face.

    Specifying a large taper angle or a long extrusion height can cause the object or portions of the object to taper to a point
    before reaching the extrusion height.

    * *Angle of taper.* Sets an angle between -90 and +90 degrees.
    * *Specify two points.* Sets the taper angle to be the distance between two specified points.

#### Related Concepts

* [About Modifying Meshes](About-Modifying-Meshes.md)
* [About Modifying Mesh Faces](About-Modifying-Mesh-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*