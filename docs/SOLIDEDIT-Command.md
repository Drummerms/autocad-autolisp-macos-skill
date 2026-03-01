# SOLIDEDIT (Command)

Edits faces and edges of 3D solid objects.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid Edit - Face drop-down.
![](../images/GUID-FBFC80EC-0F9C-4BE3-9976-B081F4B4B11F-low.png)

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid Edit - Body drop-down.
![](../images/GUID-0E8EE4B1-8C10-4B1C-999D-88B0E75BC276-low.png)

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid Edit - Edge drop-down.
![](../images/GUID-D38EE01F-6646-42AF-BE45-7ACE70090076-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Solid Editing.

## Summary

You can extrude, move, rotate, offset, taper, copy, delete, and assign colors and materials to faces. You can also copy and
assign colors to edges. You can imprint, separate, shell, clean, and check the validity of the entire 3D solid object (*body*).

You cannot use SOLIDEDIT with mesh objects. However, if you select a closed mesh object, you will be prompted to convert it
to a 3D solid.

## List of Prompts

The following prompts are displayed.

Enter a solids editing option [Face/Edge/Body/Undo/Exit] <eXit>:

Face

Face

Edits selected 3D solid faces by extruding, moving, rotating, offsetting, tapering, deleting, copying, or changing their color.

Enter a face editing option [[Extrude](SOLIDEDIT-Command.md)/[Move](SOLIDEDIT-Command.md)/[Rotate](SOLIDEDIT-Command.md)/[Offset](SOLIDEDIT-Command.md)/[Taper](SOLIDEDIT-Command.md)/[Delete](SOLIDEDIT-Command.md)/[Copy](SOLIDEDIT-Command.md)/[coLor](SOLIDEDIT-Command.md)/[mAterial](SOLIDEDIT-Command.md)/[Undo](SOLIDEDIT-Command.md)/[eXit](SOLIDEDIT-Command.md)]:

Face: Extrude
![](../images/GUID-FBFC80EC-0F9C-4BE3-9976-B081F4B4B11F-low.png)

Extrude
:   Extends a 3D solid face in the
    *X*,
    *Y*, or
    *Z* direction. You can change the shape of the object by moving its faces.

    ![](../images/GUID-14329827-7BFB-4ED1-9B2D-D3086B724487-low.png)

    * *Select faces.* Specifies which faces to modify.
    * [Undo](SOLIDEDIT-Command.md)
    * [Remove](SOLIDEDIT-Command.md)

Remove
:   Removes previously selected faces from the selection set.

    * *Remove faces.* Removes the selected face from the solid object.
    * [Undo](SOLIDEDIT-Command.md)
    * [Add](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Undo
:   Cancels the selection of the faces you added most recently to the selection set and redisplays the prompt.

    ![](../images/GUID-04DC9BF0-C7BC-4199-8A85-CAE1CC7EFD27-low.png)

Add
:   Adds faces you select to the selection set.

    ![](../images/GUID-676A9187-CFEA-455C-AB86-DB4740EFEF19-low.png)

    * [Undo](SOLIDEDIT-Command.md)
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

All
:   Selects all faces and adds them to the selection set.

    ![](../images/GUID-D0F7699A-15FD-4F6A-A780-E4BD9EEF38DC-low.png)

    * *Select faces.* Selects specific faces (instead of all of them).
    * [Undo](SOLIDEDIT-Command.md)
    * [Remove](SOLIDEDIT-Command.md)

Height of extrusion
:   Sets the direction and distance of the extrusion. Entering a positive value extrudes the face in the direction of its normal.
    Entering a negative value extrudes the face in the direction opposite to its normal.

    * *Angle of taper for extrusion.*Specify an angle between -90 and +90 degrees.

      ![](../images/GUID-BF90D687-E181-40BB-99AD-D7F486E58241-low.png)

      Tapering the selected face with a positive angle tapers the face in, and a negative angle tapers the face out. The default
      angle, 0, extrudes the face perpendicular to its plane. All selected faces in the selection set are tapered to the same value.
      If you specify a large taper angle or height, you can cause the face to taper to a point before it reaches the extrusion height.

Path
:   Sets a path for the extrusion path based on a specified line or curve. All the profiles of the selected face are extruded
    along the chosen path to create the extrusion.

    * *Select an extrusion path.*

      ![](../images/GUID-E12F71FB-4F16-4CFB-B6C5-F77192E4A427-low.png)

      Lines, circles, arcs, ellipses, elliptical arcs, polylines, or splines can be paths. The path should not lie on the same plane
      as the face, nor should it have areas of high curvature.

      The extruded face starts from the plane of the profile and ends on a plane perpendicular to the path at the path's endpoint.
      One of the endpoints of the path should be on the plane of the profile; if not, the path is moved to the center of the profile.

      If the path is a spline, the path should be perpendicular to the plane of the profile and at one of the endpoints of the path.
      If not, the profile is rotated to be perpendicular to the spline path. If one of the endpoints of the spline is on the plane
      of the face, the face is rotated about the point; otherwise, the spline path is moved to the center of the profile and the
      profiles are rotated about its center.

      If the path contains segments that are not tangent, the object is extruded along each segment and then the joint along the
      plane is mitred, bisecting the angle formed by the segments. If the path is closed, the profile lies on the miter plane. This
      allows the start and end sections of the solid to match up. If the profile is not on the miter plane, the path is rotated
      until it is on the miter plane.

Face: Move
![](../images/GUID-4269B1B5-9192-4FDD-86DC-0A8D416B5E90-low.png)

Move
:   Moves the selected face on a 3D solid object to a specified height or distance. You can select multiple faces at one time.

    ![](../images/GUID-996CADA6-0C8B-4ACE-A0EA-2781E85CB045-low.png)

    * [Select faces](SOLIDEDIT-Command.md)
    * *Undo.* Cancels selection of the faces that you selected most recently.
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

    You can change the shape of the object by moving its faces. This option is recommended for minor adjustments.

    ![](../images/GUID-7A9E8FB0-7B37-47C8-827E-B771C8CDD68B-low.gif)

Select faces
:   Specifies the face to be moved.

    * *Base point of displacement.* Sets the base point for the move. If you specify a single point, usually entered as a coordinate, and then press Enter, the
      coordinate is used as the new location.
    * *Second point of displacement.* Sets a displacement vector that indicates how far the selected face is moved and in what direction.

Face: Rotate
![](../images/GUID-8D61507C-EC5E-42E2-88C5-540FDDF605C6-low.png)

Rotate
:   Rotates one or more faces or a collection of features on a solid about a specified axis.

    You can change the shape of the object by rotating its faces. This option is recommended for minor adjustments.

    * [Select faces (rotate)](SOLIDEDIT-Command.md)
    * *Undo.* Cancels selection of the faces that you selected most recently.
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (rotate)
:   Rotates the face according to the specified angle and axis.

    In the drawing area, select one or more faces.

    * [Axis point](SOLIDEDIT-Command.md)
    * [Axis by object](SOLIDEDIT-Command.md)
    * [View](SOLIDEDIT-Command.md)
    * [Xaxis, Yaxis, Zaxis](SOLIDEDIT-Command.md)
    * [2Point](SOLIDEDIT-Command.md)

Axis point, 2Point
:   Sets two points to define the axis of rotation.

    ![](../images/GUID-BDB73A79-C5BD-44D8-B360-45D76AACAA78-low.png)

    Pressing Enter at the main Rotate prompt displays the following prompts. Specifying a point at the main prompt skips the prompt
    for the first point:

    * *First point on the rotation axis*. Sets the first point on the axis of revolution.
    * *Second point on the rotation axis*. Sets the second point on the axis.
      + [Rotation angle](SOLIDEDIT-Command.md)
      + [Reference](SOLIDEDIT-Command.md)

Axis by object
:   Aligns the axis of rotation with an existing object. You can select the following objects:

    * *Line:* Aligns the axis with the selected line.
    * *Circle:* Aligns with the 3D axis of the circle (perpendicular to the plane of the circle and passing through the center of the circle).
    * *Arc:* Aligns with the 3D axis of the arc (perpendicular to the plane of the arc and passing through the center of the arc).
    * *Ellipse:* Aligns with the 3D axis of the ellipse (perpendicular to the plane of the ellipse and passing through the center of the ellipse).
    * *2D polyline:* Aligns with the 3D axis formed by the polyline start points and endpoints.
    * *3D polyline:* Aligns with the 3D axis formed by the polyline start points and endpoints.
    * *Spline:* Aligns with the 3D axis formed by the spline's start points and endpoints.

View
:   Aligns the axis of rotation with the viewing direction of the current viewport that passes through the selected point.

    * [Origin of rotation](SOLIDEDIT-Command.md)
      + [Rotation angle](SOLIDEDIT-Command.md)
      + [Reference](SOLIDEDIT-Command.md)

Xaxis, Yaxis, Zaxis
:   Aligns the axis of rotation with the axis (*X*,
    *Y*, or
    *Z*) that passes through the selected point.

    * [Origin of rotation](SOLIDEDIT-Command.md)
      + [Rotation angle](SOLIDEDIT-Command.md)
      + [Reference](SOLIDEDIT-Command.md)

Origin of rotation
:   Sets the point of rotation.

    * [Rotation angle](SOLIDEDIT-Command.md)
    * [Reference](SOLIDEDIT-Command.md)

Rotation angle
:   Rotates the object about the selected axis the specified amount from the current orientation.

Reference
:   Specifies the reference angle and the new angle.

    * *Reference (starting) angle.*Sets the start point for the angle.
    * *Ending angle.*Sets the endpoint for the angle. The difference between the starting angle and the ending angle is the computed rotation angle.

Face: Offset
![](../images/GUID-F154409E-3C47-47B1-862C-ED3B473F9875-low.png)

Offset
:   Offsets faces equally by a specified distance or through a specified point. A positive value increases the size or volume
    of the solid. A negative value decreases the size or volume of the solid.

    * [Select faces (offset)](SOLIDEDIT-Command.md)
    * [Undo](SOLIDEDIT-Command.md)
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (offset)
:   Specifies the faces you want to offset.

    NOTE:The size of holes inside a solid object that is offset decreases as the volume of the solid increases.

    ![](../images/GUID-D7689E44-DF65-48CD-BF90-B3586F511515-low.png)

    * *Specify the offset distance.*Sets a positive value to increase the size of the solid or a negative value to decrease the size of the solid.

Face: Taper
![](../images/GUID-08D599BE-62B5-4351-8EA7-3D4E5C4B6B7E-low.png)

Taper
:   Tapers faces on a 3D solid at a specified angle. The rotation of the taper angle is determined by the selection sequence of
    the base point and second point along the selected vector.

    ![](../images/GUID-42E6705C-736C-41D4-A6B0-896EEF658EC5-low.png)

    A positive angle tapers the face in, and a negative angle tapers the face out. The default angle, 0, extrudes the face perpendicular
    to its plane. All selected faces in the selection set are tapered to the same value.

    ![](../images/GUID-FBF3FE76-D6D1-491E-A1EA-28A249DA107C-low.gif)

    * [Select faces (taper)](SOLIDEDIT-Command.md)
    * [Undo](SOLIDEDIT-Command.md)
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (taper)
:   Specifies the faces to be tapered and then sets the slope of the taper.

    * *Base point.* Sets the first point for determining the plane.
    * *Another point along the axis of tapering.* Sets the orientation of the axis that determines the direction of the taper.
    * *Taper angle.*Specify an angle between -90 and +90 degrees to set the slope of the taper from the axis.

Face: Delete
![](../images/GUID-5BE423D7-8E74-43DA-8C15-F09B96B64457-low.png)

Delete
:   Deletes or removes faces, including fillets and chamfers.

    Use this option to remove and later modify filleted and chamfered edges. The face is not deleted if the change results in
    a non-valid 3D solid.

    ![](../images/GUID-E30B32BD-C4A0-4A77-B7C7-3E921AB2C5F2-low.png)

    * [Select faces (copy)](SOLIDEDIT-Command.md)
    * *Undo*. Cancels the selection of the faces that you selected most recently.
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (delete)
:   Specifies the face to be removed. The face must be in a location that can be filled by surrounding faces after it is removed.

Face: Copy
![](../images/GUID-2DDE5972-9C21-4365-B5CB-C8979CD9AAA2-low.png)

Copy
:   Copies faces as a region or a body. If you specify two points, SOLIDEDIT uses the first point as a base point and places a
    single copy relative to the base point. If you specify a single point (usually entered as a coordinate) and then press Enter,
    SOLIDEDIT uses the coordinate as the new location.

    ![](../images/GUID-D2BAA646-2897-48AD-9C98-48278E7B61D9-low.png)

    Creates a new object with the original orientation and profile of the face. The result can be used as a reference to create
    a new 3D solid.

    * [Select faces (copy)](SOLIDEDIT-Command.md)
    * *Undo*. Cancels the selection of the faces that you selected most recently.
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (copy)
:   Specifies the face to be copied.

    * *Base point or displacement.*Sets the first point to determine the distance and direction for the placement of the copied face (displacement).
    * *Second point of displacement.*Sets the second displacement point.

Face: Color
![](../images/GUID-379D3B45-9BD0-4EBF-AB1D-D162E9967197-low.png)

Color
:   Changes the color of faces.

    Colored faces can be used to highlight details within a complex 3D solid model.

    * [Select faces (color)](SOLIDEDIT-Command.md)
    * *Undo*. Cancels the selection of the faces that you selected most recently.
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (color)
:   Specifies the faces to be modified. The
    [Color Palette dialog box](Color-Palette-Dialog-Box.md) is displayed.

Face: Material

Material
:   Assigns a material to selected faces.

    * [Select faces (material)](SOLIDEDIT-Command.md)
    * *Undo*. Cancels the selection of the faces that you selected most recently.
    * [Remove](SOLIDEDIT-Command.md)
    * [All](SOLIDEDIT-Command.md)

Select faces (material)
:   Specifies the faces to be modified. The
    [Color Palette dialog box](Color-Palette-Dialog-Box.md) is displayed.

    * *Enter new material name.*Enter the name of the material to be assigned to the selected face. (The name of a material can be found by opening the Materials
      window and selecting the material swatch to display the name in the Name field.)
    * *ByLayer.* Assigns the material based on the layer assignment.

Face: Undo

Reverses actions as far back as the beginning of the SOLIDEDIT session.

Face: Exit

Exits the face-editing options and displays the Enter a Solids Editing Option prompt.

Edge

Edge

Edits 3D solid objects by changing the color of or copying individual edges.

Enter an edge editing option [[Copy](SOLIDEDIT-Command.md)/[coLor](SOLIDEDIT-Command.md)/[Undo](SOLIDEDIT-Command.md)/[eXit](SOLIDEDIT-Command.md)] <eXit>:

Edge: Copy
![](../images/GUID-BE5C89F4-8E7A-4FCD-86BB-0FBCF80373E7-low.png)

Copies selected edges on a 3D solid as 2D arcs, circles, ellipses, lines, or splines.

![](../images/GUID-849CA9C5-021F-42C0-84EC-3771EB3B11F3-low.png)

Retains the angle of the edge and allows you to make modifications and extensions, and create new geometry based on the extracted
edge.

Provides a method for making modifications, extensions, and new 3D solids based on the extracted edge.

* [Select Edges (copy)](SOLIDEDIT-Command.md)
* [Undo](SOLIDEDIT-Command.md)
* [Remove](SOLIDEDIT-Command.md)

Select Edges (copy)
:   Specifies the edges to copy. Press Ctrl+click to select the edge. Then set the displacement:

    * *Base point of displacement.*Sets the first point for determining where the new object is placed.
    * *Second point of displacement.*Sets the relative direction and distance for the new object.

Undo
:   Cancels selection of the edges you added most recently to the selection set. The previous prompt is displayed. If all edges
    have been removed, the following prompt is displayed:

Remove
:   Removes previously selected edges from the selection set. The prompt is redisplayed.

    * Remove edges. Removes the edges you select from the current selection set.
    * [Undo](SOLIDEDIT-Command.md)
    * [Add](SOLIDEDIT-Command.md)

Add
:   Adds edges to the selection set.

    * [Select Edges (copy)](SOLIDEDIT-Command.md)
    * [Undo](SOLIDEDIT-Command.md)
    * [Remove](SOLIDEDIT-Command.md)

Edge: Color
![](../images/GUID-823F9D5E-DD33-4DD1-9018-E1790A7BE2A2-low.png)

Changes the color of individual edges on a 3D solid object.

* [Select edges (color)](SOLIDEDIT-Command.md)
* [Undo](SOLIDEDIT-Command.md)
* [Remove](SOLIDEDIT-Command.md)

Select edges (color)
:   Colored edges can be used to highlight intersections, interferences, or critical clearances.

    Press Ctrl+click to select the edge.

Edge: Undo

Reverses actions as far back as the beginning of the SOLIDEDIT session.

Edge: Exit

Exits the face-editing options and displays the Enter a Solids Editing Option prompt.

Body

Body

Edits the entire solid object by imprinting other geometry on the solid, separating the solid into individual solid objects,
shelling, cleaning, or checking the selected solid.

Enter a body editing option [[Imprint](SOLIDEDIT-Command.md)/[seParate solids](SOLIDEDIT-Command.md)/[Shell](SOLIDEDIT-Command.md)/[cLean](SOLIDEDIT-Command.md)/[Check](SOLIDEDIT-Command.md)/[Undo](SOLIDEDIT-Command.md)/[eXit](SOLIDEDIT-Command.md)] <eXit>:

Body: Imprint
![](../images/GUID-C2408DF0-4EB3-4A5C-845C-33F2A8CFFAC0-low.png)

Imprints an object on the selected solid. The object to be imprinted must intersect one or more faces on the selected solid
in order for imprinting to be successful. Imprinting is limited to the following objects: arcs, circles, lines, 2D and 3D
polylines, ellipses, splines, regions, bodies, and 3D solids.

![](../images/GUID-08A4B542-BCB8-44B6-870E-137378253EB5-low.png)

* *Select a 3D solid.* Specifies the 3D solid to be imprinted.
* *Select an object to imprint.* Specifies an object that overlaps the first selection.
* *Delete the source object.* Specifies whether the object to imprint is removed when the operation is complete.

Body: Separate Solids
![](../images/GUID-1A44467C-21B8-47D3-AA3C-3933AFA908CD-low.png)

Separates 3D solid objects with disjointed volumes (sometimes called
*lumps*) into independent 3D solid objects. Combining discrete solid objects using a union operation (UNION) can result in disjointed
volumes.

A union or subtract operation can result in a single 3D solid that consists of more than one continuous volume. You can separate
these volumes into independent 3D solids.

![](../images/GUID-65B49C37-71A8-44F1-9310-A779E5BB86FE-low.gif)

NOTE:Separating solids does not separate Boolean objects that form a single volume.

Select a 3D solid
:   Specifies the 3D solid object to separate. Press Ctrl+click to select the edge.

Body: Shell
![](../images/GUID-0E8EE4B1-8C10-4B1C-999D-88B0E75BC276-low.png)

Shelling creates a hollow, thin wall with a specified thickness. You can specify a constant wall thickness for all the faces.
You can also exclude faces from the shell by selecting them. A 3D solid can have only one shell. New faces are created by
offsetting existing ones outside their original positions.

It is recommended that you create a copy of a 3D solid before converting it into a shell. That way if you need to make significant
modification, use the original version and shell it again.

![](../images/GUID-93B090A1-E507-4543-9D8C-D677961F8008-low.png)

Select a 3D solid (shell)
:   Specifies a 3D solid.

    * *Remove faces.* Specifies the face subobjects to be removed when the object is shelled.
    * *Undo.*Reverses the last action.
    * *Add.*Press Ctrl+click an edge to indicate which faces to retain.
    * *All.*Temporarily selects all faces for removal. You can then use Add to add the faces you want to retain.

Enter the shell offset distance
:   Sets the size of the offset. Specify a positive value to create a shell to the inside perimeter of the solid. Specify a negative
    value to create a shell on the outside perimeter of the solid.

Body: Clean
![](../images/GUID-C5969237-EEEB-4845-85F6-91FE3C824182-low.png)

Removes shared edges or vertices having the same surface or curve definition on either side of the edge or vertex. Removes
all redundant edges, vertices, and unused geometry. Does not remove imprinted edges.

In unusual circumstances, this option removes shared edges or vertices having the same surface or curve definition on either
side of the edge or vertex.

![](../images/GUID-D1912626-A72E-4807-BE60-06C20D4794A6-low.png)

Select a 3D solid (clean)
:   Specifies a 3D solid object that you want to clean.

Body: Check
![](../images/GUID-98EE866E-464D-49DF-84FE-5A069C57C7E5-low.png)

Validates the 3D solid object as a valid solid, independent of the
[SOLIDCHECK](SOLIDCHECK-System-Variable.md) setting.

* *Select a 3D object (check).* Specifies the 3D solid object to be validated. If the object is valid, the following prompt is displayed:

  This object is a valid ShapeManager solid.

This option is used as a debugging tool to compare stages in a highly complex 3D solid model.

Body: Undo

Undoes the editing action.

Body: Exit

Exits the face-editing options and displays the Enter a Solids Editing Option prompt.

Undo

Undo

Undoes the editing action.

Exit

Exit

Exits the SOLIDEDIT command.

#### Related Concepts

* [About Modifying Composite Solids and Surfaces](About-Modifying-Composite-Solids-and-Surfaces.md)
* [About Cleaning and Checking 3D Solids](About-Cleaning-and-Checking-3D-Solids.md)
* [About Modifying Faces on 3D Solids](About-Modifying-Faces-on-3D-Solids.md)
* [About Shelling 3D Solids](About-Shelling-3D-Solids.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*