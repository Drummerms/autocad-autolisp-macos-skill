# Common Group Codes for Symbol Table Entries (DXF)

The following table shows group codes that apply to all symbol table entries in DXF files. When you refer to the table of
group codes by entity type, which lists the codes associated with specific entities, keep in mind that the codes shown here
can also be present.

| Group codes that apply to all symbol table entries | |
| Group code | Description |
| -1 | APP: entity name (changes each time a drawing is opened) |
| 0 | Entity type (table name) |
| 5 | Handle (all except DIMSTYLE) |
| 105 | Handle (DIMSTYLE table only) |
| 102 | Start of application-defined group “{*application\_name*”. For example, “{ACAD\_REACTORS” indicates the start of the AutoCAD persistent reactors group (optional) |
| *application-defined codes* | Codes and values within the 102 groups are application defined (optional) |
| 102 | End of group, “}” (optional) |
| 102 | “{ACAD\_REACTORS” indicates the start of the AutoCAD persistent reactors group. This group exists only if persistent reactors have been attached to this object (optional) |
| 330 | Soft-pointer ID/handle to owner dictionary (optional) |
| 102 | End of group, “}” (optional) |
| 102 | “{ACAD\_XDICTIONARY” indicates the start of an extension dictionary group. This group exists only if persistent reactors have been attached to this object (optional) |
| 360 | Hard-owner ID/handle to owner dictionary (optional) |
| 102 | End of group, “}” (optional) |
| 330 | Soft-pointer ID/handle to owner object |
| 100 | Subclass marker (AcDbSymbolTableRecord) |

#### Related References

* [About Symbol Table Group Codes (DXF)](About-Symbol-Table-Group-Codes-DXF.md)
* [Common Symbol Table Group Codes (DXF)](Common-Symbol-Table-Group-Codes-DXF.md)
* [About the DXF TABLES Section (DXF)](About-the-DXF-TABLES-Section-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*