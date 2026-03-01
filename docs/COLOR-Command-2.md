# -COLOR (Command)

If you enter *-color* at the Command prompt, the following prompts are displayed.

Enter default object color [[Truecolor](COLOR-Command-2.md)/[COlorbook](COLOR-Command-2.md)] <BYLAYER>: *Enter a color, enter*  *t**,* *enter* *co**,* *or press* Enter

You can enter a color from the AutoCAD Color Index (a color name or number), a true color, or a color from a color book.

You can enter the color number (1 through 255) or the color name (the names for the first seven colors). For example, you
can specify the color red by entering the ACI number *1* or the ACI name *red*.

You can also enter *bylayer* or *byblock*. If you enter *byblock*, all new objects are drawn in the default color (white or black, depending on your background color) until they are grouped
into a block. When you insert the block in a drawing, the objects in the block inherit the current setting of COLOR.

WARNING:If you used a mixture of color methods to draw the objects that make up a block, inserting that block or changing its color
produces complex results.

If you enter *bylayer*, new objects assume the color assigned to the layer on which you create them. See the [LAYER](LAYER-Command.md) command for information about assigning a color to a layer.

## List of Prompts

The following prompts are displayed.

True Color
:   Specifies a true color to be used for the selected object. Enter three integer values from 0 to 255 separated by commas to
    specify a true color

Color Book
:   Specifies a color from a loaded color book to be used for the selected object. Enter the name of a color book that has been
    installed.

    If you enter a color book name, you are prompted to enter the color name in the color book.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*