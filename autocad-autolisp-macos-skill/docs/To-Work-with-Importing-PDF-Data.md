# To Work with Importing PDF Data

You can import the geometry, fills, raster images, and TrueType text from a PDF file or PDF underlay into the current drawing.

## Import the Data from a PDF File

1. Click Import.
   ![](../images/GUID-272A489E-1040-49E0-B327-B5E841C87610-low.png)
2. Select PDF Files (\*.pdf).
3. Find and select the PDF file that you want to import, or enter the name of the PDF file in the File Name box. Click Open.

   The Import PDF dialog box is displayed.
4. If the PDF has multiple pages, choose the page to import by clicking a thumbnail image or by entering a page number.
5. Choose any of the options and click OK.
6. Specify the insertion point if prompted.

## Import a Specified Area from a PDF Underlay

1. Select the PDF underlay.
2. Click
   PDF Underlay visor![](../images/ac.menuaro.gif) ![](../images/GUID-0D3C6EAD-AA46-42B9-9C96-1D1866C3C6DB-low.png)
3. At the prompt, click two diagonal points that define a rectangular
   *crossing area*, or use the Polygonal option to specify a polygonal crossing area.

   A crossing area is similar to a crossing selection. The Settings option displays a dialog box in which you can choose what
   types of objects to import, how layers should be accommodated, whether the imported objects should be imported as a block,
   and several other options.
4. Choose whether you want to keep, detach, or unload the attached PDF.

The specified area of the attached PDF is imported into the drawing as AutoCAD objects.

## Convert SHX Geometry into Multiline Text Objects

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Recognition Settings.
   ![](../images/GUID-3F1648D6-ACDB-4022-9A3D-B8C25954BD66-low.png)
2. In the PDF Text Recognition Settings dialog box, under SHX Fonts to Compare, select whether you want to use the first matching
   font or the best matching font.
3. Drag fonts to order the list so the most likely font is at the top.
4. Click one or more fonts that appear to be the most similar to the imported SHX geometry.
5. Click
   ![](../images/GUID-9174311E-7DC8-49C8-B39F-991EC3DAD0E2-low.png) to add SHX fonts to the list.
6. Set the conversion settings percentage. The geometry is converted to text when it meets the comparison threshold.
7. Choose any other options as desired and then click OK.
8. Select the geometric objects that represented the SHX text in the PDF and press Enter. Be careful to avoid selecting any objects
   that are not part of the characters.

A dialog box reports the percent of the objects that could not be converted to multiline text. The characters that were converted
are highlighted. If none of the fonts pass the threshold try one of the following:

* Select fewer objects for processing. This can help you identify problems and extraneous geometry.
* Select a different font that might be a better match.
* Lower the success threshold percent in the PDF Text Recognition Settings dialog box.

Once you're satisfied with your settings, the process for converting SHX geometry into multiline text becomes much simpler:

* Click
  Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Recognize SHX Text.
  ![](../images/GUID-CFD896EE-30B7-4BB7-962F-0F83C1338472-low.png)

NOTE:To combine separate multiline text objects, use the Combine Text (TXT2MTXT) command.

Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Combine Text.
![](../images/GUID-547349A1-E4A8-4B4D-A78C-3E1AA7615E67-low.png)

#### Related References

* [PDFIMPORT (Command)](PDFIMPORT-Command-2.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)
* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*