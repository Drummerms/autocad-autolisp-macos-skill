# POLYSOLID (Command)

Creates a 3D wall-like polysolid.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid drop-down ![](../images/ac.menuaro.gif) Polysolid.
![](../images/GUID-F298C2A7-4B42-40C7-9332-5D8E73E3B810-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Polysolid.

## Summary

You can create walls with straight and curved segments of constant height and width.

![](../images/GUID-8A6F33F7-512B-43EB-BB45-7722B595C968-low.gif)

With the POLYSOLID command, you can convert an existing line, 2D polyline, arc, or circle to a solid with a rectangular profile.
A polysolid can have curved segments, but the profile is always rectangular by default.

![](../images/GUID-756A5275-DEC6-4D61-8990-1A92E4E8BF2A-low.png)

You can draw a solid with POLYSOLID just as you would a polyline. The
[PSOLWIDTH](PSOLWIDTH-System-Variable.md) system variable sets the default width for the solid. The
[PSOLHEIGHT](PSOLHEIGHT-System-Variable.md) system variable sets the default height for the solid.

## List of Prompts

The following prompts are displayed.

Specify start point or [[Object](POLYSOLID-Command.md)/[Height](POLYSOLID-Command.md)/[Width](POLYSOLID-Command.md)/[Justify](POLYSOLID-Command.md)] <Object>: *Specify a start point for the profile of the solid, press*Enter *to specify an object to convert to a solid, or enter an option*

Specify the
[next point](POLYSOLID-Command.md) or [[Arc](POLYSOLID-Command.md)/[Undo](POLYSOLID-Command.md)]: *Specify the next point for the profile of the solid,* *or enter an option*

Object

Specifies an object to convert to a solid. You can convert:

* Line
* Arc
* 2D polyline
* Circle

Select object:
*Select an object to convert to a solid*

Height

Specifies the height of the solid. The default height is set to the current
[PSOLHEIGHT](PSOLHEIGHT-System-Variable.md) setting.

Specify height <default>:
*Specify a value for the height, or press*Enter *to specify the default value*

The specified height value will update the
[PSOLHEIGHT](PSOLHEIGHT-System-Variable.md) setting.

Width

Specifies the width of the solid. The default width is set to the current
[PSOLWIDTH](PSOLWIDTH-System-Variable.md) setting.

Specify width <current>:
*Specify a value for the width by entering a value or specifying two points, or press*Enter *to specify the current width value*

The specified width value will update the
[PSOLWIDTH](PSOLWIDTH-System-Variable.md) setting.

Justify

Sets the width and height as the solid to be left, right, or center justified when defining the profile with the command.
The justification is based on the starting direction of the first segment of the profile.

Enter justification [Left/Center/Right] <Center>:
*Enter an option for the justification or press* Enter
*to specify center justification*

Next Point

Specify the next point or [Arc/Close/Undo]: *Specify the next point for the profile of the solid, enter an option, or press* Enter
*to end the command*

Arc
:   Adds an arc segment to the solid. The default starting direction of the arc is tangent to the last drawn segment. You can
    specify a different starting direction with the Direction option.

    Specify endpoint of arc or [Close/Direction/Line/Second point/Undo]:
    *Specify an endpoint or enter an option*

    * *Close.* Closes the solid by creating a line or arc segment from the last point specified to the starting point of the solid. At least
      two points must be specified to use this option.
    * *Direction.* Specifies a starting direction for the arc segment.

      Specify the tangent direction from the start point of arc: *Specify a point*

      Specify endpoint of arc:
      *Specify a point*
    * *Line.* Exits the Arc option and returns to the initial POLYSOLID command prompts.
    * *Second Point.* Specifies the second point and endpoint of a three-point arc segment.

      Specify second point on arc:
      *Specify a point*

      Specify end point of arc:
      *Specify a point*
    * *Undo.* Removes the most recent arc segment added to the solid.

Close
:   Closes the solid by creating a line or arc segment from the last point specified to the starting point of the solid. At least
    three points must be specified to use this option.

Undo
:   Removes the most recent arc segment added to the solid.

Arc

Adds an arc segment to the solid. The default starting direction of the arc is tangent to the last drawn segment. You can
specify a different starting direction with the Direction option.

Specify endpoint of arc or [Close/Direction/Line/Second point/Undo]:
*Specify an endpoint or enter an option*

Close
:   Closes the solid by creating a linear or arc segment from the last vertex to the start of the solid.

Direction
:   Specifies a starting direction for the arc segment.

    Specify the tangent direction from the start point of arc: *Specify a point*

    Specify endpoint of arc:
    *Specify a point*

Line
:   Exits the Arc option and returns to the initial POLYSOLID command prompts.

Second Point
:   Specifies the second point and endpoint of a three-point arc segment.

    Specify second point on arc:
    *Specify a point*

    Specify end point of arc:
    *Specify a point*

Undo
:   Removes the most recent arc segment added to the solid.

Undo

Removes the most recent segment added to the solid.

#### Related References

* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*