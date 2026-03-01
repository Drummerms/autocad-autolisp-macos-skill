# LAYLOCKFADECTL (System Variable)

Controls the amount of fading for objects on locked layers.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 50 |

Fades the objects on locked layers to contrast them with objects on unlocked layers and reduces the visual complexity of a
drawing. Objects on locked layers are still visible for reference and for object snapping.

![](../images/GUID-D367EED7-7395-4520-BAD3-7C744CE8913D-low.gif)

The range for controlling the fading for objects on locked layers is from -90 to 90.

| 0 | Locked layers are not faded |
| >0 | When the value is positive, controls the percent of fading up to 90 percent |
| <0 | When the value is negative, locked layers are not faded, but the value is saved for switching to that value by changing the sign |

NOTE:The fading value is limited to 90 percent to avoid confusion with layers that are turned off or frozen.

#### Related Tasks

* [To Lock or Unlock a Layer](To-Lock-or-Unlock-a-Layer.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*