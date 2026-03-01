# edit\_width Attribute (DCL)

Specifies the width in character-width units of the edit (input) portion of the box—the actual boxed portion of the
edit\_box tile.

*Supported Platforms:* Windows, Mac OS, and Web

```
edit_width = number;
```

Possible values are an integer or a real number. If
edit\_width is not specified or is zero, and the width of the tile is not fixed, the box expands to fill the available space. If
edit\_width is nonzero, then the box is right-justified within the space occupied by the tile. If it's necessary to stretch the tile
for layout purposes, the PDB feature inserts white space between the label and the edit portion of the box.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [popup\_list Tile (DCL)](popup_list-Tile-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*