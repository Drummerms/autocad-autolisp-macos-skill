# RAPIDRTRENDERSETTINGS (DXF)

The following group codes are used by RAPIDRTRENDERSETTINGS objects.

| RAPIDRTRENDERSETTINGS group codes | |
| Group code | Description |
| 0 | Object name (RAPIDRTRENDERSETTINGS) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group; always “}” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 100 | Subclass marker (AcDbRenderSettings) |
| 90 | Subclass version |
| 1 | Render preset name |
| 290 | Materials flag  0 = Disabled  1 = Enabled |
| 290 | Texture sampling flag  0 = Disabled  1 = Enabled |
| 290 | Back faces flag  0 = Disabled  1 = Enabled |
| 290 | Shadows flag  0 = Disabled  1 = Enabled |
| 1 | Preview image file name (Reserved for future use) |
| 1 | Render preset description |
| 90 | Display index |
| 290 | Predefined flag  0 = Custom render preset  1 = Predefined render preset |
| 100 | Subclass marker (AcDbRapidRTRenderSettings) |
| 90 | Subclass version |
| 70 | Render duration type  0 = Render by time  1 = Render by level  2 = Until satisfactory |
| 90 | Number of levels when rendering by levels |
| 90 | Duration when rendering by time |
| 70 | Render accuracy type  0 = Low  1 = Draft  2 = High |
| 70 | Sampling filter type  0 = Box  1 = Triangle  2 = Gauss  3 = Mitchell  4 = Lanczos |
| 40 | Filter width |
| 40 | Filter height |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*