# DIMTVP (System Variable)

Controls the vertical position of dimension text above or below the dimension line.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 0.0000 |

The DIMTVP value is used when DIMTAD is off. The magnitude of the vertical offset of text is the product of the text height
and DIMTVP. Setting DIMTVP to 1.0 is equivalent to setting DIMTAD to on. The dimension line splits to accommodate the text
only if the absolute value of DIMTVP is less than 0.7.

#### Related Concepts

* [About Fitting Dimension Text Within Extension Lines](About-Fitting-Dimension-Text-Within-Extension-Lines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*