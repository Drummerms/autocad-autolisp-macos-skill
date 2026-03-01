# BREAK (Command)

Breaks the selected object between two points.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Break drop-down ![](../images/ac.menuaro.gif) Break.
![](../images/GUID-80FF8BCE-417E-49B8-B945-3EE246031EC0-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Break.

You can create a gap between two specified points on an object, breaking it into two objects. If the points are off of an
object, they are automatically projected on to the object. BREAK is often used to create space for a block or text.

![](../images/GUID-243F9D4A-5FFF-43B7-BC1D-F153E8FACBCC-low.gif)

The prompts that are displayed depend on how you select the object. If you select the object by using your pointing device,
the program both selects the object and treats the selection point as the first break point. At the next prompt, you can continue
by specifying the second point or by overriding the first point.

First point
:   Overrides the original first point where you selected the object with a new point that you specify.

    ![](../images/GUID-255F4E1B-6D4F-4E72-918A-123DDB3AB45D-low.png)

Second point
:   Specifies a second point. The portion of the object is erased between the two points that you specify. If the second point
    is not on the object, the nearest point on the object is selected; therefore, to break off one end of a line, arc, or polyline,
    specify the second point beyond the end to be removed.

To split an object in two without erasing a portion, enter the same point for both the first and second points. You can do
this by entering @ to specify the second point.

Lines, arcs, circles, polylines, ellipses, splines, donuts, and several other object types can be split into two objects or
have one end removed.

The program converts a circle to an arc by removing a piece of the circle starting counterclockwise from the first to the
second point.

![](../images/GUID-85270B64-DE63-4309-8094-28A377EC092E-low.png)

To break selected objects at a single point, use the BREAKATPOINT command.

#### Related Tasks

* [To Break an Object](To-Break-an-Object.md)

#### Related References

* [BREAKATPOINT (Command)](BREAKATPOINT-Command.md)

#### Related Concepts

* [About Breaking and Joining Objects](About-Breaking-and-Joining-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*