# About Attaching Files as Underlays

You can attach a PDF file as an underlay to a drawing file.

You reference and place underlay files in drawing files the same as you do raster image files; they are not actually part
of the drawing file. Like raster files, the underlay is linked to the drawing file through a path name. The path to the file
can be changed or removed at any time.

By attaching underlays this way, you can use files in your drawing without greatly increasing the drawing file size. You can
only view PDF underlays in the 2D Wireframe visual style.

NOTE:Although underlay files are reproductions of their source drawing, they are not as precise as drawing files. Underlays will
show slight discrepancies in precision.

## Attach PDF Files

There are a few things specific to PDF files that you need to consider. PDF files with more than one page are attached one
page at a time. Also, hypertext links from PDF files are converted to straight text and digital signatures are ignored.

You can drag PDF files from Finder directly into the drawing canvas. If the PDF file contains multiple pages, only the first
page is inserted. When you release the mouse button, the file is inserted at the current mouse location. If you need more
control over the pages or location, use PDFATTACH.

## Attaching an Underlay Multiple Times

You can reattach an underlay multiple times, treating it as a block. Each underlay has its own clip boundary and settings
for contrast, fade, and monochrome. However, you cannot bind an underlay to a drawing and you cannot edit or modify the underlay’s
content.

## Layers in Underlay Files

If the underlay file contains layers, you can control how the layers display after attaching the file. If the file does not
contain layer information, the Underlay Layers dialog box does not display any layer information.

## Underlay Files in Xrefs

DWG file references (xrefs), in a drawing can include an underlay. In this situation, objects in the underlay are visible
in the parent DWG file.

For example, drawing A includes a PDF underlay showing some mechanical details. You need the content of drawing A attached
to your current drawing, drawing B. If you attach drawing A as an external reference to drawing B, the PDF underlay that was
already attached to drawing A is also be present.

All of the property settings made to the underlay in the external reference, such as clipping boundaries, appear as they do
in the parent drawing.

#### Related Tasks

* [To Detach an Underlay](To-Detach-an-Underlay.md)

#### Related Concepts

* [About Underlays](About-Underlays.md)

#### Related Information

* [To Attach a PDF Underlay](To-Attach-a-PDF-Underlay.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*