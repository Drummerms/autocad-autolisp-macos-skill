# About Adjusting the Layout of Dialog Boxes (DCL)

By default, tiles automatically resize to fit almost the full width of a dialog box.

![](../images/GUID-ED973896-78CF-4B4C-AD54-FF9E986E686B-low.png)

In the previous illustration, the OK button occupies almost the full width of the dialog box. The DCL file for the dialog
box looks like:

```
hello : dialog {
  label = "Sample Dialog Box";
  : text {
    label = "Hello, world";
  }:
  button {
    key = "accept";
    label = "OK";
    is_default = true;
  }
}
```

You can edit the DCL file to improve the appearance of the dialog box by adding the
fixed\_width and
alignment attributes to the button tile. Setting the
fixed\_width attribute to
true prevents the button from filling the available space and causes the button's border to shrink so that it is just slightly
wider than the text inside. Setting the
alignment attribute to
centered forces the button to be centered in the middle of the dialog box. By default, tiles in a column are left-justified.

![](../images/GUID-2CE5C940-4F8B-41DB-A613-C90492877EDD-low.png)

The revised DCL file would be as follows:

```
hello : dialog {
  label = "Sample Dialog Box";
  : text {
    label = "Hello, world";
  }:
  button {
    key = "accept";
    label = "OK";
    is_default = true;
    fixed_width = true;
    alignment = centered;
  }
}
```

#### Topics in this section

* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
  
  When laying out tiles in a dialog box, you need to arrange them into rows and columns based on the relative size of each tile.

* [About Adjusting the Space Between Tiles (DCL)](About-Adjusting-the-Space-Between-Tiles-DCL.md)
  
  By default, tiles located within a column are distributed vertically to take advantage of all available space.

* [About Adjusting Space along the Right Side or Bottom of a Dialog Box (DCL)](About-Adjusting-Space-along-the-Right-Side-or-Bottom-of-a-Dialog-Box-DCL.md)
  
  A dialog box may contain unused space along its right side or bottom.

* [About Fixing the Spacing Around a Boxed Row or Column (DCL)](About-Fixing-the-Spacing-Around-a-Boxed-Row-or-Column-DCL.md)
  
  If the label attribute of a boxed row or column is either blank (
  " "
  ) or null (
  ""
  ), the box encloses the cluster but no text is shown.

* [About Customizing Exit Buttons (DCL)](About-Customizing-Exit-Buttons-DCL.md)
  
  You may want to change the text of one of the exit buttons for some dialog boxes.

#### Related Concepts

* [About Adjusting Space along the Right Side or Bottom of a Dialog Box (DCL)](About-Adjusting-Space-along-the-Right-Side-or-Bottom-of-a-Dialog-Box-DCL.md)
* [About Adjusting the Space Between Tiles (DCL)](About-Adjusting-the-Space-Between-Tiles-DCL.md)
* [About Fixing the Spacing Around a Boxed Row or Column (DCL)](About-Fixing-the-Spacing-Around-a-Boxed-Row-or-Column-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*