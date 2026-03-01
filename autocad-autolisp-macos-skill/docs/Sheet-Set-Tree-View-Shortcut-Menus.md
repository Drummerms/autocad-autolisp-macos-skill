# Sheet Set Tree View Shortcut Menus

When working in the sheet set tree view in the Sheet Manager, there are several shortcut menus that can be displayed when
you right-click an item.

The following tables show the shortcut menu items that you are presented under certain conditions.

## Sheet Set Selected

When the sheet set is selected, the top node in the tree, the shortcut menu presents the following functions:

| Menu Item | Description |
| Close Sheet Set | Closes the current sheet set data (DST) file. |
| New Sheet | Displays the [New Sheet dialog box](New-Sheet-Dialog-Box.md) and adds the new sheet to the sheet set. |
| Import Layout as Sheet | Displays a file navigation dialog box and adds all the named layouts to the sheet set from the selected drawing. |
| New Subset | Creates a new subset. |
| Rename | Changes the name of the sheet set. |
| Publish | Displays the Batch Publish dialog box and adds all sheets in the sheet set.  NOTE:Subsets and sheets that are designated as not to be included for publish are excluded from the Batch Publish dialog box. |
| Page Setup | Displays the Page Setup Manager and allows you to modify the page setup overrides in the current sheet set. |
| Publish with Overrides | Publishes all the sheets in the sheet set using the selected page setup override rather than the page setup specified in each drawing.  Page setup overrides are stored in the Page Setup Overrides File property of the sheet set. |
| Reveal in Finder | Opens Finder and displays the location where the sheet set data (DST) file is stored. |
| Properties | Toggles the display of the Details panel. |

## Sheet Selected

When a sheet is selected, the shortcut menu presents the following functions:

| Menu Item | Description |
| Open | Opens the drawing (DWG) file associated with the sheet and sets the sheet current. |
| Open Read-Only | Opens the drawing (DWG) file associated with the sheet as read-only and sets the sheet current. |
| Duplicate | Creates a copy of the drawing (DWG) file associated with the sheet and imports the layout from the new drawing into the sheet set.  NOTE:The new sheet in the sheet set might have a different title than the original layout. |
| Remove Sheet | Removes the sheet from the sheet set.  NOTE:The drawing (DWG) file associated with the sheet is not removed from disk. |
| Rename | Changes the name of the sheet. |
| Place Callout Block | Specifies and places a callout block onto a sheet. |
| Publish | Displays the Batch Publish dialog box and adds the sheet.  NOTE:When the Publish property for a sheet is not enabled, the sheet is excluded from the Batch Publish dialog box. |
| Page Setup | Displays the Page Setup Manager and allows you to modify the page setup overrides in the current sheet set. |
| Publish with Overrides | Publishes the selected sheets using the selected page setup override rather than the page setup specified in each drawing.  Page setup overrides are stored in the Page Setup Overrides File property of the sheet set. |
| Reveal in Finder | Opens Finder and displays the location of the drawing (DWG) file associated with the sheet. |
| Properties | Toggles the display of the Details panel. |

## Subset Selected

When you select a subset, the shortcut menu presents the following functions:

| Menu Item | Description |
| New Sheet | Displays the [New Sheet dialog box](New-Sheet-Dialog-Box.md) and adds the new sheet to the subset. |
| Import Layout as Sheet | Displays a file navigation dialog box and adds all the named layouts to the subset from the selected drawing. |
| New Subset | Creates a new subset. |
| Rename | Changes the name of the subset. |
| Remove Subset | Removes the subset and all the sheets under it from the sheet set.  NOTE:The drawing (DWG) files associated with the sheets are not removed from disk. |
| Publish | Displays the Batch Publish dialog box and adds all sheets in the subset.  NOTE:When the Do Not Publish Layouts property for a subset is not enabled, the sheets in the subset are excluded from the Batch Publish dialog box. |
| Page Setup | Displays the Page Setup Manager and allows you to modify the page setup overrides in the current sheet set. |
| Publish with Overrides | Publishes all the sheets in the subset using the selected page setup override rather than the page setup specified in each drawing.  Page setup overrides are stored in the Page Setup Overrides File property of the sheet set. |
| Reveal in Finder | Opens Finder and displays the folder location that the subset represents. |
| Properties | Toggles the display of the Details panel. |

## View Selected

When you select a view placed on a sheet, the shortcut menu presents the following functions:

| Menu Item | Description |
| Go to View | Opens the drawing (DWG) file that contains the sheet in which the view is placed on. |
| Place Label Block | Places a view label block onto a sheet. |

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*