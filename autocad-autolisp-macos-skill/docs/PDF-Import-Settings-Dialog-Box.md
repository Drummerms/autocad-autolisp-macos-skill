# PDF Import Settings Dialog Box

Sets the options for importing geometry, fills, raster images, and TrueType text objects from a specified PDF file or underlay.

PDFIMPORT (Command):
Select a PDF Underlay ![](../images/ac.menuaro.gif) Specify the settings option at the prompt

![](../images/GUID-41A72D5C-C0C6-43A4-B5A3-434087894FBA-low.png)

## List of Options

The following options are displayed.

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

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [-PDFIMPORT (Command)](PDFIMPORT-Command.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*