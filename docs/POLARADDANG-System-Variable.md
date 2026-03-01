# POLARADDANG (System Variable)

Stores additional angles for polar tracking and polar snap.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Registry |
| Initial value: | "" |

You can add up to 10 angles. Each angle can be separated with semicolons (;). The AUNITS system variable sets the format for
display of angles.Unlike POLARANG, POLARADDANG angles do not result in multiples of their values.

The bit value for the POLARMODE system variable must have 4 turned on for POLARADDANG to have an effect.

When using fractions of an angle, set the AUPREC system variable (angular precision) to a higher value. Otherwise, the POLARADDANG
value will be rounded off.

#### Related Concepts

* [About Polar Tracking and PolarSnap](About-Polar-Tracking-and-PolarSnap.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*