# New Commands and System Variables Reference

Provides a quick guide to which commands are new in this release.

## 2026 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [-BSEARCH](BSEARCH-Command.md) | At the Command prompt, converts the selected entities and identical instances into blocks. | ✓ | ✓ |
| [BSEARCH](BSEARCH-Command-2.md) | Displays the Convert dialog box, which provides options to convert selected entities and identical instances into blocks. | ✓ | ✓ |
| [IMAGEASYNCWAIT](IMAGEASYNCWAIT-Command.md) | Ensures that raster images being loaded in the background during file opening are complete before proceeding. | ✓ | ✓ |
|  |  |  |  |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [BSEARCHINCLUDEEXISTINGBLOCKS](BSEARCHINCLUDEEXISTINGBLOCKS-System-Variable.md) | Controls whether existing block instances are selected by BSEARCH command by default. | ✓ | ✓ |
| [FOLLOWSYSTEMSCROLL](FOLLOWSYSTEMSCROLL-System-Variable.md) | Controls whether the AutoCAD trackpad follows the system scrolling direction during panning or orbiting in 3D. | ✓ | ✓ |
| [IMAGEASYNC](IMAGEASYNC-System-Variable.md) | Controls whether images are asynchronous loaded in the background during the opening of a drawing file. | ✓ | ✓ |
| [MAXINTERSECTIONCURVEPOINTS](MAXINTERSECTIONCURVEPOINTS-System-Variable.md) | Controls the upper limit of the number of control points or vertices that splines and polylines can include in the intersection calculations. | ✓ | ✓ |
| [TEXTTOATTRIBUTE](TEXTTOATTRIBUTE-System-Variable.md) | In the BSEARCH command, if text objects are selected, controls whether text variations will be searched for conversion into block attributes. | ✓ | ✓ |
|  |  |  |  |

## 2025.1 New Commands and System Variables

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [MLEADERLAYER](MLEADERLAYER-System-Variable.md) | Specifies a default layer for new multileaders. | ✓ | ✓ |

## 2025 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [ACTIVITYINSIGHTSCLOSE](ACTIVITYINSIGHTSCLOSE-Command.md) | Closes the Activity Insights palette which displays activities for the current drawing. | ✓ | ✓ |
| [ACTIVITYINSIGHTSOPEN](ACTIVITYINSIGHTSOPEN-Command.md) | Opens the Activity Insights palette to view activities for the current drawing. | ✓ | ✓ |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [ACTIVITYINSIGHTSPATH](ACTIVITYINSIGHTSPATH-System-Variable.md) | Specifies the location Activity Insights activities are recorded. | ✓ | ✓ |
| [ACTIVITYINSIGHTSSUPPORT](ACTIVITYINSIGHTSSUPPORT-System-Variable.md) | Enables or disables the Activity Insights feature. | ✓ | ✓ |
| [ACTIVITYINSIGHTSVIEWEDLOGGING](ACTIVITYINSIGHTSVIEWEDLOGGING-System-Variable.md) | Turns on or off logging Viewed activities, such as opening a drawing. | ✓ | ✓ |
| [HPDRAWMODE](HPDRAWMODE-System-Variable.md) | Controls the drawing mode used when defining new boundaries to hatch or fill. | ✓ | ✓ |
| [HPPATHALIGNMENT](HPPATHALIGNMENT-System-Variable.md) | Specifies the alignment of new drawn paths to be hatched or filled. | ✓ | ✓ |
| [HPPATHWIDTH](HPPATHWIDTH-System-Variable.md) | Specifies the width of new drawn paths to be hatched or filled. | ✓ | ✓ |

