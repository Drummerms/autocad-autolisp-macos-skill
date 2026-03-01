# CELWEIGHT (System Variable)

Sets the lineweight of new objects.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | -1 |

| -1 | Sets the lineweight to "BYLAYER." |
| -2 | Sets the lineweight to "BYBLOCK." |
| -3 | Sets the lineweight to "DEFAULT." "DEFAULT" is controlled by the  [LWDEFAULT](LWDEFAULT-System-Variable.md) system variable. |

Other valid values entered in hundredths of millimeters include 0, 5, 9, 13, 15, 18, 20, 25, 30, 35, 40, 50, 53, 60, 70, 80,
90, 100, 106, 120, 140, 158, 200, and 211.

All values must be entered in hundredths of millimeters. (Multiply a value by 2540 to convert values from inches to hundredths
of millimeters.)

#### Related Concepts

* [About Lineweights](About-Lineweights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*