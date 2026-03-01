# Leader Settings Dialog Box

Creates a leader and leader annotation.

QLEADER (Command): Specify the settings option at the prompt

## Summary

Customizes the QLEADER command and sets properties for leaders and leader annotations.

The Leader Settings dialog box includes the following tabs: Annotation, Leader Line & Arrow, Attachment.

## List of Tabs

The following tabs are displayed.

Annotation Tab (Leader Settings Dialog Box)

![](../images/GUID-018C2E5F-B50A-41E2-B1A4-BAA72313300B-low.png)

Annotation Type

Sets the leader annotation type. The type you select changes the QLEADER leader annotation prompt.

MText
:   Prompts you to create multiline text (mtext) annotation.

Copy an Object
:   Prompts you to copy a multiline text, single-line text, tolerance, or block reference object and connects the copy to the
    end of the leader line. The copy is associated with the leader line, meaning that if the copied object moves, the end of the
    leader line moves with it. The display of the hook line depends on the object copied.

Tolerance
:   Displays the Tolerance dialog box, which you can use to create a feature control frame to attach to the leader.

Block Reference
:   Prompts you to insert a block reference. The block reference is inserted at an offset from the end of the leader line and
    is associated to the leader line, meaning that if the block moves, the end of the leader line moves with it. No hook line
    is displayed.

None
:   Creates a leader with no annotation.

MText Options

The options are available only when the multiline text annotation type is selected.

Prompt for Width
:   Prompts you to specify the width of the multiline text annotation.

Always Left Justify
:   Left-justifies the multiline text annotation, regardless of leader location.

Frame Text
:   Places a frame around multiline text annotation.

Annotation Reuse

Sets options for reusing leader annotation.

None
:   Does not reuse leader annotation.

Reuse Next
:   Reuses the next annotation you create for all subsequent leaders.

Reuse Current
:   Reuses current annotation. This option is automatically selected when you reuse annotation after selecting Reuse Next.

Leader Line & Arrow Tab (Leader Settings Dialog Box)

![](../images/GUID-10FBEEE8-54C1-49F2-A485-7DE0584EA7C3-low.png)

Leader Line

:   Sets the leader line format.

Straight
:   Creates straight-line segments between the points you specify.

Spline
:   Creates a spline object using the leader points you specify as control points.

Arrowhead

:   Defines the leader arrowhead. The arrowheads are also available for dimension lines ([DIMSTYLE](DIMSTYLE-System-Variable.md) command). If you select User Arrow, a list of blocks in the drawing is displayed.

Number of Points

:   Sets the number of leader points that QLEADER prompts you to specify before prompting for the leader annotation. For example,
    if you set the points to 3, QLEADER automatically prompts you to specify the annotation after you specify two leader points.
    Set the number to one more than the number of leader segments you want to create.

    If you set the option to No Limit, QLEADER prompts for leader points until you press Enter.

Angle Constraints

:   Sets angle constraints for the first and second leader lines.

First Segment
:   Sets the angle of the first leader segment.

Second Segment
:   Sets the angle of the second leader segment.

Attachment Tab (Leader Settings Dialog Box)

:   Sets the attachment location for leader lines and multiline text annotation. This tab is available only when Mtext is selected
    on the Annotation tab.

![](../images/GUID-F05BB750-96DC-4912-80FA-8E10713B2DD1-low.png)

Top of Top Line
:   Attaches the leader line at the top of the top multiline text line.

Middle of Top Line
:   Attaches the leader line at the middle of the top multiline text line.

Middle of Multiline Text
:   Attaches the leader line at the middle of the multiline text.

Middle of Bottom Line
:   Attaches the leader line at the middle of the bottom multiline text line.

Bottom of Bottom Line
:   Attaches the leader line at the bottom of the bottom multiline text line.

Underline Bottom Line
:   Underlines the bottom multiline text line.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*