## 2024 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [COPYFROMTRACE](COPYFROMTRACE-Command.md) | Copies objects from a trace into the drawing. | ✓ | ✓ |
| [FADEMARKUP](FADEMARKUP-Command.md) [-FADEMARKUP](FADEMARKUP-Command.md) | Fades individual markups so they are less visible on a trace. | ✓ |  |
| [MARKUPASSIST](MARKUPASSIST-Command.md) [-MARKUPASSIST](MARKUPASSIST-Command-2.md) | Analyzes an imported markup and can help place text callouts and revision clouds faster and with less manual effort. | ✓ |  |
| [MARKUPIMPORT](MARKUPIMPORT-Command-2.md) [-MARKUPIMPORT](MARKUPIMPORT-Command.md) | Imports a marked up drawing (image/pdf) in-place into your DWG as a new trace. | ✓ |  |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [AUTOPLACEMENT](AUTOPLACEMENT-System-Variable.md) | Controls whether placement suggestions are displayed as you insert a block. | ✓ | ✓ |
| [COMMENTHIGHLIGHT](COMMENTHIGHLIGHT-System-Variable.md) | Controls the display of the indicator badge on PDF text comments. | ✓ |  |
| [MARKUPASSISTMODE](MARKUPASSISTMODE-System-Variable.md) | Controls whether identified markups are highlighted. | ✓ |  |
| [MARKUPPAPERDISPLAY](MARKUPPAPERDISPLAY-System-Variable.md) | Indicates whether or not a digital markup is currently active. | ✓ |  |
| [MARKUPPAPERTRANSPARENCY](MARKUPPAPERTRANSPARENCY-System-Variable.md) | Controls the level of transparency when a digital markup is active. | ✓ |  |
| [MARKUPSELECTIONMODE](MARKUPSELECTIONMODE-System-Variable.md) | Enables selection using boundary markup assist boxes as criteria. | ✓ |  |
| [TRACEMARKUPFADECTL](TRACEMARKUPFADECTL-System-Variable.md) | Controls the transparency of faded markups. The lower the number, the more visible the markup is. | ✓ |  |
| [TRACEVPSUPPORT](TRACEVPSUPPORT-System-Variable.md) | Controls whether markup boxes are actionable within a currently active model space viewport. | ✓ |  |

