# TREESTAT (Command)

Displays information about the drawing's current spatial index.

## Access Methods

![](../images/ac.keyboard.gif) Command entry:  *'treestat* for transparent use

## Summary

The program indexes objects in a region by recording their positions in space. The result is called a *spatial index*. The spatial index is tree structured and has branching nodes to which objects are attached. The index has two major branches.
The paper space branch is called a quad-tree and treats objects as two-dimensional. The model space branch is called an oct-tree
and treats objects as either two- or three-dimensional. The model space branch can also be changed to a quad-tree when you
are working on two-dimensional drawings.

TREESTAT displays information about each branch. The most important information is in the first two lines of the report—number
of nodes, number of objects, maximum depth of the branch, and average number of objects per node.

If [REDRAW](REDRAW-Command.md) and object selection are very slow, you can improve their performance. For example, if there are 50 megabytes of memory available
and the current drawing has 50,000 objects with only 1,000 nodes in the index tree, increase the [TREEDEPTH](TREEDEPTH-System-Variable.md) value to improve performance.

Each node consumes about 80 bytes of memory. The fewer objects per node of the oct-tree, the better the performance.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*