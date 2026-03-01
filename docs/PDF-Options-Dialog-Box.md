# PDF Options Dialog Box

PLOT (Command)

*Toolbar*:
![](../images/GUID-E98FB764-041C-4F90-8F08-3FD0683C3611-low.png) :
Select a PDF output ![](../images/ac.menuaro.gif) ![](../images/GUID-8A01F33F-D790-424E-9774-A7BEC8D003AA-low.png)

![](../images/GUID-AB2150D1-0CA9-4C9C-B548-7DA03D5D4C0F-low.png)

## Quality

Specifies the resolution of the PDF file.

Vector quality
:   Controls the resolution of vector graphics and gradients. If the PDF file is intended for printing from a viewer, select
    a resolution to match the output of the plotter or printer. If the PDF file is intended for on-screen viewing, select a high
    resolutions (above 2400 dpi).

Raster image quality
:   Controls the resolution of raster images. If the PDF file is intended for printing from a viewer, select a resolution to
    match the output of the plotter or printer. If the PDF file is intended for on-screen viewing select a high resolutions (above
    2400 dpi). The raster image quality cannot exceed the vector image quality.

    TIP:When you generate PDF files from drawings that contain a lot of detail, such as a topographical map of a large region, use
    a higher resolution setting for greater detail. As you increase the resolution setting, the image quality increases, the speed
    of printing decreases, and the file size increases.

Merge control
:   Specifies whether overlapping lines overwrite (the top line hides the bottom line) or merge (the colors of the lines blend
    together).

## Data

Specifies the data you can optionally include in the PDF file.

Include layer information
:   Adds layer information to the PDF file so that you can turn layers on or off when viewing or printing PDF files.

Include hyperlinks
:   Converts hyperlinks to PDF hyperlinks. If you don't select this option, hyperlinks do not get transferred to the PDF file.

Create bookmarks
:   Displays links to named views in the bookmarks panel of the PDF viewer.

Keep TrueType Fonts Embed all referenced fonts
:   Embeds TrueType fonts in the PDF file so that they don't need to be available on the PDF viewer. If you do not select this
    option, the PDF viewer uses substitute fonts.

    NOTE: The following fonts are not embedded even if you select this option:

    * Fonts that cannot be distributed because of legal restrictions, the determination of which is encoded in the font definition.
    * Fonts that are not TrueType fonts.
    * Vertical Asian fonts.

Convert all text to geometry
:   Converts all text to geometry in the PDF file. Selecting this option ensures that the text in the PDF file will be identical
    to that of the drawing. However, the PDF file size increases and pixelation of text can occur when you view the PDF file at
    a high zoom level. You can reduce pixelation by increasing raster image quality.

    NOTE:

    * Even when you convert text to geometry, you can locate the text in the PDF viewer using Search.
    * Text in SHX fonts is always converted to geometry, even if you don't select this option. Additionally, the text is copied
      to the PDF file as a comment. You can locate the converted text in the PDF file by searching comments in the PDF viewer.

#### Related References

* [PUBLISH (Command)](PUBLISH-Command.md)
* [Batch Publish Dialog Box](Batch-Publish-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*