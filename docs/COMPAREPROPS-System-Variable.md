# COMPAREPROPS (System Variable)

Controls whether a change in an object's property is identified as a change between two drawings revisions.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 0 |

Based on the value of the sysvar, the corresponding object property changes are included in the drawing comparison as described
in the following table:

| Value | Description |
| 0 | Object property changes are not included in the drawing comparison |
| 1 | Color |
| 2 | Layer |
| 4 | Linetype |
| 8 | Linetype scale |
| 16 | Lineweight |
| 32 | Transparency |
| 64 | Thickness |

To specify more than one property that you want to include in the comparison, enter the sum of their values.

#### Related Tasks

* [To Compare Drawings](To-Compare-Drawings.md)

#### Related References

* [COMPAREHATCH (System Variable)](COMPAREHATCH-System-Variable.md)
* [COMPARERCMARGIN (System Variable)](COMPARERCMARGIN-System-Variable.md)
* [COMPARETEXT (System Variable)](COMPARETEXT-System-Variable.md)
* [COMPARETOLERANCE (System Variable)](COMPARETOLERANCE-System-Variable.md)

#### Related Concepts

* [About Comparing Differences Between Drawings](About-Comparing-Differences-Between-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*