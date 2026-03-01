# About Working With Drawings in Earlier Versions

When you work with drawings created in earlier versions, you should be aware of the following visual fidelity issues.

## Visual Fidelity for Annotative Objects in Previous Versions

You can specify that "annotative" objects maintain visual fidelity when they are viewed in earlier versions of the product,
with the SAVEFIDELITY system variable.

If you work primarily in model space, we recommend that you turn off visual fidelity (set SAVEFIDELITY to 0). However, if
you need to exchange drawings with other users, and layout fidelity is most important, then turn on visual fidelity (set SAVEFIDELITY
to 1).

Annotative objects may have multiple scale representation. When visual fidelity is on, annotative objects are decomposed
and scale representations are saved (in an anonymous block) to separate layers. These layers are named based on their original
layer and appended with a number. If you explode the block in an earlier version, and then open the drawing in the current
version, each scale representation becomes a separate annotative object, each with one annotation scale. It is recommended
that you do not edit or create objects on these layers when working on such a drawing with an earlier version.

When visual fidelity for annotative objects is not selected, a single model space representation is displayed on the Model
tab. Depending on the setting of the ANNOALLVISIBLE system variable, more annotation objects may be displayed on the Model
tab, and more objects may be displayed in paper space viewports at different sizes when viewed in an earlier version.

## Annotative Object Properties in Previous Versions

In an AutoCAD 2008 drawing, when an annotative block does not have its paper orientation set to match the layout, and the
block contains multiline attributes that are based on a text style that is not set to match the orientation of the layout,
the attributes may shift positions if you open this drawing in an earlier version.

NOTE:The above and all subsequent references to AutoCAD 2008 extend to all AutoCAD-based products.

## Layer Property Overrides in Previous Versions

When you open an AutoCAD 2008 drawing containing layer property overrides, overrides are not visible. The property override
settings are retained when the drawing is saved in a previous version, and are visible again when the drawing is opened in
AutoCAD 2008.

If a viewport containing layer property overrides is deleted when the drawing is opened in a previous version, the override
settings are not retained and are not available when the drawing is opened in the current version.

When the VISRETAIN system variable is set to 0 when the drawing is opened in a previous version, xref layers containing viewport
property overrides are not retained.

If you open an AutoCAD 2008 drawing in a previous version, property overrides may display in a thumbnail image. When the drawing
is saved with a layout tab, and then opened in the previous version, those property overrides do not display.

## DGN Underlays in Previous Versions

DGN underlays do not display in versions prior to AutoCAD 2008.

## Dimension Enhancements in Previous Versions

AutoCAD 2008 dimension enhancements are lost when they are edited in earlier versions. If you don’t change these dimensions,
they are restored when you open the drawing in AutoCAD 2008.

The following dimension enhancements do not lose visual fidelity in previous versions if they are not edited:

* Dimension breaks
* Jogged linear dimensions
* Inspection dimensions
* Angular dimensions that are dimensioned using the quadrant option
* Arc extension lines for radial and diameter dimensions

## Multileader Objects in Previous Versions

Multileaders display as proxy objects in versions prior to AutoCAD 2008 and related products. The PROXYSHOW system variable
controls the display of proxy objects in a drawing.

## MTEXT Paragraph and Paragraph Line Spacing in Previous Versions

Some of the new paragraph spacing and paragraph line spacing options are not supported when an AutoCAD 2008 mtext object
is opened in earlier versions.

The following mtext formatting features have *no* visual fidelity in previous versions:

* Paragraphs with justified alignment
* Paragraphs with distributed alignment
* Fields that wrap across columns
* Fields that wrap across lines that have new paragraph alignments
* Paragraphs with non-default alignments in mtext without left object-level justification

The following mtext formatting features have *some* visual fidelity in previous versions (when it’s possible to add white spaces or replace text with white spaces):

* Paragraphs with non-default alignments (other than justified or distributed) in mtext that has left object-level justification
* Paragraphs with tabs using new tab alignments (center, right, or decimal alignment applied)
* Paragraphs with new line spacing that can be "approximated" with "tall" spaces

Mtext with new formatting that is edited and saved in previous versions loses the new formatting when re-opened in AutoCAD
2008.

## Tables in Previous Versions

Editing AutoCAD 2008 tables in previous versions removes AutoCAD 2008 table formatting. Also, table cells with long block
and text strings may extend outside of cell borders when opened in previous versions.

