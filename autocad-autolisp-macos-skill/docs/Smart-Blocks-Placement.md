# Smart Blocks: Placement

The new smart block functionality can offer placement suggestions based on where you've placed that block before in the drawing.

The block placement engine learns how the existing block instances are placed in your drawing to infer the next placement
of the same block. As you insert a block, the engine gives placement suggestions close to a similar geometry where you've
placed that block before.

For example, if you've already placed a chair block close to the corner of a wall, when inserting another instance of that
same chair block, AutoCAD automatically positions the chair as you move it close to a similar corner. As you move the block,
the walls are highlighted, and the position, rotation, and scale of the chair block are adjusted to match the other block
instance. You can click to accept the suggestion, press Cmd to switch to other suggestions, or move the cursor away to ignore
the current suggestion. To temporarily turn off suggestions when placing a block, hold Shift+W or Shift+[ while inserting
or moving your block.

![](../images/GUID-F5AE1A52-6C6B-4954-A633-1876712E0E8C-low.png)

## *New System Variables*

[AUTOPLACEMENT](AUTOPLACEMENT-System-Variable.md) - Controls whether placement suggestions are displayed as you insert a block.

#### Related Tasks

* [To Insert a Block Using Automatic Placement](To-Insert-a-Block-Using-Automatic-Placement.md)

#### Related Concepts

* [What's New in AutoCAD for Mac 2024](What's-New-in-AutoCAD-for-Mac-2024.md)
* [About Smart Blocks](About-Smart-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*