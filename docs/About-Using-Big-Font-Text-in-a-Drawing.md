# About Using Big Font Text in a Drawing

A Big Font file can be used for drawing text by creating a text style with the STYLE command that specifies the name of the
Big Font file.

The text style can be used as a normal ASCII font as well; enter only the two file names, separated by a comma. The following
example uses the command line version of the STYLE command.

Command: -STYLE

Enter name of text style or [?] <*current*>: *style\_name*

Specify full font name or font file name (TTF or SHX): *txt,greek*

The program assumes that the first name is the normal font and that the second is the big font.

If you enter only one name, the program assumes it is the normal font and removes any associated Big Font.

By using leading or trailing commas when specifying the font file names, you can change one font without affecting the other,
as shown in the following table.

| Input for changing fonts | |
| Input | Result |
| *normal, big* | Both normal and Big Font specified |
| *normal,* | Normal font only (Big Font unchanged) |
| *,big* | Big Font only (normal font unchanged) |
| *normal* | Normal font only (if necessary, Big Font removed) |
| Enter (null response) | No change |

When you use the -STYLE command to list styles or to revise an existing style, the program displays the normal font file,
a comma, and the Big Font file. If the style has only a Big Font file, it is displayed with a leading comma: ,greek.

For each character in a text string, the program searches the Big Font file first. If the character is not found there, the
normal font file is searched.

#### Related Tasks

* [To Enable Big Fonts](To-Enable-Big-Fonts.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Using a Big Font to Extend a Font](About-Using-a-Big-Font-to-Extend-a-Font.md)
* [About Defining an Extended Big Font File](About-Defining-an-Extended-Big-Font-File.md)
* [About Defining a Big Font](About-Defining-a-Big-Font.md)
* [About Shape Descriptions](About-Shape-Descriptions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*