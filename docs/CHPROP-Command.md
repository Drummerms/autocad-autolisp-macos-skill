# CHPROP (Command)

Changes the properties of an object.

## List of Prompts

The following prompts are displayed.

Select objects:

Enter property to change [[Color](CHPROP-Command.md)/[LAyer](CHPROP-Command.md)/[LType](CHPROP-Command.md)/[ltScale](CHPROP-Command.md)/[LWeight](CHPROP-Command.md)/[Thickness](CHPROP-Command.md)/[TRansparency](CHPROP-Command.md)/[Material](CHPROP-Command.md)/[Annotative](CHPROP-Command.md)]:

NOTE:The Plotstyle option is displayed only when you are using named plot styles.

If you select several objects with different values for the property you want to change, *varies* is displayed as the current value.

Color

Changes the color of the selected objects.

For example, to change a color to red, enter *red* or *1*. If you enter *bylayer*, the object assumes the color of the layer on which it is located. If you enter *byblock*, the object inherits the color of the block of which it is a component.

True Color
:   Specifies a true color to be used for the selected object.

Color Book
:   Specifies a color from a loaded color book to be used for the selected object.

Layer

Changes the layer of the selected objects.

Ltype

Changes the linetype of the selected objects.

If the new linetype is not loaded, the program tries to load it from the standard linetype library file,  *acad.lin* . If this procedure fails, use [LINETYPE](LINETYPE-Command.md) to load the linetype.

![](../images/GUID-69DA2F3D-2858-4D8B-8D45-854C48DF67C8-low.png)

Ltscale

Changes the linetype scale factor of the selected objects.

Lweight

Changes the lineweight of the selected objects. Lineweight values are predefined values. If you enter a value that is not
a predefined value, the closest predefined lineweight is assigned to the selected objects.

Thickness

Changes the *Z*-direction thickness of 2D objects.

Changing the thickness of a 3D polyline, dimension, or layout viewport object has no effect.

![](../images/GUID-3AC9C256-6316-4A23-9E65-1A96C446298C-low.png)

Transparency

Changes the transparency level of selected objects.

Set the transparency to ByLayer or ByBlock, or enter a value from 0 to 90.

Material

Changes the material of the selected objects if a material is attached.

Annotative

Changes the Annotative property of the selected objects.

#### Related Concepts

* [Overview of Object Properties](Overview-of-Object-Properties.md)

#### Related Information

* [Display and Change the Properties of Objects](Display-and-Change-the-Properties-of-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*