## 2023 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [COUNT](COUNT-Command.md) | Counts and highlights the instances of the selected object in the drawing. | ✓ | ✓ |
| [COUNTAREA](COUNTAREA-Command.md) | Defines the area to count the instances of an object or block. NOTE:Only available while a count is active. | ✓ | ✓ |
| [COUNTAREACLOSE](COUNTAREACLOSE-Command.md) | Cancels the count selection area. NOTE:Only available while a count is active. | ✓ | ✓ |
| [COUNTCLOSE](COUNTCLOSE-Command.md) | Closes the Count toolbar and ends the count. | ✓ | ✓ |
| [COUNTFIELD](COUNTFIELD-Command.md) | Creates a field that's set to the value of the current count. | ✓ | ✓ |
| [COUNTLIST](COUNTLIST-Command.md) | Opens the Count palette to view and manage the counted blocks. | ✓ | ✓ |
| [COUNTLISTCLOSE](COUNTLISTCLOSE-Command.md) | Closes the Count palette. | ✓ | ✓ |
| [COUNTNAVNEXT](COUNTNAVNEXT-Command.md) | Zooms to the next object in the count result. | ✓ | ✓ |
| [COUNTNAVPREV](COUNTNAVPREV-Command.md) | Zooms to the previous object in the count result. | ✓ | ✓ |
| [COUNTTABLE](COUNTTABLE-Command.md) | Inserts a table containing the block names and the corresponding count of each block in the drawing. | ✓ | ✓ |
| [CUTBASE](CUTBASE-Command.md) | Copies selected objects to the Clipboard, along with a specified base point, and removes them from the drawing. | ✓ | ✓ |
| [EXPORTUSERSETTINGS](EXPORTUSERSETTINGS-Command.md) | Exports custom user settings for import on another machine. | ✓ | ✓ |
| [IMPORTUSERSETTINGS](IMPORTUSERSETTINGS-Command.md) | Imports custom user settings from an export file created previously with EXPORTUSERSETTINGS. | ✓ | ✓ |
| [SELECTCOUNT](SELECTCOUNT-Command.md) | Finds all objects within the current count that match the properties of the selected objects, and then adds them to the selection set. NOTE:Only available while a count is active. | ✓ | ✓ |
| [SHARE](SHARE-Command.md) | Shares a link to a copy of the current drawing to view or edit in the AutoCAD web app. The drawing copy includes all external references and images. | ✓ | ✓ |
| [TABLESTYLE](TABLESTYLE-Command.md) | Creates, modifies, or specifies table styles. | ✓ | ✓ |
| [TRACE](TRACE-Command.md) | Opens and manages traces from the command prompt. | ✓ | ✓ |
| [TRACEBACK](TRACEBACK-Command.md) | Displays the host drawing with full saturation, while dimming the trace geometry. | ✓ | ✓ |
| [TRACEFRONT](TRACEFRONT-Command.md) | Displays the active trace with full saturation, while dimming the host drawing geometry. | ✓ | ✓ |
| [TRACEPALETTECLOSE](TRACEPALETTECLOSE-Command.md) | Closes the Trace palette. | ✓ | ✓ |
| [TRACEPALETTEOPEN](TRACEPALETTEOPEN-Command.md) | Opens the Trace palette where you can view and manage traces in the current drawing. | ✓ | ✓ |
| [TRACEEDIT](TRACEEDIT-Command.md) | Changes the active trace to edit mode. | ✓ | ✓ |
| [TRACEVIEW](TRACEVIEW-Command.md) | Changes the active trace to view mode. | ✓ | ✓ |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [ANNOSCALEZOOM](ANNOSCALEZOOM-System-Variable.md) | Controls whether the mouse wheel zoom in paperspace viewports is controlled by specific zoom scales or is independent (legacy behavior). | ✓ | ✓ |
| [COLORTHEME](COLORTHEME-System-Variable.md) | Sets the color theme of the toolsets, palettes, and several other interface elements to dark or light. | ✓ | ✓ |
| [COUNTCHECK](COUNTCHECK-System-Variable.md) | Controls the checking for errors in the count. | ✓ | ✓ |
| [COUNTCOLOR](COUNTCOLOR-System-Variable.md) | Sets the highlighting color on objects in a count. | ✓ | ✓ |
| [COUNTERRORCOLOR](COUNTERRORCOLOR-System-Variable.md) | Sets the highlighting color on objects that can cause potential errors in a count. | ✓ | ✓ |
| [COUNTERRORNUM](COUNTERRORNUM-System-Variable.md) | Displays the number errors in the current count. | ✓ | ✓ |
| [COUNTNUMBER](COUNTNUMBER-System-Variable.md) | Displays the number of the current count. | ✓ | ✓ |
| [COUNTPALETTESTATE](COUNTPALETTESTATE-System-Variable.md) | Reports whether the Count palette is open or closed. | ✓ | ✓ |
| [COUNTSERVICE](COUNTSERVICE-System-Variable.md) | Controls the background indexing of the count. | ✓ | ✓ |
| [FASTSHADEDMODE](FASTSHADEDMODE-System-Variable.md) | Specifies whether the new cross platform 3D graphics system is turned on or off. | ✓ |  |
| [JIGZOOMMAX](JIGZOOMMAX-System-Variable.md) | Controls the maximum percentage of the view dimensions that the block extents must fit when being inserted. | ✓ | ✓ |
| [JIGZOOMMIN](JIGZOOMMIN-System-Variable.md) | Controls the minimum percentage of the view dimensions that the block extents must fit when being inserted. | ✓ | ✓ |
| [TRACECURRENT](TRACECURRENT-System-Variable.md) | Displays the name of the active trace when TRACEMODE=1 or 2. | ✓ | ✓ |
| [TRACEDISPLAYMODE](TRACEDISPLAYMODE-System-Variable.md) | Indicates whether the tracing paper effect is displayed (front) or not (back) while a trace is active. | ✓ | ✓ |
| [TRACEFADECTL](TRACEFADECTL-System-Variable.md) | Controls the amount of fading when TRACEMODE is active. The setting effects only the objects not being edited - the host drawing geometry or Trace geometry. | ✓ | ✓ |
| [TRACEMODE](TRACEMODE-System-Variable.md) | Indicates whether Trace is active and which mode is current - editing or viewing. | ✓ | ✓ |
| [TRACEOSNAP](TRACEOSNAP-System-Variable.md) | Controls whether object snaps apply to trace geometry while viewing a trace. | ✓ | ✓ |
| [TRACEPALETTESTATE](TRACEPALETTESTATE-System-Variable.md) | Reports whether the Trace palette is open or closed. | ✓ | ✓ |
| [TRACEPAPERCTL](TRACEPAPERCTL-System-Variable.md) | Controls the opaqueness of the tracing paper effect. The lower the number, the more transparent the tracing paper is. | ✓ | ✓ |

## 2022 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [EXPORTLAYOUT](EXPORTLAYOUT-Command.md) | Creates a visual representation of the current layout in the model space of a new drawing. | ✓ | ✓ |
| [PURGEAECDATA](PURGEAECDATA-Command.md) | Removes the invisible AutoCAD Architecture custom data in the drawing allowing you to save the drawing to a previous version without any warnings. | ✓ | ✓ |

