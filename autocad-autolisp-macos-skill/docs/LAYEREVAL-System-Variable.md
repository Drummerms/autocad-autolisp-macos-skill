# LAYEREVAL (System Variable)

Specifies whether the layer list is evaluated for new layers when added to the drawing or to attached xrefs.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

The setting is stored in an integer using one of the following values:

| 0 | Off |
| 1 | Detects when new xref layers have been added in the drawing |
| 2 | Detects when new layers have been added in the drawing and xrefs |

NOTE: [LAYEREVALCTL](LAYEREVALCTL-System-Variable.md) overrides the LAYEREVAL and [LAYERNOTIFY](LAYERNOTIFY-System-Variable.md) setvars when LAYEREVALCTL = 0. It acts like a global off (but not a global on). There is no effect even if LAYEREVALCTL is
turned on if LAYERNOTIFY = 0 or LAYEREVAL = 0. LAYEREVALCTL must be set to 1 for LAYERNOTIFY and LAYEREVAL to function correctly.

#### Related Concepts

* [About Receiving Notification of New Layers](About-Receiving-Notification-of-New-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*