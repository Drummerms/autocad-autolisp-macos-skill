# Import PDF Dialog Box

Sets the options for importing geometry, fills, raster images, and TrueType text objects from a specified page of the PDF
file.

PDFIMPORT (Command)

![](../images/GUID-92EA4C81-7B7A-4B6F-A607-285A9691B15C-low.png)

## List of Options

The following options are displayed.

### Browse

Displays a standard file selection dialog box, in which you can select a different PDF file to import.

### Page to Import

When you import a PDF file, you choose the page by entering the page number or by clicking the thumbnail image. If you want
to display a larger view of the selected page, you can toggle between a full-size view and thumbnail views. You import a single
page at a time.

Page size
:   Displays a standard page size, imperial or metric. If the page is non-standard, the dimensions are displayed in inches or
    in millimeters depending on the setting of the MEASUREMENT system variable.

PDF scale
:   Displays the scale of the PDF file. Metric units are assumed to be in millimeters; imperial units are assumed to be in inches.

### Location

Specifies the location of the imported PDF relative to the location of the current UCS.

Specify insertion point on-screen
:   When this option is selected, you can specify the location with your input device or by entering coordinates relative to the
    current UCS after the dialog box closes. When this option is cleared, the PDF is imported at the UCS origin (0,0).

Scale
:   You can specify a different import scale factor for the imported objects. Importing a page from a PDF file does not use the
    setting of the INSUNITS system variable since each page might be at a different scale.

Rotation
:   Provides a list of standard rotations. You can also enter a custom rotation.

### PDF Data to Import

You can include or exclude data by type.

Vector geometry
:   PDF geometric data types include linear paths, Beziér curves, and solid-filled areas, which are imported as polylines, and
    2D solids or solid-filled hatches. Within a tolerance, curves that resemble arcs, circles, and ellipses are interpolated as
    such. Patterned hatches are imported as many separate objects.

Solid fills
:   Includes all solid-filled areas. If these filled areas were originally exported into PDF format from AutoCAD, the solid areas
    would include solid-filled hatches, 2D solids, wipeout objects, wide polylines, and triangular arrowheads.

    NOTE:Solid-filled hatches are assigned a 50% transparency so that objects on top or underneath can be easily seen. You can change
    the color and transparency of these objects manually, or you can select them all by filtering for transparency with Quick
    Select (QSELECT command).

TrueType text
:   Imports text objects that use TrueType fonts. PDF files recognize only TrueType text objects; text objects that use SHX fonts
    are treated as geometric objects. TrueType fonts are either matched or substituted with similar fonts available on your system.
    Imported text is assigned to an AutoCAD text style that begins with the characters PDF\_ and the TrueType font name. You can
    assign a different font to the PDF style with the STYLE command.

Raster Images
:   Imports raster images by saving them as PNG files and attaching them to the current drawing. The path to each raster image
    is controlled by the PDFIMPORTIMAGEPATH system variable.

### Layers

You can choose what method to apply for assigning imported objects to layers.

Use PDF layers
:   Creates AutoCAD layers from the layers stored in the PDF file, and applies them to the imported objects. The layer names have
    a PDF prefix. If no layers are present in the PDF file, object layers are created instead.

Create object layers
:   Creates AutoCAD layers for each of the following general types of objects imported from the PDF file: PDF\_Geometry, PDF\_Solid
    Fills, PDF\_Images, and PDF\_Text.

Current layer
:   Imports all specified PDF objects to the current layer.

### Import Options

Several options are available to control how PDF objects are processed after being imported.

Import as block
:   Imports the PDF file as a block rather than as separate objects.

Join line and arc segments
:   Joins contiguous segments into a polyline where possible.

Convert solid fills to hatches
:   Converts 2D solid objects into solid-filled hatches. 2D solids that can be inferred as arrowheads are excluded. You can use
    QSELECT to create separate selection sets, hatches and arrowheads to change their properties in a single operation.

Apply lineweight properties
:   Retains or ignores the lineweight properties of the imported objects.

Infer linetypes from collinear dashes
:   Combines sets of short collinear segments into single polyline segments. These polylines are assigned a dashed linetype named
    PDF\_Import and assigned linetype scale. You can use QSELECT to identify the objects with this linetype, and reassign different
    linetypes to them at an appropriate linetype scale.

    NOTE:The inference process is imperfect. Turn this option off if you see dashed lines created from small regularly spaced line
    segments or underlined text.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [PDFIMPORT (Command)](PDFIMPORT-Command-2.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)
* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*