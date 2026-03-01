# Common Group Codes for Entities (DXF)

The following table shows group codes that apply to virtually all graphical objects. Some of the group codes shown here are
included with an entity definition only if the entity has non-default values for the property. When you refer to the group
codes by entity type, the lists of codes associated with
*specific* entities, keep in mind that the codes shown here are also present.

NOTE:Do not write programs that rely on the order shown in these DXF code tables. Although these tables show the order of group
codes as they usually appear, the order can change under certain conditions or may be changed in a future
AutoCAD ®  release. The code that controls an entity should be driven by a case (switch) or a table so that it can process each group
correctly even if the order is unexpected.

When a group is omitted, its default value upon input (when using OPEN) is indicated in the third column. If the value of
a group code is equal to the default, it is omitted upon output (when using SAVEAS).

| Group codes that apply to all graphical objects | | |
| Group code | Description | If omitted, defaults to… |
| -1 | APP: entity name (changes each time a drawing is opened) | not omitted |
| 0 | Entity type | not omitted |
| 5 | Handle | not omitted |
| 102 | Start of application-defined group  “{*application\_name*” (optional) | no default |
| *application-defined codes* | Codes and values within the 102 groups are application-defined (optional) | no default |
| 102 | End of group, “}” (optional) | no default |
| 102 | “{ACAD\_REACTORS” indicates the start of the AutoCAD persistent reactors group. This group exists only if persistent reactors have been attached to this object (optional) | no default |
| 330 | Soft-pointer ID/handle to owner dictionary (optional) | no default |
| 102 | End of group, “}” (optional) | no default |
| 102 | “{ACAD\_XDICTIONARY” indicates the start of an extension dictionary group. This group exists only if an extension dictionary has been attached to the object (optional) | no default |
| 360 | Hard-owner ID/handle to owner dictionary (optional) | no default |
| 102 | End of group, “}” (optional) | no default |
| 330 | Soft-pointer ID/handle to owner BLOCK\_RECORD object | not omitted |
| 100 | Subclass marker (AcDbEntity) | not omitted |
| 67 | Absent or zero indicates entity is in model space. 1 indicates entity is in paper space (optional). | 0 |
| 410 | APP: layout tab name | not omitted |
| 8 | Layer name | not omitted |
| 6 | Linetype name (present if not BYLAYER). The special name BYBLOCK indicates a floating linetype (optional) | BYLAYER |
| 347 | Hard-pointer ID/handle to material object (present if not BYLAYER) | BYLAYER |
| 62 | Color number (present if not BYLAYER); zero indicates the BYBLOCK (floating) color; 256 indicates BYLAYER; a negative value indicates that the layer is turned off (optional) | BYLAYER |
| 370 | Lineweight enum value. Stored and moved around as a 16-bit integer. | not omitted |
| 48 | Linetype scale (optional) | 1.0 |
| 60 | Object visibility (optional):  0 = Visible  1 = Invisible | 0 |
| 92 | Number of bytes in the proxy entity graphics represented in the subsequent 310 groups, which are binary chunk records (optional) | no default |
| 310 | Proxy entity graphics data (multiple lines; 256 characters max. per line) (optional) | no default |
| 420 | A 24-bit color value that should be dealt with in terms of bytes with values of 0 to 255. The lowest byte is the blue value, the middle byte is the green value, and the third byte is the red value. The top byte is always 0. The group code cannot be used by custom entities for their own data because the group code is reserved for AcDbEntity, class-level color data and AcDbEntity, class-level transparency data | no default |
| 430 | Color name. The group code cannot be used by custom entities for their own data because the group code is reserved for AcDbEntity, class-level color data and AcDbEntity, class-level transparency data | no default |
| 440 | Transparency value. The group code cannot be used by custom entities for their own data because the group code is reserved for AcDbEntity, class-level color data and AcDbEntity, class-level transparency data | no default |
| 390 | Hard-pointer ID/handle to the plot style object | no default |
| 284 | Shadow mode  0 = Casts and receives shadows  1 = Casts shadows  2 = Receives shadows  3 = Ignores shadows  NOTE:Starting with AutoCAD 2016-based products, this property is obsolete but still supported for backwards compatibility. | no default |

#### Related References

* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*