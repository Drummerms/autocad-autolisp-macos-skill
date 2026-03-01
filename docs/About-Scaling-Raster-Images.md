# About Scaling Raster Images

You can control the size of a raster image in a drawing to match the scale of the drawing.

You can specify the raster image scale factor when you attach the image so that the scale of the geometry in the image matches
the scale of the geometry in the drawing. The default image scale factor is 1, and the default unit for all images is “Unitless.”
The image file can contain resolution information defining the dots per inch (DPI), relating to how the image was scanned.

If an image has resolution information, the program combines this information with the scale factor and the unit of measurement
of the drawing to scale the image in your drawing. For example, if your raster image is a scanned blueprint on which the scale
is 1 inch equals 50 feet, or 1:600, and your drawing is set up so that 1 unit represents 1 inch, then in the Image dialog
box under Scale, select Specify On-Screen. To scale the image, you clear Specify On-Screen, and then enter *600* in Scale. The image is then attached at a scale that brings the geometry in the image into alignment with the geometry in
the drawing.

If no resolution information is defined with the attached image file, the width of the raster image is set to one unit. Thus,
when the image file is attached, the image width in units is equal to the raster image scale factor.

#### Related Information

* [To Attach and Scale an Image](To-Attach-and-Scale-an-Image.md)
* [About Raster Images in Drawings](About-Raster-Images-in-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*