# OSMODE (System Variable)

Sets running object snaps

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 4133 |

The setting is stored as a bitcode using the sum of the following values:

| 0 | NONe |
| 1 | ENDpoint |
| 2 | MIDpoint |
| 4 | CENter |
| 8 | NODe |
| 16 | QUAdrant |
| 32 | INTersection |
| 64 | INSertion |
| 128 | PERpendicular |
| 256 | TANgent |
| 512 | NEArest |
| 1024 | Geometric CEnter |
| 2048 | APParent Intersection |
| 4096 | EXTension |
| 8192 | PARallel |
| 16384 | Suppresses the current running object snaps |

To specify more than one object snap, enter the sum of their values. For example, entering 3 specifies the Endpoint (bitcode
1) and Midpoint (bitcode 2) object snaps. Entering 16383 specifies all object snaps.

When object snaps are switched off using the Osnap button on the status bar, a bitcode of 16384 (0x4000) is returned, in addition
to the normal value of OSMODE. With this additional value, developers can distinguish this mode from Object Snap modes that
have been turned off from within the Drafting Settings dialog box. Setting this bit toggles running object snaps off. Setting
OSMODE to a value with this bit off toggles running object snaps on.

#### Related Concepts

* [About Using Object Snaps](About-Using-Object-Snaps.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*