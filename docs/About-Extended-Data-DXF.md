# About Extended Data (DXF)

Extended data (xdata) is created by AutoLISP or ObjectARX applications. If an entity contains extended data, it follows the
entity's normal definition data. The group codes 1000 through 1071 describe extended data. The following is an example of
an entity containing extended data in DXF format.

*Normal entity definition data:*

```
0
INSERT
  5
F11
100
AcDbEntity
  8
TOP
100
AcDbBlockReference
 2
BLOCK_A
 10
0.0
 20
0.0
 30
0.0
```

*Extended entity definition data:*

```
1001
AME_SOL
1002
{
1070
 0
1071
 1.95059E+06
1070
 519
1010
2.54717
1020
2.122642
1030
2.049201
1005
ECD
1005
EE9
1005
0
1040
0.0
1040
1.0
1000
MILD_STEEL
```

The group code 1001 indicates the beginning of extended data. In contrast to normal entity data, with extended data the same
group code can appear
*multiple times*, and
*order* is important.

Extended data is grouped by registered application name. Each registered application group begins with a 1001 group code,
with the application name as the string value. Registered application names correspond to APPID symbol table entries.

An application can use as many APPID names as needed. APPID names are permanent, although they can be purged if they aren't
currently used in the drawing. Each APPID name can have no more than one data group attached to each entity. Within an application
group, the sequence of extended data groups and their meaning is defined by the application.

The extended data group codes are listed in the following table.

| Extended data group codes and descriptions | | |
| Entity name | Group code | Description |
| String | 1000 | Strings in extended data can be up to 255 bytes long (with the 256th byte reserved for the null character). |
| Application name | 1001  also a string value | Application names can be up to 31 bytes long (the 32nd byte is reserved for the null character).  NOTE:Do not add a 1001 group into your extended data because the program assumes it is the beginning of a new application extended data group. |
| Control string | 1002 | An extended data control string can be either “{”or “}”. These braces enable applications to organize their data by subdividing the data into lists. The left brace begins a list, and the right brace terminates the most recent list. Lists can be nested.  When the program reads the extended data for a particular application, it checks to ensure that braces are balanced. |
| Layer name | 1003 | Name of the layer associated with the extended data. |
| Binary data | 1004 | Binary data is organized into variable-length *chunks*. The maximum length of each chunk is 127 bytes. In ASCII DXF files, binary data is represented as a string of hexadecimal digits, two per binary byte. |
| Database handle | 1005 | Handles of entities in the drawing database  NOTE:When a drawing with handles and extended data handles is imported into another drawing using INSERT, INSERT \*, XREF Bind, XBIND, or partial OPEN, the extended data handles are translated in the same manner as their corresponding entity handles, thus maintaining their binding. This is also done in the EXPLODE block operation or for any other operation. When AUDIT detects an extended data handle that doesn't match the handle of an entity in the drawing file, it is considered an error. If AUDIT is fixing entities, it sets the handle to 0. |
| 3 reals | 1010, 1020, 1030 | Three real values, in the order *X*, *Y*, *Z*. They can be used as a point or vector record. The program never alters their value. |
| World space position | 1011, 1021, 1031 | Unlike a simple 3D point, the world space coordinates are moved, scaled, rotated, and mirrored along with the parent entity to which the extended data belongs. The world space position is also stretched when the STRETCH command is applied to the parent entity and this point lies within the select window. |
| World space displacement | 1012, 1022, 1032 | Also a 3D point that is scaled, rotated, and mirrored along with the parent (but is not moved or stretched). |
| World direction | 1013, 1023, 1033 | Also a 3D point that is rotated and mirrored along with the parent (but is not moved, scaled, or stretched). |
| Real | 1040 | A real value. |
| Distance | 1041 | A real value that is scaled along with the parent entity. |
| Scale factor | 1042 | Also a real value that is scaled along with the parent. The difference between a distance and a scale factor is application-defined. |
| Integer | 1070 | A 16-bit integer (signed or unsigned). |
| Long | 1071 | A 32-bit signed (long) integer. |

#### Related References

* [About Advanced DXF Issues (DXF)](About-Advanced-DXF-Issues-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*