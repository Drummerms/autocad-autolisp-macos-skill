# Sheet Set Manager Palette

Displays and organizes named collections of drawing sheets.

SHEETSET (Command)

*Menu:* Window ![](../images/ac.menuaro.gif) Sheet Set Manager

*Keyboard:* Cmd-8

## Summary

The Sheet Set Manager is not fully functional if

* A command is active
* No drawing is open
* The sheet set is locked
* A sheet is locked by another user

![](../images/GUID-FCE99A0F-CCD8-42C9-8EF7-F8403BA90239-low.png)

## Components of the Sheet Set Manager

The following explains which each of the components of the Sheet Set Manager are used for.

1. *Sheet Set Popup Menu.* Lists all the open and recently opened sheet sets. Use the list to switch between open sheet sets.
2. *Publish Button.* Displays and populates the Batch Publish dialog box with all the sheets in the current sheet sets.
3. *Sheet Set Tree View.* Displays an organized list of all sheets in the current sheet set.

   You can perform the following actions in the tree view:

   * Double-click a sheet or view to open the associated drawing.
   * Right-click to access shortcut menus of the operations that are relevant to the currently selected item. For more information,
     see
     [Sheet Set Tree View Shortcut Menus](Sheet-Set-Tree-View-Shortcut-Menus.md).
   * Drag items within the tree view to reorder them.
4. *Details Panel.* Displays the properties for the item selected in the sheet set tree view. At the bottom pane of the Sheet Set Manager, scroll
   up or down to view the available properties for the selected item.

   For more information on the properties listed in the Details panel, see

   * [Sheet Set Properties](Sheet-Set-Properties-Sheet-Set-Manager.md)
   * [Sheet Properties](Sheet-Properties-Sheet-Set-Manager.md)
   * [Subset Properties](Subset-Properties-Sheet-Set-Manager.md)
   * [View Properties](View-Properties-Sheet-Set-Manager.md)
5. *Create Action Button.* Displays a popup menu that allows you to create a new sheet set, or add sheets and subsets to the current sheet set.

   * *New Sheet.* Displays the
     [New Sheet dialog box](New-Sheet-Dialog-Box.md) and creates a new sheet in the sheet set or under the selected subset.
   * *Import layout as Sheet.* Displays the file navigation dialog box and allows you to select a layout from an existing drawing to add to the sheet set.
   * *New Subset.* Creates a new subset.
   * *New Sheet Set.* Displays the
     [New Sheet Set dialog box](New-Sheet-Set-Dialog-Box.md) and creates a new sheet set data (DST) file.
6. *Remove Button.* Removes the selected subset or sheet from the sheet set. Removing a sheet does not delete the associated drawing file.
7. *Sheet Set Action Button.* Displays a popup menu that allows you open, close, or publish a sheet set. You can also control how sheets are opened and
   renamed.

   * *Open Sheet Set.* Displays a file navigation dialog box and loads the information in the sheet set data (DST) file into the Sheet Set Manager.
   * *Close Sheet Set.* Closes the current sheet set.
   * *Batch Publish.* Displays the Batch Publish dialog box and adds the selected sheet, or the sheets contained in the selected subset or sheet
     set.
   * *Page Setup Manager.* Displays the Page Setup Manager and allows you to modify the page setup overrides in the current sheet set.
   * *Open Drawings to Model.* Controls whether the named layout or model space is set current when opening a layout from the Sheet Set Manager.
   * *Show File Users.* Controls the display of the user that created the sheet or currently has a sheet opened appears below the layout in the sheet
     set tree view.
   * *Name Synchronization.* Controls the renaming of drawing (DWG) files and sheets when changing the name and numbers of a sheet in the Sheet Set Manager.
     + *Sheet Title.* When checked, renaming a sheet in the Sheet Set Manager changes the layout name in the drawing (DWG) file.
       - *Prefix with Sheet Number.* When checked, renaming a sheet in the Sheet Set Manager changes the layout name in the drawing (DWG) file to a new name that
         prefixes the sheet title with the sheet number (<number> <title>).
     + *Drawing Title.* When checked, renaming a sheet in the Sheet Set Manager changes both the drawing (DWG) file and layout names.
       - *Prefix with Sheet Number.* When checked, renaming a sheet in the Sheet Set Manager changes both the drawing (DWG) file and layout names to a new name
         that prefixes the sheet title with the sheet number (<number> <title>).

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*