# slide\_image (AutoLISP/DCL)

Displays an AutoCAD slide in the currently active dialog box image tile

*Supported Platforms:* Windows only

## Signature

```
(slide_image x1 y1 width height sldname)
```

*x1*
:   *Type:* Integer

    *X*-offset from the upper-left corner of the tile, in pixels. Must be a positive value.

*y1*
:   *Type:* Integer

    *Y*-offset from the upper-left corner of the tile, in pixels. Must be a positive value.

*width*
:   *Type:* Integer

    Width of the image, in pixels.

*height*
:   *Type:* Integer

    Height of the image, in pixels.

*sldname*
:   *Type:* String

    Identifies the slide. This argument can be a slide file (*.sld*) or a slide in a slide library file (*.slb*). Specify
    *sldname* the same way you would specify it for the AutoCAD VSLIDE command or for a customization file. Use one of the following formats
    for
    *sldname*:

    *sldname* or
    *libname*(*sldname*)

## Return Values

*Type:* String

A value containing
*sldname*.

## Remarks

The first (upper-left) corner of the slide—its insertion point—is located at (*x1*,*y1*), and the second (lower-right) corner is located at the relative distance (*wid*,*hgt*) from the first (*wid* and
*hgt* must be positive values). The origin (0,0) is the upper-left corner of the image. You obtain the coordinates of the lower-right
corner by calling the dimension functions (dimx\_tile and
dimy\_tile).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows

## Examples

```
(slide_image
  0
  0
  (dimx_tile "slide_tile")
  (dimy_tile "slide_tile")
  "myslide"
)
(end_image)
```

#### Related References

* [dimx\_tile (AutoLISP/DCL)](dimx_tile-AutoLISP-DCL.md)
* [dimy\_tile (AutoLISP/DCL)](dimy_tile-AutoLISP-DCL.md)
* [end\_image (AutoLISP/DCL)](end_image-AutoLISP-DCL.md)
* [fill\_image (AutoLISP/DCL)](fill_image-AutoLISP-DCL.md)
* [start\_image (AutoLISP/DCL)](start_image-AutoLISP-DCL.md)
* [vector\_image (AutoLISP/DCL)](vector_image-AutoLISP-DCL.md)

#### Related Concepts

* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*