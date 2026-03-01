# PDFIMPORT (Command)

Imports the geometry, fills, raster images, and TrueType text objects from a specified PDF file.

If the PDFIMPORT command is entered at the Command prompt, options are provided for selecting either a PDF underlay or for
specifying a file. The following prompts are displayed, after which the Import PDF dialog box is displayed. You can also specify
a PDF file with the IMPORT command.

## File

Opens a standard file selection dialog box, in which you can specify a PDF file.

NOTE:Importing a page from a PDF file does not use the setting of the INSUNITS system variable.

## Select PDF Underlay

Imports part or all of an attached PDF underlay as AutoCAD objects. The following options are displayed.

Specify first corner, Specify opposite corner
:   Prompts for the diagonal corners of a rectangular
    *crossing area*. Any objects crossing the specified area are imported.

Polygonal
:   Prompts for a polygonal
    *crossing area* defined by at least three points to specify the objects to be imported.

All
:   Selects all objects within the selected PDF underlay to be imported.

Settings
:   Opens the PDF Import Settings dialog box.

Keep, Detach or Unload PDF underlay?
:   Determines what to do with the selected PDF underlay after importing the specified objects. The Keep option leaves the PDF
    underlay unchanged; the Detach option removes the PDF underlay; and the Unload option temporarily hides the attached PDF.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [Import PDF Dialog Box](Import-PDF-Dialog-Box.md)
* [-PDFIMPORT (Command)](PDFIMPORT-Command.md)
* [IMPORT (Command)](IMPORT-Command.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)
* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*