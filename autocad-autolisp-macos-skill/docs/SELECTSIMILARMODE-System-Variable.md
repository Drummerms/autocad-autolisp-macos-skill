# SELECTSIMILARMODE (System Variable)

Controls which properties must match for an object of the same type to be selected with SELECTSIMILAR.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | User-settings |
| Initial value: | 130 |

The default value is 130. Objects of the same type are considered similar if they are on the same layer, and, for referenced
objects, have the same name.

The setting is stored as a bitcode using the sum of the following values:

| 0 | Object type |
| 1 | Color |
| 2 | Layer |
| 4 | Linetype |
| 8 | Linetype scale |
| 16 | Lineweight |
| 32 | Plot style |
| 64 | Object style (such as text styles, dimension styles, and table styles) |
| 128 | Name (for referenced objects, such as blocks, xrefs, and images) |

#### Related Concepts

* [About Selecting Objects Based on Shared Properties](About-Selecting-Objects-Based-on-Shared-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*