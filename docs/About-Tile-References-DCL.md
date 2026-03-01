# About Tile References (DCL)

Tile references are used to add a tile to your dialog box definition.

Tile references have one of the following syntaxes in a DCL file:

```
name;
```

or

```
: name
{
  attribute = value;
  . . .
}
```

where
*name* is the name of a previously defined tile. Tile names are case sensitive. In the first instance, all the attributes defined
in
*name* are incorporated into the reference. In the second instance, the attribute definitions within the curly braces either supplement
or replace the definitions inherited from
*name*. Because this is a tile reference, as opposed to a definition, the attribute changes apply only to this instance of the tile.

NOTE:The format of the second instance can refer only to prototypes, not to subassemblies.

The
spacer tile is used for layout in a dialog box definition. It has no unique attributes, so references to it specify only its name:

```
spacer;
```

The
ok\_cancel tile defined in
*base.dcl* is a subassembly, so it too can be referenced only by name:

```
ok_cancel;
```

On the other hand, you have the option of redefining the attributes of an individual tile. For example, the following statement
creates a button with the same properties as a previously defined button, but with different text:

```
: retirement_button
{
  label = "Goodbye";
}
```

#### Related References

* [Predefined Tiles and Clusters Reference (DCL)](Predefined-Tiles-and-Clusters-Reference-DCL.md)

#### Related Concepts

* [About Tile Definitions (DCL)](About-Tile-Definitions-DCL.md)
* [About Dialog Box Components (DCL)](About-Dialog-Box-Components-DCL.md)
* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Distributing Tiles in a Cluster (DCL)](About-Distributing-Tiles-in-a-Cluster-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*