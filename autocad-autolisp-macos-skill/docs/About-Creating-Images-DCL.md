# About Creating Images (DCL)

The calling sequence to create images for image tiles and image buttons is similar to the list-handling sequence.

The
start\_image function begins the creation of an image, and
end\_image ends it. However, the type of image to draw is specified in separate function calls, instead of arguments:

vector\_image
:   Draws a vector (a single, straight line) in the current image.

fill\_image
:   Draws a filled rectangle in the current image.

slide\_image
:   Draws an AutoCAD slide in the image.

Vectors and filled rectangles are useful for simple images, such as the color swatches (filled rectangles) that the AutoCAD
Select Color dialog box uses to display the user's choice of color. For complicated images, slides are more convenient. However,
displaying slides can be time-consuming. If you use slides, keep them simple.

NOTE:If you use slides with filled objects (such as wide polylines, solids, and 3D faces) in image tiles, the images will appear
as outlines unless you make the slides from an image created with the AutoCAD SHADEMODE command.

The
vector\_image function requires that you specify absolute coordinates, while
fill\_image and
slide\_image require that you specify a starting coordinate along with a relative width and height. To do this correctly you must know
the exact dimensions of the image tile or image button. Because these dimensions are usually assigned when the dialog box
is laid out, the PDB feature provides functions that return the width and height of a particular tile. These dimension functions
are
dimx\_tile and
dimy\_tile. You should call them before you begin creating an image. The origin of a tile, (0,0), is always the upper-left corner.

Colors can be specified as AutoCAD color numbers or as one of the logical color numbers shown in the following table. (The
values and mnemonics are defined by the Autodesk Device Interface [ADI].)

| Dialog box color attribute | | |
| Color number | ADI mnemonic | Meaning |
| -2 | BGLCOLOR | Current background of the AutoCAD graphics screen |
| -15 | DBGLCOLOR | Current dialog box background color |
| -16 | DFGLCOLOR | Current dialog box foreground color (for text) |
| -18 | LINELCOLOR | Current dialog box line color |

In the following example, "cur\_color" is an image tile you want to fill entirely with a patch of red as follows:

```
(setq width (dimx_tile "cur_color")
      height (dimy_tile "cur_color")
)
(start_image "cur_color")
(fill_image 0 0 width height 1)   ;1 = AutoCAD red.
(end_image)
```

You can use the image-drawing functions in conjunction with each other. The following code fills an image and then draws
a vertical stripe over it:

```
(setq width (dimx_tile "stripe")
      height (dimy_tile "stripe")
)
(start_image "stripe")
(fill_image 0 0 width height 3)   ;3 = AutoCAD green.
(setq x (/ width 2))              ;Center the vector vertically.
(vector_image x 0 x height 4)     ;4 = AutoCAD cyan.
(end_image)
```

The slides you display with
slide\_image can be standalone slide (SLD) files, or part of a slide library (SLB) file. If the slide is in an SLD file, you specify its
name without the
*.sld* extension (for example,
"frntview"). If the slide is in a slide library, you specify the name of the library, followed by the name of the slide enclosed in
parentheses. Note that the library and slide names are also specified without extensions—for example,
"allviews(frntview)". The
slide\_image function searches for the slide or slide library file according to the current AutoCAD library search path.

In the following example, the slide is in a single file called
*topview.sld*:

```
(setq x (dimx_tile "view")
      y (dimy_tile "view")
)
(start_image "view")
(slide_image 0 0 x y "topview")
(end_image)
```

Vectors in slides are often drawn in white (color number 7), which is the default background color of an image. If your image
tile is blank when you first display a slide, try changing its
color attribute to
graphics\_background. (You can also change the background of the image by preceding the
slide\_image call with a
fill\_image call.)

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*