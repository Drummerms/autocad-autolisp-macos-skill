# DIMTM (System Variable)

Sets the minimum (or lower) tolerance limit for dimension text when DIMTOL or DIMLIM is on.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 0.0000 |

DIMTM accepts signed values. If DIMTOL is on and DIMTP and DIMTM are set to the same value, a tolerance value is drawn.

If DIMTM and DIMTP values differ, the upper tolerance is drawn above the lower, and a plus sign is added to the DIMTP value
if it is positive.

For DIMTM, the program uses the negative of the value you enter (adding a minus sign if you specify a positive number and
a plus sign if you specify a negative number).

#### Related Concepts

* [About Displaying Lateral Tolerances](About-Displaying-Lateral-Tolerances.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*