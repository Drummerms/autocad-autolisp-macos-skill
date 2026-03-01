# TRIM (Command)

Trims objects to meet the edges of other objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Trim.
![](../images/GUID-53B8A7B8-0050-44CA-A923-870AF64E125A-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Trim.

## Overview

There are two modes that you can use to trim objects, Quick mode and Standard mode.

*Quick Mode.* To trim objects, select the objects to be trimmed individually, press and drag to start a freehand selection path, or pick
two empty locations to specify a crossing Fence. All objects automatically act as cutting edges. Selected objects that can't
be trimmed are deleted instead.

![](../images/GUID-65713623-9458-4606-A8F5-9009D4E3FE5A-low.png)

*Standard Mode.* To trim objects, first select the boundaries and press Enter. Then select the objects to be trimmed. To use all objects as
boundaries, press Enter at the first Select Objects prompt.

![](../images/GUID-9B6BB9D4-2C18-4735-AD1B-53686218F2D4-low.gif)

NOTE:The TRIMEXTENDMODE system variable controls whether the TRIM command defaults to Quick or Standard behavior.

The following prompts are displayed.

## Select cutting edges

Specifies one or more objects to be used as a boundary for the trim. TRIM projects the cutting edges and the objects to be
trimmed onto the
*XY* plane of the current user coordinate system (UCS).

![](../images/GUID-98D18A7E-CAE0-4D65-8346-84DA444CF562-low.png)

NOTE: To select cutting edges that include blocks, you can use only the single selection, Crossing, Fence, and Select All options.

Select objects
:   Specifies objects individually.

Select all
:   Specifies that all objects in the drawing can be used as a trim boundary.

## Object to Trim

Specifies the object to trim. If more than one trim result is possible, the location of the first selection point determines
the result.

![](../images/GUID-F1E70293-B0FD-448F-B543-EB39F6F93D30-low.png)

## Shift-Select to Extend

Extends the selected objects rather than trimming them. This option provides an easy method to switch between trimming and
extending.

## Cutting Edges

Switches from selecting objects to trim, to selecting the cutting edges.

## Fence

Selects all objects that cross the selection fence. The selection fence is a series of temporary line segments that you specify
with two or more fence points. The selection fence does not form a closed loop.

## Crossing

Selects objects within and crossing a rectangular area defined by two points.

NOTE: Some crossing selections of objects to be trimmed are ambiguous. TRIM resolves the selection by following along the rectangular
crossing window in a clockwise direction from the first point to the first object encountered.

## Mode

Sets the default trim mode either to Quick, which uses all objects as potential cutting edges or to Standard, which prompts
you to select cutting edges.

## Project

Specifies the projection method used when trimming objects.

None
:   Specifies no projection. The command trims only objects that intersect with the cutting edge in 3D space.

    ![](../images/GUID-153D1A9B-3886-4C38-A727-573D74843117-low.png)

UCS
:   Specifies projection onto the
    *XY* plane of the current UCS. The command trims objects that do not intersect with the cutting edge in 3D space.

    ![](../images/GUID-8B0EB18A-4FD9-4FAA-8B8E-A6A2209E5A7E-low.png)

View
:   Specifies projection along the current view direction. The command trims objects that intersect the boundary in the current
    view.

    ![](../images/GUID-A919E808-1108-4DC0-9DC0-916E81B51782-low.png)

## Edge

Determines whether an object is trimmed at another object's extrapolated edge or only to an object that intersects it in 3D
space.

![](../images/GUID-1D76B1B4-20AD-416F-87A4-E11EB7D93259-low.png)

Extend
:   Extends the cutting edge along its natural path to intersect an object in 3D space.

    ![](../images/GUID-1BE56E0A-7FA0-4FF2-B3A1-7E1FA86BD51B-low.png)

No Extend
:   Specifies that the object is trimmed only at a cutting edge that intersects it in 3D space.

NOTE: When trimming hatches, do not set Edge to Extend. If you do, gaps in the trim boundaries will not be bridged when trimming
hatches, even when the gap tolerance is set to a correct value.

![](../images/GUID-37A639DB-968F-4638-A460-75F500E14247-low.png)

## Erase

Deletes selected objects. This option provides a convenient method to erase unneeded objects without leaving the TRIM command.

## Undo

Reverses the most recent change made by TRIM.

#### Related Tasks

* [To Trim an Object](To-Trim-an-Object.md)
* [To Trim Objects in 3D Wireframe Models](To-Trim-Objects-in-3D-Wireframe-Models.md)
* [To Trim in 3D Using the Current View Plane](To-Trim-in-3D-Using-the-Current-View-Plane.md)
* [To Extend an Object](To-Extend-an-Object.md)
* [To Lengthen an Object](To-Lengthen-an-Object.md)
* [To Stretch an Object](To-Stretch-an-Object.md)

#### Related Information

* [About Trimming and Extending Objects](About-Trimming-and-Extending-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*