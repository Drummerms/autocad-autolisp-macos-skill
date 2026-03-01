# About Improving the Display Speed of Raster Images

To increase the display speed of images, you can change image display quality, hide images not currently needed, use image
tiling, or suppress image selection highlighting.

To increase the display speed of images, you can change image display quality from the default high quality to draft quality.
Draft-quality images appear more grainy (depending on the image file type), but they are displayed more quickly than high-quality
images. Use the IMAGEQUALITY command to control image quality.

You can improve the image quality when using True Color (24 or 32 bits per pixel) for raster images by selecting or clearing
certain options on the Display tab in the Options dialog box. When images are displayed at optimum quality, regeneration time
increases significantly. To improve performance, decrease the number of colors for the system display setting while working
in a drawing.

You can increase redrawing speed by hiding images you do not need in the current drawing session. Hidden images are not displayed
or plotted; only the drawing boundary is displayed. You can choose to hide an image regardless of the user coordinate system
(UCS) in the current viewport.

## Use Tiled Images

Tiled images are small portions (a series of tiles) of large images that load much faster than non-tiled images. If you edit
or change any properties of an image, only the modified portion is regenerated, thus improving the regeneration time. TIFF
(Tagged Image File Format) is the only tiled format that the program supports. The TIFF reader supports all image types:

* Bitonal (1 bit per pixel)
* Gray scale and indexed color (8 bits per pixel)
* True Color (24 or 32 bits per pixel)

You can save tiled TIFF images with most image scanning tools. The image tiles should be no smaller than 64 x 64 pixels and
no larger than 512 x 512 pixels. Additional file readers that support other tiled formats, such as CALS Type II, are available
from third-party developers.

## Suppress Highlighting When Selecting Images

You can turn on or off the highlighting that identifies the selection of a raster image or the image frame by selecting Highlight
Raster Image Frame Only on the Display tab in the Options dialog box. You can also set the IMAGEHLT system variable directly.
By default, IMAGEHLT is set to 0, to highlight only the raster image frame. Turning off highlighting of the entire image improves
performance.

#### Related Information

* [To Change the Image Display Quality](To-Change-the-Image-Display-Quality.md)
* [About Raster Images in Drawings](About-Raster-Images-in-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*