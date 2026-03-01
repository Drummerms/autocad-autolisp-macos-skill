# XDWGFADECTL (System Variable)

Controls the dimming for all DWG xref objects.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 70 |

The valid XDWGFADECTL system variable value is between -90 and 90. When XDWGFADECTL is set to a negative value, the Xref Fading
feature is not turned on, but the setting is stored.

| 0 | DWG xref objects are not faded. |
| >0 | When the value is positive, controls the percent of fading up to 90 percent. |
| <0 | When the value is negative, xref objects are not faded, but the value is saved for switching to that value by changing the sign. |

#### Related Concepts

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*