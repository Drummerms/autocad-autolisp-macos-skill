# DIMJOGGED (Command)

Creates jogged dimensions for circles and arcs.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension drop-down ![](../images/ac.menuaro.gif) Jogged.
![](../images/GUID-FB79A1E3-7936-4D07-A83B-85D3DCC75913-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Jogged.

## Summary

DIMJOGGED measures the radius of the selected object and displays the dimension text with a radius symbol in front of it.
The origin point of the dimension line can be specified at any convenient location.

NOTE:Jogged radius dimensions are also called
*foreshortened radius dimensions*.

Creates jogged radius dimensions when the center of an arc or circle is located off the layout and cannot be displayed in
its true location. The origin point of the dimension can be specified at a more convenient location called the center location
override.

![](../images/GUID-2B8B2F29-6725-4BE0-AF72-9588A9280249-low.gif)

## List of Prompts

The following prompts are displayed.

Select arc or circle:
*Select an arc, circle, or polyline arc segment*

Specify center location override:
*Specify a point*

Accepts a new center point for a jogged radius dimension that takes the place of the true center point of the arc or circle.

Specify dimension line location or [Mtext/Text/Angle]:
*Specify a point or enter an option*

Dimension Line Location
:   Determines the angle of the dimension line and the location of the dimension text. If the dimension is placed off of an arc
    resulting in the dimension pointing outside the arc,
    AutoCAD 2026 automatically draws an arc extension line.

Mtext
:   Displays the In-Place Text Editor, which you can use to edit the dimension text. Use control codes and Unicode character strings
    to enter special characters or symbols.

    If alternate units are not turned on in the dimension style, you can display them by entering square brackets ([ ]).

    The current dimension style determines the appearance of the generated measurements.

Text
:   Customizes the dimension text at the Command prompt. The generated dimension measurement is displayed within angle brackets.

    To include the generated measurement, use angle brackets (< >) to represent the generated measurement. If alternate units
    are not turned on in the dimension style, you can display alternate units by entering square brackets ([ ]).

    Dimension text properties are set on the Text tab of the New, Modify, and Override Dimension Style dialog boxes.

Angle
:   Changes the angle of the dimension text.

    Also determines the angle of the dimension line and the location of the dimension text.

Specify Jog Location
:   Locates the middle point of the jog. The transverse angle of the jog is determined by the Dimension Style Manager.

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Dimensioning](About-Dimensioning.md)
* [About Creating Radial Dimensions](About-Creating-Radial-Dimensions.md)
* [About Adding a Jog to a Linear Dimension](About-Adding-a-Jog-to-a-Linear-Dimension.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*