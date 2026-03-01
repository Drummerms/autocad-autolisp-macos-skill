# color Attribute (DCL)

Specifies the background (fill) color of the image.

*Supported Platforms:* Windows, Mac OS, and Web

```
color = colorname;
```

Possible values are an integer or reserved word (default:
7) specified as an AutoCAD color number or as one of the symbolic names shown in the following table:

| Symbolic names for colors | |
| Symbolic name | Meaning |
| dialog\_line | Current dialog box line color |
| dialog\_foreground | Current dialog box foreground color (for text) |
| dialog\_background | Current dialog box background color |
| graphics\_background | Current background of the AutoCAD graphics screen (usually equivalent to 0) |
| black | AutoCAD color = 0 (black) (appears light on a black background) |
| red | AutoCAD color = 1 (red) |
| yellow | AutoCAD color = 2 (yellow) |
| green | AutoCAD color = 3 (green) |
| cyan | AutoCAD color = 4 (cyan) |
| blue | AutoCAD color = 5 (blue) |
| magenta | AutoCAD color = 6 (magenta) |
| white  graphics\_foreground | AutoCAD color = 7 (white) (appears black on a light background) |

The symbolic names
graphics\_background and
graphics\_foreground are provided as alternatives to the names
black and
white. The use of a specific color can be confusing because the color that is actually displayed varies depending on the current
AutoCAD configuration. Also, vectors in slides that you display in an image are often drawn in black or white. If your image
tile is blank when you first display it, try changing its
color to
graphics\_background or
graphics\_foreground.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [image\_button Tile (DCL)](image_button-Tile-DCL.md)
* [image Tile (DCL)](image-Tile-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*