# PDFSHXTEXT (Command)

Converts the SHX geometry imported from PDF files into individual multiline text objects.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Recognize SHX Text.
![](../images/GUID-CFD896EE-30B7-4BB7-962F-0F83C1338472-low.png)

The PDF format stores text using TrueType fonts, but PDF does not support text that uses AutoCAD SHX fonts. Instead, text
objects that use SHX fonts are stored in PDF as geometric objects to maintain visual fidelity.

When you import a PDF file that includes SHX geometry, you can use PDFSHXTEXT as a post-processing tool to convert the selected
geometry into single-line mtext objects.

For the best results, do the following:

* Find a closely matching SHX font against which to compare the selected SHX geometry
* Be careful to select only SHX geometry
* Select small amounts of text to increase your chances for locating problems and reduce the possibility of inadvertently selecting
  non-SHX geometry

IMPORTANT:Make sure that the UCS X axis is aligned with the direction of the text. You can use a horizontal segment of the SHX geometry
as a reference. For example, enter UCS /OBject and then select the horizontal segment in the SHX geometry.

The selected objects that were successfully converted to multiline text are temporarily highlighted. Objects that are not
highlighted need additional attention. In most circumstances, it's easier to edit the text that was successfully converted
by manually adding the missing text.

NOTE: Asian-language big fonts are not supported.

## Select Objects

Select only the geometric objects that represents the SHX text imported from a PDF file.

Specify first corner, Specify opposite corner
:   Prompts for the diagonal corners of a rectangular
    *crossing* or
    *window* selection area. All objects selected are processed.

## Settings

Displays the PDF Text Recognition Settings dialog box.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [-PDFSHXTEXT (Command)](PDFSHXTEXT-Command-2.md)
* [TXT2MTXT (Express Tool)](TXT2MTXT-Express-Tool.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*