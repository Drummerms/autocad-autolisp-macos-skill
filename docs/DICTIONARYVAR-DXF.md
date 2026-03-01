# DICTIONARYVAR (DXF)

The following group codes are used by DICTIONARYVAR objects.

| DICTIONARYVAR group codes | |
| Group code | Description |
| 0 | Object name (DICTIONARYVAR) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary (ACDBVARIABLEDICTIONARY) |
| 102 | End of persistent reactors group, always “}” |
| 100 | Subclass marker (DictionaryVariables) |
| 280 | Object schema number (currently set to 0) |
| 1 | Value of variable |

DICTIONARYVAR objects are used as a means to store named values in the database for
 *setvar* / *getvar*  purposes without the need to add entries to the DXF™ HEADER section. System variables that are stored as DICTIONARYVAR objects
are the following: DEFAULTVIEWCATEGORY, DIMADEC, DIMASSOC, DIMDSEP, DRAWORDERCTL, FIELDEVAL, HALOGAP, HIDETEXT, INDEXCTL,
INDEXCTL, INTERSECTIONCOLOR, INTERSECTIONDISPLAY, MSOLESCALE, OBSCOLOR, OBSLTYPE, OLEFRAME, PROJECTNAME, SORTENTS, UPDATETHUMBNAIL,
XCLIPFRAME, and XCLIPFRAME.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*