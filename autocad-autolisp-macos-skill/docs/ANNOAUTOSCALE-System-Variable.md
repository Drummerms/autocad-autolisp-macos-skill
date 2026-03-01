# ANNOAUTOSCALE (System Variable)

Updates annotative objects to support the annotation scale when the annotation scale is changed.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | -4 |

When the value is negative, the autoscale functionality is turned off, but the settings are maintained:

| 0 | Newly set annotation scale is not added to annotative objects. |
| 1 | Adds the newly set annotation scale to annotative objects that support the current scale except for those on layers that are turned off, frozen, locked or that are set to Viewport > Freeze. |
| 2 | Adds the newly set annotation scale to annotative objects that support the current scale except for those on layers that are turned off, frozen, or that are set to Viewport > Freeze. |
| 3 | Adds the newly set annotation scale to annotative objects that support the current scale except for those on layers that are locked. |
| 4 | Adds the newly set annotation scale to all annotative objects that support the current scale. |

#### Related Concepts

* [About Annotation Scale](About-Annotation-Scale.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*