# BACTIONTOOL (Command)

Adds an action to a dynamic block definition.

Add a screenshot just like Windows

## Summary

Actions define how the geometry of a dynamic block reference moves or changes when the custom properties of a block reference
are manipulated in a drawing. You associate actions with parameters. The BACTIONTOOL command is used within the Block Editor.

## List of Prompts

The following prompts are displayed.

Array

Also found on
Block Editor contextual tab
![](../images/ac.menuaro.gif) Action Parameters panel
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Array.
![](../images/GUID-5A59BD15-9752-4480-9E2C-842282575937-low.png)

Specifies that the selection set of objects arrays when the action is triggered in a dynamic block reference. An array action
can be associated with a linear, polar, or XY parameter.

Select Parameter
:   Select a parameter to associate with the action.

Select Objects
:   Defines the objects that will be included in the action when modified.

Distance Between Columns
:   When a linear or polar parameter is selected, specifies the distance between the selected objects when the array action is
    modified. To specify the distance, you can use the mouse pointer.

Distance Between Rows
:   When an XY parameter is selected, specifies the distance between the selected objects when the array action is modified. To
    specify the distance, use the mouse pointer. To specify unit cell, enter two values separated by a comma for each of the two
    points.

Flip

Also found on
Block Editor contextual tab
![](../images/ac.menuaro.gif) Action Parameters panel
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Flip.
![](../images/GUID-8ACFD79D-D630-40C6-A02F-2E39C34E8439-low.png)

A set of objects is flipped around the reflection line of the flip parameter when the action is triggered in the block reference.
A flip action can only be associated with a flip parameter.

Specify Selection Set
:   Determines the objects that will be mirrored about the flip parameter reflection line.

Move

Also found on
Block Editor contextual tab
![](../images/ac.menuaro.gif) Action Parameters panel
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Move.
![](../images/GUID-B7F73685-EFFA-4ECA-A3D7-3251FBC3C266-low.png)

Specifies that the selection set of objects moves when the action is triggered in a dynamic block reference. A move action
can be associated with a point, linear, polar, or XY parameter.

Select Parameter
:   Select the parameter to associate with the action.

Specify Parameter Point
:   When a linear or polar parameter is selected, determines whether the start or end point of the parameter is used to determine
    the base point of the action.

    When an XY parameter is selected, determines which corner of the parameter will be associated with the action. The objects
    selected for the action will be moved relative to this point.

XCorner
:   When an XCorner parameter is selected, it specifies whether the distance applied to the action is the parameter's
    *X* distance from the parameter's base point.

YCorner
:   When an YCorner parameter is selected, it specifies whether the distance applied to the action is the parameter's
    *Y* distance from the parameter's base point.

Rotate

Also found on
Block Editor contextual tab
![](../images/ac.menuaro.gif) Action Parameters panel
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Rotate.
![](../images/GUID-4F77A562-8EF4-427A-8C60-94875592F4F6-low.png)

Specifies that the selection set of objects rotates when the action is triggered in a dynamic block reference. A rotate action
can only be associated with a rotation parameter.

Select Parameter
:   Select the parameter to associate with the action.

Select Objects
:   Defines which objects to include in the action.

Base Type
:   Specifies whether the base point for the action is dependent or independent of the associated parameter’s base point.

Dependent
:   Scales or moves selected objects relative to the base point of the associated parameter.

    ![](../images/GUID-9B36F30C-F443-4BCB-8136-B45E5C1DAC43-low.png)

Independent
:   Scales or moves selected objects relative to a base point defined separately from that of the associated parameter.

    ![](../images/GUID-37573537-E269-4BEC-841A-5E628CF7048F-low.png)

Scale

Also found on
Block Editor contextual visor
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Scale.
![](../images/GUID-2C45E982-30CE-4EBF-A994-F006175D99CA-low.png)

Specifies that the selection set of objects scales relative to the defined base point when the action is triggered in a dynamic
block reference. A scale action can only be associated with a linear, polar, or XY parameter.

Select Parameter
:   Select the parameter to associate with the action.

Select Objects
:   Defines which objects to include in the action.

Base Type
:   Specifies whether the base point for the action is dependent or independent.

XY
:   When an XY parameter is selected, sets the
    *Scale Type* custom property.

    * **X.**  Scales the selected object only along the
      *X*-axis of the
      *XY* parameter.
    * **Y.**  Scales the selected object only along the
      *Y*-axis of the
      *XY* parameter.
    * **XY.**  Scales the selected object along both the
      *X*- and
      *Y*-axes of the
      *XY* parameter.

Stretch

Also found on
Block Editor contextual visor
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Stretch.
![](../images/GUID-3AEDE473-6BB1-44F1-A317-8FBFE6BC9A42-low.png)

Specifies that the selection set of objects will stretch or move when the action is triggered in a dynamic block reference.
A stretch action can be associated with a point, linear, polar, or XY parameter.

Select Parameter
:   Select the parameter to associate with the action.

Specify Parameter Point
:   When a linear or polar parameter is selected, determines whether the start or end point of the parameter is used to determine
    the base point of the action.

    When an XY parameter is selected, determines which corner of the parameter will be associated with the action. The objects
    selected for the action will be stretched relative to this point.

Specify Stretch Frame
:   Creates a box that represents the boundary area for the action when modified.

CPolygon
:   Creates a polygon that represents the boundary area for the action when modified.

Select Objects
:   Defines which objects to include in the action.

Polar Stretch

Also found on
Block Editor contextual visor
![](../images/ac.menuaro.gif) Actions drop-down
![](../images/ac.menuaro.gif) Polar Stretch.
![](../images/GUID-1BB5278F-6640-4914-968A-C6BF6DA032F8-low.png)

Specifies that the selection set of objects stretches or moves when the action is triggered in a dynamic block reference.
A polar stretch action can only be associated with a polar parameter.

Select Parameter
:   Select the parameter to associate with the action.

Specify Parameter PointSpecify Parameter Point
:   Determines whether the start or end point of the parameter is used to determine the base point of the action.

    Determines whether the start or end point of the parameter is used to determine the base point of the action.

Specify Stretch Frame
:   Creates a box that represents the boundary area for the action when modified.

CPolygon
:   Creates a polygon that represents the boundary area for the action when modified.

Specify Objects to Rotate Only
:   Determines the objects in the selection that will rotate and not stretch.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*