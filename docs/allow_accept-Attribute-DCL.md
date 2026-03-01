# allow\_accept Attribute (DCL)

Specifies whether the tile is activated when the user presses the accept key (usually Enter).

*Supported Platforms:* Windows, Mac OS, and Web

```
allow_accept = true-false;
```

NOTE:This attribute isn't supported by the
edit\_box tile on Mac OS or Web.

If
true and the user presses the accept key, the default button (if any) is pressed. The default button is the
button tile whose
is\_default attribute is set to
true. The
allow\_accept attribute defaults to
false.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [image\_button Tile (DCL)](image_button-Tile-DCL.md)
* [list\_box Tile (DCL)](list_box-Tile-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*