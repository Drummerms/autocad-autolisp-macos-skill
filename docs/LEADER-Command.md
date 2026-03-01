# LEADER (Command)

Creates a line that connects annotation to a feature.

## Summary

It is recommended that you use the workflow available through the
[MLEADER](MLEADER-Command.md) command to create leader objects.

## List of Prompts

The following prompts are displayed.

Specify leader start point:

Specify next point:

A leader line segment is drawn and prompts for points and options are displayed.

Specify
[next point](LEADER-Command.md) or [[Annotation](LEADER-Command.md)/[Format](LEADER-Command.md)/[Undo](LEADER-Command.md)] <Annotation>:
*Specify a point, enter an option, or press* Enter

Point Specification

Draws a leader line segment to the point specified and continues to prompt you for points and options.

Annotation

Inserts an annotation at the end of the leader line. The annotation can be single or multiple lines of text, a feature control
frame containing geometric tolerances, or a block.

If you press Enter at the Annotation prompt without entering text first, the following options are displayed:

Tolerance
:   Creates a feature control frame containing geometric tolerances using the Geometric Tolerance dialog box (see TOLERANCE).

    You can create datum indicators and basic dimension notation in these dialog boxes. After you specify the geometric tolerance,
    LEADER ends.

    ![](../images/GUID-C4831B5E-A64C-4654-8F16-88E874112C3A-low.png)

Copy
:   Copies text, a multiline text object, a feature control frame with geometric tolerances, or a block and connects the copy
    to the end of the leader line. The copy is associated with the leader line, meaning that if the copied object moves, the end
    of the leader line moves with it. The display of the hook line depends on the object copied.

    The value of the current text gap (see DIMSTYLE or the DIMGAP system variable) determines where the text and multiline text
    objects are inserted. Blocks or feature control frames with geometric tolerances are attached to the end of the leader line.

Block
:   Inserts a block at the end of the leader line. The prompts are the same as for INSERT. The block reference is inserted at
    an offset from the end of the leader line and is associated to the leader line, meaning that if the block moves, the end of
    the leader line moves with it. No hook line is displayed.

    ![](../images/GUID-B779D78B-0423-41CD-903D-B83FFEF6251E-low.png)

None
:   Ends the command without adding any annotation to the leader line.

Mtext
:   Creates text using the
    [In-Place Text Editor](In-Place-Text-Editor.md) when you specify an insertion point and a second point for the text boundary.

    Enter the characters for the text. Enclose format strings for prefixes and suffixes in angle brackets (< >). Enclose format
    strings for alternate units in square brackets ([ ]).

    The units settings and the current text style determine how the text is displayed. The multiline text is vertically centered
    and horizontally aligned according to the
    *X* axis direction of the last two vertices of the leader line. The text is offset from the hook line by the distance specified
    under Offset from Dim Line on the Text tab of the
    [New, Modify, or Override Dimension Style dialog box](New,-Modify,-and-Override-Dimension-Style-Dialog-Boxes.md). If the offset specified is negative, the multiline text is enclosed in a box as a basic dimension.

    ![](../images/GUID-7CCC28F2-1527-4127-A716-0BADD4A6DE63-low.png)

Format

Controls the way the leader is drawn and whether it has an arrowhead.

![](../images/GUID-AC00CA61-BA84-44E4-B32E-7FB68464C12E-low.png)

Spline
:   Draws the leader line as a spline. The vertices of the leader line are the control points, each of equal unit weight.

Straight
:   Draws the leader line as a set of straight line segments.

Arrow
:   Draws an arrowhead at the start point of the leader line.

None
:   Draws a leader line with no arrowhead at the start point.

Undo

Undoes the last vertex point on the leader line. The previous prompt is displayed.

#### Related Tasks

* [To Control the Display of Dimension Lines](To-Control-the-Display-of-Dimension-Lines.md)

#### Related Concepts

* [About Leader Objects](About-Leader-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*