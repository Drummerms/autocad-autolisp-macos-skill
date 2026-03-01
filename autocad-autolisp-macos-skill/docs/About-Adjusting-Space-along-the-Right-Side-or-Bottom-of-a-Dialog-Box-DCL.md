# About Adjusting Space along the Right Side or Bottom of a Dialog Box (DCL)

A dialog box may contain unused space along its right side or bottom.

You can define a
text tile and explicitly specify a width greater than the width required by its current value. For example, the following defines
a tile that does not display anything (its value is
null) until an application sets its value:

```
: text {
  key = "l_text";
  width = 18;
  fixed_width = true;
}
```

In the previous example, the
width attribute reserves space for 18 characters in the dialog box. The application can add text with a statement like the following:

```
(set_tile "l_text" "Bylayer")
```

Because "Bylayer" does not need all 18 characters, the dialog box has surplus space along its right side. A similar situation
occurs when displaying an error message with an
errtile. Unless an error message is currently shown, it looks as if there is extra space at the bottom of the dialog box. In this
case, an extra
spacer tile at the top of the dialog box can help balance the vertical layout.

#### Related Concepts

* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Adjusting the Space Between Tiles (DCL)](About-Adjusting-the-Space-Between-Tiles-DCL.md)
* [About Fixing the Spacing Around a Boxed Row or Column (DCL)](About-Fixing-the-Spacing-Around-a-Boxed-Row-or-Column-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*