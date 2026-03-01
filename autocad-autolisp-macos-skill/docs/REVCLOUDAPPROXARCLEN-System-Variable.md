# REVCLOUDAPPROXARCLEN (System Variable)

Stores the current approximate arc length for revision clouds.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Registry |
| Initial value: | 0.0000 |

When REVCLOUDARCVARIANCE is set to 1, the stored value is used to calculate the minimum and maximum arc lengths for revision
clouds.

* Minimum arc length =
  *value* x 2/3
* Maximum arc length =
  *value* x 1 1/3

If REVCLOUDARCVARIANCE is set to 0, the stored value is used as the actual arc length for revision clouds.

#### Related Tasks

* [To Work With Revision Clouds](To-Work-With-Revision-Clouds.md)

#### Related References

* [REVCLOUD (Command)](REVCLOUD-Command.md)

#### Related Concepts

* [About Revision Clouds](About-Revision-Clouds.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*