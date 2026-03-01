# EXTEND (Command)

Extends objects to meet the edges of other objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Trim drop-down ![](../images/ac.menuaro.gif) Extend.
![](../images/GUID-74AC1D5E-0799-450B-8370-58FEE9FF962E-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Extend.

## Overview

There are two modes that you can use to extend objects, Quick mode and Standard mode.

*Quick Mode.* To extend objects, select the objects to be extended individually, press and drag to start a freehand selection path, or
pick two empty locations to specify a crossing Fence. All objects automatically act as boundary edges.

![](../images/GUID-11FBAAC9-368E-4396-AD48-78A45E9DE445-low.png)

*Standard Mode.* To extend objects, first select the boundaries and press Enter. Then select the objects to be extended. To use all objects
as boundaries, press Enter at the first Select Objects prompt.

![](../images/GUID-B8F36591-CC86-48F6-9A65-519AED348826-low.gif)

NOTE:The TRIMEXTENDMODE system variable controls whether the EXTEND command defaults to Quick or Standard behavior.

The following prompts are displayed either in Quick mode or Standard mode.

## Select boundary edges ...

Uses the selected objects to define the boundary edges to which you want to extend an object.

## Select object to extend ...

Specifies the objects to extend. Press Enter to end the command.

## Shift-select to trim

Trims the selected objects to the nearest boundary rather than extending them. This is an easy method to switch between trimming
and extending.

## Cutting Edges

Switches from selecting objects to extend, to selecting the boundary edges.

## Fence

Selects all objects that cross the selection fence. The selection fence is a series of temporary line segments that you specify
with two or more fence points. The selection fence does not form a closed loop.

## Crossing

Selects objects within and crossing a rectangular area defined by two points.

NOTE:Some crossing selections of objects to be extended are ambiguous. EXTEND resolves the selection by following along the rectangular
crossing window in a clockwise direction from the first point to the first object encountered.

## Mode

Sets the default extend mode either to Quick, which uses all objects as potential boundary edges, or to Standard, which prompts
you to select boundary edges.

## Project

Specifies the projection method used when extending objects.

![](../images/GUID-74783F48-5AF3-4C56-A38A-D04F7DE273D6-low.png)

None
:   Specifies no projection. Only objects that intersect with the boundary edge in 3D space are extended.

    ![](../images/GUID-9034DB77-D75E-4FE2-AB52-2D09020976FA-low.png)

UCS
:   Specifies projection onto the
    *XY* plane of the current user coordinate system (UCS). Objects that do not intersect with the boundary objects in 3D space are
    extended.

    ![](../images/GUID-913B1F81-6CE5-4963-87B0-4AFEAE6C5D74-low.png)

View
:   Specifies projection along the current view direction.

    ![](../images/GUID-C15C7F52-4FB7-4717-8296-2A08B694BD7F-low.png)

## Edge

Extends the object to another object's implied edge, or only to an object that actually intersects it in 3D space.

![](../images/GUID-8BD013DC-F504-43C1-857A-06AD6F66F4D6-low.png)

Extend
:   Extends the boundary object along its natural path to intersect another object or its implied edge in 3D space.

    ![](../images/GUID-9BC868C8-FC80-4F72-AED8-C8523E8828EC-low.png)

No Extend
:   Specifies that the object is to extend only to a boundary object that actually intersects it in 3D space.

    ![](../images/GUID-BD4A6213-FC7A-4074-BC87-1068E7061821-low.png)

## Undo

Reverses the most recent changes made by EXTEND.

#### Related Tasks

* [To Extend an Object](To-Extend-an-Object.md)
* [To Trim an Object](To-Trim-an-Object.md)

#### Related Concepts

* [About Trimming and Extending Objects](About-Trimming-and-Extending-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*