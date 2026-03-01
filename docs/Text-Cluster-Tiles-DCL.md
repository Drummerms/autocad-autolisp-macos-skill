# Text Cluster Tiles (DCL)

A text tile is surrounded by margin space (like any other kind of tile), which presents a problem when you want to combine
pieces of text.

For example, assume you want to display the following message:

The time is now 0800 hours and 37 seconds.

The actual values (0800 and 37) are supplied by your program. You can do this by creating a concatenated line of text built
out of
text\_part tiles. You can also use text parts vertically to create a paragraph that doesn't have too much space between the lines.

The following text cluster tiles are prototypes defined in the
*base.dcl* file.

| Text Cluster Tiles | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Tile name | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [concatenation](concatenation-Tile-DCL.md) | A concatenation is a line of text made up of multiple, concatenated text\_part tiles. | ✓ | ✓ | ✓ | -- | ✓ |
| [text](text-Tile-DCL.md) | A text tile displays a text string for titling or informational purposes. | ✓ | ✓ | ✓ | -- | ✓ |
| [text\_part](text_part-Tile-DCL.md) | A text part is a text tile that is part of a larger piece of text. | ✓ | ✓ | ✓ | -- | ✓ |
| [paragraph](paragraph-Tile-DCL.md) | A paragraph is a cluster of text\_part or concatenation tiles that are arranged vertically. | ✓ | ✓ | ✓ | -- | ✓ |

#### Related Concepts

* [concatenation Tile (DCL)](concatenation-Tile-DCL.md)
* [paragraph Tile (DCL)](paragraph-Tile-DCL.md)
* [text Tile (DCL)](text-Tile-DCL.md)
* [text\_part Tile (DCL)](text_part-Tile-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*