# 3DSELECTIONMODE (System Variable)

Controls the selection precedence of both visually and physically overlapping objects when using 3D visual styles.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

| Value | Description |
| 0 | Use legacy 3D selection precedence. |
| 1 | Use line-of-sight 3D selection precedence for selecting 3D solids and surfaces. Also, a defining object is given selection precedence over the associated surface. |

3DSELECTIONMODE has no effect when selecting 3D solids if they are displayed as 2D or 3D wireframes.

#### Related Concepts

* [About Selecting Subobjects](About-Selecting-Subobjects.md)
* [About Selecting Objects Based on Shared Properties](About-Selecting-Objects-Based-on-Shared-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*