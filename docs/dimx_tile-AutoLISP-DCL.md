# dimx\_tile (AutoLISP/DCL)

Retrieves the width of a tile in dialog box units

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(dimx_tile key)
```

*key*
:   *Type:* String

    Value that specifies a tile. This argument is case-sensitive.

## Return Values

*Type:* Integer

The width of the tile.

The coordinates returned are the maximum allowed within the tile. Because coordinates are zero based, this function returns
one less than the total
*X* dimension (*X*-1). The
dimx\_tile and
dimy\_tile functions are provided for use with
vector\_image,
fill\_image, and
slide\_image, which require that you specify absolute tile coordinates.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

```
(setq tile_width (dimx_tile "my_tile"))
```

#### Related References

* [dimy\_tile (AutoLISP/DCL)](dimy_tile-AutoLISP-DCL.md)
* [end\_image (AutoLISP/DCL)](end_image-AutoLISP-DCL.md)
* [fill\_image (AutoLISP/DCL)](fill_image-AutoLISP-DCL.md)
* [slide\_image (AutoLISP/DCL)](slide_image-AutoLISP-DCL.md)
* [start\_image (AutoLISP/DCL)](start_image-AutoLISP-DCL.md)
* [vector\_image (AutoLISP/DCL)](vector_image-AutoLISP-DCL.md)

#### Related Concepts

* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*