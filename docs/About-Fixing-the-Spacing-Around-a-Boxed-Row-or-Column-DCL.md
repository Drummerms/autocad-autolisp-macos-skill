# About Fixing the Spacing Around a Boxed Row or Column (DCL)

If the label attribute of a boxed row or column is either blank ( *" "* ) or null ( *""* ), the box encloses the cluster but no text is shown.

A single blank does not appear as a space in the box. However, there is a difference in the way blank and null labels are
laid out:

* If the label is a single blank, any vertical space the text occupied inside the box is lost, but any vertical space the label
  occupied above the box is not lost.
* If the label is a null string, all vertical space is lost, whether above the box or inside it.

In the following DCL code, the top lines of the boxes around the first two columns are guaranteed to line up (with the same
*Y* location), and the top line of the box around the third column is guaranteed to have no spacing above or below it, except
for the default margins:

```
: row {
  : boxed_column {
    label = "Some Text";
  }
  : boxed_column {
    label = " ";         // single blank: the default
  }
  : boxed_column {
    label = "";          // null string
  }
}
```

#### Related Concepts

* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Adjusting the Space Between Tiles (DCL)](About-Adjusting-the-Space-Between-Tiles-DCL.md)
* [About Adjusting Space along the Right Side or Bottom of a Dialog Box (DCL)](About-Adjusting-Space-along-the-Right-Side-or-Bottom-of-a-Dialog-Box-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*