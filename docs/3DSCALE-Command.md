# 3DSCALE (Command)

In a 3D view, displays the 3D Scale gizmo to aid in resizing 3D objects.

## Summary

With the 3D Scale gizmo, you can resize selected objects and subobjects along an axis or plane, or resize the objects uniformly.

When the 3D Scale gizmo is displayed, the
[3D Scale Gizmo shortcut menu](3D-Scale-Gizmo-Shortcut-Menu.md) offers options for aligning, moving, or changing to another gizmo.

## List of Prompts

The following prompts are displayed.

Select objects
:   Specifies the objects to be scaled.

Specify base point
:   Specifies the base point for the scaling.

Pick a scale axis or plane
:   Specifies whether the object is scaled uniformly or only along a specific axis or plane. You have the following choices:

    * *Scale uniformly.* Click the area closest to the vertex of the 3D Scale gizmo. The interior region of all axes of the gizmo is highlighted.

      ![](../images/GUID-DD4E2004-E4F2-483E-AB31-4E49B3F44FE9-low.png)
    * *Constrain the scale to a plane.* Click between the parallel lines between the axes that define the plane. This option is only available for meshes, not solids
      or surfaces.

      ![](../images/GUID-4F607D35-5266-4D0D-9010-C818EAE840EB-low.png)
    * *Constrain the scale to an axis.* Click the axis. This option is only available for meshes, not solids or surfaces.

      ![](../images/GUID-AC2B411B-236E-43DC-872A-00C3F7379906-low.png)

Specify scale factor
:   Specifies the amount of change. Drag to dynamically modify the size of the selected objects or enter a scale value. For example,
    enter 2 to double the size of the selection.

Copy
:   Creates and scales a copy of the selected objects.

Reference
:   Sets a scale based on a ratio.

    * *Reference length.* Sets the relative amount that represents the current size in the scale ratio.
    * *New Length.*Sets the relative value used to calculate the new size. For example, if the reference length is 1 and the new length is 3,
      the size of the selected objects is tripled.
    * *Points.* Specifies the relative value used to calculate the new size based on two points that you specify.

#### Related References

* [3D Scale Gizmo Shortcut Menu](3D-Scale-Gizmo-Shortcut-Menu.md)

#### Related Concepts

* [About Moving, Rotating, and Scaling 3D Subobjects](About-Moving,-Rotating,-and-Scaling-3D-Subobjects.md)
* [About Moving, Rotating, and Scaling Faces on 3D Solids and Surfaces](About-Moving,-Rotating,-and-Scaling-Faces-on-3D-Solids-and-Surfaces.md)
* [About Scaling 3D Objects](About-Scaling-3D-Objects.md)
* [About Using 3D Gizmos](About-Using-3D-Gizmos.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*