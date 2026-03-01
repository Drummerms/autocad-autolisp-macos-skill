# Symbol Table Group Codes in DXF Files (DXF)

The following is an example of the TABLES section of a DXF file.

| 0  SECTION  2  TABLES | *Beginning of TABLES section* |
| 0  TABLE  2  <table type>  5  <handle>  100  AcDbSymbolTable  70  <max. entries> | *Common table group codes; repeats for each entry* |
| 0  <table type>  5  <handle>  100  AcDbSymbolTableRecord  .  . <data>  . | *Table entry data; repeats for each table record* |
| 0  ENDTAB | *End of table* |
| 0  ENDSEC | *End of TABLES section* |

#### Topics in this section

* [Symbol Table Example (DXF)](Symbol-Table-Example-DXF.md)

#### Related References

* [About ASCII DXF Files](About-ASCII-DXF-Files.md)
* [Symbol Table Example (DXF)](Symbol-Table-Example-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*