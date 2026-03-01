# Block Object Properties Reference

The objects in a block can be set to retain their original properties or inherit properties from the destination drawing.

Color, linetype, lineweight, and transparency properties of objects in a block are treated three ways when a block reference
is inserted. The properties of the original objects affect whether they retain their original settings or inherit settings
from the drawing or insertion layer. The following guidelines for displaying block properties also affect the components of
nested blocks.

| If you want objects in a block to | Create objects on these layers | Create objects with these properties |
| Retain original properties | Any but 0 (zero) | Any but ByBlock or ByLayer |
| Inherit properties from the current layer | 0 (zero) | ByLayer |
| Inherit individual properties first, then layer properties | Any | ByBlock |

#### Related References

* [Commands for Basic Blocks](Commands-for-Basic-Blocks.md)

#### Related Concepts

* [About Defining Blocks](About-Defining-Blocks.md)
* [About Working With the Block Editor](About-Working-With-the-Block-Editor.md)

#### Related Information

* [To Define a New Block (Block Editor)](To-Define-a-New-Block-Block-Editor.md)
* [To Define a Block for the Current Drawing](To-Define-a-Block-for-the-Current-Drawing.md)
* [To Create a New Drawing File From Selected Objects](To-Create-a-New-Drawing-File-From-Selected-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*