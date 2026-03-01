# DIMAPOST (System Variable)

Specifies a text prefix or suffix (or both) to the alternate dimension measurement for all types of dimensions except angular.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | "" |

For instance, if the current units are Architectural,  [DIMALT](DIMALT-System-Variable.md) is on,  [DIMALTF](DIMALTF-System-Variable.md) is 25.4 (the number of millimeters per inch),  [DIMALTD](DIMALTD-System-Variable.md) is 2, and DIMAPOST is set to "mm", a distance of 10 units would be displayed as 10"[254.00mm].

To turn off an established prefix or suffix (or both), set it to a single period (.).

#### Related Concepts

* [About Controlling the Display of Dimension Units](About-Controlling-the-Display-of-Dimension-Units.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*