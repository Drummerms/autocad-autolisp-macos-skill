# XPLODE (Command)

Breaks a compound object into its component objects.

## Summary

Reports how many objects were selected and, of those, how many objects cannot be exploded.

## List of Prompts

The following prompts are displayed.

Enter an option [[Individually](XPLODE-Command.md)/[Globally](XPLODE-Command.md)].

![](../images/GUID-07DDDB40-A3F0-4CF3-BB03-DF45E883FFFD-low.png)

Individually

Applies changes to the selected objects one at a time. The following prompt is displayed for each object.

All
:   Sets the color, linetype, lineweight, and layer of the component objects after you explode them. The prompts associated with
    the Color, Linetype, Lineweight, and Layer options are displayed.

Color
:   Sets the color of the objects after you explode them.

    * Enter
      *bylayer* to inherit the color of the exploded object's layer.
    * Enter
      *byblock*to inherit the color of the exploded object.
    * Enter
      *t*for a true color to be used for the selected object.
    * Enter
      *co* for a color from a loaded color book to be used for the selected object.

Layer
:   Sets the layer of the component objects after you explode them. The default option is to inherit the current layer rather
    than the layer of the exploded object.

LType
:   Sets the linetype of the component objects after you explode them.

    Enter
    *bylayer* to inherit the linetype of the exploded object's layer.

    Enter
    *byblock* to inherit the linetype of the exploded object.

LWeight
:   Sets the lineweight of the component objects after you explode them.

Inherit from Parent Block
:   Sets the color, linetype, lineweight, and layer of the component objects to that of the exploded object if the component objects'
    color, linetype, and lineweight are BYBLOCK and the objects are drawn on layer 0.

Explode
:   Breaks a compound object into its component objects exactly as the EXPLODE command does.

Globally

Applies changes to all the selected objects.

#### Related Concepts

* [About Modifying Block References](About-Modifying-Block-References.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*