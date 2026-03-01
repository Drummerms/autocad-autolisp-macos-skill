# About Tile Definitions (DCL)

Tile definitions are used to create new prototypes or subassemblies that can be used in your dialog boxes.

Tile definitions have the following syntax:

```
name : item1 [ : item2 : item3 ... ]
{
  attribute = value;
  ...
}
```

where each item is a previously defined tile. The new tile (*name*) inherits the attributes of all the specified tiles (*item1*,
*item2*,
*item3*, …). The attribute definitions within the curly braces ( *{}* ) either supplement, or, if the attribute's name is identical, replace the inherited definitions. When the definition has
multiple parents, attributes take precedence in left-to-right order. In other words, if more than one item specifies the same
attribute, the first one encountered is the one used.

If the new definition contains no children, it is a prototype, and you can alter or augment its attributes when referring
to it. If it is a subassembly with children, its attributes cannot be altered.

The name of a tile or tile prototype can contain only letters, numbers, or the underscore character ( *\_* ), and must begin with a letter.

NOTE:Tile names are case-sensitive. For example,
bigbutton is not the same as
BigButton or
BIGBUTTON. Be careful when using capitalization.

This is the (internal) definition of a button:

```
button : tile
{
  fixed_height = true;
  is_tab_stop = true;
}
```

The
*base.dcl* file defines a
default\_button as follows:

```
default_button : button
{
  is_default = true;
}
```

The
default\_button inherits the button tile's values for the
fixed\_height and
is\_tab\_stop attributes. It adds a new attribute,
is\_default, and sets it to
true.

#### Related References

* [Predefined Tiles and Clusters Reference (DCL)](Predefined-Tiles-and-Clusters-Reference-DCL.md)

#### Related Concepts

* [About Tile References (DCL)](About-Tile-References-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [About Dialog Box Components (DCL)](About-Dialog-Box-Components-DCL.md)
* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*