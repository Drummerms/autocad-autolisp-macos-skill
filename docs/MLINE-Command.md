# MLINE (Command)

Creates multiple parallel lines.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Multiline.
![](../images/GUID-958E6FF4-E7CC-4D1C-A225-2E5ABB828B2C-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

*Menu*:
Draw ![](../images/ac.menuaro.gif) Multiline.

The following prompts are displayed.

### Start point

Specifies the next vertex of the multiline.

If you create a multiline with two or more segments, the prompt includes the Close option.

![](../images/GUID-C46B2609-27C6-43AB-8AD9-AC7E2A95889A-low.png)

Next point
:   Draws a multiline segment to the specified point using the current multiline style and continues to prompt for points.

    ![](../images/GUID-A47A287E-2A62-45C0-B1C8-62CDFD0E502C-low.png)

Undo
:   Undoes the last vertex point on the multiline.

Close
:   Closes the multiline by joining the last segments with the first segments.

    ![](../images/GUID-E04FB6B6-2B42-473D-AAA6-D013D4962AB9-low.png)

### Justification

Determines how the multiline is drawn between the points you specify.

* Top
* Zero
* Bottom

Top
:   Draws the multiline below the cursor, so that the line with the most positive offset is at the specified points.

    ![](../images/GUID-19711990-1A59-419D-90A2-49DCC31F7CCB-low.png)

Zero
:   Draws the multiline with its origin centered at the cursor, so that the MLSTYLE Element Properties offset of 0.0 is at the
    specified points.

    ![](../images/GUID-D37E0B75-ACE2-4395-9FB7-AD89DBB1B49A-low.png)

Bottom
:   Draws the multiline above the cursor, so that the line with the most negative offset is at the specified points.

    ![](../images/GUID-500B99DA-F28C-4E6F-887B-0ACD45C105AA-low.png)

### Scale

Controls the overall width of the multiline. This scale does not affect linetype scale.

The scale factor is based on the width established in the multiline style definition. A scale factor of 2 produces a multiline
twice as wide as the style definition. A negative scale factor flips the order of the offset line—the smallest on top when
the multiline is drawn from left to right. A negative scale value also alters the scale by the absolute value. A scale factor
of 0 collapses the multiline into a single line.

![](../images/GUID-8F069448-0AF2-4411-8D86-67ACCFB838B3-low.png)

### Style

Specifies a style to use for the multiline.

Style name
:   Specifies the name of a style that has already been loaded or that has been defined in a multiline library (MLN) file.

?—List styles
:   Lists the loaded multiline styles.

#### Related Concepts

* [About Multilines](About-Multilines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*