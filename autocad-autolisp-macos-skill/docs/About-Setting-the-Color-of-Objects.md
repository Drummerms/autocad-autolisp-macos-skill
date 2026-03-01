# About Setting the Color of Objects

You can set the color of an object either by its layer or by specifying its color explicitly, independent of its layer.

* Assigning colors by layer makes it easy to identify each layer within your drawing.
* Assigning colors explicitly provides additional distinctions between objects on the same layer.

All objects are created using the *current color*, which is displayed in the Properties Inspector.

* If the current color is set to ByLayer, objects are created with the color assigned to the current layer.
* If the current color is set to ByBlock, objects are created using color 7 (white or black) until the objects are combined
  into a block definition. When the block is inserted into the drawing, it displays the current color for those objects.

You can use a variety of color palettes when assigning color to objects, including

* AutoCAD Color Index (ACI)
* True Color
* PANTONE ®  Colors
* RAL™ Classic and RAL Design color books
* DIC ®  Color Guide
* Colors from imported color books.

Color is also used as a way to indicate lineweight for color-dependent plotting.

## ACI Colors

ACI colors are the standard colors used in AutoCAD-based products. Each color is identified by an ACI number, an integer
from 1 through 255. Standard color names are available only for colors 1 through 7. The colors are assigned as follows: 1
Red, 2 Yellow, 3 Green, 4 Cyan, 5 Blue, 6 Magenta, 7 White/Black.

## True Colors

True colors use 24-bit color definitions to display over 16 million colors. When specifying true colors, you can use either
an RGB or HSL color model. With the RGB color model, you can specify the red, green, and blue components of the color; with
the HSL color model, you can specify the hue, saturation, and luminance aspects of the color.

## Color Books

Several standard PANTONE color books are included in the product. You can also import other color books such as the DIC color
guide or RAL color sets. Importing user-defined color books can further expand your available color selections.

You install color books on your system by using the Files tab in the Options dialog box. Once a color book is loaded, you
can select colors from the color book and apply them to objects in your drawings.

## PANTONE® Color Books

Pantone has updated the PANTONE MATCHING SYSTEM® with the PANTONE® PLUS SERIES of Publications that provides a chromatic arrangement
of colors. In AutoCAD-based products, the RGB values of the PANTONE Colors that are assigned to objects are preserved in all
current and legacy drawing files.

Color book (.acb) files provide access through the Select Color dialog box to the names of all PANTONE Colors and color books.
These .acb files are installed in the \Support\Color folder in the product installation folder.

#### Related Information

* [To Change the Color of Selected Objects](To-Change-the-Color-of-Selected-Objects.md)
* [To Set a True Color for All New Objects](To-Set-a-True-Color-for-All-New-Objects.md)
* [About Color Books](About-Color-Books.md)
* [Overview of Object Properties](Overview-of-Object-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*