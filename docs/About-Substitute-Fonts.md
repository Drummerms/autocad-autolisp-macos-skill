# About Substitute Fonts

The program accommodates a font that is not currently on your system by substituting another font.

## Specifying an Alternate Font

If your drawing specifies a font that is not currently on your system, the font designated as your alternate font is automatically
substituted. By default, the *simplex.shx* file is used. If you want to specify a different font, enter the alternate font file name by changing the FONTALT system
variable. If you use a text style that uses an Asian Big Font, you can map it to another font using the FONTALT system variable.
This system variable uses a default font file pair: *txt.shx* and *bigfont.shx*.

In previous releases, you could display PostScript ®  fonts in the drawing. Because later releases cannot display PostScript fonts, Autodesk has supplied TrueType font equivalents.
These PostScript fonts are mapped to the equivalent TrueType fonts in a font mapping file. Additionally, when a TrueType font
is not available, you can specify a different TrueType font, making sure that the fonts are similar to avoid text length or
wrapping problems.

If the default font does not support the characters you enter using the In-Place Text Editor, an alternative font is substituted.

CIF or MIF codes entered with the In-Place Text Editor are now automatically converted to display the actual characters.

## Editing the Font Mapping File

A font mapping file is a list of text fonts and their substitutes. If a text font used in a drawing cannot be located, another
text font is substituted for the missing font using a font mapping file.

Each line in the font mapping file contains the name of a font file (with no file extension or path) followed by a semicolon
(;) and the name of the substitute font file. The substitute file name includes a file extension such as *.ttf*.

A font mapping file is an ordinary ASCII text file with a .*fmp* extension. You can change the font assignments in a font mapping file using any ASCII text editor.

For example, you could use the following entry in a font map file to specify that the *timesnr.pfb* font file be substituted with the *times.ttf* font file:

timesnr;times.ttf

The following table shows the font substitution rules used if a font file cannot be located when a drawing is opened.

| Font substitution | | | | |
| File extension | First mapping order | Second mapping order | Third mapping order | Fourth mapping order |
| *.ttf* | Use font mapping table | Use font defined in text style | Windows substitutes a similar font |  |
| *.shx* | Use font mapping table | Use font defined in text style | Use FONTALT | Prompt for new font |
| *.pfb* | Use font mapping table | Use FONTALT | Prompt for new font |  |

## Displaying Proxy Fonts

For third-party or custom SHX fonts that have no TrueType equivalent, one of several different TrueType fonts called proxy
fonts is substituted. In the In-Place Text Editor, proxy fonts look different from the fonts they represent to indicate that
the proxy fonts are substitutions for the fonts used in the drawing.

If you want to format characters by assigning one of these fonts, first create a text style that uses the font and then apply
that text style to the characters.

#### Related Information

* [To Specify a Font Mapping File](To-Specify-a-Font-Mapping-File.md)
* [To Specify a Default Alternate Font](To-Specify-a-Default-Alternate-Font.md)
* [Font Not Found Dialog Box](Font-Not-Found-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*