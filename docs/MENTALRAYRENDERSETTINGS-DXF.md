# MENTALRAYRENDERSETTINGS (DXF)

The following group codes are used by MENTALRAYRENDERSETTINGS objects.

NOTE:Starting with AutoCAD 2016-based products on Windows and AutoCAD 2017 on Mac OS, the MentalRay feature set is no longer available
for use but the data is retained in the drawing file for backwards compatibility.

| MENTALRAYRENDERSETTINGS group codes | |
| Group code | Description |
| 0 | Object name (MENTALRAYRENDERSETTINGS) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary |
| 102 | End of persistent reactors group; always “}” |
| 100 | Subclass marker (AcDbRenderSettings) |
| 90 | Class version 1 |
| 1 | Render preset name |
| 290 | Render materials flag |
| 90 | Texture sampling quality |
| 290 | Render back-faces flag |
| 290 | Render shadows flag |
| 1 | Preview image file name(can be blank) |
| 100 | Subclass marker (AcDbMentalRayRenderSettings) |
| 90 | Class version 1 |
| 90 | Sampling rate (minimum) |
| 90 | Sampling rate (maximum) |
| 70 | Sampling filter type  0 = Box  1 = Triangle  2 = Gauss  3 = Mitchell  4 = Lanczos |
| 40, 40 | Filter width, height |
| 40, 40, 40, 40 | Sampling contrast color; Red, green, blue, and alpha channel values |
| 70 | Shadow mode  0 = Simple  1 = Sort  2 = Segment |
| 290 | Shadow map flag; applies only to lights using mapped shadows |
| 290 | Ray tracing flag |
| 90, 90, 90 | Ray tracing depth for reflections, refractions, and maximum depth |
| 290 | Global illumination flag |
| 90 | Photons/sample count |
| 290 | Global illumination radius flag |
| 40 | Global illumination sample radius |
| 90 | Photons per light |
| 90, 90, 90 | Global illumination photo trace depth for reflections, refractions, and maximum depth |
| 290 | Final gather flag |
| 90 | Final gather ray count |
| 290, 290 | Final gather minimum and maximum radius flags |
| 290 | Final gather pixels flag |
| 40, 40 | Final gather minimum and maximum sample radius |
| 40 | Luminance scale (energy multiplier) |
| 70 | Diagnostic mode  0 = Off  1 = Grid  2 = Photon  4 = BSP |
| 70 | Diagnostic Grid mode  0 = Object  1 = World  2 = Camera |
| 40 | Grid size |
| 70 | Diagnostic Photon mode  0 = Density  1 = Irradiance |
| 70 | Diagnostic BSP mode  0 = Depth  1 = Size |
| 290 | Export MI statistics flag |
| 1 | MI statistics file name (can be blank) |
| 90 | Tile size |
| 70 | Tile order  0 = Hilbert  1 = Spiral  2 = Left to right  3 = Right to left  4 = Top to bottom  5 = Bottom to top |
| 90 | Memory limit |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [RENDER (DXF)](RENDER-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*