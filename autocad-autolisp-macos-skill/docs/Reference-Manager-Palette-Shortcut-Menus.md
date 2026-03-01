# Reference Manager Palette Shortcut Menus

EXTERNALREFERENCES (Command)

*Menu*:
Window ![](../images/ac.menuaro.gif) Reference Manager.

When working in the File References panel, there are several shortcut menus that can be displayed when you right-click on
a file reference or an empty area. The following tables show the shortcut menu items that you are presented under certain
conditions.

## Current Drawing File Selected

When the current drawing file is selected, the top node in the tree, the shortcut menu presents the following functions:

| Menu Item | Description |
| Show Details | Displays the thumbnail preview and details for the selected file reference. |
| Open a Copy | Opens the drawing in a new drawing window as read-only. |
| Reveal in Finder | Opens Finder and displays the location where the current drawing file is stored. |
| Print | Displays the Plot dialog box. |
| Reload | Reloads all file referenced files attached to the current drawing. (Unavailable if no file references are attached.) |
| Close File | Closes the drawing file. If changes were made, you are prompted to save or discard them before the drawing can be closed. |

## No File Reference Selected

When no file reference is selected, the shortcut menu presents the following functions:

| Menu Item | Description |
| Attach Reference | Displays the Select Reference File dialog box. |
| Reload All References | Reloads all file referenced files attached to the current drawing. (Unavailable if no file references are attached.) |

## File Reference Selected

When you select a file reference, the shortcut menu presents the following functions:

| Menu Item | Description | Reference Status |
| Show in Model | Zooms to the location of the file reference attachment in the drawing so it is fully displayed in the drawing area. | Available only for file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Edit Xref in Place | Opens the selected file reference for edit in the current drawing window. | Available only for DWG file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Open File | Opens the selected file reference in the default editor (specified by the operating system). | Available only for file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Show Details | Displays the thumbnail preview and details for the selected file reference. | Always available - status has no affect on this function. |
| Reveal in Finder | Opens Finder and displays the location where the file reference is stored. | Available only for file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Compare -> Recent Changes | Compares the selected xref with the latest version of the referenced drawing file. | Available only for DWG file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Compare -> Selected File | Opens a standard file navigation selection dialog box, in which you can select another drawing file to compare with the specified xref. | Always available for DWG file references - status has no affect on this function. |
| Attach | Switches the selected DWG file reference to the Attach attachment type. | Always available for DWG file references - status has no affect on this function. |
| Overlay | Switches the selected DWG file reference to the Overlay attachment type. | Always available for DWG file references - status has no affect on this function. |
| Unload | Unloads the selected file references. | Always available - status has no affect on this function. |
| Reload | Reloads the selected file reference. | Always available - status has no affect on this function. |
| Bind | Binds the selected DWG reference to the current drawing. Xref-dependent named objects are changed from *blockname*|*definitionname* to *blockname*$*n*$*definitionname* syntax. In this manner, unique named objects are created for all xref-dependent definition tables bound to the current drawing. | Available only for DWG file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Bind-Insert | Binds the DWG reference to the current drawing in a way similar to detaching and inserting the reference drawing. Rather than being renamed using *blockname*$*n*$*definitionname* syntax, xref-dependent named objects are stripped of the xref name. As with inserting drawings, no name-incrementing occurs if a local named object shares the same name as a bound xref-dependent named object. The bound xref-dependent named object assumes the properties of the locally defined named object. | Available only for DWG file references with a Loaded status - Unavailable when Unloaded, Not Found or Unresolved. |
| Detach | Detaches the selected file reference. | Available for all file references. |
| Change Path Type -> Make Absolute | Specifies the full path with hierarchy of folders that locates the file reference. | Available for all file references. |
| Change Path Type -> Make Relative | Specifies the partially folder path that assumes the current drive letter or the folder of the host drawing. | Available for all file references. |
| Change Path Type -> Remove Path | Removes the path to only mention file reference name. | Available for all file references except data link. |
| Select New Path | Allows you to browse to a new location for a not found reference file (fix one), and then provides you with an option to apply the same new location for other missing reference files (fix all). | Available for all file references. |

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)
* [To Change the Layer of Selected Objects](To-Change-the-Layer-of-Selected-Objects.md)
* [To Match the Layer Setting Between Selected Objects](To-Match-the-Layer-Setting-Between-Selected-Objects.md)
* [To Change the Visibility of Layers](To-Change-the-Visibility-of-Layers.md)
* [To Purge All Unused Layers](To-Purge-All-Unused-Layers.md)

#### Related References

* [Layers Palette](Layers-Palette.md)
* [VISRETAIN (System Variable)](VISRETAIN-System-Variable.md)
* [VISRETAINMODE (System Variable)](VISRETAINMODE-System-Variable.md)
* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Xref Layer Properties and Overrides](About-Xref-Layer-Properties-and-Overrides.md)
* [About Layers](About-Layers.md)
* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [About Overriding Layer Properties in a Layout Viewport](About-Overriding-Layer-Properties-in-a-Layout-Viewport.md)

#### Related Information

* [About Saving and Restoring Layer States and Settings](About-Saving-and-Restoring-Layer-States-and-Settings.md)
* [Overview of Object Properties](Overview-of-Object-Properties.md)
* [Reference Manager Palette](Reference-Manager-Palette.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*