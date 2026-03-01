# Attach External Reference Dialog Box

Attaches drawings as an external reference (xref).

XATTACH (Command)

*Menu*:
Insert
![](../images/ac.menuaro.gif) DWG Reference.

![](../images/GUID-05004652-55F2-4815-9407-FE445E4FAEB2-low.png)

## Summary

If you attach a drawing that contains an attached xref, the attached xref appears in the current drawing. You can select
multiple DWG files to attach. Like blocks, attached xrefs can be nested. If another person is currently editing the xref,
the attached drawing is based on the most recently saved version.

## List of Options

The following options are displayed.

Name

Identifies the DWG you have selected to attach.

Browse

Displays the Select Reference File dialog box (a
[standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)), in which you can select a new external reference for the current drawing.

Reference Type

Specifies whether the external reference is an attachment or an overlay. Unlike an xref that is an attachment, an overlay
is ignored when the drawing to which it is attached is then attached as an xref to another drawing.

Preview

Displays the DWG you have selected to attach.

Insertion Point

Specify On-Screen
:   Allows you to input at the Command prompt or the pointing device.

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

Specify On-screen
:   Allows you to input at the Command prompt or the pointing device.

X
:   Sets the
    *X* scale factor.

Y
:   Sets the
    *Y* scale factor.

Z
:   Sets the
    *Z* scale factor.

Uniform Scale
:   Sets the
    *Y* and
    *X* scale factors as the same as
    *Z*.

Rotation

Specify on-screen
:   If Specify On-Screen is selected, you may wait until you exit the dialog box to rotate the object with your pointing device
    or at the Command prompt.

Angle
:   If Specify On-Screen is cleared, enter the rotation angle value in the dialog box.

Path Type

Select the full (absolute) path, the relative path to the external reference file, or No Path, the name of the external reference
(the file must be located in the same folder as the current drawing file).

Details

Displays block and path information about the external reference being attached.

Block
:   Displays information about the block in the drawing.

    * *Unit.* Displays the specified
      [INSUNITS](INSUNITS-System-Variable.md) value for the inserted block.
    * *Factor.* Displays the unit scale factor, which is calculated based on the
      [INSUNITS](INSUNITS-System-Variable.md) value of the block and the drawing units.

Path
:   Displays the external reference file paths.

    * *Found In.* Displays the path where the external reference file is located.
    * *Saved Path.* Displays the path that is saved with the drawing when the external reference is attached. The path is dependent upon the
      Path Type setting.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*