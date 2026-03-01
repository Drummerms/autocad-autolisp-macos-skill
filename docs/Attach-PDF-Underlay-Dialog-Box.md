# Attach PDF Underlay Dialog Box

Names, locates, and defines the insertion point, scale, and rotation of attached PDF underlays.

PDFATTACH (Command)

*Menu*:
Insert ![](../images/ac.menuaro.gif) PDF Underlay

![](../images/GUID-D3903454-221A-4635-A75D-85DEEB15D4B9-low.png)

## List of Options

The following options are displayed.

Name

Identifies the PDF file you have selected to attach.

Browse

Opens the Select Reference File dialog (a
[standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)).

Details

Saved Path
:   Displays the path that is saved with the drawing when the PDF file is attached. The path is dependent upon the Path Type setting.

Found In
:   Displays the path to the PDF file.

Select page(s)

Displays all of the pages that are found in the PDF file. If the PDF file only contains a single page, that page is listed.
You can select multiple pages by holding Shift or Cmd and selecting the pages to attach.

Show\Hide Attachment Options

Expands or collapses the Attachment Options section to allow you to specify the insertion point, rotation and scale for the
PDF underlay being attached.

Insertion Point

Specifies the insertion point for the selected PDF file.

Specify On-Screen
:   Directs input at the Command prompt or the pointing device.

X
:   Sets the
    *X* coordinate value.

Y
:   Sets the
    *Y* coordinate value.

Z
:   Sets the
    *Z* coordinate value.

Rotation

Specifies the rotation angle of the selected PDF underlay.

Specify on-screen
:   If Specify On-Screen is selected, you may wait until you exit the dialog box to rotate the object with your pointing device
    or enter a rotation angle value at the Command prompt.

Angle
:   If Specify On-Screen is cleared, enter the rotation angle value in the dialog box. The default rotation angle is 0.

Path Type

Select the full (absolute) path, the relative path to the PDF file, or No Path, and the name of the PDF file. For the No Path
option, the PDF file must be located in the same folder as the current drawing file.

Scale

Specifies the scale factor of the selected PDF underlay.

If
[INSUNITS](INSUNITS-System-Variable.md) is set to “unitless” or if the underlay does not contain resolution information, the scale factor becomes the underlay width
in AutoCAD units. If INSUNITS has a value such as millimeters, centimeters, inches, or feet, and the underlay has resolution
information, the scale factor is applied after the true width of the underlay in AutoCAD units is determined.

Specify On-screen
:   Inputs information at the Command prompt or with the pointing device. If Specify On-Screen is cleared, enter a value for the
    scale factor.

Scale Factor Field
:   Enter a value for the scale factor.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*