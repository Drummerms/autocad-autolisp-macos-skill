# DIMEDIT (Command)

Edits dimension text and extension lines.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Text Edit drop-down ![](../images/ac.menuaro.gif) Oblique.
![](../images/GUID-063AC646-D457-4DC9-8691-2B3318996042-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Oblique.

## Summary

Rotates, modifies, or restores dimension text. Changes the oblique angle of extension lines. The companion command that moves
text and the dimension line is
[DIMTEDIT](DIMTEDIT-Command.md).

## List of Prompts

The following prompts are displayed.

Enter type of dimension editing [Home/New/Rotate/Oblique] <Home>:
*Enter an option or press*Enter

Home
:   Moves rotated dimension text back to its default position.

    ![](../images/GUID-FDF1BF2E-B20B-44D7-AFEB-9199B5BB0545-low.png)

    The selected dimension text is returned to its default position and rotation as specified in its dimension style.

New
:   Changes dimension text using the
    [In-Place Text Editor](In-Place-Text-Editor.md).

    ![](../images/GUID-154627ED-827A-4614-BE1F-98D48D8FD1DC-low.png)

    The generated measurement is represented with angle brackets (< >). Use control codes and Unicode character strings to enter
    special characters or symbols.

    To edit or replace the generated measurement, delete the angle brackets, enter the new dimension text, and then choose OK.
    If alternate units are not turned on in the dimension style, you can display them by entering square brackets ([ ]).

Rotate
:   Rotates dimension text. This option is similar to the Angle option of
    [DIMTEDIT](DIMTEDIT-Command.md).

    Entering
    *0* places the text in its default orientation, which is determined by the vertical and horizontal text settings on the Text
    tab of the New, Modify, and Override Dimension Style dialog boxes. See
    [DIMSTYLE](DIMSTYLE-Command-2.md). The
    [DIMTIH](DIMTIH-System-Variable.md) and
    [DIMTOH](DIMTOH-System-Variable.md) system variables control this orientation.

    ![](../images/GUID-EED28F8A-3BDF-4A57-A9C9-47ECA7BD1D24-low.png)

Oblique
:   The Oblique option is useful when extension lines conflict with other features of the drawing. The oblique angle is measured
    from the
    *X* axis of the UCS.

    ![](../images/GUID-DD5039B1-CFF7-420D-ABBF-BF6CA9C477AF-low.gif)

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)

#### Related Concepts

* [About Dimensioning](About-Dimensioning.md)
* [About Creating Linear Dimensions With Oblique Extension Lines](About-Creating-Linear-Dimensions-With-Oblique-Extension-Lines.md)
* [About Modifying Dimension Text](About-Modifying-Dimension-Text.md)
* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*