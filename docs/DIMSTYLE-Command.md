# -DIMSTYLE (Command)

Creates and modifies dimension styles.

## Summary

You can save or restore dimensioning system variables to a selected dimension style.

## List of Prompts

The following prompts are displayed.

Current dimension style: <*current*> Annotative: <*current>*

Enter a dimension style option

[[ANnotative](DIMSTYLE-Command.md)/[Save](DIMSTYLE-Command.md)/[Restore](DIMSTYLE-Command.md)/[STatus](DIMSTYLE-Command.md)/[Variables](DIMSTYLE-Command.md)/[Apply](DIMSTYLE-Command.md)/[?](DIMSTYLE-Command.md)] <Restore>: *Enter an option or press* Enter

Annotative

Creates an annotative dimension style.

Save

Saves the current settings of dimensioning system variables to a dimension style.

Name
:   Saves the current settings of dimensioning system variables to a new dimension style using the name you enter. The new dimension
    style becomes the current one.

    If you enter the name of an existing dimension style, the following prompts are displayed:

    That name is already in use, redefine it? <N>: *Enter*  *y* *or press* Enter

    If you enter *y*, associative dimensions that use the redefined dimension style are regenerated.

    To display the differences between the dimension style name you want to save and the current style, enter a tilde (~) followed
    by the style name at the Enter Name for New Dimension Style prompt. Only settings that differ are displayed, with the current
    setting in the first column, and the setting of the compared style in the second column.

?—List Dimension Styles
:   Lists the named dimension styles in the current drawing.

Restore

Restores dimensioning system variable settings to those of a selected dimension style.

Name
:   Makes the dimension style you enter the current dimension style.

    To display the differences between the dimension style name you want to restore and the current style, enter a tilde (~) followed
    by the style name at the Enter Dimension Style Name prompt. Only settings that differ are displayed, with the current setting
    in the first column, and the setting of the compared style in the second column. After the differences are displayed, the
    previous prompt returns.

?—List Dimension Styles
:   Lists the named dimension styles in the current drawing.

Select Dimension
:   Makes the dimension style of the selected object the current dimension style.

Status

Displays the current values of all dimension system variables.

Variables

Lists the dimension system variable settings of a dimension style or selected dimensions without modifying the current settings.

Name
:   Lists the settings of dimension system variables for the dimension style name you enter.

    To display the differences between a particular dimension style and the current style, enter a tilde (~) followed by the style
    name at the Enter Dimension Style Name prompt. Only settings that differ are displayed, with the current setting in the first
    column, and the setting of the compared style in the second column.

?—List Dimension Styles
:   Lists the named dimension styles in the current drawing.

Select Dimension
:   Lists the dimension style and any dimension overrides for the dimension object you select.

Apply

Applies the current dimensioning system variable settings to selected dimension objects, permanently overriding any existing
dimension styles applied to these objects.

The dimension line spacing between existing baseline dimensions is not updated (see the [DIMDLI](DIMDLI-System-Variable.md) system variable); dimension text variable settings do not update existing leader text.

?—List Dimension Styles

Lists the named dimension styles in the current drawing.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*