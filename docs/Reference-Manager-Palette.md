# Reference Manager Palette

Manage external references attached to the current drawing.

EXTERNALREFERENCES (Command)

*Menu*:
Window ![](../images/ac.menuaro.gif) Reference Manager.

![](../images/GUID-7EDD8C06-4D79-4E01-8062-4CD5C7321FB1-low.png)

## Summary

The Reference Manager palette organizes, displays, and manages
*referenced files*. The referenced files that can be managed from the Reference Manager palette are:

* External drawings (xrefs)
* Raster images
* Excel Files (\*.xls, \*.xlsx)
* Underlays (PDF files)

The Reference Manager palette contains a toolbar along the top. You can right-click over the files list to display a shortcut
menu that allows you to attach or manage an attached external reference. Click the Show Details button on the toolbar to view
details and thumbnail preview for the selected external reference.

## Toolbar

Attach Reference
![](../images/GUID-8F1CD821-F5B3-4571-8E03-B82409C83BBC-low.png)

Displays the Select Reference File dialog box. Select the file format you want to attach and then the file you want to attach
to the drawing.

You can choose from the following reference file types:

* *Drawing (DWG) files.* Starts the
  [XATTACH](XATTACH-Command.md) command.
* *Raster image files.* Starts the
  [IMAGEATTACH](IMAGEATTACH-Command-2.md) command.
* *Excel Files.*Starts the DATALINK
  [DATALINK](DATALINK-Command.md)command.
* *PDF files.* Starts the
  [PDFATTACH](PDFATTACH-Command.md) command.

Edit Reference
![](../images/GUID-B6DA942C-3B95-4AE9-BF6C-E91538EAFB57-low.png)

Opens the selected file reference for edit in the current drawing window. ([REFEDIT](REFEDIT-Command.md) command)

Toggle References State
![](../images/GUID-4825BEB0-B178-493E-B68A-3481E148CA46-low.png)

Unloads the selected file reference or reloads the file reference if it is currently unloaded.

Detach Referenced File
![](../images/GUID-5BDC59BB-E944-4A80-AEE9-E543BC2BED38-low.png)

Detaches the selected file reference from the drawing.

Refresh Content
![](../images/GUID-F5EBC0D2-FED2-46AD-BB69-2B1E423CE758-low.png)

Synchronizes the status of the selected file reference with the data in memory.

Select New Path
![](../images/GUID-D62FD1F4-CCEC-43F7-97DE-CA1FA21B12D5-low.png)

Allows you to browse to a new location for a not found reference file (fix one), and then provides you with an option to apply
the same new location for other missing reference files (fix all).

Server Path Mapping
![](../images/GUID-1AE74AA4-F38E-4F75-AA7C-4743CBD95BE7-low.png)

Displays the Server Path Mapping dialog where you can map server address between Mac and PC.

Show Details
![](../images/GUID-6364B815-1C7B-485B-A6D5-1D3B961D3025-low.png)

Displays the
[Details and Preview panel](Details-and-Preview-Panel.md) which displays a thumbnail preview and details for the selected file reference.

NOTE:The Pending Relative Path property in the Details pane indicates the reference file is pending a save.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*