# DIMZIN (System Variable)

Controls the suppression of zeros in the primary unit value.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 (imperial) or 8 (metric) |

Values 0-3 affect feet-and-inch dimensions only:

| 0 | Suppresses zero feet and precisely zero inches |
| 1 | Includes zero feet and precisely zero inches |
| 2 | Includes zero feet and suppresses zero inches |
| 3 | Includes zero inches and suppresses zero feet |
| 4 | Suppresses leading zeros in decimal dimensions (for example, 0.5000 becomes .5000) |
| 8 | Suppresses trailing zeros in decimal dimensions (for example, 12.5000 becomes 12.5) |
| 12 | Suppresses both leading and trailing zeros (for example, 0.5000 becomes .5) |

DIMZIN also affects real-to-string conversions performed by the AutoLISP  *rtos*  and  *angtos*  functions.

#### Related Concepts

* [About Suppressing Zeros in Dimensions](About-Suppressing-Zeros-in-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*