# About Exporting PostScript Files

You can convert a drawing file to a PostScript file, a format that is used by many desktop publishing applications.

The PostScript file format type is used by many desktop publishing applications. Its high-resolution print capabilities make
it preferable to raster formats, such as GIF, PCX, and TIFF. By converting the drawing to a PostScript format, you can also
use PostScript fonts.

## Export in PostScript Format

When you export a file in PostScript format as an EPS file, some objects are handled specially.

* *Thickened text, text control code* *s*. If text has a thickness greater than 0 or contains control codes (such as %%O or %%D), it is not plotted as PostScript text,
  although the text is accurately plotted. International and special symbols (such as %%213) are output as PostScript text.
* *ISO 8859 Latin/1 character set*. When text uses character codes in the 127 to 255 range, the text is interpreted according to the ISO 8859 Latin/1 character
  set. If such a character appears in text that is mapped to PostScript, a version of the font is generated with an encoding
  vector remapped to represent the ISO character set. The resulting text is output in PostScript in a form compatible with the
  font.
* *Circles, arcs, ellipses, elliptical arcs*. Except when they have thickness, arcs and circles are translated into the equivalent PostScript path objects.
* *Filled solids*. A solid fill is plotted as a PostScript filled path.
* *2D polylines*. A 2D (planar) polyline with uniform width is output as a PostScript stroked path. The PostScript end cap and miter limit
  variables are set to approximate the segment joining.

#### Related Information

* [To Export 3D Solids to an STL File](To-Export-3D-Solids-to-an-STL-File.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*