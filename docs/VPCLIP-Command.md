# VPCLIP (Command)

Clips layout viewport objects and reshapes the viewport border.

## Access Methods

Menu:
Modify
![](../images/ac.menuaro.gif) Clip
![](../images/ac.menuaro.gif) Viewport.

Shortcut menu: Select the viewport to clip. Right-click in the drawing area and choose Viewport Clip.

## Summary

You can either select an existing object to designate as the new boundary, or specify the points of a new boundary. The new
boundary does not clip the old boundary, it redefines it.

TIP:Use the
[CLIP](CLIP-Command.md) command to clip any type of referenced file: images, external references, viewports, and PDF underlays.

## List of Prompts

The following prompts are displayed.

Clipping Object
:   Specifies an object to act as a clipping boundary. Objects that are valid as clipping boundaries include closed poly-lines,
    circles, ellipses, closed splines, and regions.

Polygonal
:   Draws a clipping boundary. You can draw line segments or arc segments by specifying points. The following prompt is displayed:

    The descriptions of the Next Point, Arc, Close, Length, and Undo options match the descriptions of the corresponding options
    in the PLINE command.

Delete
:   Deletes the clipping boundary of a selected viewport. This option is available only if the selected viewport has already been
    clipped. If you clip a viewport that has been previously clipped, the original clipping boundary is deleted, and the new clipping
    boundary is applied.

#### Related Concepts

* [About Layout Viewports](About-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*