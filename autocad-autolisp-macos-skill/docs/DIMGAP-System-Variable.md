# DIMGAP (System Variable)

Sets the distance around the dimension text when the dimension line breaks to accommodate dimension text.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 0.0900 (imperial) or 0.6250 (metric) |

Also sets the gap between annotation and a hook line created with the LEADER command. If you enter a negative value, DIMGAP
places a box around the dimension text.

DIMGAP is also used as the minimum length for pieces of the dimension line. When the default position for the dimension text
is calculated, text is positioned inside the extension lines only if doing so breaks the dimension lines into two segments
at least as long as DIMGAP. Text placed above or below the dimension line is moved inside only if there is room for the arrowheads,
dimension text, and a margin between them at least as large as DIMGAP: 2 \* ([DIMASZ](DIMASZ-System-Variable.md) + DIMGAP).

#### Related Information

* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*