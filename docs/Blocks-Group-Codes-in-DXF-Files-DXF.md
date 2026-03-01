# Blocks Group Codes in DXF Files (DXF)

The following is an example of the BLOCKS section of a DXF file:

| 0  SECTION  2  BLOCKS | *Beginning of BLOCKS section* |
| 0  BLOCK  5  <handle>  100  AcDbEntity  8  <layer>  100  AcDbBlockBegin  2  <block name>  70  <flag>  10  <X value>  20  <Y value>  30  <Z value>  3  <block name>  1  <xref path> | *Begins each block entry (a block entity definition)* |
| 0  <entity type>  .  . <data>  . | *One entry for each entity definition within the block* |
| 0  ENDBLK  5  <handle>  100  AcDbBlockEnd | *End of each block entry (an endblk entity definition)* |
| 0  ENDSEC | *End of BLOCKS section* |

#### Related References

* [About ASCII DXF Files](About-ASCII-DXF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*