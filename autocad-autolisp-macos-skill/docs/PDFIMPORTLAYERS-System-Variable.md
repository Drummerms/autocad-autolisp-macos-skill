# PDFIMPORTLAYERS (System Variable)

Controls what layers are assigned to objects imported from PDF files.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 |

| Value | Description |
| 0 | Creates layers corresponding to the PDF layers. These layers have a PDF\_ prefix. If no layers exist in the PDF file, setting 1 is used instead. |
| 1 | Creates layers corresponding to the general types of objects: PDF\_Geometry, PDF\_Solid Fills, PDF\_Images, and PDF\_Text. |
| 2 | Use the current layer. All objects are imported to the current layer even if layers were defined in the PDF file. If necessary, turns on the current layer. |

Raster and markup objects in PDF files are not supported data types and are automatically excluded.

NOTE:Text that was originally created with AutoCAD SHX fonts are stored as geometric objects in PDF files.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*