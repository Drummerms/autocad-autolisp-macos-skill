# About Distributing Tiles in a Cluster (DCL)

When laying out tiles in a dialog box, you need to arrange them into rows and columns based on the relative size of each tile.

The following DCL defines a row of three tiles that runs along the top of another tile:

```
: column {
  : row {
    : compact_tile {
    }
    : compact_tile {
    }
    : compact_tile {
    }
  }
  : large_tile {
  }
}
```

If the
compact\_tile components have
fixed\_width and the
large\_tile is wider than the minimum space required by the row of
compact\_tiles above it, the default horizontal alignment of this assembly appears as follows:

![](../images/GUID-015AD087-075F-4643-99DD-57A17871BB3F-low.png)

The leading edge of the first
compact\_tile in the row aligns with the leading edge of the
large\_tile, and the trailing edge of the last
compact\_tile aligns with the trailing edge of the
large\_tile. Tiles in between are distributed evenly. The situation with adjoining columns is analogous.

You can control the default distribution by using the
spacer\_0 and
spacer\_1 tiles, which are variants of the
spacer tile defined in
*base.dcl*.

#### Related Concepts

* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Adjusting the Space Between Tiles (DCL)](About-Adjusting-the-Space-Between-Tiles-DCL.md)
* [About Adjusting Space along the Right Side or Bottom of a Dialog Box (DCL)](About-Adjusting-Space-along-the-Right-Side-or-Bottom-of-a-Dialog-Box-DCL.md)
* [About Fixing the Spacing Around a Boxed Row or Column (DCL)](About-Fixing-the-Spacing-Around-a-Boxed-Row-or-Column-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*