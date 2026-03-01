# label Attribute (DCL)

Specifies the text displayed within the tile.

*Supported Platforms:* Windows, Mac OS, and Web

```
label = "string";
```

Possible value is a quoted string (default: a blank string,
""). The placement of
label text is tile-specific.

The label attribute can specify a mnemonic character for the tile. The mnemonic is underlined in the tile's label.

Any character in a label string that is preceded by an ampersand (&) becomes the mnemonic. The character doesn't have to be unique to the dialog box. If more than one tile has the same mnemonic,
the user presses that key to cycle through the tiles sequentially.

NOTE:On Windows only, the
mnemonic attribute can also be used to specify a mnemonic character.

Mnemonics change focus but do not select a tile. If the user specifies a mnemonic key for a tile that contains a group of
items, such as a cluster or a list box, the focus is put on the first item in the tile that is a tab stop. Any active tile
is a tab stop unless its
is\_tab\_stop attribute is set to
false.

NOTE:The
is\_tab\_stop attribute is supported on Windows only.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [boxed\_column Tile (DCL)](boxed_column-Tile-DCL.md)
* [boxed\_radio\_column Tile (DCL)](boxed_radio_column-Tile-DCL.md)
* [boxed\_radio\_row Tile (DCL)](boxed_radio_row-Tile-DCL.md)
* [boxed\_row Tile (DCL)](boxed_row-Tile-DCL.md)
* [button Title (DCL)](button-Title-DCL.md)
* [dialog Tile (DCL)](dialog-Tile-DCL.md)
* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [list\_box Tile (DCL)](list_box-Tile-DCL.md)
* [popup\_list Tile (DCL)](popup_list-Tile-DCL.md)
* [radio\_button Tile (DCL)](radio_button-Tile-DCL.md)
* [text Tile (DCL)](text-Tile-DCL.md)
* [toggle Tile (DCL)](toggle-Tile-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*