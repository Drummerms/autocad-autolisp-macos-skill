# Attach Image Dialog Box

Locates, inserts, names, and defines the parameters and details of attached images.

IMAGEATTACH (Command)

*Menu*:
Insert
![](../images/ac.menuaro.gif) Raster Image Reference.

![](../images/GUID-BC3A9F00-44E7-48E7-8CC2-AD46BEFC0A01-low.png)

## List of Options

The following options are displayed.

Name

Identifies the image you have selected to attach.

Browse

Opens the Select Reference File dialog (a
[standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)).

Preview

Displays the image that you have selected to attach.

Insertion Point

Specifies the insertion point for the selected image file. Specify On-Screen is the default. The default insertion point is
0,0,0.

Specify On-Screen
:   Directs input at the Command prompt or the pointing device. If Specify On-Screen is cleared, enter the insertion point in
    X, Y, and Z.

X
:   Sets the
    *X* coordinate value.

Y
:   Sets the
    *Y* coordinate value.

Z
:   Sets the
    *Z* coordinate value.

Scale

Specifies the scale factor of the selected image.

If
[INSUNITS](INSUNITS-System-Variable.md) is set to “unitless” or if the image does not contain resolution information, the scale factor becomes the image width in
AutoCAD units. If INSUNITS has a value such as millimeters, centimeters, inches, or feet, and the image has resolution information,
the scale factor is applied after the true width of the image in AutoCAD units is determined.

Specify On-Screen
:   Allows you to input at the Command prompt or the pointing device. If Specify On-Screen is cleared, enter a value for the scale
    factor. The default scale factor is 1.

Scale Factor Field
:   Enter a value for the scale factor. The default scale factor is 1.

Rotation

Specifies the rotation angle of the selected image.

Specify On-Screen
:   If Specify On-Screen is selected, you may wait until you exit the dialog box to rotate the object with your pointing device
    or enter a rotation angle value at the Command prompt.

Angle
:   If Specify On-Screen is cleared, enter the rotation angle value in the dialog box. The default rotation angle is 0.

Path Type

Select the full (absolute) path, the relative path to the image file, or No Path, the name of the image file (the image file
must be located in the same folder as the current drawing file).

Details

Displays details about the selected image file.

Resolution
:   Displays the number of horizontal and vertical pixels per the current unit measurement in
    AutoCAD 2026.

Unit
:   Displays the current
    AutoCAD 2026 unit.

Image Size in Pixels
:   Displays the width and height of the raster image measured in pixels.

Image Size in Units
:   Displays the width and height of the raster image measured in
    AutoCAD 2026 units.

Path
:   * *Found In.* Displays the path where the image file is located.
    * *Saved Path.* Displays the path that is saved with the drawing when the image file is attached. The path is dependent upon the Path Type
      setting.

#### Related References

* [IMAGEATTACH (Command)](IMAGEATTACH-Command-2.md)
* [Image Visor](Image-Visor.md)
* [-IMAGEATTACH (Command)](IMAGEATTACH-Command.md)

#### Related Concepts

* [About Scaling Raster Images](About-Scaling-Raster-Images.md)
* [About Viewing Raster Image Information](About-Viewing-Raster-Image-Information.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*