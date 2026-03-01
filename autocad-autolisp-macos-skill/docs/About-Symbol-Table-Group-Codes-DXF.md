# About Symbol Table Group Codes (DXF)

The order of the tables may change, but the LTYPE table always precedes the LAYER table. Each table is introduced with a
0 group code with the label TABLE. This is followed by a 2 group code identifying the particular table (APPID, DIMSTYLE, LAYER,
LTYPE, STYLE, UCS, VIEW, VPORT, or BLOCK\_RECORD), a 5 group code (a handle), a 100 group code (AcDbSymbolTable subclass marker),
and a 70 group code that specifies the maximum number of table entries that may follow. Table names are output in uppercase.
The DIMSTYLE handle is a 105 group code, and not a 5 group code.

The tables in a drawing can contain deleted items, but these are not written to the DXF file. As a result, fewer table entries
may follow the table header than are indicated by the 70 group code, so do not use the count in the 70 group code as an index
to read in the table. This group code is provided so that a program that reads DXF files can allocate an array large enough
to hold all the table entries that follow.

Following this header for each table are the table entries. Each table entry consists of a 0 group identifying the item type
(same as table name, such as LTYPE or LAYER), a 2 group giving the name of the table entry, a 70 group specifying flags relevant
to the table entry (defined for each following table), and additional groups that give the value of the table entry. The end
of each table is indicated by a 0 group with the value ENDTAB.

Both symbol table records and symbol tables are database objects. At a very minimum, with all prevailing usage within
AutoCAD ® , this implies that a handle is present, positioned after the 2 group codes for both the symbol table record objects and the
symbol table objects.

The DIMSTYLE table is the only record type in the system with a handle code of 105 because of its earlier usage of group
code 5. As a rule, programmers should not be concerned about this exception unless it is in the context of the DIMSTYLE table
section. This is the only context in which this exception should occur.

#### Related References

* [About the DXF TABLES Section (DXF)](About-the-DXF-TABLES-Section-DXF.md)
* [Common Symbol Table Group Codes (DXF)](Common-Symbol-Table-Group-Codes-DXF.md)
* [Common Group Codes for Symbol Table Entries (DXF)](Common-Group-Codes-for-Symbol-Table-Entries-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*