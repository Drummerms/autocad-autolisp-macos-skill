# IMAGEDEF (DXF)

The following group codes are used by IMAGEDEF objects.

| IMAGEDEF group codes | |
| Group code | Description |
| 0 | Object name (IMAGEDEF) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to the ACAD\_IMAGE\_DICT dictionary |
| 330 | Soft-pointer ID/handle to IMAGEDEF\_REACTOR object (multiple entries; one for each instance) |
| 102 | End of persistent reactors group, always “}” |
| 100 | Subclass marker (AcDbRasterImageDef) |
| 90 | Class version 0 |
| 1 | File name of image |
| 10 | Image size in pixels  DXF: *U* value; APP: 2D point (*U* and *V* values) |
| 20 | DXF: *V* value of image size in pixels |
| 11 | Default size of one pixel in AutoCAD units  DXF: *U* value; APP: 2D point (*U* and *V* values) |
| 12 | DXF: *V* value of pixel size |
| 280 | Image-is-loaded flag. 0 = Unloaded; 1 = Loaded |
| 281 | Resolution units. 0 = No units; 2 = Centimeters; 5 = Inch |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*