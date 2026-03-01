# CACHEMAXTOTALSIZE (System Variable)

Sets the maximum total size of all graphics cache files saved in the GraphicsCache folder for the product.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1024 |

The valid range is from 0 to 65535 megabytes.

When the total size of the graphics cache files reaches the maximum, the oldest files in the cache are automatically deleted.
Setting this variable to 0 disables caching entirely and deletes any existing files in the GraphicsCache folder that are not
in use by an open drawing file.

#### Related Concepts

* [About Memory Tuning](About-Memory-Tuning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*