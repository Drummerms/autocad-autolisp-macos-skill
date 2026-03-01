# -PDFSHXTEXT (Command)

Converts the SHX geometry imported from PDF files into individual multiline text objects from the command line.

For additional information, see the PDFSHXTEXT command topic.

The following prompts are displayed.

### Select Objects

Select only the geometric objects that represents the SHX text imported from a PDF file.

Specify first corner, Specify opposite corner
:   Prompts for the diagonal corners of a rectangular
    *crossing* or
    *window* selection area. All objects selected are processed.

### Settings

Select only the geometric objects that represents the SHX text imported from a PDF file.

Add Font
:   Adds an SHX font to the comparison list.

Remove Font
:   Removes an SHX font to the comparison list.

Threshold
:   Sets the percentage of geometry that must match a font before replacing it with text. A lower value creates text even when
    some characters aren't recognized. A high value ensures the closest matching selected font is used if possible.

Layer
:   Specifies the layer of the multiline text objects that are created by the conversion, either the current layer or the original
    layer of the geometry.

Best Match
:   Specifies whether the best match from all the selected fonts is used for replacement, or the first match that exceeds the
    recognition threshold is used.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)
* [TXT2MTXT (Express Tool)](TXT2MTXT-Express-Tool.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*