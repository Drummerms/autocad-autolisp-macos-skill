# GEODATA (DXF)

The following group codes are used by GEODATA objects.

| GEODATA group codes | |
| Group code | Description |
| 90 | AcDbGeoData Object version  1 - 2009  2 - 2010 |
| 70 | Type of design coordinates:  0 - Unknown  1 - Local grid  2 - Projected grid  3 - Geographic (latitude/longitude) |
| 330 | ObjectId of host block table record |
| 10,20,30 | Design point, reference point in WCS coordinates |
| 11,21,31 | Reference point in coordinate system coordinates, valid only when coordinate type is Local Grid. |
| 12,22 | North direction vector (2D) |
| 40 | Horizontal unit scale, factor which converts horizontal design coordinates to meters by multiplication. |
| 41 | Vertical unit scale, factor which converts vertical design coordinates to meters by multiplication. |
| 91 | Horizontal units per UnitsValue enumeration; will be kUnitsUndefined if the units specified are not supported. |
| 92 | Vertical units per UnitsValue enumeration; will be kUnitsUndefined if the units specified are not supported. |
| 210,220,230 | Up direction |
| 95 | Scale estimation method:  1 - None  2 - User specified scale factor  3 - Grid scale at reference point  4 - Prismoidal |
| 294 | Bool flag specifying whether to do sea level correction |
| 141 | User specified scale factor |
| 142 | Sea level elevation |
| 143 | Coordinate projection radius |
| 301 | Coordinate system definition string |
| 302 | GeoRSS tag |
| 305 | Observation from tag |
| 306 | Observation to tag |
| 307 | Observation coverage tag |
| 93 | Number of Geo-Mesh points |
| 13,23 | Coordinate of source mesh point (repeat) |
| 14,24 | Coordinate of destination mesh point (repeat) |
| 96 | Number of faces |
| 97 | Point index for face (repeat) |
| 98 | Point index for face (repeat) |
| 99 | Point index for face (repeat) |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*