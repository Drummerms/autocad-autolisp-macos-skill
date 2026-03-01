# LAYERNOTIFY (System Variable)

Specifies when an alert displays when unreconciled new layers are found.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Drawing |
| Initial value: | 0 |

| 0 | Off |
| 1 | Plot |
| 2 | Open |
| 4 | Load/Reload/Attach for xrefs |
| 8 | Restore layer state |
| 16 | Save |
| 32 | Insert |

NOTE:[LAYEREVALCTL](LAYEREVALCTL-System-Variable.md) overrides the [LAYEREVAL](LAYEREVAL-System-Variable.md) and LAYERNOTIFY setvars when LAYEREVALCTL = 0. It acts like a global off (but not a global on). There is no effect even if
LAYEREVALCTL is turned on if LAYERNOTIFY = 0 or LAYEREVAL = 0. LAYEREVALCTL must be set to 1 for LAYERNOTIFY and LAYEREVAL
to function correctly.

#### Related Concepts

* [About Receiving Notification of New Layers](About-Receiving-Notification-of-New-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*