# DIMLINEAR (Command)

Creates a linear dimension.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension drop-down ![](../images/ac.menuaro.gif) Linear.
![](../images/GUID-9266F586-2093-40A2-8CD8-964342AC9E84-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Linear.

## Summary

Creates a linear dimension with a horizontal, vertical, or rotated dimension line. This command replaces the DIMHORIZONTAL
and DIMVERTICAL commands.

![](../images/GUID-A2580380-B7D0-436E-81A1-1D52E375C0D0-low.gif)

## List of Prompts

The following prompts are displayed.

Specify first extension line origin or <select object>:
*Specify a point or press* Enter
*to select an object to dimension*

After you specify the extension line origin points or the object to dimension, the following prompt is displayed:

Specify dimension line location or [Mtext/Text/Angle/Horizontal/Vertical/Rotated]:
*Specify a point or enter an option*

First Extension Line Origin

Prompts for the origin point of the second extension line after you specify the origin point of the first.

![](../images/GUID-2FD5423E-F114-4CF7-81F4-CC0577B5FDEF-low.png)

Dimension Line Location

Uses the point you specify to locate the dimension line and determines the direction to draw the extension lines. After you
specify the location, the dimension is drawn.

![](../images/GUID-2EEA851E-A924-4D51-9501-C4813F15A3A1-low.png)

Mtext

Displays the In-Place Text Editor, which you can use to edit the dimension text. Use control codes and Unicode character strings
to enter special characters or symbols.

If alternate units are not turned on in the dimension style, you can display them by entering square brackets ([ ]).

The current dimension style determines the appearance of the generated measurements.

Text

Customizes the dimension text at the Command prompt. The generated dimension measurement is displayed within angle brackets.

To include the generated measurement, use angle brackets (< >) to represent the generated measurement. If alternate units
are not turned on in the dimension style, you can display alternate units by entering square brackets ([ ]).

Dimension text properties are set on the Text tab of the New, Modify, and Override Dimension Style dialog boxes.

Angle

Changes the angle of the dimension text.

![](../images/GUID-F21DB51E-6D36-45FC-BF56-F0B548F2DBB1-low.png)

Horizontal

Creates horizontal linear dimensions.

![](../images/GUID-06C802AB-2FF3-4227-AFD9-D86CDDF162C2-low.png)

Dimension Line Location
:   Uses the point you specify to locate the dimension line.

Vertical

Creates vertical linear dimensions.

![](../images/GUID-65BAF39B-AA89-406F-9EF5-43D01CD28611-low.png)

Dimension Line Location
:   Uses the point you specify to locate the dimension line.

Rotated

Creates rotated linear dimensions.

![](../images/GUID-E85BE629-8E4E-407E-B043-4512ECAA79F2-low.png)

Object Selection

Automatically determines the origin points of the first and second extension lines after you select an object.

For polylines and other explodable objects, only the individual line and arc segments are dimensioned. You cannot select objects
in a non-uniformly scaled block reference.

If you select a line or an arc, the line or arc endpoints are used as the origins of the extension lines. The extension lines
are offset from the endpoints by the distance you specify in Offset from Origin in the Lines and Arrows tab of the New, Modify,
and Override Dimension Style dialog boxes. See
[DIMSTYLE](DIMSTYLE-Command-2.md). This value is stored in the
[DIMEXO](DIMEXO-System-Variable.md) system variable.

![](../images/GUID-09B45A4D-47A1-435E-9464-104328834E42-low.png)

If you select a circle, the diameter endpoints are used as the origins of the extension line. When the point used to select
the circle is close to the north or south quadrant point, a horizontal dimension is drawn. When the point used to select the
circle is close to the east or west quadrant point, a vertical dimension is drawn.

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Creating Horizontal and Vertical Dimensions](About-Creating-Horizontal-and-Vertical-Dimensions.md)
* [About Creating Linear Dimensions](About-Creating-Linear-Dimensions.md)
* [About Creating Rotated Linear Dimensions](About-Creating-Rotated-Linear-Dimensions.md)
* [About Dimensioning](About-Dimensioning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*