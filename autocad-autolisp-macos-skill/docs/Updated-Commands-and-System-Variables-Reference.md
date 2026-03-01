# Updated Commands and System Variables Reference

Provides a quick guide to which commands are changed in this release.

## 2026 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [CENTERLINE](CENTERLINE-Command.md) | Creates centerline geometry associated with selected lines and linear polyline segments. | Added Layer option to specify the layer for new centerlines. | ✓ | ✓ |
| [CENTERMARK](CENTERMARK-Command.md) | Creates an associative, cross-shaped mark at the center of a selected circle or arc. | Added Layer option to specify the layer for new center marks. | ✓ | ✓ |
| [MLEADER](MLEADER-Command.md) | Creates a multileader object. | Added Layer option to specify the layer for new multileaders. | ✓ | ✓ |

## 2025 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [HATCH](HATCH-Command.md) | Fills an enclosed area or selected objects with a hatch pattern, solid fill, or gradient fill. | Draw boundary option was added. | ✓ | ✓ |
| [MARKUPASSIST](MARKUPASSIST-Command.md) | Analyzes an imported markup and can help place text callouts and revision clouds faster and with less manual effort. | Markup Assist can now be applied to external references, revision clouds can be inserted as rectangular or polygonal, and multiple text markups can be added to a single Markup Assist text insertion. | ✓ |  |
| [OPTIONS](OPTIONS-Command.md) | Customizes the program settings. | Added a setting to change the Activity Insights Event Location. | ✓ | ✓ |
| [REFEDIT](REFEDIT-Command.md) | Edits an xref or a block definition directly within the current drawing. | When a Trace is open, you can now make changes to xrefs. | ✓ | ✓ |
| [SHARE](SHARE-Command.md) | Shares a link to a copy of the current drawing to view or edit in the AutoCAD web app. The drawing copy includes all external references and images. | User interface has received minor changes. | ✓ | ✓ |
| [TRACEPALETTEOPEN](TRACEPALETTEOPEN-Command.md) | Opens the Trace palette where you can view and manage traces in the current drawing. | Improvements to the Trace toolbar. | ✓ | ✓ |

| *Updated system variable* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [FASTSHADEDMODE](FASTSHADEDMODE-System-Variable.md) | Specifies whether the new cross platform 3D graphics system is turned on or off. | 3D Wireframe visual style is now supported as part of Fast Shaded mode. | ✓ |  |

## 2024 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [INSERT](INSERT-Command.md) | Displays the Blocks palette, which you can use to insert blocks and drawings into the current drawing. | As you insert a block from the Blocks palette, the Block Placement engine displays placement suggestions based on where you've placed that block before in the drawing. | ✓ | ✓ |
| [OPTIONS](OPTIONS-Command.md) | Customizes the program settings. | Added controls to customize the background color for 3D visual styles including both parallel and perspective mode. | ✓ | ✓ |

## 2023 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [FIELD](FIELD-Command.md) | Creates a multiline text object with a field that can be updated automatically as the field value changes. | Count option was added to the Objects category. | ✓ | ✓ |
| [MLEADER](MLEADER-Command.md) | Creates a multileader object. | Mtext option added so you can select an existing mtext object to use for the new leader. | ✓ | ✓ |
| [PDFATTACH](PDFATTACH-Command.md) | Attaches a PDF file as an underlay into the current drawing. | Now using the Adobe API instead of the PDFTron API. | ✓ | ✓ |
| [PDFIMPORT](PDFIMPORT-Command-2.md) | Imports the geometry, fills, raster images, and TrueType text objects from a specified PDF file. | Now using the Adobe API instead of the PDFTron API. | ✓ | ✓ |
| [PUBLISH](Batch-Publish-Dialog-Box.md) | Specifies drawing sheets that you can assemble, reorder, and publish as a multi-sheet drawing set. | You can now save the current list of drawings as a DSD file for reuse or load a list of drawings from a saved DSD file. | ✓ | ✓ |
| [TABLE](TABLE-Command-2.md) | Creates an empty table object. | Insert Table dialog box added. | ✓ | ✓ |

## 2022 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [CUI](Shortcuts-Tab-Customize-Dialog-Box.md) | Manages the commands, menus, command aliases, and keyboard shortcuts in the product. | Shortcuts tab added where you can manage shortcut keys. | ✓ | ✓ |
| [CONTENT](CONTENT-Command.md) [INSERT](INSERT-Command.md) | Displays the Blocks palette, which you can use to insert blocks and drawings into the current drawing. | * Specify a drawing file or a folder to access your AutoCAD blocks. Sign in to your Autodesk Account to access block libraries   on your cloud storage. * A list view was added to the Blocks palette. * The Favorites tab was removed from the Blocks palette. | ✓ | ✓ |

## 2021.1 Updated Commands and System Variables

| *Updated system variable* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [CMDINPUTHISTORYMAX](CMDINPUTHISTORYMAX-System-Variable.md) | Sets the maximum number of previous input values that are stored for a prompt in a command. | Supported in the new Recent Input shortcut option. | ✓ | ✓ |
| [INPUTHISTORYMODE](INPUTHISTORYMODE-System-Variable.md) | Controls the content and location of the user input history. | Supported in the new Recent Input shortcut option. | ✓ | ✓ |

