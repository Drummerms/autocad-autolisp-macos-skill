# DIMBASELINE (Command)

Creates a linear, angular, or ordinate dimension from the baseline of the previous or selected dimension.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Base and Continue drop-down drop-down ![](../images/ac.menuaro.gif) Baseline.
![](../images/GUID-98DDA65E-AE3C-49C3-B7C1-55174765BD2B-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Baseline.

## Summary

The default spacing between baseline dimensions can be set from the Dimension Style Manager, Lines tab, Baseline Spacing ([DIMDLI](DIMDLI-System-Variable.md) system variable).

![](../images/GUID-0B7AF53A-4184-4C45-9F94-C0A63A492050-low.gif)

If no dimension was created in the current session, you are prompted to select a linear, ordinate, or angular dimension to
use as the base for the baseline dimension.

## List of Prompts

The following prompts are displayed.

Select base dimension:
*Select a linear, ordinate, or angular dimension*

Otherwise, the program skips this prompt and uses the dimension object that was last created in the current session. If the
base dimension is linear or angular, the following prompt is displayed:

Specify a
[second extension line origin](DIMBASELINE-Command.md) or [[Undo](DIMBASELINE-Command.md)/[Select](DIMBASELINE-Command.md)] <Select>:
*Specify a point, enter an option, or press*Enter
*to select a base dimension*

If the base dimension is ordinate, the following prompt is displayed:

Specify
[feature location](DIMBASELINE-Command.md) or [Undo/Select] <Select>:

To end the command, press Enter twice, or press Esc. The current dimension style determines the appearance of the text.

Second Extension Line Origin
:   By default, the first extension line of the base dimension is used as the extension line origin for the baseline dimension.
    To override this default behavior, explicitly select the base dimension; the extension line origin becomes the extension line
    of the base dimension closest to the pick point of the selection. When you select a second point, the baseline dimension is
    drawn and the Specify a Second Extension Line Origin prompt is redisplayed. To end the command, press Esc. To select another
    linear, ordinate, or angular dimension to use as the basis for the baseline dimension, press Enter.

    ![](../images/GUID-09FDCF8E-6EA3-40D9-9C82-94284CA28B8D-low.png)

Feature Location
:   Uses the endpoint of the base dimension as the endpoint for the baseline dimension; you are prompted for the next feature
    location. When you select a feature location, the baseline dimension is drawn and the Specify Feature Location prompt is redisplayed.
    To select another linear, ordinate, or angular dimension to use as the basis for the baseline dimension, press Enter.

Undo
:   Undoes the last baseline dimension entered during this command session.

Select
:   Prompts you to select a linear, ordinate, or angular dimension to use as the base for the baseline dimension.

#### Related Concepts

* [About Creating Baseline and Continued Dimensions](About-Creating-Baseline-and-Continued-Dimensions.md)
* [About Creating Angular Dimensions](About-Creating-Angular-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*