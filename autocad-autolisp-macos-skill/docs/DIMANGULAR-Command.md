# DIMANGULAR (Command)

Creates an angular dimension.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension drop-down ![](../images/ac.menuaro.gif) Angular.
![](../images/GUID-989ABCF5-279A-4D3E-B3E5-B504CF125129-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Angular.

## Summary

Measures the angle between selected objects or 3 points. Objects that can be selected include arcs, circles, and lines, among
others.

![](../images/GUID-D40162DD-59FB-42E1-9E93-0EF506F367A5-low.gif)

## List of Prompts

The following prompts are displayed.

Select arc, circle, line, or <specify vertex>:
*Select an arc, circle, or line, or press* Enter
*to create the angular dimension by specifying three points*

After you define the angle to dimension, the following prompt is displayed:

Specify dimension arc line location or [Mtext/Text/Angle/Quadrant]:

Arc Selection
:   Uses points on the selected arc as the defining points for a three-point angular dimension. The center of the arc is the angle
    vertex. The arc endpoints become the origin points of the extension lines.

    ![](../images/GUID-D4FD980D-8CD3-4B5C-A404-06BD2A49A13C-low.png)

    The dimension line is drawn as an arc between the extension lines. The extension lines are drawn from the angle endpoints
    to the intersection of the dimension line.

Circle Selection
:   Uses the selection point (1) as the origin of the first extension line. The center of the circle is the angle vertex.

    The second angle endpoint is the origin of the second extension line and does not have to lie on the circle.

    ![](../images/GUID-B4F22917-E90F-4EE7-8142-7D09096E776C-low.png)

Line Selection
:   Defines the angle using two lines.

    The program determines the angle by using each line as a vector for the angle and the intersection of the lines for the angle
    vertex. The dimension line spans the angle between the two lines. If the dimension line does not intersect the lines being
    dimensioned, extension lines are added as needed to extend one or both lines. The arc is always less than 180 degrees.

    ![](../images/GUID-08AB9B46-C039-4660-90A2-6BC354E8009C-low.png)

Three-Point Specification
:   Creates a dimension based on three points you specify.

    The angle vertex can be the same as one of the angle endpoints. If you need extension lines, the endpoints are used as origin
    points.

    ![](../images/GUID-2DB8877F-A721-4769-9B89-CF5CA5F93B30-low.png)

    The dimension line is drawn as an arc between the extension lines. The extension lines are drawn from the angle endpoints
    to the intersection of the dimension line.

Dimension Arc Line Location
:   Specifies the placement of the dimension line and determines the direction to draw the extension lines.

Mtext
:   Displays the In-Place Text Editor, which you can use to edit the dimension text. To add a prefix or a suffix, enter the prefix
    or suffix text before or after the generated measurement. Use control codes and Unicode character strings to enter special
    characters or symbols.

    The current dimension style determines the appearance of the generated measurements.

Text
:   Customizes the dimension text at the Command prompt. The generated dimension measurement is displayed within angle brackets.

    To include the generated measurement, use angle brackets (< >) to represent the generated measurement.

    ![](../images/GUID-B5E2EF10-5AD1-48CE-AC3A-A8CDB9732CCE-low.png)

    Dimension text properties are set on the Text tab of the New, Modify, and Override Dimension Style dialog boxes.

Angle
:   Changes the angle of the dimension text.

    ![](../images/GUID-016AFF96-F025-4792-9C58-57BC1417E606-low.png)

Quadrant
:   Specifies the quadrant that the dimension should be locked to. When quadrant behavior is on, the dimension line is extended
    past the extension line when the dimension text is positioned outside of the angular dimension.

    ![](../images/GUID-9B1E82D6-AA50-420B-BD33-AC73D8F84924-low.png)

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Dimensioning](About-Dimensioning.md)
* [About Creating Aligned Dimensions](About-Creating-Aligned-Dimensions.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*