## 2021 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [BREAKATPOINT](BREAKATPOINT-Command.md) | Breaks the selected object into two objects at a specified point. | ✓ | ✓ |
| [-INSERTCONTENT](INSERTCONTENT-Command.md) | Inserts a drawing or block into the current drawing. | ✓ | ✓ |
| [-PAGESETUP](PAGESETUP-Command.md) | Command line version of the PAGESETUP command intended for overriding the settings of page setups in scripts and other customization. | ✓ | ✓ |
| [REVCLOUDPROPERTIES](REVCLOUDPROPERTIES-Command.md) | Controls the approximate chord-length for the arcs in a selected revision cloud. | ✓ | ✓ |
| [XCOMPARE](XCOMPARE-Command.md) | Compares an attached xref with the latest state of the referenced drawing file, highlighting the differences with color within revision clouds. | ✓ | ✓ |
| [XCOMPARECLOSE](XCOMPARECLOSE-Command.md) | Closes the Xref Compare visor and ends the comparison. | ✓ | ✓ |
| [XCOMPARERCNEXT](XCOMPARERCNEXT-Command.md) | Zooms to the next change set of the xref comparison result. | ✓ | ✓ |
| [XCOMPARERCPREV](XCOMPARERCPREV-Command.md) | Zooms to the previous change set of the xref comparison result. | ✓ | ✓ |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [COMMANDWINDOWDOCKSTATE](COMMANDWINDOWDOCKSTATE-System-Variable.md) | Indicates whether the command window is docked or floating. | ✓ | ✓ |
| [COMPARESHOWCONTEXT](COMPARESHOWCONTEXT-System-Variable.md) | Controls the visibility of objects that are not used in the xref comparison. | ✓ | ✓ |
| [REVCLOUDARCVARIANCE](REVCLOUDARCVARIANCE-System-Variable.md) | Controls whether revcloud arcs are created with varying or uniform chord lengths. | ✓ | ✓ |
| [SECUREREMOTEACCESS](SECUREREMOTEACCESS-System-Variable.md) | Controls whether ObjectARX programs are restricted from accessing internet locations or remote servers. | ✓ | ✓ |
| [TEXTGAPSELECTION](TEXTGAPSELECTION-System-Variable.md) | Controls whether you can select text or mtext objects within the gaps or spaces between the letters. | ✓ | ✓ |
| [TEXTLAYER](TEXTLAYER-System-Variable.md) | Specifies a default layer for new text and multiline text objects in the current drawing. | ✓ | ✓ |
| [TRIMEDGES](TRIMEDGES-System-Variable.md) | Controls whether trimming and extending to hatches with Quick mode is limited to the edges of the hatches or includes the objects within hatch patterns. | ✓ | ✓ |
| [TRIMEXTENDMODE](TRIMEXTENDMODE-System-Variable.md) | Controls whether the TRIM and EXTEND commands use streamlined inputs by default. | ✓ | ✓ |
| [XCOMPAREBAKPATH](XCOMPAREBAKPATH-System-Variable.md) | Specifies the path where the backup xref file is stored. | ✓ | ✓ |
| [XCOMPAREBAKSIZE](XCOMPAREBAKSIZE-System-Variable.md) | Sets the size of the folder where the backup xref file is stored. | ✓ | ✓ |
| [XCOMPARECOLORMODE](XCOMPARECOLORMODE-System-Variable.md) | Switches the visual effect of objects in the host drawing during an xref comparison. | ✓ | ✓ |
| [XCOMPAREENABLE](XCOMPAREENABLE-System-Variable.md) | Enables the comparison between an xref and the referenced drawing file. | ✓ | ✓ |

## 2020 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [CLASSICINSERT](CLASSICINSERT-Command.md) | Inserts a block or drawing into the current drawing using the classic version of the INSERT command. | ✓ | ✓ |
| [COMPARECLOSE](COMPARECLOSE-Command.md) | Closes the DWG Compare visor and exits the comparison. | ✓ | ✓ |
| [COMPAREEXPORT](COMPAREEXPORT-Command.md) | Exports the comparison results into a new drawing, called a snapshot drawing, and opens the drawing. | ✓ | ✓ |
| [COMPAREIMPORT](COMPAREIMPORT-Command.md) | Imports objects from the compared file into the current drawing. Only the selected objects that exist in the compared file and not in the current file are imported. | ✓ | ✓ |
| [COMPAREINFO](COMPAREINFO-Command.md) | Displays the information about the two compared drawing files. | ✓ | ✓ |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [BLOCKMRULIST](BLOCKMRULIST-System-Variable.md) | Controls the number of most recently used blocks displayed in the Recent pane of the Blocks palette. | ✓ | ✓ |
| [BLOCKREDEFINEMODE](BLOCKREDEFINEMODE-System-Variable.md) | Controls whether a dialog box displays when inserting a block from the Blocks palette with the same name as an existing block definition. | ✓ | ✓ |
| [LTGAPSELECTION](LTGAPSELECTION-System-Variable.md) | Controls whether you can select or snap to the gaps on objects defined with non-continuous linetype. | ✓ | ✓ |
| [MEASUREMODE](MEASUREMODE-System-Variable.md) | Controls whether the MEASUREGEOM command always defaults to the Quick option. | ✓ | ✓ |
| [ROLLOVERTIPS](ROLLOVERTIPS-System-Variable.md) | Controls the display of rollover tooltips when the cursor hovers over an object. | ✓ | ✓ |

