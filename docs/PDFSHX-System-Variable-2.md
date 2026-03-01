# PDFSHX (System Variable)

Controls whether text objects using SHX fonts are stored in PDF files as comments when you export a drawing as a PDF file.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

Because text that uses SHX fonts is not supported in PDF, drawings that are exported as PDF files can store this text as
hidden text or comments labeled "AutoCAD SHX Text." However, some older PDF viewers display these comments in the drawing
along with any other comments, which is usually not desirable.

| Value | Description |
| 0 | No additional comments are created when exporting a PDF file. Text that uses SHX fonts is preserved visually as geometric objects. |
| 1 | Creates comments from text objects that use SHX fonts. |
| 2 | Creates hidden text from text objects that use SHX fonts. |

NOTE:Previously, this system variable was named EPDFSHX.

#### Related Concepts

* [About Exporting Drawing Files to PDF](About-Exporting-Drawing-Files-to-PDF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*