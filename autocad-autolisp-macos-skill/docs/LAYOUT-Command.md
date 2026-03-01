# LAYOUT (Command)

Creates and modifies drawing layouts.

## Access Methods

*Menu*:
Insert
![](../images/ac.menuaro.gif) Layout
![](../images/ac.menuaro.gif) New Layout.

*Menu*:
Insert
![](../images/ac.menuaro.gif) Layout
![](../images/ac.menuaro.gif) Layout from Template.

*Status bar:* ![](../images/GUID-9174311E-7DC8-49C8-B39F-991EC3DAD0E2-low.png)

## List of Prompts

The following prompts are displayed.

Enter layout option [Copy/Delete/New/Template/Rename/SAveas/Set/?] <set>:

NOTE:Many of these options are available by right-clicking a layout tab name.

Copy
:   Copies a layout. If you do not provide a name, the new layout assumes the name of the copied layout with an incremental number
    in parentheses.

Delete
:   Deletes a layout. The most current layout is the default.

    The Model layout cannot be deleted. To remove all the geometry from the Model layout, you must select all geometry and use
    the ERASE command.

New
:   Creates a new layout. Up to 255 layouts can be created in a single drawing.

    Layout names must be unique. Layout names can be up to 255 characters long and are not case sensitive.

Template
:   Creates a new layout based on an existing layout in a template (DWT), drawing (DWG), or drawing interchange (DXF) file. If
    the FILEDIA system variable is set to 1, a
    [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md) is displayed for selecting a DWT, DWG, or DXF file. After you select a file, the Insert Layouts dialog box is displayed,
    which lists the layouts saved in the selected file. After you select a layout, the layout and all objects from the specified
    template or drawing file are inserted into the current drawing.

Rename
:   Renames a layout. The last current layout is used as the default for the layout to rename.

    Layout names must be unique. Layout names can be up to 255 characters long and are not case sensitive.

Saveas
:   Saves a layout as a drawing template(DWT) file without saving any unreferenced symbol table and block definition information.
    You can then use the template to create new layouts in your drawings without having to eliminate unnecessary information.

    The last current layout is used as the default for the layout to save as a template. If the FILEDIA system variable is set
    to 1, a standard file selection dialog box is displayed in which you can specify the template file in which to save the layout.

    The default layout template directory is specified in the Application Preferences dialog box.

Set
:   Makes a layout current.

?—List Layouts
:   Lists all the layouts defined in the drawing.

#### Related Information

* [Reuse Layouts and Layout Settings](Reuse-Layouts-and-Layout-Settings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*