## 2019 New Commands and System Variables

| *New commands* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [COMPARE](COMPARE-Command.md) | Provides a visual comparison between two drawings, highlighting the differences. | ✓ | ✓ |
| [-COMPARE](COMPARE-Command-2.md) | Provides a visual comparison between two drawings, highlighting the differences, using the command line. | ✓ | ✓ |
| [NEWVIEW](NEWVIEW-Command.md) | Saves a new, named view from the display in the current viewport, or by defining a rectangular window. | ✓ | ✓ |

| *New system variables* | *Description* | *AutoCAD* | *AutoCAD LT* |
| [COMPARECOLOR1](COMPARECOLOR1-System-Variable.md) | Sets the color in the comparison drawing for the objects that exist only in the first drawing selected for comparison. | ✓ | ✓ |
| [COMPARECOLOR2](COMPARECOLOR2-System-Variable.md) | Sets the color in the comparison drawing for the objects that exist only in the second drawing selected for comparison. | ✓ | ✓ |
| [COMPARECOLORCOMMON](COMPARECOLORCOMMON-System-Variable.md) | Sets the color in the comparison drawing for the objects that are identical in the two drawings selected for comparison. | ✓ | ✓ |
| [COMPAREFRONT](COMPAREFRONT-System-Variable.md) | Controls the default display order of overlapping objects in the comparison drawing. | ✓ | ✓ |
| [COMPAREHATCH](COMPAREHATCH-System-Variable.md) | Controls whether hatch objects are included in the drawing comparison. | ✓ | ✓ |
| [COMPAREPROPS](COMPAREPROPS-System-Variable.md) | Controls whether a change in an object's property is identified as a change in the drawing comparison. | ✓ | ✓ |
| [COMPARERCMARGIN](COMPARERCMARGIN-System-Variable.md) | Specifies the offset distance between the boundary of a change set and the revision cloud in the comparison drawing. | ✓ | ✓ |
| [COMPARERCSHAPE](COMPARERCSHAPE-System-Variable.md) | Controls whether individual changes are merged as a single large rectangle or a series of smaller rectangle in the compare result drawing. | ✓ | ✓ |
| [COMPARESHOW1](COMPARESHOW1-System-Variable.md) | Displays the objects that exists only in the first drawing. | ✓ | ✓ |
| [COMPARESHOW2](COMPARESHOW2-System-Variable.md) | Displays the objects that exists only in the second drawing. | ✓ | ✓ |
| [COMPARESHOWCOMMON](COMPARESHOWCOMMON-System-Variable.md) | Displays the objects that are identical in both the drawings that are being compared. | ✓ | ✓ |
| [COMPARESHOWRC](COMPARESHOWRC-System-Variable.md) | Shows a revision cloud around the difference in the compare result drawing. | ✓ | ✓ |
| [COMPARETEXT](COMPARETEXT-System-Variable.md) | Controls whether text objects are included in the drawing comparison. | ✓ | ✓ |
| [COMPARETOLERANCE](COMPARETOLERANCE-System-Variable.md) | Specifies the tolerance used when comparing two drawing files-entities are considered identical if they are below or equal to a specified decimal point value. | ✓ | ✓ |
| [VISRETAINMODE](VISRETAINMODE-System-Variable.md) | Controls which xref layer properties to automatically sync on reload when the VISRETAIN system variable is set to 1. | ✓ | ✓ |
| [XREFLAYER](XREFLAYER-System-Variable.md) | Specifies a default layer for a new xref. | ✓ | ✓ |

#### Related References

* [Updated Commands and System Variables Reference](Updated-Commands-and-System-Variables-Reference.md)
* [Obsolete AutoCAD Commands and System Variables Reference](Obsolete-AutoCAD-Commands-and-System-Variables-Reference.md)

#### Related Concepts

* [What's New in AutoCAD for Mac 2024](What's-New-in-AutoCAD-for-Mac-2024.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*