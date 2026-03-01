# Object Group Codes in DXF Files (DXF)

The following is an example of the OBJECTS section of a DXF file:

| 0  SECTION  2  OBJECTS | *Beginning of OBJECTS section* |
| 0  DICTIONARY  5  <handle>  100  AcDbDictionary | *Beginning of named object dictionary (root dictionary object)* |
| 3  <dictionary name>  350  <handle of child> | *Repeats for each entry* |
| 0  <object type>  .  . <data>  . | *Groups of object data* |
| 0  ENDSEC | *End of OBJECTS section* |

#### Related References

* [About ASCII DXF Files](About-ASCII-DXF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*