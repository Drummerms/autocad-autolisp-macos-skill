# DEFLPLSTYLE (System Variable)

Specifies the default plot style for all layers in a drawing when opening a drawing that was created in a release prior to
AutoCAD 2000, or for Layer 0 when creating a new drawing from scratch without using a drawing template.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Registry |
| Initial value: | ByColor |

When the drawing is opened and [PSTYLEPOLICY](PSTYLEPOLICY-System-Variable.md) is set to 1 (color-dependent plot style mode), DEFLPLSTYLE is read-only and has a value of “BYCOLOR.” If PSTYLEPOLICY is
set to 0 (named plot style mode) when the drawing is opened, DEFLPLSTYLE is writable and has a default value of “NORMAL.”

#### Related Concepts

* [About Plot Styles](About-Plot-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*