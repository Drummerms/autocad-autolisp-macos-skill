# RENDERGLOBAL (DXF)

The following group codes are used by RENDERGLOBAL objects.

| RENDERGLOBAL group codes | |
| Group code | Description |
| 0 | Object name (RENDERGLOBAL) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary. For a RENDERGLOBAL object, this is always the ACAD\_RENDER\_GLOBAL entry of the named object dictionary |
| 102 | End of persistent reactors group; always “}” |
| 100 | Subclass marker (AcDbRenderGlobal) |
| 90 | Class version 2 |
| 90 | Render procedure:  0 = View  1 = Crop  2 = Selection |
| 90 | Render destination  0 = Render Window  1 = Viewport |
| 290 | Save to file flag |
| 1 | Rendered image save file name |
| 90 | Image width |
| 90 | Image height |
| 290 | Predefined presets first flag |
| 290 | High info level flag |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [RENDER (DXF)](RENDER-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*