# DRAWORDERCTL (System Variable)

Controls the default display behavior of overlapping objects when they are created or edited.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 3 |

| 0 | Turns off the default draw order of overlapping objects: after objects are edited, regardless of their draw order, the objects are displayed on top until a drawing is regenerated (REGEN) or reopened. This setting also turns off draw order inheritance: new objects that are created from another object using the commands listed below are not assigned the draw order of the original object. Use this setting to improve the speed of editing operations in large drawings. The commands that are affected by inheritance are BREAK, FILLET, HATCH, HATCHEDIT, EXPLODE, TRIM, JOIN, PEDIT, and OFFSET. |
| 1 | Turns on the default draw order of objects: after objects are edited, they are automatically displayed according to the correct draw order. |
| 2 | Turns on draw order inheritance: new objects created from another object using the commands listed above are assigned the draw order of the original object. |
| 3 | Provides full draw order display. Turns on the correct draw order of objects, and turns on draw order inheritance. |

NOTE:Full draw order display may slow some editing operations.

#### Related Concepts

* [About the Draw Order of Overlapping Objects](About-the-Draw-Order-of-Overlapping-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*