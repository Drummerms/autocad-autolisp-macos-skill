# PROJECTNAME (System Variable)

Assigns a project name to the current drawing.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | "" |

Used when an xref, image, or PDF underlay file is not found in its original path. The project name points to a section in
the registry that can contain one or more search paths for each project name defined. Project names and their search directories
are created from the Application tab of the Application Preferences dialog box.

Project names make it easier for users to manage xrefs, images, and underlays when drawings are exchanged between customers,
or if users have different drive mappings to the same location on a server.

If the xref, image, or underlay file is not found at the original path, the project paths associated with the project name
are searched. If the xref, image, or underlay file is not found there, the folders defined under Support File Search Path
in the Application Preferences dialog box are searched.

#### Related Concepts

* [Set Paths to Referenced Drawings](Set-Paths-to-Referenced-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*