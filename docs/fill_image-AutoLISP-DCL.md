# fill\_image (AutoLISP/DCL)

Draws a filled rectangle in the currently active dialog box image tile

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(fill_image x1 y1 width height color)
```

*x1*
:   *Type:* Integer

    *X* coordinate of the upper-left corner of the rectangle located at (*x1*,*y1*). Must be a positive value.

*y1*
:   *Type:* Integer

    *Y* coordinate of upper-left corner. Must be a positive value.

*width*
:   *Type:* Integer

    Width of the fill area (in pixels), relative to
    *x1*.

*height*
:   *Type:* Integer

    Width of the fill area (in pixels), relative to
    *y1*.

*color*
:   *Type:* Integer

    An AutoCAD color number, or one of the logical color numbers shown in the following table:

    | Symbolic names for color attribute | | |
    | Color number | ADI mnemonic | Description |
    | -2 | BGLCOLOR | Current background of the AutoCAD drawing area |
    | -15 | DBGLCOLOR | Current dialog box background color |
    | -16 | DFGLCOLOR | Current dialog box foreground color (text) |
    | -18 | LINELCOLOR | Current dialog box line color |

## Return Values

*Type:* Integer

A numeric value representing the fill color.

## Remarks

The first (upper-left) corner of the rectangle is located at (*x1*,*y1*) and the second (lower-right) corner is located the relative distance (*width*,*height*) from the first corner. The origin (0,0) is the upper-left corner of the image. You can obtain the coordinates of the lower-right
corner by calling the dimension functions
dimx\_tile and
dimy\_tile.

The
fill\_image function must be used between
start\_image and
end\_image function calls.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

```
(setq color -2) ;; color of AutoCAD drawing area
(fill_image
  0
  0
  (dimx_tile "slide_tile")
  (dimy_tile "slide_tile")
  color
)
(end_image)
```

#### Related References

* [dimx\_tile (AutoLISP/DCL)](dimx_tile-AutoLISP-DCL.md)
* [dimy\_tile (AutoLISP/DCL)](dimy_tile-AutoLISP-DCL.md)
* [end\_image (AutoLISP/DCL)](end_image-AutoLISP-DCL.md)
* [slide\_image (AutoLISP/DCL)](slide_image-AutoLISP-DCL.md)
* [start\_image (AutoLISP/DCL)](start_image-AutoLISP-DCL.md)
* [vector\_image (AutoLISP/DCL)](vector_image-AutoLISP-DCL.md)

#### Related Concepts

* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*