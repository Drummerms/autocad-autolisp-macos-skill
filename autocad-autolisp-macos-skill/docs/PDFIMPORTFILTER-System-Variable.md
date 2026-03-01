# PDFIMPORTFILTER (System Variable)

Controls what types of data are imported from a PDF file and converted to AutoCAD objects.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 8 |

| Value | Description |
| 0 | Imports all supported data types. |
| 1 | Excludes geometric objects. |
| 2 | Excludes TrueType text objects. |
| 4 | Excludes solid fills. |
| 8 | Excludes raster images. |

Markup objects in PDF files are not supported data types and are automatically excluded.

NOTE:Text that was originally created with AutoCAD SHX fonts is exported to PDF as geometric objects. When such PDF files are imported,
any SHX geometry is not automatically converted back to text, and you would use the PDFSHXTEXT command for the conversion.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*