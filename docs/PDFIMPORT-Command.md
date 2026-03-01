# -PDFIMPORT (Command)

Imports the objects in a PDF file or an attached PDF underlay from the command line.

Options are provided for selecting either a PDF underlay or for specifying a file.

The following prompts are displayed.

File
:   Opens a standard file selection dialog box, in which you can specify a PDF file. If the FILEDIA system variable is changed
    from 1 to 0, the dialog box is replaced by a command line prompt to enter the file name.

Enter Page Number
:   Enter a page number. For a list of pages, enter
    *?*.

Enter Page(s) to list <\*>
:   Lists the pages available in the PDF file in a separate text window.

Insertion Point
:   Specifies the insertion point for the PDF file.

Scale Factor
:   Specifies the scale factor of the imported PDF data and the scale factor units.

    NOTE:Importing a page from a PDF file does not use the setting of the INSUNITS system variable.

Rotation
:   Specifies the rotation angle of the imported PDF data.

Select PDF Underlay
:   Imports part or all of an attached PDF underlay as AutoCAD objects. The following options are displayed.

*Specify first corner, Specify opposite corner*
:   Prompts for the diagonal corners of a rectangular
    *crossing area*. Any objects crossing the specified area are imported.

Polygonal
:   Prompts for a
    *polygonal crossing area* defined by at least three points to specify the objects to be imported.

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

* [PDF Import Settings Dialog Box](PDF-Import-Settings-Dialog-Box.md)
* [PDFIMPORT (Command)](PDFIMPORT-Command-2.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)
* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*