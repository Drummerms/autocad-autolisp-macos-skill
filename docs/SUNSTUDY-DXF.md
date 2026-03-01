# SUNSTUDY (DXF)

The following group codes are used by SUNSTUDY objects.

| SUNSTUDY group codes | |
| Group code | Description |
| 0 | Object name (SUNSTUDY) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group, always “}” |
| 330 | Soft-owner ID/handle to owner object |
| 100 | Subclass marker (AcDbSunStudy) |
| 90 | Version Number |
| 1 | Sun setup name |
| 2 | Description |
| 70 | Output type |
| 3 | Sheet set name. Included only if Output type is Sheet Set. |
| 290 | Use subset flag. Included only if Output type is Sheet Set. |
| 4 | Sheet subset name. Included only if Output type is Sheet Set. |
| 291 | Select dates from calender flag |
| 91 | Date input array size (represents the number of dates picked) |
| 90 | Julian day; represents the date. One entry for each date picked. |
| 90 | Seconds past midnight; represents the time of day. One entry for each date picked. |
| 292 | Select range of dates flag |
| 93 | Start time. If range of dates flag is true. |
| 94 | End time. If range of dates flag is true. |
| 95 | Interval in seconds. If range of dates flag is true. |
| 73 | Number of hours |
| 290 | Hour. One entry for every hour as specified by the number of hours entry above. |
| 340 | Page setup wizard hard pointer ID |
| 341 | View hard pointer ID |
| 342 | Visual style ID |
| 74 | Shade plot type |
| 75 | Viewports per page |
| 76 | Number of rows for viewport distribution |
| 77 | Number of columns for viewport distribution |
| 40 | Spacing |
| 293 | Lock viewports flag |
| 294 | Label viewports flag |
| 343 | Text style ID |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*