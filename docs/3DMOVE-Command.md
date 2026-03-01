# 3DMOVE (Command)

In a 3D view, displays the 3D Move gizmo to aid in moving 3D objects a specified distance in a specified direction.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) 3D Move.
![](../images/GUID-683FBEA4-FF89-47F7-B7CE-81B57C391E37-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) 3D Operations ![](../images/ac.menuaro.gif) 3D Move.

## Summary

With the 3D Move gizmo, you can move selected objects and subobjects freely or constrain the movement to an axis or plane.

![](../images/GUID-75A048E4-9B34-483C-9770-1ED29F4894F0-low.gif)

If the default gizmo ([DEFAULTGIZMO](DEFAULTGIZMO-System-Variable.md)) is 3D Move, the 3D Move gizmo is displayed whenever you select an object in a view with a 3D visual style. If you are working
in a viewport with 2D Wireframe set as the visual style, 3DMOVE temporarily changes the visual style to 3D Wireframe for the
duration of the command.

The 3D Move gizmo is displayed at the center of the selected 3D object or objects by default. You can use the shortcut menu
to change its location.

You can also align the 3D Move gizmo with the plane of a face or object by using the Align Gizmo With ![](../images/ac.menuaro.gif) Face option on the shortcut menu. The direction of the move operation is then constrained relative to this work plane.

![](../images/GUID-A213E13E-E2E8-4EB5-A17F-6DD1CED92F98-low.png)

When the 3D Move gizmo is displayed, the
[3D Move Gizmo shortcut menu](3D-Move-Gizmo-Shortcut-Menu.md) offers options for aligning, moving, or changing to another gizmo.

## List of Prompts

The following prompts are displayed.

Select objects
:   Selects the 3D objects you want to move. When you have selected the objects, press Enter.

    When you have selected an object, the gizmo is displayed. You can constrain the movement by clicking one of the following
    locations on the gizmo:

    * *Move along an axis.* Click an axis to constrain the movement to that axis.

      ![](../images/GUID-5D06157A-1C9F-457F-BDB3-65919AC9A6C3-low.png)
    * *Move along a plane.*Click the area between the axes to constrain the movement to that plane.

      ![](../images/GUID-D675B783-00D9-45B8-8D18-E9D3988EE489-low.png)

Stretch point
:   When you are specifying the move using the gizmo, sets the new location of the selected objects. Drag and click to move the
    objects dynamically.

Copy
:   When you are specifying the move using the gizmo, creates a copy of the selected objects instead of moving them. You can make
    multiple copies by continuing to specify locations.

Base point
:   Specifies the base point of the 3D objects you want to move.

    * *Second point.* Specifies where the 3D object or objects will be dragged. You can also move the cursor to indicate a direction and then enter
      a distance.

Displacement
:   Specifies a relative distance and direction for the placement of the selected 3D objects using coordinate values that you
    enter at the command prompt.

#### Related References

* [3D Move Gizmo Shortcut Menu](3D-Move-Gizmo-Shortcut-Menu.md)

#### Related Concepts

* [About Moving 3D Objects](About-Moving-3D-Objects.md)
* [About Moving, Rotating, and Scaling 3D Subobjects](About-Moving,-Rotating,-and-Scaling-3D-Subobjects.md)
* [About Moving, Rotating, and Scaling Faces on 3D Solids and Surfaces](About-Moving,-Rotating,-and-Scaling-Faces-on-3D-Solids-and-Surfaces.md)
* [About Using 3D Gizmos](About-Using-3D-Gizmos.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*