## Data Extraction Tables in Previous Versions

For tables that were created with the Data Extraction wizard in AutoCAD 2008, you can’t edit or update the extracted data
in previous versions.

## Materials in Previous Versions

AutoCAD 2008 introduces new procedural maps for materials and luminance. Drawings created earlier than AutoCAD 2007 that
contain materials need to be converted. AutoCAD 2008 provides a system variable, 3DCONVERSIONMODE, that is set to automatically
convert old materials to the AutoCAD 2008 format. However, there are some fidelity issues when saving back to previous versions
of AutoCAD.

* Procedural maps Checker, Noise, Speckle, Tiles, and Waves are not available in AutoCAD 2007 (and previous versions.) They
  do not appear when an AutoCAd 2008 drawing is opened in AutoCAD 2007. Marble and Wood are available but the material mayshow
  some variation.
* The behavior of the Opacity map channel under the Realistic material type has been corrected in AutoCAD 2008. In AutoCAD 2008,
  the Opacity map channel behaves like a transparency map, where white is transparent and black is opaque (this was how it behaved
  prior to AutoCAD 2007). In AutoCAD 2007, white represented opaque areas and black represented transparent areas.
* The spherical map rotation is different in AutoCAD 2008. When you open a drawing prior to AutoCAD 2008 AutoCAD 2008, the seam
  for the map is towards the +Y axis. In AutoCAD 2008, it is towards the +X axis.

## Lighting in Previous Versions

AutoCAD 2008 provides two options for lighting: standard (generic) lighting and photometric lighting. Previous versions offered
only standard (generic) lighting. There is no explicit conversion required for lights from AutoCAD 2007 to AutoCAD 2008. Drawings
from AutoCAD 2007 open by default in AutoCAD 2008 in the standard (generic) lighting workflow. The additional photometric
properties available in AutoCAD 2008 are available as soon as the photometric lighting workflow is enabled in the drawing.

There is a conversion process required for drawings with lighting prior to AutoCAD 2007. You can use a system variable, 3DVCONVERSTIONMODE,
to automatically convert drawings with lighting from previous versions to the AutoCAD 2007 and AutoCAD 2008 lighting format.
3DCONVERSIONMODE has three settings. If set to 0, no conversion takes place. If set to 1, the default value, the conversion
takes place automatically. If set to 2, then you are prompted when lights need to be converted and will have the option to
convert or not to convert.

Other lighting fidelity issues include

* *Lights in blocks.* Lights in blocks created in AutoCAD 2008 do not always display in AutoCAD 2007.
* *Texture illumination.* In versions prior to AutoCAD 2008, you can’t add lighting to textures. In AutoCAD 2008, you can.
* *Ground Shadows.* The intensity of ground shadows in AutoCAD 2008 depends on the brightness of the light and angle of incidence.

## Multiple-Language Support in Previous Versions

Drawing properties in AutoCAD 2008 are saved with Unicode characters. For instance, if you save the latest format drawing
containing multiple language drawing properties to a 2004-format drawing, the drawing properties are converted to the native
characters of the current Windows language. If text cannot be converted to the native characters, it is saved to CIF codes
(\U+nnnn) or MIF codes (\M+nxxxx).

When saving the latest format drawing to a 2004-format drawing, any new symbol or dictionary names (for example, layout name,
text style name, dimension style name) created in AutoCAD 2008 are saved in the language that was used when the symbol names
were created.

Text styles for Asian languages that use SHX and Big Font can support characters only from the same code page. For example,
text styles that use a Japanese Big Font cannot support German or Korean characters. (English characters, which are part of
every code page, are supported.) Multiple-language support for non-Asian languages is supported for text styles that use SHX
fonts with Big Fonts disabled. (The SHX font must define the required characters.)

Multiple-language support does not exist in some earlier releases of AutoCAD. For example, when you save a file to AutoCAD
2000 format, the contents of multiple-language multiline text may be corrupted. This problem is more likely to happen when
you open and save a drawing on an operating system with a system language setting that differs from the system in which the
drawing was last saved.

NOTE:Drawings that include external references (xrefs) to drawing files saved in earlier releases also have the limitations described
above.

#### Related Information

* [To Save a Drawing to a Previous Release Format](To-Save-a-Drawing-to-a-Previous-Release-Format.md)
* [To Save Drawings With Visual Fidelity for Annotative Objects](To-Save-Drawings-With-Visual-Fidelity-for-Annotative-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*