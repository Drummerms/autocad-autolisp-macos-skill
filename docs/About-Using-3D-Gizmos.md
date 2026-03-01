# About Using 3D Gizmos

3D gizmos help you move, rotate, or scale a set of objects along a 3D axis or plane.

## How Gizmos Are Used

There are three types of gizmos:

* *3D Move gizmo.*  Relocates selected objects along an axis or plane.
* *3D Rotate gizmo.*  Rotates selected objects about a specified axis.
* *3D Scale gizmo.*  Scales selected objects along a specified plane or axis, or uniformly along all 3 axes.

![](../images/GUID-A67A1239-F373-43DF-A434-0763DC2930AE-low.png)

By default, gizmos are displayed automatically when you select an object or subobject in a view that has a 3D visual style.
Because they constrain modifications along specific planes or axes, gizmos help ensure more predictable results.

You can specify which gizmos are displayed when an object is selected, or you can suppress their display.

## Display the Gizmos

Gizmos are available only in 3D views that are set to use a 3D visual style such as Hidden. You can set the gizmo to be displayed
automatically when you select a 3D object or subobject. Gizmos are also displayed during the 3D Move, 3D Rotate, and 3D Scale
operations.

By default, the gizmo is initially placed in the center of the selection set. However, you can relocate it anywhere in 3D
space. The center box (or base grip) of the gizmo sets the base point for the modification. This behavior is equivalent to
temporarily changing the position of the UCS as you move or rotate the selected objects. The axis handles on the gizmo constrain
the movement or rotation to an axis or plane.

![](../images/GUID-1FEAC414-FDA0-4244-ACE6-6616FB2E10FE-low.png)

## Switch Between the Gizmos

Whenever you select an object in a 3D view, the default gizmo is displayed. You can change the value of the DEFAULTGIZMO
system variable. You can also suppress the display of gizmos when objects are selected.

After the gizmo is active, you can also switch to a different type of gizmo. The switching behavior differs, depending on
when you select the objects:

* *Select objects first.* If a gizmo operation is in progress, you can press the Spacebar repeatedly to cycle through the other gizmo types. When you
  switch gizmos this way, the gizmo activity is constrained to the originally selected axis or plane.

  During a gizmo operation, you can also select a different gizmo type on the shortcut menu.
* *Run the command first.* When you start the 3D Move, 3D Rotate, or 3D Scale operation before selecting objects, the gizmo is placed at the center
  of the selection set. Use the Relocate Gizmo option on the shortcut menu to relocate the gizmo anywhere in 3D space.You can
  also choose a different type of gizmo on the shortcut menu.

## Change the Gizmo Settings

The following settings affect the display of gizmos:

* *Default gizmo.* The DEFAULTGIZMO system variable specifies which gizmo is displayed by default when an object is selected in a view with
  a 3D visual style. You can turn off display of the gizmo.
* *Default location.* The GTLOCATION system variable sets the default location of the gizmo. The gizmo can be displayed at the center of the selection
  set (default), or it can be positioned at the 0,0,0 coordinates of the current UCS.
* *Automatic display.* The GTAUTO system variable sets whether gizmos are displayed automatically whenever you select objects in a 3D view that is
  set to a 3D visual style (default). If you turn off this system variable, the grips are not displayed until the gizmos are
  active.
* *Conversion of move, rotate, and scale operations from 2D to 3D.* Turn on the GTDEFAULT system variable to start the 3DMOVE, 3DROTATE, or 3DSCALE command automatically when the MOVE, ROTATE,
  or SCALE command is started in a 3D view. This system variable is turned off by default.
* *Active status of subobject grips.* If you select a subobject, the GRIPSUBOBJMODE system variable sets whether the subobject grips are active immediately. Setting
  subobject grips to be active upon selection helps you modify groups of mesh subobjects without selecting them again.

#### Related Tasks

* [To Work With 3D Gizmo Tools](To-Work-With-3D-Gizmo-Tools.md)
* [To Move 3D Objects Along a Plane or Axis](To-Move-3D-Objects-Along-a-Plane-or-Axis.md)
* [To Rotate 3D Objects Along an Axis](To-Rotate-3D-Objects-Along-an-Axis.md)
* [To Scale a 3D Object](To-Scale-a-3D-Object.md)

#### Related Concepts

* [About Moving 3D Objects](About-Moving-3D-Objects.md)
* [About Rotating 3D Objects](About-Rotating-3D-Objects.md)
* [About Scaling 3D Objects](About-Scaling-3D-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*