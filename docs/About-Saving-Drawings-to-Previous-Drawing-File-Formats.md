# About Saving Drawings to Previous Drawing File Formats

You can save a drawing in a format compatible with previous versions of the product.

You can save a drawing created with the current release of the program in a format compatible with previous versions. This
process creates a drawing with information specific to the current release stripped out or converted to another object type.

If you use the current release to open a drawing created with a previous release, and you do not add any information specific
to the current release, you can then save the drawing in the format of the previous release without loss of data.

NOTE: To use files with AutoCAD Release 12 or AutoCAD LT Release 2, save the drawing using the AutoCAD R12/LT2 DXF option.

If you need to keep a drawing created in a previous release in its original format, either mark the file as read-only, or
open it in the current release and use the File Type options in the Save As dialog box to save it in its original format.

Because saving a drawing in an earlier release format may cause some data loss, be sure to assign a different name to avoid
overwriting the current drawing. If you overwrite the current drawing, you can restore the overwritten version from the backup
file (*filename.bak*) that is created during the saving process.

## Save Drawings with Traces

Trace provides a safe space to add changes to a drawing in the web and mobile apps without altering the existing drawing.
The analogy is of a virtual collaborative tracing paper that is laid over the drawing that allows collaborators to add feedback
on the drawing. Create traces in a drawing, then share the drawing with collaborators so they can view the trace and its contents.

Traces are only supported in drawing file formats 2010 or later and they are not supported in the DXF format.

## Maintain Associativity in Dimensions

Associative dimensions created in AutoCAD 2002 or later generally maintain their associativity when saved to a previous release
and then reopened in the current release. However, if you modify dimensioned objects using a previous release to the extent
that new objects are formed, the dimension associations change when the drawing is loaded into the current release. For example,
if a line that was dimensioned is trimmed so that an interior portion of the line is removed, two line objects result and
the associated dimension applies to only one of the line objects.

Dimension associativity is not maintained when a drawing is saved as an AutoCAD R12/LT 2 DXF file and then reopened in the
current release.

## Save Drawings with Large Objects

Drawings saved to a legacy drawing file format (AutoCAD 2007 or AutoCAD LT 2007 or earlier) do not support objects greater
than 256MB.

## Limitations of Saving to Earlier Versions

Saving a drawing containing model documentation drawing views in Release 2012 format has the following limitation:

* Although drawing views display and list correctly, none of the editing commands (with the exception of the MOVE command) work
  on the drawing views.

  NOTE:Drawing views created by a newer version of AutoCAD cannot be edited by an older version of AutoCAD. For example, drawing
  views saved by AutoCAD 2014 cannot be edited in AutoCAD 2013, even though both versions of AutoCAD use the AutoCAD 2013 file
  format.

Saving a drawing in Release 2000/LT 2000 format is subject to the following limitations:

* File size can increase.
* Encryption and digital signatures are not preserved.

Saving a drawing in Release 14/LT 98/LT 97 format is subject to the following limitations:

* Hyperlinks are converted to Release 14/LT 98/LT 97 attached URLs.
* Database links and freestanding labels are converted to Release 14/LT 98/LT 97 links and displayable attributes.
* Database attached labels are converted to multiline text and leader objects, and their link information is not available.
  Attached labels are restored if you open the drawing in AutoCAD 2000 or later.
* Dynamic block geometry can be redefined independent of the block’s dynamic elements, and the geometry in the block reference
  is not updated when the drawing is opened.
* Dimensions created using the DIMARC and DIMJOGGED commands may not retain their original color in Release 14/LT 98/LT 97.

Saving a drawing in Release 12/LT 2 DXF format is subject to the following limitations:

* Lightweight polylines and hatch patterns are converted to Release 12 polylines and hatch patterns.
* All solids, bodies, regions, ellipses, leaders, multilines, rays, tolerances, and xlines are converted to lines, arcs, and
  circles as appropriate.
* Groups, complex linetypes, OLE objects, and preview images are not displayed.
* Many objects are lost if you save a drawing as Release 12 and open it in Release 2000/LT 2000 or later.
* Multiple layouts and layout names are lost. Only the Model tab and the current layout tab are saved.
* Spaces in the names of layers and other objects are converted to underscores, and their maximum length is 32 characters.
* DWF or DWFx underlay files attached to drawings cannot be saved to Release 12/LT 2 DXF format.
* The status of external references as unloaded is lost.

  NOTE:This does not apply to AutoCAD LT.

#### Related Information

* [To Save a Drawing to a Previous Release Format](To-Save-a-Drawing-to-a-Previous-Release-Format.md)
* [About Working With Drawings in Earlier Versions](About-Working-With-Drawings-in-Earlier-Versions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*