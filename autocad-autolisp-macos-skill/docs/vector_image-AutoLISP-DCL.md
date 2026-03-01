# vector\_image (AutoLISP/DCL)

Draws a vector in the currently active dialog box image

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vector_image x1 y1 x2 y2 color)
```

*x1*
:   *Type:* Integer

    *X* coordinate of the first point.

*y1*
:   *Type:* Integer

    *Y* coordinate of the first point.

*x2*
:   *Type:* Integer

    *X* coordinate of the second point.

*y2*
:   *Type:* Integer

    *Y* coordinate of the second point.

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

A numeric value representing the color of the vector.

## Remarks

This function draws a vector in the currently active dialog box image (opened by
start\_image) from the point (*x1*,*y1*) to (*x2*,*y2*). The origin (0,0) is the upper-left corner of the image. You can obtain the coordinates of the lower-right corner by calling
the dimension functions (dimx\_tile and
dimy\_tile).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

```
(setq color -2) ;; color of AutoCAD drawing area
(vector_image
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
* [fill\_image (AutoLISP/DCL)](fill_image-AutoLISP-DCL.md)
* [slide\_image (AutoLISP/DCL)](slide_image-AutoLISP-DCL.md)
* [start\_image (AutoLISP/DCL)](start_image-AutoLISP-DCL.md)

#### Related Concepts

* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*