# About Sheet Views

A view on a sheet, called a
*sheet view*, consists of several coincident entities:

* an xref or geometry in model space
* a layout viewport on a sheet
* a named view in paper space

The Sheet Set Manager automates and enhances the process for adding views to a sheet.

* The sheet view can display model space from a different drawing file. In this case, that drawing is attached as an xref in
  your current drawing. The layers of that drawing file are displayed only in the sheet view that you create.

  NOTE:The xref is attached using a relative path. If you need to change the path to a fully specified (absolute) path, use the External
  References palette.
* A layout viewport that displays the model space view is created on your current sheet.
* A named view that encompasses the area of the layout viewport is created in paper space.

When you place a sheet view on a sheet, all the layers in the current drawing (including layer 0) are frozen in the new viewport
created by the view. The layers are shown as frozen in the VP Freeze column of the Layer Properties Manager.

If you need to remove a sheet view from a sheet, you can delete the layout viewport to remove the view. However, to remove
all unused items, you need to detach the xref and delete the named paper space view.

NOTE:The easiest method for removing a sheet view immediately after placing it is to use UNDO.

#### Related Tasks

* [To Add a View to a Sheet](To-Add-a-View-to-a-Sheet.md)

#### Related References

* [Sheet Set Manager Palette](Sheet-Set-Manager-Palette.md)

#### Related Concepts

* [About Publishing Sheet Sets](About-Publishing-Sheet-Sets-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*