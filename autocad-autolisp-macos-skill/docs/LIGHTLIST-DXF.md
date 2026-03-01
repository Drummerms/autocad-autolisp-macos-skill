# LIGHTLIST (DXF)

The following group codes are used by LIGHTLIST objects.

| LIGHTLIST group codes | |
| Group code | Description |
| 0 | Object name (LIGHTLIST) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary. For LIGHTLIST objects, this is always the ACAD\_LIGHT entry of the named object dictionary |
| 102 | End of persistent reactors group, always “}” |
| 330 | Soft-pointer ID/handle to owner object |
| 100 | Subclass marker (AcDbLightList) |
| 90 | Version number |
| 90 | Number of lights |
| 5 | Light handle (one for each light) |
| 1 | Light name (one for each light) |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*