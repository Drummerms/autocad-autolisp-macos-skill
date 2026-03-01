# Format Codes for Alternate Text Editor Reference

If you use an alternate text editor, you apply formatting by entering format codes.

To apply formatting, use the format codes shown in the following table.

| Format codes for paragraphs | | | |
| Format code | Purpose | Enter this … | To produce this … |
| \0...\o | Turns overline on  and off | Autodesk \OAutoCAD\o | ![](../images/GUID-FDCF2074-F960-4128-86C1-AC5A45A0F261-low.png) |
| \L...\l | Turns underline on  and off | Autodesk \LAutoCAD\l | ![](../images/GUID-C181986E-D896-4869-836E-E0619AB3DC6A-low.png) |
| \K...\k | Turns stikethrough on and off | Autodesk\KAutoCAD\k | ![](../images/GUID-C0918BC2-656B-45BA-AE41-97C3FB47ED21-low.png) |
| \~ | Inserts a nonbreaking  space | Autodesk AutoCAD\~LT | ![](../images/GUID-4A4A81B5-0960-45C7-B620-CDF96A8CF58A-low.png) |
| \\ | Inserts a backslash | Autodesk \\AutoCAD | ![](../images/GUID-40657A66-DF44-48C8-B6D0-725E3BA10EE3-low.png) |
| \{...\} | Inserts opening and closing braces | Autodesk \{AutoCAD\} | ![](../images/GUID-0DBF121A-967B-4A01-80BC-EEBB383CA85F-low.png) |
| \C*value;* | Changes to the  specified color | Autodesk \C2;AutoCAD | ![](../images/GUID-69B63D24-34C3-48AF-AE58-D8A33D174AC3-low.png) |
| \*File name*; | Changes to the  specified font file | Autodesk \Ftimes; AutoCAD | ![](../images/GUID-1C6609C6-FC4E-41B2-97FE-AF593AE3826E-low.png) |
| \H*value*; | Changes to the text  height specified in  drawing units | Autodesk \H2;AutoCAD | ![](../images/GUID-4073F948-4448-4856-96E9-68BA81810D78-low.png) |
| \H*valuex*; | Changes the text height  to a multiple of the  current text height | Autodesk \H3x;AutoCAD | ![](../images/GUID-D0704B52-D9C7-412E-A9BE-F222B62FFBF5-low.png) |
| \S...^...; | Stacks the subsequent text at the /, #, or ^ symbol | 1.000\S+0.010^-0.000; | ![](../images/GUID-1F7C3B60-46B7-4D44-BFC4-49035301EE66-low.png) |
| \T*value*; | Adjusts the space between characters. Valid values range from a minimum of .75 to 4 times the original spacing between characters. | \T2;Autodesk | ![](../images/GUID-80C77B8A-F7EA-4EEC-BFD9-36870799E5E6-low.png) |
| \Q*angle*; | Changes obliquing angle | \Q20;Autodesk | ![](../images/GUID-6D96D9FB-1AB6-497A-9CA4-B996A787F43A-low.png) |
| \W*value*; | Changes width factor to produce wide text | \W2;Autodesk | ![](../images/GUID-26DE87FB-4050-4C1A-B3F1-6EE3B4B34ED6-low.png) |
| \A | Sets the alignment value; valid values: 0, 1, 2  (bottom, center, top) | \A1;1\S1/2 | ![](../images/GUID-3D0868AB-9353-4306-8795-185BBC87F4C0-low.png) |
| \P | Ends paragraph | Autodesk\PAutoCAD | ![](../images/GUID-3AD955E2-30E5-41BE-A083-84435EBE8AB7-low.png) |

Braces can be nested up to eight levels deep.

#### Related Concepts

* [About Using an Alternate Text Editor](About-Using-an-Alternate-Text-Editor.md)
* [About Formatting Multiline Text in an Alternate Text Editor](About-Formatting-Multiline-Text-in-an-Alternate-Text-Editor.md)

#### Related Information

* [To Work With an Alternate Text Editor](To-Work-With-an-Alternate-Text-Editor.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*