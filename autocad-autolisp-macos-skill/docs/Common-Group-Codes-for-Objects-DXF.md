# Common Group Codes for Objects (DXF)

The following table shows group codes that apply to virtually all nongraphical objects. When you refer to a table of group
codes by object type, a list of codes associated with a *specific* object, keep in mind that the codes shown here can also be present. Some of the group codes are included with an object only
if the object has nondefault values for those group code properties.

| Common object group codes | |
| Group code | Description |
| 0 | Object type |
| 5 | Handle |
| 102 | Start of application-defined group “{*application\_name*” (optional) |
| *application-defined codes* | Codes and values within the 102 groups are application defined (optional) |
| 102 | End of group, “}” (optional) |
| 102 | “{ACAD\_REACTORS” indicates the start of the AutoCAD persistent reactors group. This group exists only if persistent reactors have been attached to this object (optional) |
| 330 | Soft-pointer ID/handle to owner dictionary (optional) |
| 102 | End of group, “}” (optional) |
| 102 | “{ACAD\_XDICTIONARY” indicates the start of an extension dictionary group. This group exists only if persistent reactors have been attached to this object (optional) |
| 360 | Hard-owner ID/handle to owner dictionary (optional) |
| 102 | End of group, “}” (optional) |
| 330 | Soft-pointer ID/handle to owner object |

#### Related References

* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*