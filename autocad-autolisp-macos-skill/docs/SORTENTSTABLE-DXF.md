# SORTENTSTABLE (DXF)

The following group codes are used by SORTENTSTABLE objects.

| SORTENTSTABLE group codes | |
| Group code | Description |
| 0 | Object name (SORTENTSTABLE) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary (ACAD\_SORTENTS) |
| 102 | End of persistent reactors group; always “}” |
| 100 | Subclass marker (AcDbSortentsTable) |
| 330 | Soft-pointer ID/handle to owner (currently only the \*MODEL\_SPACE or \*PAPER\_SPACE blocks) |
| 331 | Soft-pointer ID/handle to an entity (zero or more entries may exist) |
| 5 | Sort handle (zero or more entries may exist) |

If the SORTENTS Regen flag (bit-code value 16) is set, the program regenerates entities in ascending handle order. When the
DRAWORDER command is used, a SORTENTSTABLE object is attached to the \*Model\_Space or \*Paper\_Space block's extension dictionary
under the name ACAD\_SORTENTS. The SORTENTSTABLE object related to this dictionary associates a different handle with each
entity, which redefines the order in which the entities are regenerated.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*