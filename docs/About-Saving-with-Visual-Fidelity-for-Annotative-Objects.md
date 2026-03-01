# About Saving with Visual Fidelity for Annotative Objects

When working with annotative objects, you can maintain visual fidelity for these objects when viewed in AutoCAD 2007-based
products and earlier releases. Visual fidelity is controlled by the SAVEFIDELITY system variable.

If you work primarily in model space, it is recommended that you turn off visual fidelity. However, if you need to exchange
drawings with other users, and layout fidelity is most important, then visual fidelity should be turned on (set SAVEFIDELITY
to 1).

Annotative objects may have multiple scale representations. When visual fidelity is on, annotative objects are decomposed
and scale representations are saved, as anonymous blocks, to separate layers. These layer names are based on their original
layer and appended with a number. If you explode the block in a 2007 or earlier AutoCAD-based product and subsequently open
that drawing in a 2008 or later AutoCAD-based product, each scale representation becomes a separate annotative object with
each at one annotation scale.

#### Related Information

* [About Saving Drawings](About-Saving-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*