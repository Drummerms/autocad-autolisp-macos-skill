# FIELD (DXF)

The following group codes are used by FIELD objects.

| FIELD group codes | |
| Group code | Description |
| 0 | Object name (ACAD\_FIELD) |
| 1 | Evaluator ID |
| 2 | Field code string |
| 3 | Overflow of field code string |
| 90 | Number of child fields |
| 360 | Child field ID (AcDbHardOwnershipId); repeats for number of children |
| 97 | Number of object IDs used in the field code |
| 331 | Object ID used in the field code (AcDbSoftPointerId); repeats for the number of object IDs used in the field code |
| 93 | Number of the data set in the field |
| 6 | Key string for the field data; a key-field pair is repeated for the number of data sets in the field |
| 7 | Key string for the evaluated cache; this key is hard-coded as ACFD\_FIELD\_VALUE |
| 90 | Data type of field value |
| 91 | Long value (if data type of field value is long) |
| 140 | Double value (if data type of field value is double) |
| 330 | ID value, AcDbSoftPointerId (if data type of field value is ID) |
| 92 | Binary data buffer size (if data type of field value is binary) |
| 310 | Binary data (if data type of field value is binary) |
| 301 | Format string |
| 9 | Overflow of format string |
| 98 | Length of format string |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*