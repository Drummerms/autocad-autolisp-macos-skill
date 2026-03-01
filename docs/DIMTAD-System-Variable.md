# DIMTAD (System Variable)

Controls the vertical position of text in relation to the dimension line.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 (imperial) or 1 (metric) |

| 0 | Centers the dimension text between the extension lines. |
| 1 | Places the dimension text above the dimension line except when the dimension line is not horizontal and text inside the extension lines is forced horizontal ([DIMTIH](DIMTIH-System-Variable.md) = 1). The distance from the dimension line to the baseline of the lowest line of text is the current [DIMGAP](DIMGAP-System-Variable.md) value. |
| 2 | Places the dimension text on the side of the dimension line farthest away from the defining points. |
| 3 | Places the dimension text to conform to Japanese Industrial Standards (JIS). |
| 4 | Places the dimension text below the dimension line. |

#### Related Concepts

* [About Fitting Dimension Text Within Extension Lines](About-Fitting-Dimension-Text-Within-Extension-Lines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*