# Block Editor

The Block Editor contains a special authoring area in which you can draw and edit geometry as you would in the drawing area.

## Summary

You use the Block Editor to define the objects and behavior for a block definition.

The following commands are used for editing blocks and are available only in the Block Editor:

* BACTION
* BACTIONBAR
* BACTIONSET
* BACTIONTOOL
* BATTORDER
* BCLOSE
* BGRIPSET
* BPARAMETER
* BSAVE
* BSAVEAS
* BVHIDE
* BVSHOW
* BVSTATE

When the BLOCKEDITLOCK system variable is set to 1, the Block Editor cannot be opened.

## Block Editor Visor

Provides tools for adding attributes to the block open for edit, save changes to a block, and close the Block Editor.

Name
:   Displays the name of the current block definition.

Define Attribute (ATTDEF)
:   Creates an attribute definition for storing data in a block.

Add Parameter (BPARAMETER)
:   Adds a parameter with grips to a dynamic block definition.

Add Action (BACTIONTOOL)
:   Adds an action to a dynamic block definition.

Manage Visibility States (BVSTATE)
:   Creates, sets, or deletes a visibility state in a dynamic block.

    When a visibility parameter doesn't exist in the dynamic block definition, this control allows you to add one and then you
    can define its custom visibility properties for the block reference. With a visibility parameter, you can create visibility
    states and control the visibility of objects in the block. A visibility parameter always applies to the entire block and needs
    no action associated with it. In a drawing, you click the grip to display a list of visibility states available for the block
    reference. In the Block Editor, a visibility parameter displays as text with an associated grip.

Toggle Visibility Mode (BVMODE)
:   Controls how objects that are made invisible for the current visibility state are displayed in the Block Editor.

Make Visible (BVSHOW)
:   Makes objects visible in the current visibility state or all visibility states in a dynamic block definition.

Make Invisible (BVHIDE)
:   Makes objects invisible in the current visibility state or all visibility states in a dynamic block definition.

Save (BSAVE)
:   Saves the current block definition.

Save New (BSAVEAS)
:   Saves a copy of the current block definition under a new name.

Close (BCLOSE)
:   Closes the Block Editor.

## Add Parameter Drop-down List (BPARAMETER)

Provides tools for adding parameters to a dynamic block definition in the Block Editor. Parameters specify positions, distances,
and angles for geometry in the block reference. When you add a parameter to a dynamic block definition, it defines one or
more custom properties for the block.

NOTE:Lookup parameters are defined as part of an existing block definition are supported, but they can't be added to a dynamic
block definition using the Block Editor on Mac.

Point
:   Adds a point parameter to the dynamic block definition and defines custom
    *X* and
    *Y* properties for the block reference. A point parameter defines an
    *X* and
    *Y* location in the drawing. In the Block Editor, a point parameter looks similar to an ordinate dimension.

Linear
:   Adds a linear parameter to the dynamic block definition and defines a custom distance property for the block reference. A
    linear parameter shows the distance between two anchor points. A linear parameter constrains grip movement along a preset
    angle. In the Block Editor, a linear parameter looks similar to an aligned dimension.

Polar
:   Adds a polar parameter to the dynamic block definition and defines custom distance and angle properties for the block reference.
    A polar parameter shows the distance between two anchor points and displays an angle value. You can use both grips and the
    Properties palette to change both the distance value and the angle. In the Block Editor, a polar parameter looks similar to
    an aligned dimension.

XY
:   Adds an XY parameter to the dynamic block definition and defines custom horizontal and vertical distance properties for the
    block reference. An XY parameter shows the
    *X* and
    *Y* distances from the base point of the parameter. In the Block Editor, an XY parameter displays as a pair of dimensions (horizontal
    and vertical). These dimensions share a common base point.

Rotation
:   Adds a rotation parameter to the dynamic block definition and defines a custom angle property for the block reference. A rotation
    parameter defines an angle. In the Block Editor, a rotation parameter displays as a circle.

Alignment
:   Adds an alignment parameter to the dynamic block definition. An alignment parameter defines an
    *X* and
    *Y* location and an angle. An alignment parameter always applies to the entire block and needs no action associated with it.
    An alignment parameter allows the block reference to automatically rotate around a point to align with other objects in the
    drawing. An alignment parameter affects the angle property of the block reference. In the Block Editor, an alignment parameter
    looks like an alignment line.

Flip
:   Adds a flip parameter to the dynamic block definition and defines a custom flip property for the block reference. A flip parameter
    flips objects. In the Block Editor, a flip parameter displays as a reflection line. Objects can be flipped about this reflection
    line. A flip parameter displays a value that shows if the block reference has been flipped or not.

Base Point
:   Adds a base point parameter to the dynamic block definition. A base point parameter defines a base point for the dynamic block
    reference relative to the geometry in the block. A base point parameter cannot be associated with any actions, but can belong
    to an action's selection set. In the Block Editor, a base point parameter displays as a circle with crosshairs

## Add Action Drop-down List (BACTIONTOOL)

Provides tools for adding actions to a dynamic block definition in the Block Editor. Actions define how the geometry of a
dynamic block reference move or change when the custom properties of a block reference are manipulated in a drawing. You associate
actions with parameters.

Move
:   Adds a move action to the dynamic block definition when you associate the action with a point, linear, polar, or XY parameter.
    A move action is similar to the
    MOVE command. In a dynamic block reference, a move action causes objects to move a specified distance and angle.

Scale
:   Adds a scale action to the dynamic block definition when you associate the action with a linear, polar, or XY parameter. A
    scale action is similar to the
    SCALE command. In a dynamic block reference, a scale action causes its selection set to scale when the associated parameter is
    edited by moving grips or by using the Properties palette.

Stretch
:   Adds a stretch action to the dynamic block definition when you associate the action with a point, linear, polar, or XY parameter.
    A stretch action causes objects to move and stretch a specified distance in a specified location.

Polar Stretch
:   Adds a polar stretch action to the dynamic block definition when you associate the action with a polar parameter. A polar
    stretch action rotates, moves, and stretches objects a specified angle and distance when the key point on the associated polar
    parameter is changed through a grip or the Properties palette

Rotate
:   Adds a rotate action to the dynamic block definition when you associate the action with a rotation parameter. A rotate action
    is similar to the
    ROTATE command. In a dynamic block reference, a rotate action causes its associated objects to rotate when the associated parameter
    is edited through a grip or the Properties palette.

Flip
:   Adds a flip action to the dynamic block definition when you associate the action with a flip parameter. With a flip action
    you can flip a dynamic block reference about a specified axis called a reflection line similar to using the
    [MIRROR](MIRROR-Command.md) command.

Array
:   Adds an array action to the dynamic block definition when you associate the action with a linear, polar, or XY parameter.
    An array action causes its associated objects to copy and array in a rectangular pattern when the associated parameter is
    edited through a grip or the Properties palette.

#### Related References

* [PARAMETERS Command (-PARAMETERS)](PARAMETERS-Command-PARAMETERS.md)

#### Related Concepts

* [About Parametric Drawing](About-Parametric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*