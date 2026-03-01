# Cross-reference of MicroStation to AutoCAD Terms

Understanding the differences between MicroStation and AutoCAD terminology helps when attaching DGN files as underlays.

The table below explains many of the different terms that are used in MicroStation and provides a reference to the term that
is used in AutoCAD when possible.

| MicroStation to AutoCAD Terms | | |
| MicroStation Term | AutoCAD Term | Notes |
| AccuSnap | Osnap | Drafting tool for automatic snaps. |
| ACS | UCS | Coordinate system acronyms.  ACS = Auxiliary Coordinate System  UCS = User Coordinate System |
| ByLevel setting | BYLAYER setting | Setting that controls whether color, line weight, and line style are set for each level (layer). |
| Cell libraries | N/A | No reference in AutoCAD terminology. |
| Cells: shared and normal | Blocks | In AutoCAD, all blocks behave like shared cells. There is no reference in AutoCAD terminology to a normal cell. |
| Design model | Model space | DWG workmode and AutoCAD only allow for a single model. MicroStation DGN workmode allows for multiple models. |
| DGN file | DWG file | Native file format for each program. |
| Drop Element | Explode | Command used to demote element/object types to lower level. For example, cells/blocks can be demoted to geometry. |
| Element Attributes | Properties | Name for characteristics of elements/objects. |
| Fit View | Zoom extents | Command for zooming in on all elements currently in the drawing.   * MicroStation’s “Fit View” tool fits only visible geometry. * “Zoom Extents” area includes layers that have display turned off. |
| Handles | Grips | Vertices on geometry that can be selected and manipulated. |
| Key-in | Command Line | Place for entering commands/variables manually. |
| Levels | Layers | Organizational structure used to control the appearance of objects in a drawing. |
| Line styles | Linetypes | Setting used to control the appearance of the line work in a drawing. |
| Merge into Master | Bind XREF | Inserting an external reference into the current drawing. |
| Message Center | Text Window | Place for viewing text messages from program feedback. |
| Parasolid | ACIS | Native 3D modeling kernel for each program. |
| Patterning | Hatching | Filling of a defined area with a defined pattern. |
| Pen tables | Plot styles | Used to control how linework appears when printing or plotting. |
| References | References: attachments, overlays, and underlays | References to the current drawing are stored externally, which keeps the file size down, but still allows for access to the geometry for drafting and plotting. In Microstation, you can have references with Live Nesting or No Nesting. References with No Nesting are translated as overlays in AutoCAD-based products.  MicroStation V7 does not support nested references. |
| Seed file | Template drawing file | Files are used as a starting point for newly created files and store commonly used settings. For DGNEXPORT, the chosen seed file determines what master and sub units are used for translation to DGN as well as resolution and accuracy values. |
| Sheet model | Drawing layout  (paper space) | Commonly used to control the output of a drawing for plotting. |
| Smart Line | Polyline | Multi-segmented lines. |
| Tags | Attributes | Element used to store textual information in a cell (block). |
| View | Viewport | Used to control the visibility of different sections of a drawing. |
| View Attributes | Drafting settings | There is no direct reference in AutoCAD terminology. Similar options can be found in the taskbar/drafting settings area of AutoCAD. |
| Working units | Drawing units | Used to control command input values that are dependent on unit values. |

#### Related Concepts

* [About Underlays](About-Underlays.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*