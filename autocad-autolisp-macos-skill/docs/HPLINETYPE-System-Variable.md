# HPLINETYPE (System Variable)

Controls how non-continuous linetypes are displayed in hatch patterns.

|  |  |
| --- | --- |
| Type: | Switch |
| Saved in: | Registry |
| Initial value: | 0 |

Performance and memory enhancements for hatches were added in AutoCAD 2015-based products. Hatch patterns using non-continuous
linetypes do not benefit from these enhancements. It is recommended that you choose a predefined hatch pattern that was defined
with a non-continuous linetype, rather than assigning a non-continuous linetype to a hatch pattern.

| Value | Description |
| 0 | Displays continuous linetypes in predefined and custom hatch patterns, regardless of the assigned linetype |
| 1 | Displays non-continuous linetypes in hatch patterns (legacy behavior) |

NOTE:Use the REGEN command to update the linetype display of existing hatch patterns.

#### Related Tasks

* [To Hatch or Fill Objects or Areas](To-Hatch-or-Fill-Objects-or-Areas.md)
* [To Create an Unbounded Hatch](To-Create-an-Unbounded-Hatch.md)

#### Related References

* [HATCH (Command)](HATCH-Command.md)
* [Hatch Visor](Hatch-Visor.md)
* [HPMAXLINES (System Variable)](HPMAXLINES-System-Variable.md)
* [OSOPTIONS (System Variable)](OSOPTIONS-System-Variable.md)

#### Related Concepts

* [Hatch and Gradient Dialog Box](Hatch-and-Gradient-Dialog-Box.md)
* [-HATCH (Command)](HATCH-Command-2.md)
* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)
* [About Hatch Islands](About-Hatch-Islands.md)
* [About Hatch Pattern Scaling](About-Hatch-Pattern-Scaling.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*