# EDGEMODE (System Variable)

Controls how the TRIM and EXTEND commands determine cutting and boundary edges.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 |

| 0 | Uses the selected edge without any extensions |
| 1 | Extends or trims the selected object to an imaginary extension of the cutting or boundary edge |

Lines, arcs, elliptical arcs, rays, and polylines are objects eligible for natural extension. The natural extension of a line
or ray is an unbounded line (xline), an arc is a circle, and an elliptical arc is an ellipse. A polyline is broken down into
its line and arc components, which are extended to their natural boundaries.

#### Related Concepts

* [About Trimming and Extending Objects](About-Trimming-and-Extending-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*