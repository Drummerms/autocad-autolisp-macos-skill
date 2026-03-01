# PRESSPULL (Command)

Dynamically modifies objects by extrusion and offset.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Presspull.
![](../images/GUID-7BAD4DA5-0A85-410F-A3A4-00F1A7483B7B-low.png)

## Summary

Get visual feedback as you move the cursor after selecting a 2D object, an area formed by a closed boundary or a 3D solid
face. The press or pull behavior responds to the type of object you select to create extrusions and offsets. In this example,
the area between two polylines is pulled to create a 3D solid wall.

![](../images/GUID-73A2708C-C1D4-4D86-B575-96C31865CFF7-low.gif)

| Selection | Presspull behavior |
| Open 2D object (such as an arc) | Extrudes to create a surface |
| Closed 2D object (such as a circle) | Extrudes to create a 3D solid |
| Inside a bounded area | Extrudes to create a 3D solid |
| 3D solid face | Offsets the face, expanding or condensing the 3D solid |

The command repeats automatically until you press Esc, Enter, or the Spacebar.

## List of Prompts

The following prompts are displayed.

Object or bounded area
:   Select the object, bounded area, 3D solid face, or 3D solid edge that you want to modify.

    Selecting a face extrudes the face without affecting the adjacent faces. If you Ctrl+click a face, the face is offset, and
    the change also affects the adjacent faces.

Multiple
:   Specifies that you want to make more than one selection.

    You can also Shift+click to make multiple selections.

Offset distance
:   If you selected the face of a 3D solid, specify the offset by moving the cursor or entering a distance.

Extrusion height
:   If you selected a 2D object or clicked inside a closed area, specify an extrusion height by moving the cursor or entering
    a distance. The extrusion direction of planar objects is normal to planar objects and in the
    *Z* direction of the current UCS for non-planar objects.

#### Related Concepts

* [About Pressing or Pulling Areas, Objects, and Faces](About-Pressing-or-Pulling-Areas,-Objects,-and-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*