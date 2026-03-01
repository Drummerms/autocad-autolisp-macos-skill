# LEGACYCTRLPICK (System Variable)

Specifies the keys for selection cycling and the behavior for Ctrl-click.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

| 0 | Ctrl-click is used to select subobjects (faces, edges, and vertices) on 3D solids, surfaces, and meshes. |
| 1 | Ctrl-click is used to cycle through overlapping objects. Disallows using Ctrl-click to select subobjects on 3D solids, surfaces, and meshes. |
| 2 | Ctrl-click is used to select subobjects (faces, edges, and vertices) on 3D solids, surfaces, and meshes when [SUBOBJSELECTIONMODE](SUBOBJSELECTIONMODE-System-Variable.md) is set to 0.If SUBOBJSELECTIONMODE is set to 1, 2, 3, or 4, it is not necessary to hold down the Ctrl key to select subobjects.If you hold down the Ctrl key when SUBOBJSELECTIONMODE is set to 1, 2, 3, or 4, the subobject filter is turned off until the Ctrl key is released. |

#### Related Tasks

* [To Select Overlapping or Close Objects](To-Select-Overlapping-or-Close-Objects.md)

#### Related Concepts

* [About Selecting Subobjects](About-Selecting-Subobjects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*