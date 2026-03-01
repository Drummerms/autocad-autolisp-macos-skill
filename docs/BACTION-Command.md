# BACTION (Command)

Adds an action to a dynamic block definition.

## Summary

This command is available only in the Block Editor. Actions define how the geometry of a dynamic block reference moves or
changes when the custom properties of a block reference are manipulated in a drawing. You associate actions with parameters.

## List of Prompts

The following prompts are displayed.

Select Parameter

Select a parameter in the block definition with which to associate the action.

You can associate parameters with the actions listed below.

Array

Adds an array action to the current dynamic block definition. An array action can be associated with a linear, polar, or XY
parameter. Specifies that the selection set of objects arrays when the action is triggered in a dynamic block reference.

Select Objects
:   Defines the objects that will be included in the action when modified.

Enter Distance Between Columns
:   When a linear or polar parameter is selected, specifies the distance between the selected objects when the array action is
    modified. To specify the distance, use the mouse pointer.

    * *Specify opposite corner.*

Enter Distance Between Rows or Specify Unit Cell
:   When an XY parameter is selected, specifies the distance between the selected objects when the array action is modified. To
    specify the distance, use the mouse pointer. To specify unit cell, enter two values separated by a comma for each of the two
    points.

Move

Specifies that the selection set of objects moves when the action is triggered in a dynamic block reference. A move action
can be associated with a point, linear, polar, or XY parameter.

Select Objects
:   Select the objects for the move action.

Specify Parameter Point
:   When a linear or polar parameter is selected, determines whether the start or end point of the parameter is used to determine
    the base point of the action.

    When an XY parameter is selected, determines which corner of the parameter will be associated with the action. The objects
    selected for the action will be moved relative to this point.

Multiplier
:   When BACTIONBARMODE is set to 0 and the action is triggered, changes the associated parameter value by the specified distance.

Offset
:   When BACTIONBARMODE is set to 0 and the action is triggered, increases or decreases the angle of the selected parameter by
    the specified value.

XY
:   When an XY parameter is selected, specifies whether the distance applied to the action is the parameter's *X* distance, *Y* distance, or *XY* distance from the parameter's base point.

Scale

Specifies that the selection set of objects scales relative to the defined base point when the action is triggered in a dynamic
block reference. A scale action can only be associated with a linear, polar, or XY parameter.

Select Objects
:   Specifies the objects to use for the scale action

Base Type
:   Specifies whether the base point for the action is dependent or independent of the associated parameter’s base point.

Dependent
:   Scales or moves selected objects relative to the base point of the associated parameter.

    ![](../images/GUID-9B36F30C-F443-4BCB-8136-B45E5C1DAC43-low.png)

Independent
:   Scales or moves selected objects relative to a base point defined separately from that of the associated parameter.

    ![](../images/GUID-37573537-E269-4BEC-841A-5E628CF7048F-low.png)

XY
:   When an XY parameter is selected, sets the *Scale Type* custom property.

    * **X.**  Scales the selected object only along the *X*-axis of the *XY* parameter.
    * **Y.**  Scales the selected object only along the *Y*-axis of the *XY* parameter.
    * **XY.**  Scales the selected object along both the *X*- and *Y*-axes of the *XY* parameter.

Stretch

Specifies that the selection set of objects will stretch or move when the action is triggered in a dynamic block reference.
A stretch action can be associated with a point, linear, polar, or XY parameter.

Specify Parameter Point
:   When a linear or polar parameter is selected, determines whether the start or end point of the parameter is used to determine
    the base point of the action.

    When an XY parameter is selected, determines which corner of the parameter will be associated with the action. The objects
    selected for the action will be stretched relative to this point.

First Corner of Stretch Frame
:   Creates a box that represents the boundary area for the action when modified.

    * *Specify opposite corner.* Sets the opposite boundary of the stretch frame.
    * *Specify objects.* Specifies the object to be included in the action.

CPolygon
:   Creates a polygon that represents the boundary area for the action when modified. Specify a series of points to define the
    boundary.

Select Objects
:   Specifies objects to use for the stretch operation.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*