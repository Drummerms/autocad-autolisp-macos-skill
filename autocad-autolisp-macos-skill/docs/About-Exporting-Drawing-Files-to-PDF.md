# About Exporting Drawing Files to PDF

The Adobe® Portable Document Format (PDF) is a compressed electronic document format that can be viewed on multiple platforms.
PDF files are widely used to transmit drawing data over the Internet.

## Commands that Create PDF files

There are many commands and methods you can use to produce PDF files. Use these guidelines to select the most appropriate
method.

| Operation | Recommended Command/Workflow |
| Export model space or a single layout to a PDF file | The PLOT command |
| Export selected layouts of a drawing to PDF | The PUBLISH command |
| Export model space and selected layouts to PDF | The PUBLISH command |
| Export multiple drawing files to PDF | The PUBLISH command |
| Export a sheet set to a PDF file | The Publish to PDF option in the Project Manager |

## PDF Presets

PDF presets are named groups of settings that control the PDF creation process and are saved as plotter configuration files
(\*.pc3). Presets let you balance the file size with quality and functionality, depending on how you want to use the PDF files.
The predefined PDF presets listed address most typical usage scenarios. However, if you have specific requirements that a
predefined preset cannot meet, customize an existing preset and save it as a \*.pc3 file with a different name.

| PC3 File / PDF Preset | Details |
| AutoCAD PDF (General Documentation).pc3 | General purpose driver suitable for most uses. |
| AutoCAD PDF (High Quality Print).pc3 | Produces a PDF file optimized for printing on paper. |
| AutoCAD PDF (Smallest File).pc3 | Produces a PDF with the smallest possible file size. |
| AutoCAD PDF (Web and Mobile).pc3 | Produces a PDF file that supports hyperlinks mobile devices and Web browsers. |
| DWG to PDF.pc3 | General purpose driver. |

## Considerations for TrueType Fonts

If a PDF viewer does not have access to a font that you used in a drawing, it displays the affected text using a substitute
font. Often, the substitute font doesn't match up to the original font. Consequently, the text in the drawing can appear different
than the text in the PDF file.

You can prevent font substitution by capturing the font in the drawing and embedding it in the PDF file. Alternatively, you
can convert all text to geometry. Converting text to geometry ensures that the text in the PDF file is identical to that of
the drawing. However, the PDF file size increases and text pixelation can occur when you view the PDF file at a high magnification.
You can reduce pixelation by increasing raster image quality.

NOTE: Fonts that cannot be distributed because of legal restrictions are not embedded in the PDF file, even though you enable the
capture fonts option.

## Consideration for SHX Fonts

Unlike TrueType fonts, SHX fonts are geometric shapes. When you export a drawing to a PDF file, the SHX text is exported as
geometry. This text cannot be selected or highlighted in a PDF viewer. To work around this limitation, the program exports
SHX text as hidden PDF comments.

## Limitations

* *Resolution*- The highest possible resolution of PDF data is 4800 dpi.
* *3D Visual Styles* - All viewports, model space or layout that have a 3D Visual style applied to them are converted to raster images when plotted
  to PDF. As a result, drawing information such as the layers within the viewport is lost. Furthermore, text within the viewport
  is not searchable, and hyperlinks are removed.
* *Printing PDF files* - If you use the Adobe Acrobat Reader default printer settings to print a PDF drawing, transparent objects and wipeouts might
  not print correctly. If the PDF file contains transparent objects, you may need to adjust some settings in Adobe Acrobat.
  Set Transparency Flattening to "Print as Image" or reduce the Raster/Vector Balance in Adobe Acrobat. Refer to the Adobe documentation
  for more information.
* *Loss of precision* - PDF stores data in single precision numbers, while DWG stores data as double-precision numbers. This loss of precision
  can become apparent as:
  + Round-off errors on computed locations of objects, such as the locations of tangent points, and arc radiuses and their endpoints.
  + Round-off errors on large coordinates such as those found in geolocated drawings.
  + Deformities and round-off errors in tiny objects when a drawing contains very large objects as well as tiny objects.

#### Related Tasks

* [To Plot a Drawing](To-Plot-a-Drawing.md)

#### Related Information

* [To Export a Drawing to a PDF File](To-Export-a-Drawing-to-a-PDF-File.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*