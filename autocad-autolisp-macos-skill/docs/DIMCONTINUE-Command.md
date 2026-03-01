# DIMCONTINUE (Command)

Creates a dimension that starts from an extension line of a previously created dimension.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Base and Continue drop-down ![](../images/ac.menuaro.gif) Continue.
![](../images/GUID-9CCB80B0-74F9-4BA2-87F9-FB156C2EB7DA-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Continue.

## Summary

Automatically continues creating additional dimensions from the last linear, angular, or ordinate dimension created, or from
a selected extension line. The dimension lines are lined up automatically.

![](../images/GUID-D6848209-09E2-4C63-B537-A12CF5FF73F0-low.gif)

If no dimension was created in the current session, you are prompted to select a linear, ordinate, or angular dimension to
use as the base for the continued dimension.

## List of Prompts

The following prompts are displayed.

Select continued dimension:
*Select a linear, ordinate, or angular dimension*

Otherwise, the program skips this prompt and uses the dimension object that was last created in the current session. If the
base dimension is linear or angular, the following prompt is displayed:

Specify a
[second extension line origin](DIMCONTINUE-Command.md) or [[Undo](DIMCONTINUE-Command.md)/[Select](DIMCONTINUE-Command.md)] <Select>:
*Specify a point, enter an option, or press*Enter
*to select a base dimension*

If the base dimension is ordinate, the following prompt is displayed:

Specify
[feature location](DIMCONTINUE-Command.md) or [Undo/Select] <Select>:

To end the command, press Enter twice, or press Esc. The current dimension style determines the appearance of the text.

![](../images/GUID-2FAE15EF-24F4-42F7-98FA-64A9B0F268B4-low.png)

Second Extension Line Origin
:   Uses the second extension line origin of the continued dimension for the first extension line origin of the next dimension.
    The current dimension style determines the appearance of the text.

    After you select a continued dimension, the Specify a Second Extension Line Origin prompt is redisplayed. To end the command,
    press Esc. To select another linear, ordinate, or angular dimension to use as the basis for the continued dimension, press
    Enter.

    Select continued dimension:
    *Select a linear, ordinate, or angular dimension*

    Select a base dimension, or press Esc to end the command.

    ![](../images/GUID-5D66E94B-15F0-41EF-8F22-08B4D4556B12-low.png)

Feature Location
:   Uses the endpoint of the base dimension as the endpoint for the continued dimension; you are prompted for the next feature
    location. When you select a feature location, the continued dimension is drawn and the Specify Feature Location prompt is
    redisplayed. To end the command, press Esc. To select another linear, ordinate, or angular dimension to use as the basis for
    the continued dimension, press Enter.

    Select continued dimension:
    *Select a linear, ordinate, or angular dimension*

    Select a base dimension, or press Esc to end the command.

Undo
:   Undoes the last continued dimension entered during the command session.

Select
:   Prompts you to select a linear, ordinate, or angular dimension to use as the continued dimension. After you select a continued
    dimension, the Specify a Second Extension Line Origin prompt or the Specify Feature Location prompt is redisplayed. To end
    the command, press Esc.

#### Related Concepts

* [About Creating Baseline and Continued Dimensions](About-Creating-Baseline-and-Continued-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*