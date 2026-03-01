# About Text Styles

The current text style sets the font, size, obliquing angle, orientation, and other text characteristics. If you want to
create text using a different text style, you can make another text style current. The table shows the settings for the STANDARD
text style.

##

| Text Style Settings | | |
| Setting | Default | Description |
| Style name | STANDARD | Name with up to 255 characters |
| Font name | *txt.shx* | File associated with a font (character style) |
| Big Font /Asian Set | None | Special shape definition file used for a non-ASCII character set, such as Kanji |
| Height | 0 | Character height |
| Width factor | 1 | Expansion or compression of the characters |
| Obliquing angle | 0 | Slant of the characters |
| Backwards | No | Backwards text |
| Upside down | No | Upside-down text |
| Vertical | No | Vertical or horizontal text |

The settings for the current text style are displayed at the command prompts. You can use or modify the current text style
or create and load a new text style. Once you've created a text style, you can modify its characteristics, change its name,
or delete it when you no longer need it.

## Creating and Modifying Text Styles

Except for the default STANDARD text style, you must create any text style that you want to use.

Text style names can be up to 255 characters long. They can contain letters, numbers, and the special characters dollar sign
($), underscore (\_), and hyphen (-). If you don't enter a text style name, the text styles are automatically named Stylen,
where *n* is a number that starts at 1.

Certain style settings affect multiline and single-line text objects differently. For example, changing the Upside Down and
Backwards options has no effect on multiline text objects. Changing Width Factor and Obliquing options has no effect on single-line
text.

If you rename an existing text style, any text using the old name assumes the new text style name.

## Changing Text Style

When you change the text style of a multiline text object, the updated settings are applied to the entire object, and some
formatting of individual characters might not be retained. The following table describes the effects of text style change
on character formatting.

| Formatting | Retained? |
| Bold | No |
| Color | Yes |
| Font | No |
| Height | No |
| Italic | No |
| Stacking | Yes |
| Underlining | Yes |

## Annotative Text Styles

Use annotative text for notes and labels in your drawing. You create annotative text by using an annotative text style, which
sets the height of the text on the paper.

#### Related Tasks

* [To Set the Current Text Style](To-Set-the-Current-Text-Style.md)

#### Related Concepts

* [About Using Asian Big Font SHX Files](About-Using-Asian-Big-Font-SHX-Files.md)

#### Related Information

* [About Assigning Fonts to Text Styles](About-Assigning-Fonts-to-Text-Styles.md)
* [To Assign a TrueType Font to a Text Style](To-Assign-a-TrueType-Font-to-a-Text-Style.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*