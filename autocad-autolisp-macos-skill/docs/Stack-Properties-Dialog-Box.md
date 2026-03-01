# Stack Properties Dialog Box

Edits the text, stack type, alignment, and size of stacked text.

To open the Stack Properties dialog box, select the stacked text, right-click, and choose Stack Properties on the shortcut
menu.

![](../images/GUID-FBFE51D8-CE4F-4585-B038-6B44CB9BFFB9-low.png)

## Summary

To open the Stack Properties dialog box, select the stacked text, right-click, and click Stack Properties on the shortcut
menu.

You can edit the upper and lower text separately. The Appearance options control the stack style, position, and text size
of the stacked text.

## List of Options

The following options are displayed.

Text

Changes the upper and lower numbers of a stacked fraction.

Upper
:   Edits the number in the upper part or first half of a stacked fraction.

Lower
:   Edits the number in the lower part or second half of a stacked fraction.

Appearance

Edits the style, position, or text size of a stacked fraction.

Style

Specifies a style format for stacked text: horizontal fraction, diagonal fraction, tolerance, and decimal.

Fraction (Horizontal)
:   Stacks the selected text with the first number on top of the second number separated by a horizontal line.

Fraction (Diagonal)
:   Stacks the selected text with the first number on top of the second number separated by a diagonal line.

    NOTE:Releases of AutoCAD earlier than AutoCAD 2000 do not support diagonal fractions. If a multiline text object contains diagonal
    fractions, the fractions are converted to horizontal fractions when you save the drawing to pre-AutoCAD 2000 releases. Diagonal
    fractions are restored when the drawing is re-opened in AutoCAD 2000 or a later release. If a single multiline text object
    contains both horizontal and diagonal fractions, all fractions are converted to diagonal fractions when the drawing is reopened
    in AutoCAD 2000 or a later release.

Tolerance
:   Stacks the selected text with the first number on top of the second number. There is no line between the numbers.

Decimal
:   A variation of the Tolerance style that aligns the decimal point of both the upper and lower numbers of selected text.

Position

Specifies how fractions are aligned. Center alignment is the default. All stacked text in an object uses the same alignment.

Top
:   Aligns the top of the fraction with the top of the text line.

Center
:   Centers the fraction vertically at the center of the text line.

Bottom
:   Aligns the bottom of the fraction with the text baseline.

Text Size

Controls the size of the stacked text as a percentage of the size of the current text style (from 25 to 125 percent).

Defaults

Saves the new settings as defaults or restores the previous default values to the current stacked text.

AutoStack Button

Displays the
[AutoStack Properties dialog box](GUID-60C5A608-2B76-4793-9FA9-011942E69ABE.htm#WSC30CD3D5FAA8F6D813D93F4FFC2D60E2B-7FB1). AutoStack only stacks numeric characters immediately before and after the carat, slash, and pound characters. To stack nonnumeric
characters, or text that includes spaces, select the text and choose Stack from the text editor shortcut menu.

#### Related Concepts

* [About Stacked Characters Within Multiline Text](About-Stacked-Characters-Within-Multiline-Text.md)

#### Related Information

* [AutoStack Properties Dialog Box](AutoStack-Properties-Dialog-Box.md)
* [In-Place Text Editor](In-Place-Text-Editor.md)
* [MTEXT (Command)](MTEXT-Command.md)
* [MTEDIT (Command)](MTEDIT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*