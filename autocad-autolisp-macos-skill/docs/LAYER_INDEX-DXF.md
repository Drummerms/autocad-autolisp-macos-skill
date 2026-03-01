# LAYER\_INDEX (DXF)

The following group codes are used by LAYER\_INDEX objects.

| LAYER\_INDEX group codes | |
| Group code | Description |
| 0 | Object name (LAYER\_INDEX) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group, always “}” |
| 100 | Subclass marker (AcDbIndex) |
| 40 | Time stamp (Julian date) |
| 100 | Subclass marker (AcDbLayerIndex) |
| 8 | Layer name (multiple entries may exist) |
| 360 | Hard-owner reference to IDBUFFER (multiple entries may exist) |
| 90 | Number of entries in the IDBUFFER list (multiple entries may exist) |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*