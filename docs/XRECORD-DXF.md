# XRECORD (DXF)

The following group codes are common to all xrecord objects.

| Xrecord group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbXrecord) |
| 280 | Duplicate record cloning flag (determines how to merge duplicate entries):  0 = Not applicable  1 = Keep existing  2 = Use clone  3 = <xref>$0$<name>  4 = $0$<name>  5 = Unmangle name |
| 1-369 (except 5 and 105) | These values can be used by an application in any way |

Xrecord objects are used to store and manage arbitrary data. They are composed of DXF group codes with “normal object” groups
(that is, non-xdata group codes), ranging from 1 through 369 for supported ranges. This object is similar in concept to xdata
but is not limited by size or order.

Xrecord objects are designed to work in such a way as to not offend releases R13c0 through R13c3. However, if read into a
pre-R13c4 version of the AutoCAD ®  program, xrecord objects disappear.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*