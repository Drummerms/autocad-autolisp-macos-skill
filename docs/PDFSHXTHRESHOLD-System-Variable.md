# PDFSHXTHRESHOLD (System Variable)

Sets the percentage of the selected geometry that must match a font before the geometry is converted to text objects.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 95 |

This system variable provides direct access to the Conversion Settings percentage setting in the PDF Text Recognition Settings
dialog box of the PDFSHXTEXT command. The percentage applies to each cluster of geometry analyzed during the conversion process.
A low value creates text even when some characters aren't recognized. A high value ensures the closest matching selected font
is used if possible.

The valid range is 1 to 100.

#### Related References

* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)
* [PDF Text Recognition Settings Dialog Box](PDF-Text-Recognition-Settings-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*