# Text Editor Visor

Controls the text style for the current multiline text object and character and paragraph formatting for selected text.

## Style Options

![](../images/GUID-9BED7C5B-B6C2-4077-AF77-0ADC0B083D79-low.png)

Style
:   Applies a text style to the multiline text object. The Standard text style is active by default.

Text Height
:   Sets the character height in drawing units for new text or changes the height of selected text. If the current text style
    has no fixed height, the text height is the value stored in the
    [TEXTSIZE](TEXTSIZE-System-Variable.md) system variable. A multiline text object can contain characters of various heights.

## Formatting Options

Bold
:   Turns bold formatting on and off for new or selected text. This option is available only for characters using TrueType fonts.

Italic
:   Turns italic formatting on and off for new or selected text. This option is available only for characters using TrueType fonts.

Strikethrough
:   Turns strikethrough on and off for new or selected text.

Underline
:   Turns underlining on and off for new or selected text.

Overline
:   Turns overline on and off for new or selected text.

Stack
:   If the selected text contains stack characters, creates stacked text, for example, fractions. When the stack characters,
    caret (^), forward slash (/), and pound sign (#), are used, the text to the left of the stack character is stacked on top
    of the text to the right.

    * Forward slash (/) stacks text vertically, separated by a horizontal line.
    * Pound sign (#) stacks text diagonally, separated by a diagonal line.
    * Caret (^) creates a tolerance stack, which is not separated by a line.

Superscript
:   Turns selected text into superscript, slightly smaller text set above the line of type. Turns selected superscript text to
    ordinary text.

Subscript
:   Turns selected text into subscript, slightly smaller text set below the line of type. Turns selected subscript text to ordinary
    text.

Match Text Formatting
:   Applies formatting of selected text to other characters within the same MTEXT object.

## Editor Options

Undo
:   Undoes actions in the text editor, including changes to either text content or text formatting.

Redo
:   Redoes actions in the text editor, including changes to either text content or text formatting.

Save
:   Closes the text editor and saves your changes.

## Additional Formatting Options

Font
:   Specifies a font for new text or changes the font of selected text. TrueType fonts are listed by font family name.
    AutoCAD 2026 compiled shape (SHX) fonts are listed by the name of the file in which the fonts are stored. Custom fonts and third-party
    fonts are displayed in the editor with Autodesk-supplied proxy fonts.

Color
:   Specifies a color for new text or changes the color of selected text.

Left, Center, Right, Justified and Distributed
:   Sets the justification and alignment for the left, center, or right text boundaries of the current or selected paragraph.
    Spaces entered at the end of a line are included and affect the justification of a line.

## Insert Options

Insert Symbols
:   Inserts a symbol or a nonbreaking space at the cursor position. You can also insert symbols manually. See
    Symbols and Special Characters.

    Commonly used symbols are listed on the submenu, along with their control code or Unicode string. Click Other to display the
    Character dialog box, which contains the entire character set for each font available on your system. When you have selected
    the character that you want to use, click Insert to place the character in the text editor. Close the Characters dialog box
    when you are done inserting special characters.

    NOTE:Symbols are not supported in vertical text.

Insert Field
:   Displays the
    [Insert Field dialog box](GUID-1B6DD22B-10D1-44ED-BAA2-E6D79FE52327.htm#WSC30CD3D5FAA8F6D8B82368FFC2D60192-7FFF), where you can select a field to insert in the text. When the dialog box closes, the current value of the field is displayed
    in the text.

## Tools

Find and Replace
:   Displays the
    [Find and Replace dialog box](GUID-39B391F5-F74D-4D6F-988D-61B24DEFEE52.htm#WSC30CD3D5FAA8F6D813D93F4FFC2D60E2B-7FB5).

Show/Hide Ruler
:   Shows or hides the ruler at the top of the Mtext editor.

#### Related Concepts

* [About Text Styles](About-Text-Styles.md)
* [About Creating Notes Using Text](About-Creating-Notes-Using-Text.md)

#### Related Information

* [In-Place Text Editor](In-Place-Text-Editor.md)
* [Paragraph Dialog Box](Paragraph-Dialog-Box.md)
* [Columns Menu](Columns-Menu.md)
* [Background Mask Dialog Box](Background-Mask-Dialog-Box.md)
* [Find and Replace Dialog Box - MTEXT](Find-and-Replace-Dialog-Box-MTEXT.md)
* [Stack Properties Dialog Box](Stack-Properties-Dialog-Box.md)
* [Text Symbols and Special Characters Reference](Text-Symbols-and-Special-Characters-Reference.md)
* [MTEXT (Command)](MTEXT-Command.md)
* [MTEDIT (Command)](MTEDIT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*