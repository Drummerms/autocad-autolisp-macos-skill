# BSEARCHINCLUDEEXISTINGBLOCKS (System Variable)

Controls whether existing block instances are selected by BSEARCH command by default. You can still make adjustments to the
selection during the review process.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 3 |

| Value | Description |
| 0 | Excludes all blocks. |
| 1 | Excludes partial blocks. This may be a block and some loose entities or two or more blocks. |
| 2 | Excludes entire blocks, where the entire instance is one block. |
| 3 | Includes all existing blocks, whether partial or whole. |

#### Related Information

* [About Converting Repetitive Geometry](About-Converting-Repetitive-Geometry.md)
* [Commands for Smart Blocks](Commands-for-Smart-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*