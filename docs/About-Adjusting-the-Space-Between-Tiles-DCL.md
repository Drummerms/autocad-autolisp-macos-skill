# About Adjusting the Space Between Tiles (DCL)

By default, tiles located within a column are distributed vertically to take advantage of all available space.

If two adjoining columns differ greatly in the amount of space their tiles occupy, then the tiles in the column that needs
less space may appear to be distributed too far apart. Setting the
fixed\_height attribute of a column to
true restricts the tiles within a column to only use the amount of space that is really needed. This improves the appearance of
the tiles in the dialog box.

The following illustrations show the results of two columns tiles and how the
fixed\_height attribute can affect vertical tile distribution:

![](../images/GUID-22CF5669-5D4B-415D-A934-84516670A646-low.png)

The columns in both illustrations have their
fixed\_height attributes set to false, with the exception of the rightmost column in the illustration on the right. The rightmost column’s
fixed\_height attribute is set to
true, this reduces the height of the column so it is just large enough to contain the tiles in its definition.

The following dialog definition represents the illustration on the right:

```
sampleColumns : dialog {
  label = "Sample Columns Dialog Box";
  : row {
    : column {
      : button {
        key = "btn1";
        label = "Button1";
        is_default = true;
        fixed_width = true;
        height = 20;
      }
    }

    : column {
      fixed_height = true;
      alignment = top;

      : button {
        key = "btn2";
        label = "Button2";
        fixed_width = true;
      }
      : button {
        key = "btn3";
        label = "Button3";
        fixed_width = true;
      }
    }
  }
}
```

#### Related Concepts

* [About Adjusting Space along the Right Side or Bottom of a Dialog Box (DCL)](About-Adjusting-Space-along-the-Right-Side-or-Bottom-of-a-Dialog-Box-DCL.md)
* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Fixing the Spacing Around a Boxed Row or Column (DCL)](About-Fixing-the-Spacing-Around-a-Boxed-Row-or-Column-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*