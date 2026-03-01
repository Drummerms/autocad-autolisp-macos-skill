# SSMSHEETSTATUS (System Variable)

Controls how the status data in a sheet set is refreshed.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

The status data for sheets in the current sheet set includes whether a sheet is locked and whether a sheet is missing (or
found in an unexpected location). This status data can be updated automatically for all sheets.

| 0 | Do not automatically refresh the status data in a sheet set |
| 1 | Refresh the status data when the sheet set is loaded or updated |
| 2 | Refresh the status data when the sheet set is loaded or updated, or at a time interval set by [SSMPOLLTIME](SSMPOLLTIME-System-Variable.md) |

#### Related Information

* [About Sheet Sets](About-Sheet-Sets.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*