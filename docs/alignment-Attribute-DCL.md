# alignment Attribute (DCL)

Specifies the horizontal or vertical positioning (justification) of a tile within its cluster.

*Supported Platforms:* Windows, Mac OS, and Web

```
alignment = position;
```

For a tile that is a child of a column, the possible values are
left,
right, or
centered (default is
left).

For a tile that is a child of a row, the possible values are
top,
bottom, or
centered (default is
centered).

You cannot specify the alignment along the long axis of a cluster. The first and last tiles in the cluster always align themselves
with the ends of the column or row. Other tiles in the cluster are distributed evenly unless you adjust the distribution by
using padding insertion points.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [spacer\_0 Tile (DCL)](spacer_0-Tile-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*