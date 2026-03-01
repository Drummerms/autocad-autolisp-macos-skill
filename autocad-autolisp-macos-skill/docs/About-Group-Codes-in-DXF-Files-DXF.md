# About Group Codes in DXF Files (DXF)

Group codes and the associated values define a specific aspect of an object or entity. The line immediately following the
group code is the associated value. This value can be a string, an integer, or a floating-point value, such as the
*X*coordinate of a point. The lines following the second line of the group, if any, are determined by the group definition and
the data associated with the group.

Special group codes are used as file separators, such as markers for the beginning and end of sections, tables, and the end
of the file itself.

Entities, objects, classes, tables and table entries, and file separators are introduced with a 0 group code that is followed
by a name describing the group.

The maximum DXF file string length is 256 characters. If your drawing contains strings that exceed this number, those strings
are truncated during SAVE, SAVEAS, and WBLOCK. OPEN and INSERT fail if your DXF file contains strings that exceed this number.

#### Topics in this section

* [About ASCII Control Characters in DXF Files](About-ASCII-Control-Characters-in-DXF-Files.md)

#### Related References

* [About ASCII DXF Files](About-ASCII-DXF-Files.md)
* [About ASCII Control Characters in DXF Files](About-ASCII-Control-Characters-in-DXF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*