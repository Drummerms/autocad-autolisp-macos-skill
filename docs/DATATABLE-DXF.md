# DATATABLE (DXF)

The following group codes are used by the DATATABLE objects.

| DATATABLE group codes | |
| Group code | Description |
| 0 | Object name (DATATABLE) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group, always “}” |
| 330 | Soft-pointer ID/handle to owner object |
| 100 | Subclass marker (AcDbDataTable) |
| 70 | Version |
| 90 | Number of columns |
| 91 | Number of valid rows |
| 1 | Table name |
| 92, 2 | Column type and name; repeats for each column |
|  | One value is written for every row in each column |
| 71 | Boolean value |
| 93 | Integer value |
| 40 | Double value |
| 3 | String value |
| 10, 20, 30 | 2D Point |
| 11, 21, 31 | 3D Point |
| 331 | Soft-pointer ID/handle to object value |
| 360 | Hard-pointer ownership ID |
| 350 | Soft-pointer ownsership ID |
| 340 | Hard-pointer ID/handle |
| 330 | Soft-pointer ID/handle |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*