# PDFSHXBESTFONT (System Variable)

When converting imported PDF geometry to text, controls whether the PDFSHXTEXT command uses the best matching font or uses
the first selected font that exceeds the recognition threshold.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 |

Using the best font option takes longer to process, but ensures the best result between similar fonts.

| Value | Description |
| 0 or OFF | Uses the first font that exceeds the recognition threshold |
| 1 or ON | Compares against all selected fonts and uses the best matching font that exceeds the recognition threshold |

NOTE:This system variable controls the setting on the PDF Text Recognition Settings dialog box.

#### Related References

* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)
* [PDF Text Recognition Settings Dialog Box](PDF-Text-Recognition-Settings-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*