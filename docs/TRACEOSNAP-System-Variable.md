# TRACEOSNAP (System Variable)

Controls whether object snaps apply to trace geometry while viewing a trace.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 |

When trace geometry consists of low fidelity markups, supporting osnaps on trace geometry while viewing a trace may make it
more difficult to update the host drawing's geometry. But when viewing high fidelity geometry in traces, osnaps may be useful.

NOTE:TRACEOSNAP only applies when TRACEBACK is on (TRACEMODE=1). When TRACEFRONT is on, (TRACEMODE=2), object snaps always apply
to trace geometry.

| Value | Description |
| 0 | Object snaps to trace geometry are disabled when viewing a trace |
| 1 | Object snaps to trace geometry are enabled when viewing a trace |

#### Related Information

* [About Trace](About-Trace.md)
* [Working With Trace](Working-With-Trace.md)
* [Commands for Working With Trace](Commands-for-Working-With-Trace.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*