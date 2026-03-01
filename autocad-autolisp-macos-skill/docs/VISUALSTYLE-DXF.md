# VISUALSTYLE (DXF)

The following group codes apply to VISUALSTYLE objects.

| VISUALSTYLE group codes | |
| Group code | Description |
| 0 | Object name (VISUALSTYLE) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group, always “}” |
| 330 | Soft-owner ID/handle to owner object |
| 100 | Subclass marker (AcDbVisualStyle) |
| 2 | Description |
| 70 | Type |
| 71 | Face lighting model  0 =Invisible  1 = Visible  2 = Phong  3 = Gooch |
| 72 | Face lighting quality  0 = No lighting  1 = Per face lighting  2 = Per vertex lighting |
| 73 | Face color mode  0 = No color  1 = Object color  2 = Background color  3 = Custom color  4 = Mono color  5 = Tinted  6 = Desaturated |
| 90 | Face modifiers  0 = No modifiers  1 = Opacity  2 = Specular |
| 40 | Face opacity level |
| 41 | Face specular level |
| 62, 63 | Color |
| 421 | Face style mono color |
| 74 | Edge style model  0 = No edges  1 = Isolines  2 = Facet edges |
| 91 | Edge style |
| 64 | Edge intersection color |
| 65 | Edge obscured color |
| 75 | Edge obscured linetype |
| 175 | Edge intersection linetype |
| 42 | Edge crease angle |
| 92 | Edge modifiers |
| 66 | Edge color |
| 43 | Edge opacity level |
| 76 | Edge width |
| 77 | Edge overhang |
| 78 | Edge jitter |
| 67 | Edge silhouette color |
| 79 | Edge silhouette width |
| 170 | Edge halo gap |
| 171 | Number of edge isolines |
| 290 | Edge hide precision flag |
| 174 | Edge style apply flag |
| 93 | Display style display settings |
| 44 | Brightness |
| 173 | Shadow type |
| 291 | Internal use only flag |

#### Related References

* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*