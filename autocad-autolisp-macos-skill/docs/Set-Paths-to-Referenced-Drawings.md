# Set Paths to Referenced Drawings

You can view and edit the file name and path used when locating a particular drawing reference (xref). Use this option if
the referenced file has been moved to a different folder or renamed since it was first attached.

You can choose from three types of folder path information to save with an attached reference: a full path, a relative path,
and no path.

## Specify a Full (Absolute) Path

A full path is a fully specified hierarchy of folders that locates the file reference. For example, a fully specified path
to a different volume will look something like this:

smb://*hostname*/*directorypath*/*resource*

Instead of smb:, you could use afp: , ftp: , or other protocol.

This is the most specific but least flexible option.

## Specify a Relative Path

Relative paths are partially specified folder paths that assume the current folder of the host drawing. This is the most flexible
option, and enables you to move a set of drawings from one folder to a different one that contains the same folder structure.

If the file that is being referenced is located on a network server, the relative path option is not available.

The conventions for specifying a relative folder path are as follows:

/
:   Look in the root folder of the host drawing's drive

*path*
:   From the folder of the host drawing, follow the specified path

/*path*
:   From the root folder, follow the specified path

. /*path*
:   From the folder of the host drawing, follow the specified path

../*path*
:   From the folder of the host drawing, move up one folder level and follow the specified path

../../*path*
:   From the folder of the host drawing, move up two folder levels and follow the specified path

*Notes:*

* If a drawing that contains referenced files is saved to a different path, you are prompted to update the relative paths.
* If a drawing that contains referenced files is moved to a different path, or to a different network server, you must edit
  any relative paths to accommodate the host drawing's new location or you must relocate the referenced files.

## Specify No Path

When no path information is saved with the attached external reference, the following search is initiated in the order shown:

* Current folder of the host drawing
* Project Search paths defined in the Project Files Search Path on the Application tab in the Application Preferences dialog
  box
* Search paths defined in the Support File Search Paths on the Application tab in the Application Preferences dialog box

Specifying the No Path option is useful when moving a set of drawings to a different folder hierarchy or to an unknown folder
hierarchy.

## Know when a Referenced Drawing has been Relocated

If the drawing you are working on contains an xref that has been moved to a different folder, a message is displayed at the
site of the xref when you load the drawing. The message indicates that the xref cannot be loaded using the old path. When
you specify the new path, the xref is reloaded into your drawing.

#### Related References

* [Reference Manager Palette](Reference-Manager-Palette.md)

#### Related Concepts

* [About Changing the Temporary Xref File Path](About-Changing-the-Temporary-Xref-File-Path.md)

#### Related Information

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [To Work With Xref Paths](To-Work-With-Xref-Paths.md)
* [To Work With Attaching and Detaching Referenced Drawings](To-Work-With-Attaching-and-Detaching-Referenced-Drawings.md)
* [About Updating Referenced Drawing Attachments](About-Updating-Referenced-Drawing-Attachments.md)
* [To Update an Attached Xref](To-Update-an-Attached-Xref.md)
* [To Resolve External References (Xrefs) while Sharing Drawings Between Mac and Windows](To-Resolve-External-References-Xrefswhile-Sharing-Drawings-Between-Mac-and-Windows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*