# DIMROTATED (Command)

Creates a rotated linear dimension.

## Summary

Creates a linear dimension with a rotated dimension line.

## List of Prompts

The following prompts are displayed.

Specify angle of dimension line <0>:
*Specify an angle or press* Enter
*to accept the default value*

Specify first extension line origin or <select object>:
*Specify a point or press* Enter
*to select an object to dimension*

After you specify the extension line origin points or the object to dimension, the following prompt is displayed:

Specify dimension line location or [Mtext/Text/Angle]:
*Specify a point or enter an option*

First Extension Line Origin

Prompts for the origin point of the second extension line after you specify the origin point of the first.

Dimension Line Location

Uses the point you specify to locate the dimension line and determines the direction to draw the extension lines. After you
specify the location, the dimension is drawn.

Mtext

Displays the In-Place Text Editor, which you can use to edit the dimension text. Use control codes and Unicode character strings
to enter special characters or symbols. .

If alternate units are not turned on in the dimension style, you can display them by entering square brackets ([ ]).

The current dimension style determines the appearance of the generated measurements.

Text

Customizes the dimension text at the Command prompt. The generated dimension measurement is displayed within angle brackets.

To include the generated measurement, use angle brackets (< >) to represent the generated measurement. If alternate units
are not turned on in the dimension style, you can display alternate units by entering square brackets ([ ]).

Dimension text properties are set on the Text tab of the New, Modify, and Override Dimension Style dialog boxes.

Angle

Changes the angle of the dimension text.

Object Selection

Automatically determines the origin points of the first and second extension lines after you select an object.

For polylines and other explodable objects, only the individual line and arc segments are dimensioned. You cannot select objects
in a non-uniformly scaled block reference.

If you select a line or an arc, the line or arc endpoints are used as the origins of the extension lines. The extension lines
are offset from the endpoints by the distance you specify in Offset from Origin in the Lines and Arrows tab of the New, Modify,
and Override Dimension Style dialog boxes. See
[DIMSTYLE](DIMSTYLE-Command-2.md). This value is stored in the
 [DIMEXO](DIMEXO-System-Variable.md) system variable.

If you select a circle, the location of the origins for the extension lines is calculated based on the center of the circle
and the angle of the rotated dimension line.

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Creating Rotated Linear Dimensions](About-Creating-Rotated-Linear-Dimensions.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)
* [About Dimensioning](About-Dimensioning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*