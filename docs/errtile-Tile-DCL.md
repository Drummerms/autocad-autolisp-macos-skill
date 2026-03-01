# errtile Tile (DCL)

An error tile is a text tile that appears at the bottom of a dialog box.

*Supported Platforms:* Windows, Mac OS, and Web

```
errtile;
```

By default it is blank, but programs can display messages in it by setting the value of the tile whose key is
"error". For example:

```
(set_tile "error" "You can only select one option")
```

The
errtile tile is defined in the
*base.dcl* file.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*