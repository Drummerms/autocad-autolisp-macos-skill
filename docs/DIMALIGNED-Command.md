# DIMALIGNED (Command)

Creates an aligned linear dimension.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension drop-down ![](../images/ac.menuaro.gif) Aligned.
![](../images/GUID-C2D7C948-670A-400C-9206-9630054CD5E1-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Aligned.

## Summary

Creates a linear dimension that is aligned with the origin points of the extension lines.

![](../images/GUID-2C30605C-5D10-4AAA-A5A8-A11FAEAAE145-low.gif)

## List of Prompts

The following prompts are displayed.

Specify first extension line origin or <select object>:
*Specify a point for manual extension lines, or press* Enter
*for automatic extension lines*

After you specify either manual or automatic extension lines, the following prompt is displayed:

Specify dimension line locationor [Mtext/Text/Angle]:
*Specify a point or enter an option*

Extension Line Origin
:   Specifies the first extension line origin (1). You are prompted to specify the second one.

Object Selection
:   Automatically determines the origin points of the first and second extension lines after you select an object.

    For polylines and other explodable objects, only the individual line and arc segments are dimensioned. You cannot select objects
    in a nonuniformly scaled block reference.

    If you select a line or an arc, its endpoints are used as the origins of the extension lines. The extension lines are offset
    from the endpoints by the distance specified in Offset from Origin on the Lines and Arrows tab of the New, Modify, and Override
    Dimension Style dialog boxes (see
    [DIMSTYLE](DIMSTYLE-Command-2.md)). This value is stored in the
     [DIMEXO](DIMEXO-System-Variable.md) system variable.

    ![](../images/GUID-5EFF672B-D712-4E6C-9273-DE0A98897764-low.png)

    If you select a circle, the endpoints of its diameter are used as the origins of the extension line. The point used to select
    the circle defines the origin of the first extension line.

Dimension Line Location
:   Specifies the placement of the dimension line and determines the direction to draw the extension lines. After you specify
    the location, the DIMALIGNED command ends.

Mtext
:   Displays the
    [In-Place Text Editor](In-Place-Text-Editor.md), which you can use to edit the dimension text. The generated measurement is represented with angle brackets (< >). To add
    a prefix or a suffix to the generated measurement, enter the prefix or suffix before or after the angle brackets. Use control
    codes and Unicode character strings to enter special characters or symbols.

    To edit or replace the generated measurement, delete the angle brackets, enter the new dimension text, and then click OK.
    If alternate units are not turned on in the dimension style, you can display them by entering square brackets ([ ]).

    The current dimension style determines the appearance of the generated measurements.

Text
:   Customizes the dimension text at the command prompt. The generated dimension measurement is displayed within angle brackets.

    Enter the dimension text, or press Enter to accept the generated measurement. To include the generated measurement, use angle
    brackets (< >) to represent the generated measurement. If alternate units are not turned on in the dimension style, you can
    display alternate units by entering square brackets ([ ]).

    Dimension text properties are set on the Text tab of the New, Modify, and Override Dimension Style dialog boxes.

Angle
:   Changes the angle of the dimension text.

    ![](../images/GUID-11BFA0FD-A868-45DF-8032-489EB65D0539-low.png)

    ![](../images/GUID-3758C9A4-0C5D-44D3-86BA-C91212E707C5-low.png)

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Creating Aligned Dimensions](About-Creating-Aligned-Dimensions.md)
* [About Creating Linear Dimensions](About-Creating-Linear-Dimensions.md)
* [About Dimensioning](About-Dimensioning.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*