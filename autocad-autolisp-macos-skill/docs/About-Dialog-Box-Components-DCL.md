# About Dialog Box Components (DCL)

A dialog box consists of the box and the components within it.

In dialog box creation and customization these components are known as tiles. The basic tile types are predefined by the programmable
dialog box (PDB) facility. The following figure shows a standard dialog box, with some of its components labeled.

![](../images/GUID-2AC2B7FA-29D9-403D-B53A-A333ED846986-low.png)

You can create complex tiles, called prototypes or subassemblies, by grouping tiles into rows and columns, with or without
an enclosing box or border. A row or column of tiles is referred to as a cluster. Prototypes and subassemblies can be used
in dialog box definitions by tile references. Each reference to a definition inherits the attributes of the original tile.
When referring to prototypes, you can change the values of the inherited attributes or add new attributes. When referring
to subassemblies, you cannot change or add attributes.

If you need multiple instances of a tile with some attributes in common, it is easiest to define and name a prototype that
contains only the common attributes. Then, in each reference to the prototype, you can change attributes or add new ones,
but you do not have to list all the common attributes each time you reference the tile. Because attributes are inherited,
you will more often need to create tile references—especially references to the predefined tiles—than to define new tiles.

For example, the OK, Cancel, and Help buttons are grouped into a subassembly, defined as a row (cluster) of three button tiles
and some spacing separating the buttons. Subassemblies are treated as single tiles. The tiles within a subassembly are called
children. DCL files are organized in a tree structure. At the top of the tree is a (dialog) tile that defines the dialog box itself. The following diagram shows a DCL file structure:

![](../images/GUID-26EC2D32-316F-43E2-A270-F3387F28F32D-low.png)

The layout, appearance, and behavior of a tile or subassembly are specified in DCL by the tile's attributes. For example,
the dialog itself, and most predefined tile types, have a
label attribute that specifies the text associated with the tile. The label of a dialog box defines the caption at the top of the
dialog box, the label of a button specifies the text inside the button, and so on.

Before you program a dialog box, plan both the dialog box and the application in detail before you code and debug. The sequence
in which the data is entered will vary with each user. The need to anticipate a variety of user actions imposes a program
structure that is less linear than conventional programming, but is more reflective of the way users work.

#### Related References

* [Predefined Tiles and Clusters Reference (DCL)](Predefined-Tiles-and-Clusters-Reference-DCL.md)

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Tile Definitions (DCL)](About-Tile-Definitions-DCL.md)
* [About Tile References (DCL)](About-Tile-References-DCL.md)
* [About Attributes and Attribute Values (DCL)](About-Attributes-and-Attribute-Values-DCL.md)
* [About Disabling Tiles (DCL)](About-Disabling-Tiles-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*