# DIMORDINATE (Command)

Creates ordinate dimensions.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension drop-down ![](../images/ac.menuaro.gif) Ordinate.
![](../images/GUID-E5FF7802-872E-4FBE-91F9-26E0442108EB-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Ordinate.

## Summary

Ordinate dimensions measure the horizontal or vertical distance from an origin point called the datum to a feature, such
as a hole in a part. These dimensions prevent escalating errors by maintaining accurate offsets of the features from the datum.

![](../images/GUID-65DE9D48-D6D6-4C36-A99D-B3688E6F7604-low.gif)

## List of Prompts

The following prompts are displayed.

Specify feature location:
*Specify a point or snap to an object*

Specify leader endpoint or [Xdatum/Ydatum/Mtext/Text/Angle]:
*Specify a point or enter an option*

Leader Endpoint Specification
:   Uses the difference between the feature location and the leader endpoint to determine whether it is an
    *X* or a
    *Y* ordinate dimension. If the difference in the
    *Y* ordinate is greater, the dimension measures the
    *X* ordinate. Otherwise, it measures the
    *Y* ordinate.

Xdatum
:   Measures the
    *X* ordinate and determines the orientation of the leader line and dimension text. The Leader Endpoint prompt is displayed, where
    you can specify the endpoint.

    ![](../images/GUID-6FF3E975-DA26-4DB0-A73F-9F93F3722121-low.png)

Ydatum
:   Measures the
    *Y* ordinate and determines the orientation of the leader line and dimension text. The Leader Endpoint prompts are displayed,
    where you can specify the endpoint.

    ![](../images/GUID-DC48AC9A-60FD-4716-9D07-DC702A15CB22-low.png)

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

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Creating Ordinate Dimensions](About-Creating-Ordinate-Dimensions.md)
* [About Dimensioning](About-Dimensioning.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*