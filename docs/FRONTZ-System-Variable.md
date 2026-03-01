# FRONTZ (System Variable)

Stores the front clipping plane offset from the target plane for the current viewport, in drawing units.

(Read-only)

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 0.0000 |

The *front clipping* and *front clip not at eye* bitcodes in [VIEWMODE](VIEWMODE-System-Variable.md) are on. The FRONTZ value is the last front clipping plane value set current with the DVIEW command. The distance of the front
clipping plane from the camera point is found by subtracting FRONTZ from the camera-to-target distance.

#### Related Concepts

* [About Creating a 3D Dynamic View](About-Creating-a-3D-Dynamic-View.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*