# RENDERENVIRONMENT (DXF)

The following group codes are used by RENDERENVIRONMENT objects.

| RENDERENVIRONMENT group codes | |
| Group code | Description |
| 0 | Object name (RENDERENVIRONMENT) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary. For a RENDERENVIRONMENT object, this is always the ACAD\_RENDER\_ENVIRONMENT entry of the named object dictionary |
| 102 | End of persistent reactors group; always “}” |
| 100 | Subclass marker (AcDbRenderEnvironment) |
| 90 | Class version 1 |
| 290 | Fog enabled flag; 1 if enabled |
| 290 | Fog in background flag; 1 if enabled |
| 280, 280, 280 | Fog color; Red, green, and blue channel values |
| 40, 40 | Fog density; Near and Far density as a percentage |
| 40, 40 | Near and Far distance as a percentage of the distance between the camera and the far clipping plane |
| 290 | Environment image flag |
| 1 | Environment image file name (can be blank if the previous flag is 0) |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [RENDER (DXF)](RENDER-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*