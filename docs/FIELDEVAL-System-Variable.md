# FIELDEVAL (System Variable)

Controls how fields are updated.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 31 |

The setting is stored as a bitcode using the sum of the following values:

| 0 | Not updated |
| 1 | Updated on open |
| 2 | Updated on save |
| 4 | Updated on plot |
| 8 | Not used |
| 16 | Updated on regeneration |

NOTE:The Date field is updated by [UPDATEFIELD](UPDATEFIELD-Command.md), but it is not updated automatically based on the setting of the FIELDEVAL system variable.

#### Related Information

* [About Using Fields in Text](About-Using-Fields-in-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*