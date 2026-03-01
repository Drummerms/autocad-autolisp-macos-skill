# About Using Asian Big Font SHX Files

Asian alphabets contain thousands of non-ASCII characters. To support such text, the program provides a special type of shape
definition known as a Big Font file. You can set a style to use both regular and Big Font files.

| Asian Language Big Fonts Included in the Product | |
| Font File Name | Description |
| @extfont2.shx | Japanese vertical font (a few characters are rotated to work correctly in vertical text) |
| bigfont.shx | Japanese font, subset of characters |
| chineset.shx | Traditional Chinese font |
| extfont.shx | Japanese extended font, level 1 |
| extfont2.shx | Japanese extended font, level 2 |
| gbcbig.shx | Simplified Chinese font |
| whgdtxt.shx | Korean font |
| whgtxt.shx | Korean font |
| whtgtxt.shx | Korean font |
| whtmtxt.shx | Korean font |

When you specify fonts using the STYLE command, the assumption is that the first name is the normal font and the second (separated
by a comma) is the Big Font. If you enter only one name, it's assumed that it is the normal font and any associated Big Font
is removed. By using leading or trailing commas when specifying the font file names, you can change one font without affecting
the other, as shown in the following table.

| Specifying fonts and Big Fonts at the Command prompt | |
| Enter this ... | To specify this ... |
| [font name],[big font name] | Both normal fonts and Big Fonts |
| [font name], | Only a normal font (Big Font unchanged) |
| ,[big font name] | Only a Big Font (normal font unchanged) |
| [font name] | Only a normal font (Big Font, if any, removed) |
| ENTER (null response) | No change |

NOTE:

Long file names that contain commas as font file names are not accepted. The comma is interpreted as a separator for an SHX
font-Big Font pair.

#### Related Tasks

* [To Set the Current Text Style](To-Set-the-Current-Text-Style.md)

#### Related Information

* [About Text Styles](About-Text-Styles.md)
* [About Assigning Fonts to Text Styles](About-Assigning-Fonts-to-Text-Styles.md)
* [To Assign a TrueType Font to a Text Style](To-Assign-a-TrueType-Font-to-a-Text-Style.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*