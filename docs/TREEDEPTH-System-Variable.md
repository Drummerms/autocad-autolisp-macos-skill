# TREEDEPTH (System Variable)

Specifies the maximum depth, that is, the number of times the tree-structured spatial index can divide into branches.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 3020 |

| 0 | Suppresses the spatial index entirely, eliminating the performance improvements it provides in working with large drawings. This setting assures that objects are always processed in database order. |
| >0 | Turns on spatial indexing. An integer of up to five digits is valid. The first three digits refer to model space, and the remaining two digits refer to paper space. |
| <0 | Treats model space objects as 2D (*Z* coordinates are ignored), as is always the case with paper space objects. Such a setting is appropriate for 2D drawings and makes more efficient use of memory without loss of performance |

NOTE:You cannot use TREEDEPTH transparently.

#### Related Concepts

* [About Layer and Spatial Indexes](About-Layer-and-Spatial-Indexes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*