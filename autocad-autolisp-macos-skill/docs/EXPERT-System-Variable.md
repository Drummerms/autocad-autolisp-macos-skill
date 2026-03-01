# EXPERT (System Variable)

Controls whether certain prompts are issued.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

| 0 | Issues all prompts normally. |
| 1 | Suppresses “About to regen, proceed?” and “Really want to turn the current layer off?” (-[LAYER](LAYER-Command.md)) |
| 2 | Suppresses the preceding prompts and “Block already defined. Redefine it?” (-[BLOCK](BLOCK-Command.md)) and “A drawing with this name already exists. Overwrite it?” ([SAVE](SAVE-Command.md) or [WBLOCK](WBLOCK-Command.md)). |
| 3 | Suppresses the preceding prompts and those issued by the [LINETYPE](LINETYPE-Command.md) Command prompt (-LINETYPE) if you try to load a linetype that's already loaded or create a new linetype in a file that already defines that linetype. |
| 4 | Suppresses the preceding prompts and those issued by [UCS](UCS-Command.md) Save and [VPORTS](VPORTS-Command-2.md) Save if the name you supply already exists. |
| 5 | Suppresses the prompt, “That name is already in Use, redefine it?” issued by the -[DIMSTYLE](DIMSTYLE-Command-2.md) Save option when you supply the name of an existing dimension style. Suppresses the same prompt issued by the -[SCALELISTEDIT](SCALELISTEDIT-Command.md) Add option. |

When a prompt is suppressed by EXPERT, the operation in question is performed as though you entered
*y* at the prompt. Setting EXPERT can affect scripts, menu macros, AutoLISP, and the command functions.

#### Related Concepts

* [Switch Between Dialog Boxes and the Command Line](Switch-Between-Dialog-Boxes-and-the-Command-Line.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*