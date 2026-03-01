# About Customizing Arrowheads

You can create your own custom arrowheads.

Arrowheads are stored as block definitions. To use your own arrowhead, provide the name of a block definition.

NOTE:Annotative blocks cannot be used as custom arrowheads for dimensions or leaders.

Arrowhead sizing relies on the overall dimension scale factor. When you create a dimension, the block is inserted where the
arrowheads would normally go. The object's *X* and *Y* scale factors are set to *arrowhead size* *overall scale*. The dimension line is trimmed by *text gap x overall scale* units at each end. To trim the dimension line, the rightmost block is inserted with a zero rotation angle for horizontal
dimensioning. The leftmost block is rotated 180 degrees about its insertion point.

NOTE:The insertion point a block is defined with affects its placement as a custom arrowhead on a dimension or leader.

If you use paper-space scaling, the scale factor is computed before applying it to the arrowhead size value.

#### Related Tasks

* [To Use a Custom Arrowhead](To-Use-a-Custom-Arrowhead.md)
* [To Flip the Direction of an Arrowhead](To-Flip-the-Direction-of-an-Arrowhead.md)

#### Related Concepts

* [About Controlling Arrowheads](About-Controlling-Arrowheads.md)
* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*