# DIMARC (Command)

Creates an arc length dimension.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension drop-down ![](../images/ac.menuaro.gif) Arc Length.
![](../images/GUID-46BC30FB-5681-44B2-98F2-041CD1567B75-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Arc Length.

## List of Prompts

The following prompts are displayed.

Select arc or polyline arc segment:
*Use an object selection method*

Specify arc length dimension location or [Mtext/Text/Angle/Partial/Leader]: Specify a point or enter an option

Arc length dimensions measure the distance along an arc or polyline arc segment. The extension lines of an arc length dimension
can be orthogonal or radial. An arc symbol is displayed either above or preceding the dimension text.

![](../images/GUID-0EC86E92-E9E3-4EA4-A2EA-0B67BF26C97D-low.gif)

Arc Length Dimension Location
:   Specifies the placement of the dimension line and determines the direction of the extension lines.

Mtext
:   Displays the In-Place Text Editor, which you can use to edit the dimension text. Use control codes and Unicode character strings
    to enter special characters or symbols.

    If alternate units are not turned on in the dimension style, you can display them by entering square brackets ([]).

    The current dimension style determines the appearance of the generated measurements.

Text
:   Customizes the dimension text at the Command prompt. The generated dimension measurement is displayed within angle brackets.

    To include the generated measurement, use angle brackets (< >) to represent the generated measurement. If alternate units
    are not turned on in the dimension style, you can display alternate units by entering square brackets ([ ]).

    Dimension text properties are set on the Text tab of the New, Modify, and Override Dimension Style dialog boxes.

Angle
:   Changes the angle of the dimension text.

Partial
:   Reduces the length of the arc length dimension.

Leader
:   Adds a leader object. This option is displayed only if the arc (or arc segment) is greater than 90 degrees. The leader is
    drawn radially, pointing towards the center of the arc being dimensioned.

No Leader
:   Cancels the Leader option before the leader is created.

    To remove a leader, delete the arc length dimension and recreate it without the leader option.

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Dimensioning](About-Dimensioning.md)
* [About Creating Arc Length Dimensions](About-Creating-Arc-Length-Dimensions.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*