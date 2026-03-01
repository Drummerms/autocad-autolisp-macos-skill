# DEMANDLOAD (System Variable)

Specifies if and when to demand-load certain applications.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 3 |

If you set this system variable to 0, third-party applications and some AutoCAD commands cannot function.

| 0 | Turns off demand-loading. |
| 1 | Demand-loads the source application when you open a drawing that contains custom objects. This setting does not demand-load the application when you invoke one of the application's commands. |
| 2 | Demand-loads the source application when you invoke one of the application's commands. This setting does not demand-load the application when you open a drawing that contains custom objects. |
| 3 | Demand-loads the source application when you open a drawing that contains custom objects or when you invoke one of the application's commands |

#### Related Concepts

* [About Improving Performance When Using Xrefs](About-Improving-Performance-When-Using-Xrefs.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*