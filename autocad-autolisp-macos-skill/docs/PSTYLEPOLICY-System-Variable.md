# PSTYLEPOLICY (System Variable)

Controls the plot style mode, Color-Dependent or Named, that is used when opening a drawing that was created in a release
prior to AutoCAD 2000 or when creating a new drawing from scratch without using a drawing template.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

| 0 | Drawing is set to use named plot styles. The plot style for new objects is set to the default defined in [DEFPLSTYLE](DEFPLSTYLE-System-Variable.md). The plot style for new layers is set to the default defined in [DEFLPLSTYLE](DEFLPLSTYLE-System-Variable.md). |
| 1 | Drawing is set to use color-dependent plot styles. The plot style for an object is based on the object’s color. |

#### Related Concepts

* [About Plot Styles](About-Plot-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*