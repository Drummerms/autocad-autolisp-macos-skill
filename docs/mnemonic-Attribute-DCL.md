# mnemonic Attribute (DCL)

Specifies a keyboard mnemonic character for the tile.

*Supported Platforms:* Windows only

```
mnemonic = "char";
```

The mnemonic is underlined in the tile's label. A possible value is a quoted string of a single character (no default). The
character must be one of the letters in the tile's label. The character does not have to be unique to the dialog box. If more
than one tile has the same mnemonic, the user presses that key to cycle through the tiles sequentially.

From the user's point of view, mnemonics are not case-sensitive. For example, if a button's mnemonic character is
*A*,entering either
*a* or
*A* gives the A button focus. However, in the DCL file the mnemonic must be one of the characters in the tile's label, and it
must be capitalized as it appears in the
label string.

NOTE:On Mac OS, use the
label attribute to specify a mnemonic character. This same technique can also be used on Windows.

Mnemonics change focus. If the user specifies a mnemonic key for a tile that contains a group of items, such as a cluster
or a list box, the focus is put on the first item in the tile that is a tab stop. Any active tile is a tab stop unless its
is\_tab\_stop attribute is set to
false.

NOTE:The
is\_tab\_stop attribute is supported on Windows only.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows

#### Related Concepts

* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*