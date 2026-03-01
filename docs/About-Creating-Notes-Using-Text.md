# About Creating Notes Using Text

The text you add to your drawing conveys various information. It may be a complex specification, title block information,
or a label.

## Single-Line Text

For short, simple entries use single-line text. Each text line is an independent object that you can relocate, reformat,
or otherwise modify.

## Multiline Text

For longer entries, or text that requires special formatting, use multiline text. Multiline text supports:

* Text wrapping
* Formatting individual characters, words, or phrases within a paragraph
* Columns
* Stacked text
* Bullet and numbered lists
* Tabs and indents

NOTE: Text that is included in a dimension or tolerance is created using the dimensioning commands. You can also create multiline
text with leaders.

## Text Styles

The text style sets the font, size, oblique angle, orientation, and other text characteristics. When you insert a text object
it uses the current text style.

The Standard text style exists by default in all drawings. You can create and modify text styles as needed. Once you create
a standard set of text styles, you can save the drawing as a template file (*.dwt*) that you can use when you start a new drawing.

## Current Layer Override

By default, all new objects are created on the
*current* layer. For new text and multiline text objects, you can specify a default layer that's different than the current layer with
the TEXTLAYER system variable. You can also use the layer override drop-down list from the Annotate tab, text panel (Windows
only).

![](../images/GUID-B2D68647-9EB0-436E-A0AB-07082B2E81FD-low.png)

## Rotated Views

Leader landings, components of dimensions, and text objects determine their horizontal and vertical directions from the UCS
axes at the time when they are created. If a view in a drawing is rotated, you can first use the UCS /View option to set the
horizontal and vertical directions relative to the
*drawing* rather than the rotated view.

#### Related Tasks

* [To Create Text](To-Create-Text.md)

#### Related Information

* [About Text Styles](About-Text-Styles.md)
* [MTEXT (Command)](MTEXT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*