## 2021 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [-BLOCK](BLOCK-Command-2.md) | Creates a block definition from selected objects. | The Mode command option has been added to the Command prompt. This option allows you to choose the effect of block definition on objects used to create a block. | ✓ | ✓ |
| [EXPORT](EXPORT-Command.md) | Saves the objects in a drawing to a different file format. | PDF output is no longer supported. Use the PLOT command to output a drawing to PDF. | ✓ | ✓ |
| [EXTEND](EXTEND-Command.md) | Extends objects to meet the edges of other objects. | The default behavior is changed to Quick mode, which is set by the TRIMEXTENDMODE system variable.  All objects become potential extend boundaries and object selection defaults to individual objects or two-point fence or freehand dragging. | ✓ | ✓ |
| [MEASUREGEOM](MEASUREGEOM-Command.md) | Measures the distance, radius, angle, area, and volume of selected objects, a sequence of points, or dynamically. | The Quick option of the MEASUREGEOM command now supports area values.  Click once inside the enclosed area to display the area value. | ✓ | ✓ |
| [OPTIONS](OPTIONS-Command.md) | Customizes the program settings. | Enhancements include:   * Enable or disable lasso selection * Select a color for the layout background * Specify your Trusted Paths; the folders which have permission to load and execute files that contain code * Simplified Chinese added | ✓ | ✓ |
| [PURGE](PURGE-Command.md) | Removes unused items, such as block definitions and layers, from the drawing. | The PURGE dialog box now has a section showing objects that can't be purged. Included are possible reasons why the objects can't be purged and an option to find those objects in the current drawing. | ✓ | ✓ |
| [REVCLOUD](REVCLOUD-Command.md) | Creates or modifies a revision cloud. | Controls the approximate chord-length for the arcs in a selected revision cloud with a single value. This value can be changed for a selected revision cloud from its shortcut menu or from the Properties palette.  The default value of the chord length is determined automatically based on the size of the drawing area the first time you create a revision cloud in a drawing.  The Properties palette now identifies an object as a Revcloud rather than a Polyline object. | ✓ | ✓ |
| [TRIM](TRIM-Command.md) | Trims objects to meet the edges of other objects. | The default behavior is changed to Quick mode, which is set by the TRIMEXTENDMODE system variable.  All objects become potential trim boundaries and object selection defaults to individual objects or Fence/Lasso. Selected objects that can't be trimmed are deleted instead. | ✓ | ✓ |
| [-WBLOCK](WBLOCK-Command-2.md) | Saves selected objects or converts a block to a specified drawing file. | The Mode command option has been added to the Command prompt. This option allows you to choose the effect of block creation on objects used to create a block. | ✓ | ✓ |

## 2020 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | *AutoCAD* | *AutoCAD LT* |
| [COMPARE](COMPARE-Command.md) [-COMPARE](COMPARE-Command-2.md) | Compares a specified drawing file with the current drawing file, highlighting the differences by color within revision clouds. | Comparisons are displayed directly in the current drawing. Objects can be imported to the current drawing from the compared drawing. | ✓ | ✓ |
| [CONTENT](CONTENT-Command.md) | Displays the Blocks palette, which you can use to insert blocks and drawings into the current drawing. | The Content palette has been updated and is renamed Blocks. | ✓ | ✓ |
| [INSERT](INSERT-Command.md) | Displays the Blocks palette, which you can use to insert blocks and drawings into the current drawing. | No longer displays the file selection dialog to insert a block. To access the classic Insert Block dialog box, use the CLASSICINSERT command. | ✓ | ✓ |
| [MEASUREGEOM](MEASUREGEOM-Command.md) | Measures the distance, radius, angle, area, and volume of selected objects or sequence of points. | The new Quick option displays dimensions, distances, and angles within a 2D drawing dynamically as you move your mouse over and between objects. | ✓ | ✓ |
| [OPTIONS (General Tab)](General-Tab-Application-Preferences-Dialog-Box.md) | Controls the behavior of program features. | * Show Rollover Tooltips option added * Graphics options removed * Korean language added | ✓ | ✓ |

## 2019 Updated Commands and System Variables

| *Updated commands* | *Description* | *How changed* | AutoCAD | AutoCAD LT |
| [-LAYER](LAYER-Command-2.md) | Manages layers and layer properties at the command line. | XREF option added to remove Xref overrides | ✓ | ✓ |
| [MVIEW](MVIEW-Command.md) | Creates and controls layout viewports. | Named views added to toolbar for easy insertion when created with NEWVIEW | ✓ | ✓ |
| [PAGESETUPEDIT](Page-Setup-Dialog-Box.md) | Specifies page layout and plotting device settings. | Page Setup dialog rearranged and layout preview added. | ✓ | ✓ |
| [PLOT](Plot-Dialog-Box.md) | Outputs a drawing to a printer or file. | Plot dialog rearranged and layout preview added. | ✓ | ✓ |
| [PURGE](PURGE-Command.md) | Removes unused items, such as block definitions and layers, from the drawing. | A user interface added to the PURGE command. | ✓ | ✓ |
| [VPLAYER](VPLAYER-Command.md) | Sets layer visibility within viewports. | Added Removeoverrides option | ✓ | ✓ |

#### Related References

* [New Commands and System Variables Reference](New-Commands-and-System-Variables-Reference.md)
* [Obsolete AutoCAD Commands and System Variables Reference](Obsolete-AutoCAD-Commands-and-System-Variables-Reference.md)

#### Related Concepts

* [What's New in AutoCAD for Mac 2024](What's-New-in-AutoCAD-for-Mac-2024.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*