# About Selecting Multiple Objects

At the Select Objects prompt, you can select many objects at the same time.

## Specify a Rectangular Selection Area

Specify opposite corners to define a rectangular area. The background inside the area changes color and becomes transparent.
The direction that you drag your cursor from the first point to the opposite corner determines which objects are selected.

* *Window selection.* Drag your cursor from left to right to select only objects that are entirely enclosed by the rectangular area.
* *Crossing selection.* Drag your cursor from right to left to select objects that the rectangular window encloses or crosses.

  ![](../images/GUID-F7B3DB95-DDD7-470A-A782-F0256F96C458-low.png)

With a window selection, usually the entire object must be contained in the rectangular selection area. However, if an object
with a noncontinuous (dashed) linetype is only partially visible in the viewport and all the visible vectors of the linetype
can be enclosed within the selection window, the entire object is selected.

## Specify an Irregularly Shaped Selection Area

Specify points to define an irregularly shaped area. Use window polygon selection to select objects entirely enclosed by
the selection area. Use crossing polygon selection to select objects enclosed
*or* crossed by the selection area.

![](../images/GUID-3C68035A-ECC4-4431-9752-55618BDB8143-low.png)

## Specify a Selection Fence

In a complex drawing, use a selection fence. A selection fence looks like a polyline and selects only the objects it passes
through. The circuit board illustration shows a fence selecting several components.

![](../images/GUID-ADBB77E9-4DB8-4DED-B852-F654658503F0-low.png)

## Use Other Selection Options

You can see all selection options by entering
*?* at the Select Objects prompt. For a description of each of the selection options, see the SELECT command.

## Remove Selection from Multiple Objects

You can enter
*r* (Remove) at the Select Objects prompt and use any selection option to remove objects from the selection set. If you are using
the Remove option and want to return to adding objects to the selection set, enter
*a*(Add).

You can also remove objects from the current selection set by holding down Shift and selecting them again, or by holding down
Shift and then clicking and dragging window or crossing selections. You can add and remove objects repeatedly from the selection
set.

#### Related Tasks

* [To Select Objects](To-Select-Objects.md)
* [To Select Objects With a Fence](To-Select-Objects-With-a-Fence.md)
* [To Select Objects Within a Polygonal Area](To-Select-Objects-Within-a-Polygonal-Area.md)
* [To Change Object Selection Settings](To-Change-Object-Selection-Settings.md)
* [To Select Overlapping or Close Objects](To-Select-Overlapping-or-Close-Objects.md)

#### Related Concepts

* [About Selecting Objects Individually](About-Selecting-Objects-Individually.md)
* [About Selecting Objects Based on Shared Properties](About-Selecting-Objects-Based-on-Shared-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*