# SAFEMODE (System Variable)

Indicates whether executable code can be loaded and executed in the current AutoCAD session.

(Read-only)

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

This system variable is controlled by the /safemode (Windows) or -safemode (Mac OS) startup switch, which should be used
only in emergency situations for disabling malicious code.

| 0 | Allows executable code to be executed |
| 1 | Prevents executable code from being executed |

NOTE:Disabling executable code will prevent some AutoCAD command tools from running. It will also prevent executing AutoLISP expressions
at the Command prompt. On Windows only, Express Tools are also disabled when safe mode is active.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*