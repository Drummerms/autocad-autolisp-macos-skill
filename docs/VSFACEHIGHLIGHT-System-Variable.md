# VSFACEHIGHLIGHT (System Variable)

Controls the display of specular highlights on faces without materials in the current viewport.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | -30 |

The range is -100 to 100. The higher the number, the larger the highlight. Objects with materials attached ignore the setting
of VSFACEHIGHLIGHT when [VSMATERIALMODE](VSMATERIALMODE-System-Variable.md) is on.

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [Shade and Color Faces](Shade-and-Color-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*