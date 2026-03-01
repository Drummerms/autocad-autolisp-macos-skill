# value Attribute (DCL)

Specifies the initial value of a tile. Possible value is a quoted string.

*Supported Platforms:* Windows, Mac OS, and Web

```
value = "string";
```

The meaning of a tile's value varies depending on the kind of tile. The value of a tile can change at runtime through user
input or
set\_tile calls.

The
value attribute of a tile is not considered when the dialog box is laid out. After the layout is finished and the dialog box has
been displayed,
new\_dialog uses the value attributes to initialize each tile in the dialog box. A tile's value attribute has no effect on the size or
spacing of tiles in the dialog box.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [text Tile (DCL)](text-Tile-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*