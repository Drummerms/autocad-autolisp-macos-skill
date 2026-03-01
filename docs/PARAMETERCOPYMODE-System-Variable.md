# PARAMETERCOPYMODE (System Variable)

Controls how constraints and referenced user parameters are handled when constrained objects are copied between drawings,
Model space and layouts, and block definitions.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

Parameters and their values apply to the current space only. Model space, individual paper space layouts, and various block
definitions in the block editor cannot access each other's parameters. Several commands, including
[PASTECLIP](PASTECLIP-Command.md) and
[EXPLODE](EXPLODE-Command.md), can introduce dimensional constraints and constraint parameters into an environment where referenced user parameters are
no longer accessible or are in conflict.

The PARAMETERCOPYMODE system variable provides several options for handling these situations.

| 0 | Do not copy any dimensional constraints or constraint parameters. Constraints are removed from copied objects. |
| 1 | Copy dimensional constraints and constraint parameters. Always replace expressions with numerical constants. Rename dimensional parameters if there is a naming conflict. |
| 2 | Copy dimensional constraints, constraint parameters, and user parameters. Reference existing user parameters when available, otherwise replace expressions with numerical constants. |
| 3 | Copy dimensional constraints, constraint parameters, and user parameters. Reference existing user parameters when available, otherwise create any missing user parameters. Change missing referenced dimensional constraints into user parameters. |
| 4 | Copy all dimensional constraints, constraint parameters, and expressions. Rename the parameters of copied objects if conflicts in value occurs for copied parameters. |

#### Related Concepts

* [About Applying Dimensional Constraints](About-Applying-Dimensional-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*