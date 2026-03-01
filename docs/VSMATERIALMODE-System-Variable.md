# VSMATERIALMODE (System Variable)

Controls the display of materials in the current viewport.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

Turn off the display of materials and textures to maximize performance during unrelated operations.

Turn off the display of textures to modify materials, or to increase performance during unrelated operations.

After turning them off, you can restore the display of materials and textures.

| 0 | No materials are displayed |
| 1 | Materials are displayed, textures are not displayed |
| 2 | Materials and textures are displayed |

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Information

* [About Using Visual Styles](About-Using-Visual-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*