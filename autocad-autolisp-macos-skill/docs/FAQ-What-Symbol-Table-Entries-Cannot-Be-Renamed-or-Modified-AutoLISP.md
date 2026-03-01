# FAQ: What Symbol Table Entries Cannot Be Renamed or Modified? (AutoLISP)

Most entries in the symbol tables can be renamed or modified with a few exceptions.

The following table shows which symbol table entries cannot be modified or renamed, except that most LAYER symbol table entries
can be renamed and xdata can be modified on all symbol table entries.

| Symbol table entries that cannot be modified or renamed | |
| Table | Entry name |
| VPORT | \*ACTIVE |
| LINETYPE | CONTINUOUS |
| LAYER | Entries cannot be modified, except for xdata, but renaming is allowed |

The following entries cannot be renamed, but are otherwise modifiable:

| Symbol table entries that cannot be renamed | |
| Table | Entry name |
| STYLE | STANDARD |
| DIMSTYLE | STANDARD |
| BLOCKS | \*MODEL\_SPACE or \*PAPER\_SPACE |
| APPID | No entries can be renamed |

#### Related Concepts

* [About Non-Graphical Object Handling (AutoLISP)](About-Non-Graphical-Object-Handling-AutoLISP.md)
* [About Symbol Tables (AutoLISP)](About-Symbol-Tables-AutoLISP.md)
* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Anonymous Blocks (AutoLISP)](About-Anonymous-Blocks-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Dictionary Objects and Entries (AutoLISP)](About-Dictionary-Objects-and-Entries-AutoLISP.md)
* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*