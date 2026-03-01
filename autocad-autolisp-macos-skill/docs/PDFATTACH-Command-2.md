# -PDFATTACH (Command)

Attach a PDF underlay from the command line.

## Summary

When you attach a PDF file as an underlay, you link that referenced file to the current drawing. Any changes to the referenced
file are displayed in the current drawing when it is opened or reloaded.

## List of Prompts

The following prompts are displayed.

Path to PDF File to Attach
:   Enters the full path name to the PDF underlay file.

    Entering a tilde (*~*) displays the Select PDF File dialog box (a [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)).

    To avoid errors when entering a file name, it is recommended that you specify both the PDF file and path as follows:

    *path name/filename.pdf*

    or

    *“path name/filename.pdf”*

    If you enter a valid PDF file name without a file extension, the program adds the extension and searches for the file.

Enter Page Number or [?]
:   Enter a page number. For a list of pages, enter ?.

Enter Page(s) to List
:   Lists the pages available in the selected PDF file.

Insertion Point
:   Specifies the insertion point for the selected PDF file.

Scale Factor or [Unit]
:   Specifies the scale factor of the selected PDF underlay and the scale factor units.

    If [INSUNITS](INSUNITS-System-Variable.md) is set to “unitless” or if the underlay does not contain resolution information, the scale factor becomes the underlay width
    in AutoCAD units. If INSUNITS has a value such as millimeters, centimeters, inches, or feet, and the underlay has resolution
    information, the scale factor is applied after the true width of the underlay in AutoCAD units is determined.

Rotation
:   Specifies the rotation angle of the selected PDF underlay.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*