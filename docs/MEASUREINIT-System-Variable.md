# MEASUREINIT (System Variable)

Controls whether a drawing you start from scratch uses imperial or metric default settings.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | Varies by country/region |

Specifically, MEASUREINIT controls which hatch pattern and linetype files are used. The
*Drawing1.dwg* that opens when you start the program is a drawing that is started from scratch.

| Value | Description |
| 0 | Imperial; uses the hatch pattern file and linetype file designated by the ANSIHatch and ANSILinetype registry settings |
| 1 | Metric; uses the hatch pattern file and linetype file designated by the ISOHatch and ISOLinetype registry settings |

#### Related Concepts

* [About Drawings and Templates](About-Drawings-and-Templates.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*