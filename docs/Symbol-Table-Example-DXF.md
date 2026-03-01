# Symbol Table Example (DXF)

This DXF sequence represents three full objects: the symbol table itself plus two entries.

| 0 |  |
| TABLE | *Indicates a symbol table entry* |
| 2 |  |
| STYLE | *Text style symbol table entry. Exception to rule that code 0 fully defines type* |
| 5 |  |
| 1C | *STYLE table handle; same as for entities and other objects* |
| 70 |  |
| 3 | *Maximum number of STYLE table records to follow (pre-Release 13 field)* |
| 1001 |  |
| APP\_X | *APP\_X has put xdata on a symbol table* |
| 1040 |  |
| 42.0 | *Just a single floating-point number* |
| 0 |  |
| STYLE | *Beginning of first element in the STYLE symbol table* |
| 5 |  |
| 3A | *The first entry's handle (DIMSTYLE entries will have 105 here)* |
| 2 |  |
| ENTRY\_1 | *The first entry's text name* |
| 70 |  |
| 64 | *Standard flag values* |
| 40 |  |
| .4 | *Text height* |
| 41 |  |
| 1.0 | *Width scale factor* |
| 50 |  |
| 0.0 | *Oblique angle* |
| 71 |  |
| 0 | *Text generation flags* |
| 42 |  |
| 0.4 | *Last height used* |
| 3 |  |
| BUFONTS.TXT | *Primary font file name* |
| 0 |  |
| STYLE | *Second entry begins. No xdata or persistent reactors on first entry* |
| 5 |  |
| C2 | *Second entry handle* |
| 2 |  |
| ENTRY\_2 | *Second entry text name* |
| ... |  |
| ... | *Other fields down to group code 3* |
| 3 |  |
| BUFONTS.TXT | *Primary font file name and last object type—specific group* |
| 102 |  |
| {ACAD\_REACTORS | *This entry has two persistent reactors* |
| 330 |  |
| 3C2 | *Soft ID to first reactor object* |
| 330 |  |
| 41B | *Soft ID to first reactor object* |
| 102 |  |
| } | *Indicates the end of the reactor set* |
| 1001 |  |
| APP\_1 | *Xdata attached to this entry* |
| 1070 |  |
| 45 |  |
| 1001 |  |
| APP\_2 |  |
| 1004 |  |
| 18A5B3EF2C199A |  |
| 0 |  |
| UCS | *Start of UCS table (and end of previous record and table)* |

#### Related References

* [Symbol Table Group Codes in DXF Files (DXF)](Symbol-Table-Group-Codes-in-DXF-Files-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*