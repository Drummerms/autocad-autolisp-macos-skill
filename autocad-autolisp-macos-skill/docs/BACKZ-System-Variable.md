# BACKZ (System Variable)

Stores the back clipping plane offset from the target plane for the current viewport, in drawing units.

(Read-only)

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 0.0000 |

Meaningful only if clipping is specified in [DVIEW](DVIEW-Command.md). If there are several cameras, the value is the last back clipping plane that you set current. The distance of the back clipping
plane from the camera point can be found by subtracting BACKZ from the camera-to-target distance.

#### Related Concepts

* [About Creating a 3D Dynamic View](About-Creating-a-3D-Dynamic-View.md)

#### Related Information

* [About Defining a Parallel Projection](About-Defining-a-Parallel-Projection.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*