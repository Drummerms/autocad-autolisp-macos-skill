# Text Style Dialog Box

Creates, modifies, or specifies text styles.

STYLE (Command)

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Style.
![](../images/GUID-A1A489F9-EDAC-453E-B777-A21DD0ADC60D-low.png)

![](../images/GUID-1899503C-3FCA-4CCB-A931-A2D428C80001-low.png)

## Summary

Creates, modifies, or sets named text styles.

## List of Options

The following options are displayed.

Preview

Displays sample text that changes dynamically as you change fonts and modify the effects.

Effects

Modifies characteristics of the font, such as its height, width factor, and obliquing angle and whether it is displayed upside
down, backwards, or vertically aligned.

Annotative (![](../images/GUID-B3D4A80D-2642-4C17-BD2D-BF5CA00B4D3F-low.png))
:   Specifies that the text is annotative. Click the information icon to learn more about the annotative objects.

Match Text Orientation to Layout
:   Specifies that the orientation of the text in paper space viewports matches the orientation of the layout. This option is
    available when the Annotative option is selected.

Upside Down
:   Displays the characters upside down.

Backwards
:   Displays the characters backwards.

Vertical
:   Displays the characters aligned vertically. Vertical is available only if the selected font supports dual orientation. Vertical
    orientation is not available for TrueType fonts.

Text Height
:   Changes the size of the text. This option is available when the Annotative option is cleared.

Paper Text Height
:   Sets the text height based on the value you enter. Entering a height greater than 0.0 sets the text height for this style
    automatically. If you enter 0.0, the text height defaults to the last text height used, or the value stored in the drawing
    template file.

    TrueType fonts might be displayed at a smaller height than SHX fonts with the same height setting.

    If the Annotative option is selected, the value entered sets the text height in paper space.

Width Factor
:   Sets the character spacing. Entering a value less than
    *1.0* condenses the text. Entering a value greater than
    *1.0* expands it.

Angle
:   Sets the obliquing angle of the text. Entering a value between
    *-85* and
    *85* italicizes the text.

NOTE:TrueType fonts using the effects described in this section might appear bold on the screen. Onscreen appearance has no effect
on plotted output. Fonts are plotted as specified by applied character formatting.

Styles

Displays the list of styles in the drawing.

Style names can be up to 255 characters long. They can contain letters, numbers, and the special characters dollar sign ($),
underscore (\_), and hyphen (-).

Family List

Lists the font family name for all registered TrueType fonts and all compiled shape (SHX) fonts in the
*Fonts* folder.

When you select a name from the list, the program reads the file for the specified font. The file's character definitions
are loaded automatically unless the file is already in use by another text style. You can define several styles that use the
same font.

Typeface

Specifies font character formatting, such as italic, bold, or regular.

When an SHX font file is selected from the Family list, you can select a Big Font file name from the Asian Set list.

Asian Set

Lists the available Big Font files when an SHX file is selected from the Family list. Select None if you do not want to use
a Big Font.

New (+)

Adds a new text style to the Styles list and automatically supplies the name “ style*n*” (where
*n* is the number of the supplied style) for the current settings. You can accept the default or enter a name and close the Text
Style dialog box to apply the current style settings to the new style name.

Delete (-)

Removes the selected text style.

NOTE:You cannot remove text styles that are in use by an annotation object or style.

Style List Filter

The drop-down list specifies whether all styles or only the styles in use are displayed in the styles list.

Family Filter

Filters the fonts listed in the Family list.

#### Related Tasks

* [To Set Text Height in a Text Style](To-Set-Text-Height-in-a-Text-Style.md)
* [To Assign a TrueType Font to a Text Style](To-Assign-a-TrueType-Font-to-a-Text-Style.md)
* [To Set the Current Text Style](To-Set-the-Current-Text-Style.md)
* [To Create Text](To-Create-Text.md)

#### Related Concepts

* [About Assigning Fonts to Text Styles](About-Assigning-Fonts-to-Text-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*