# LAYEREVALCTL (System Variable)

Controls the overall Unreconciled New Layer filter list in Layers palette which is evaluated for new layers.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | User-settings |
| Initial value: | 1 |

This system variable also affects whether the new layer notification is displayed or not.

| 0 | Disables the evaluation and notification of new layers |
| 1 | Enables the evaluation of new layers on LAYEREVAL settings in DWG file |

NOTE:LAYEREVALCTL overrides the [LAYEREVAL](LAYEREVAL-System-Variable.md) and [LAYERNOTIFY](LAYERNOTIFY-System-Variable.md) setvars when LAYEREVALCTL = 0. It acts like a global off (but not a global on). There is no effect even if LAYEREVALCTL is
turned on if LAYERNOTIFY = 0 or LAYEREVAL = 0. LAYEREVALCTL must be set to 1 for LAYERNOTIFY and LAYEREVAL to function correctly.

#### Related Concepts

* [About Receiving Notification of New Layers](About-Receiving-Notification-of-New-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*