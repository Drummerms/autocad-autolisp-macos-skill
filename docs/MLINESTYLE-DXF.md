# MLINESTYLE (DXF)

The following group codes are used by MLINESTYLE objects.

| MLINESTYLE group codes | |
| Group code | Description |
| 0 | Object name (MLINESTYLE) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” (persistent reactors group appears in all dictionaries except the main dictionary) |
| 330 | Soft-pointer ID/handle to owner dictionary. For MLINESTYLE objects this is always the ACAD\_MLINESTYLE entry of the named object dictionary |
| 102 | End of persistent reactors group; always “}” |
| 100 | Subclass marker (AcDbMlineStyle) |
| 2 | Mline style name |
| 70 | Flags (bit-coded):  1 =Fill on  2 = Display miters  16 = Start square end (line) cap  32 = Start inner arcs cap  64 = Start round (outer arcs) cap  256 = End square (line) cap  512 = End inner arcs cap  1024 = End round (outer arcs) cap |
| 3 | Style description (string, 255 characters maximum) |
| 62 | Fill color (integer, default = 256) |
| 51 | Start angle (real, default is 90 degrees) |
| 52 | End angle (real, default is 90 degrees) |
| 71 | Number of elements |
| 49 | Element offset (real, no default). Multiple entries can exist; one entry for each element |
| 62 | Element color (integer, default = 0). Multiple entries can exist; one entry for each element |
| 6 | Element linetype (string, default = BYLAYER). Multiple entries can exist; one entry for each element |

The 2 group codes in mline entities and MLINESTYLE objects are redundant fields. These groups should not be modified under
any circumstances, although it is safe to read them and use their values. The correct fields to modify are

Mline
:   The 340 group in the same object, which indicates the proper MLINESTYLE object.

Mlinestyle
:   The 3 group value in the MLINESTYLE dictionary, which precedes the 350 group that has the handle or entity name of the current
    mlinestyle.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*