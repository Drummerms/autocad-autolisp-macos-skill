# MLEADER (Command)

Creates a multileader object.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Leader panel ![](../images/ac.menuaro.gif) Multileader.
![](../images/GUID-31CC8661-13A6-4D2B-968D-39BE64E908F8-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Multileader.

![](../images/GUID-E5300815-A14A-4404-B999-611C3D541FA7-low.gif)

## Summary

A multileader object typically consists of an arrowhead, a horizontal landing, a leader line or curve, and either a multiline
text object or a block.

Multileaders can be created
[arrowhead first](MLEADER-Command.md),
[leader landing first](MLEADER-Command.md), or
[content first](MLEADER-Command.md). If a multileader style has been used, then the multileader can be created from that specified style.

## List of Prompts

The following prompts are displayed.

### Select Mtext

Specifies an existing multiline text object to use for the multileader object.

### Leader arrowhead location/first

Specifies a location for the arrowhead of the multileader object.

### Leader landing location/first

Specifies a location for the landing line of the multileader object.

### Content first

Specifies a location for the text or block associated with the multileader object.

Point selection
:   Sets placement for the text box for the text label associated with the multileader object. When you finish entering text,
    press Esc or click outside the text box.

### Options

Specifies options for placing the multileader object.

Leader type
:   Specifies how the leader line is handled.

    * *Straight.* Creates a straight multileader line.
    * *Spline*. Creates a spline multileader line.
    * *None.*Creates a multileader with no leader line.

Leader landing
:   Specifies whether to add a horizontal landing line. If you enter Yes, you are prompted to set the landing line length.

Content type
:   Specifies the type of content that will be used for the multileader.

    * *Block.* Specifies a block within your drawing to associate with the new multileader.
    * *Mtext.* Specifies that multiline text is included with the multileader.
    * *None.* Specifies that no content is displayed at the end of the leader line.

Maxpoints
:   Specifies a maximum number of points, or segments, for the new leader line.

First angle
:   Constrains the angle of the first point in the new leader line.

Second angle
:   Constrains the second angle in the new leader line.

Layer
:   Assigns new multileaders to the specified layer, overriding the current layer. Enter
    *Use Current* or " *.* " to use the current layer.
    [MLEADERLAYER (System Variable)](MLEADERLAYER-System-Variable.md)

Exit options
:   Exits the Options branch of the MLEADER command.

#### Related Tasks

* [To Create a Leader With Straight Lines](To-Create-a-Leader-With-Straight-Lines.md)
* [To Create a Leader Attached to Block Content at an Angle](To-Create-a-Leader-Attached-to-Block-Content-at-an-Angle.md)
* [To Create Multiple Leaders From the Same Annotation](To-Create-Multiple-Leaders-From-the-Same-Annotation.md)

#### Related Concepts

* [About Leader Objects](About-Leader-Objects.md)
* [About Leader Styles](About-Leader-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*