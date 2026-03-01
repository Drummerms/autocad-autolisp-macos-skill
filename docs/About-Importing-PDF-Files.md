# About Importing PDF Files

You can import the geometry, fills, raster images, and TrueType text from a PDF file into the current drawing. The visual
fidelity along with some properties such as PDF scale, layers, lineweights, and colors can be preserved.

PDF files are a common way of publishing and sharing design data for review and markup. AutoCAD supports creating PDF files
as a publishing output for AutoCAD drawings, and importing PDF data into AutoCAD using either of two options:

* PDF files can be attached to drawings as underlays, which can be used as a reference when collaborating on projects.
* PDF data can be imported as objects, in part or entirely, which can be used a reference and also modified.

If you import PDF data, you can choose to specify a page from a PDF file or you can convert all or part of an attached PDF
underlay into AutoCAD objects.

## How Objects are Translated

When a PDF file is generated, all supported objects are translated into paths, fills, raster images, markups, and TrueType
text. In PDF, paths are composed of line segments and cubic Bézier curves, either connected or independent. However, when
a PDF file is imported into AutoCAD, note the following:

* Raster images generate PNG format files, and they are saved in a folder specified by the PDFIMPORTIMAGEPATH system variable,
  which can be specified in the Preferences dialog box, Application tab. These images are attached to the drawing file.
* Bézier curves are converted into circles and arcs if they are within a reasonable tolerance to those shapes. Otherwise, they
  are converted into 2D polylines.
* Elliptical shapes can be converted into 2D polylines, splines, or ellipses depending on how they were stored in the PDF.
* Optionally, each set of approximately collinear segments are combined into a polyline with a dashed linetype named PDF\_Import.
* Compound objects such as dimensions, leaders, patterned hatches, and tables result in separate objects as if these objects
  were exploded.
* Fills are imported as 2D solids, or optionally as solid-filled hatches.
* Patterned hatches are imported as many separate objects.
* Solid-filled areas are converted into solid hatches and 2D solids. They are assigned a 50% transparency to make sure that
  any text within the areas is visible.
* Text that used TrueType fonts is preserved, but text that originally used SHX fonts is imported as separate geometric objects.
* Point objects are converted to zero-length polylines.
* Markups are not imported.

## Understand the Limitations

When an AutoCAD DWG file is exported as a PDF file, both information and precision are unavoidably lost. It is important to
be aware of the degree of visual fidelity that can be reasonably expected.

The data in DWG files are stored as double-precision floating-point numbers, while the data in PDF files are only single precision.
This reduction rounds off coordinate values, and the loss of precision is most noticeable in the following cases:

* Computed locations such as tangent points, the endpoints of arcs, and the endpoints of rotated lines
* Data with a large dynamic range, from the largest to the smallest
* Large coordinates in PDF files such as those found in maps.
* PDF files that were generated with a low dpi (dots per inch) setting

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [PDFIMPORT (Command)](PDFIMPORT-Command-2.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)
* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)

#### Related Concepts

* [About Exporting Drawing Files to PDF](About-Exporting-Drawing-Files-to-PDF.md)

#### Related Information

* [About Attaching Files as Underlays](About-Attaching-Files-as-Underlays.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*