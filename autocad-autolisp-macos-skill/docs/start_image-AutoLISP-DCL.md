# start\_image (AutoLISP/DCL)

Starts the creation of an image in the dialog box tile

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(start_image key)
```

*key*
:   *Type:* String

    Value that specifies a tile. This argument is case-sensitive.

## Return Values

*Type:* String or nil

The
*key* argument, if successful; otherwise
nil.

## Remarks

Subsequent calls to
fill\_image,
slide\_image, and
vector\_image affect the created image until the application calls
end\_image.

NOTE:Do not use the
set\_tile function between
start\_image and
end\_image function calls.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related References

* [dimx\_tile (AutoLISP/DCL)](dimx_tile-AutoLISP-DCL.md)
* [dimy\_tile (AutoLISP/DCL)](dimy_tile-AutoLISP-DCL.md)
* [end\_image (AutoLISP/DCL)](end_image-AutoLISP-DCL.md)
* [fill\_image (AutoLISP/DCL)](fill_image-AutoLISP-DCL.md)
* [slide\_image (AutoLISP/DCL)](slide_image-AutoLISP-DCL.md)
* [vector\_image (AutoLISP/DCL)](vector_image-AutoLISP-DCL.md)

#### Related Concepts

* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*