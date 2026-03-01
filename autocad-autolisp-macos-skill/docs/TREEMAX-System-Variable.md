# TREEMAX (System Variable)

Limits memory consumption during drawing regeneration by limiting the number of nodes in the spatial index (oct-tree).

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 10000000 |

By imposing a fixed limit with TREEMAX, you can load drawings created on systems with more memory than your system and with
a larger  [TREEDEPTH](TREEDEPTH-System-Variable.md) than your system can handle. These drawings, if left unchecked, have an oct-tree large enough to eventually consume more
memory than is available to your computer. TREEMAX also provides a safeguard against experimentation with inappropriately
high  [TREEDEPTH](TREEDEPTH-System-Variable.md) values.

The initial default for TREEMAX is 10000000 (10 million), a value high enough to effectively disable TREEMAX as a control
for  [TREEDEPTH](TREEDEPTH-System-Variable.md). The value to which you should set TREEMAX depends on your system's available RAM. You get about 15,000 oct-tree nodes per
megabyte of RAM.

If you want an oct-tree to use up to, but no more than, 2 megabytes of RAM, set TREEMAX to 30000 (2 x 15,000). If the program
runs out of memory allocating oct-tree nodes, restart, set TREEMAX to a smaller number, and try loading the drawing again.

The program might occasionally run into the limit you set with TREEMAX. Follow the resulting prompt instructions. Your ability
to increase TREEMAX depends on your computer's available memory.

#### Related Concepts

* [About Layer and Spatial Indexes](About-Layer-and-Spatial-Indexes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*