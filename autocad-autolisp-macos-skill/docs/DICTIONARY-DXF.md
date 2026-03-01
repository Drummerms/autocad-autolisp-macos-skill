# DICTIONARY (DXF)

The following group codes are used by DICTIONARY objects.

| DICTIONARY group codes | |
| Group code | Description |
| 0 | Object name (DICTIONARY) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group, always “}” |
| 330 | Soft-pointer ID/handle to owner object |
| 100 | Subclass marker (AcDbDictionary) |
| 280 | Hard-owner flag. If set to 1, indicates that elements of the dictionary are to be treated as hard-owned |
| 281 | Duplicate record cloning flag (determines how to merge duplicate entries):  0 = Not applicable  1 = Keep existing  2 = Use clone  3 = <xref>$0$<name>  4 = $0$<name>  5 = Unmangle name |
| 3 | Entry name (one for each entry) (optional) |
| 350 | Soft-owner ID/handle to entry object (one for each entry) (optional) |

AutoCAD  ®  maintains items such as multiline styles and group definitions as objects in dictionaries. The following sections describe
the object group codes maintained in dictionaries; however, other applications are free to create and use their own dictionaries
as they see fit. The prefix
"ACAD\_" is reserved for use by
AutoCAD.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*