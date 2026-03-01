# -XREF (Command)

Attach and manage external referenced drawings (xrefs).

## List of Prompts

The following prompts are displayed.

Enter an Option

?—List Xrefs
:   Lists the DWG reference name, path, and type and the number of DWG references currently attached to your drawing.

Bind
:   Converts a specified DWG reference into a block, making it a permanent part of the drawing.

    The xref-dependent named objects, such as layer names, of the former xref are added to your drawing. In each xref-dependent
    named object, the vertical bar (|) is replaced with three new characters: a number (usually 0) between two dollar signs ($).
    The number is increased if the same name already exists in the current drawing.

Detach
:   Detaches one or more DWG references from your drawing, erasing all instances of a specified xref and marking the xref definition
    for deletion from the definition table. Only the xrefs attached or overlaid directly to the current drawing can be detached;
    nested xrefs cannot be detached.

Path
:   Displays and edits the path name associated with a particular DWG reference. This option is useful if you change the location
    of or rename the drawing file associated with the xref.

Unload
:   Unloads the selected DWG references.

    A marker is left in place of the xref so that it can be reloaded later.

Reload
:   Reloads one or more DWG references. This option reloads and displays the most recently saved version of that drawing.

    If the program encounters an error while reloading, it ends XREF and undoes the entire reloading sequence.

Overlay
:   Displays the Enter Name of File to Overlay dialog box (a standard file selection dialog box). If you reference a drawing that
    contains an overlaid xref, the overlaid xref does not appear in the current drawing.

    Unlike blocks and attached xrefs, overlaid xrefs cannot be nested. If another person is currently editing the xref file, the
    program overlays the most recently saved version.

    If the xref you specify is not already overlaid, a new xref is crated, using the name of the referenced file.

    If FILEDIA is set to 0, the following prompt is displayed:

    Enter Name of File to Overlay.

    You can enter a tilde (*~*) to display a dialog box.

Attach
:   Displays the Select Reference File dialog box. See [XATTACH](XATTACH-Command.md).

    If you reference a drawing that contains an attached xref, the attached xref appears in the current drawing. Like blocks,
    attached xrefs can be nested. If another person is currently editing the xref file, the most recently saved version is attached.

Specify Insertion Point

Specify a point or enter an option

Scale
:   Sets the scale factor. All *X* and *Y* dimensions of the xref are multiplied by the *X* and *Y* scale factors. The xref is rotated by the specified angle, using the insertion point as the center of rotation.

X, Y, and Z
:   Sets *X*, *Y*, and *Z* scale factors.

    * *X Scale Factor.* Defines *X*, *Y*, and *Z* scale factors for the xref.
    * *Corner.* Defines the *X* and *Y* scales at the same time, using the insertion point and another point as the corners of a box, and then defines the *Z* scale.

Rotate
:   Sets the angle of insertion for the xref.

PScale
:   Sets the scale factor for the *X*, *Y*, and *Z* axes to control the display of the xref as it is dragged into position.

PX, PY, and PZ
:   Sets the *X*, *Y*, and *Z* axes to control the display of the xref as it is dragged into position.

PRotate
:   Sets the rotation angle of the xref as it is dragged into position.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*