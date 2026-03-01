# height Attribute (DCL)

Specifies the height of a tile.

*Supported Platforms:* Windows, Mac OS, and Web

```
height = number;
```

Possible values are an integer or a real number representing the distance in character height units. Do not specify this
value unless the assigned defaults do not have an acceptable appearance. You must specify, however, the height of image tiles
and image buttons.

The
height attribute specifies the minimum height of a tile. This dimension can be expanded when the tile is laid out, unless the height
is fixed by one of the
fixed\_ attributes. Defaults are dynamically assigned based on layout constraints.

Character-height units are defined as the maximum height of screen characters (including line spacing).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*