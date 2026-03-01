# FONTMAP (System Variable)

Specifies the font mapping file to be used.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Registry |
| Initial value: | acad.fmp |

A font mapping file contains one font mapping per line; the original font used in the drawing and the font to be substituted
for it are separated by a semicolon (;). For example, to substitute the Times TrueType font for the Roman font, the line in
the mapping file would read as follows:

```
romanc.shx;times.ttf
```

If FONTMAP does not point to a font mapping file, if the FMP file is not found, or if the font file name specified in the
FMP file is not found, the font defined in the style is used. If the font in the style is not found, a font is substituted
according to the substitution rules.

FONTMAP affects the creation, editing, and display of all text objects.

#### Related Concepts

* [About Substitute Fonts](About-Substitute-Fonts.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*