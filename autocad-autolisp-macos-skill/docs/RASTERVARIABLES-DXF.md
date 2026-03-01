# RASTERVARIABLES (DXF)

The following group codes are used by RASTERVARIABLES objects.

| RASTERVARIABLES group codes | |
| Group code | Description |
| 0 | Object name (RASTERVARIABLES) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary. For a RASTERVARIABLES object, this is always the ACAD\_IMAGE\_VARS entry of the named object dictionary |
| 102 | End of persistent reactors group; always “}” |
| 100 | Subclass marker (AcDbRasterVariables) |
| 90 | Class version 0 |
| 70 | Display-image-frame flag: 0 = No frame; 1 = Display frame |
| 71 | Image display quality (screen only): 0 = Draft; 1 = High |
| 72 | AutoCAD units for inserting images. This is what one AutoCAD unit is equal to for the purpose of inserting and scaling images with an associated resolution:  0 = None; 1 = Millimeter; 2 = Centimeter  3 = Meter; 4 = Kilometer; 5 = Inch  6 = Foot; 7 = Yard; 8 = Mile |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*