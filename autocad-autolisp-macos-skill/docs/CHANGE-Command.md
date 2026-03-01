# CHANGE (Command)

Changes the properties of existing objects.

## List of Prompts

The following prompts are displayed

[Select objects](CHANGE-Command.md):

Specify [change point](CHANGE-Command.md) or [[Properties](CHANGE-Command.md)]: *Specify a new point, or press* Enter *to enter new values*

Specify Objects

If you select lines and other changeable objects in the same selection set, you get varying results depending on the object
selection sequence. The easiest way to use CHANGE is to select only lines in a selection set or select only objects other
than lines in a selection set.

Except for zero-thickness lines, the objects selected must be parallel to the current user coordinate system (UCS).

Change Point or Values

Changes the selected objects. The result depends on the type of objects you select.

Lines
:   Moves the endpoints of the selected lines that are closest to the change point to the new point, unless Ortho mode is on.
    If Ortho mode is on, the selected lines are modified so that they become parallel to either the *X* or the *Y* axis; their endpoints are not moved to the specified coordinate.

    ![](../images/GUID-BADA5E4F-6B5B-4081-A76B-5B7F85E947F9-low.png)

Circles
:   Changes the circle radius. If you selected more than one circle, the prompt is repeated for the next circle.

    ![](../images/GUID-19EE62C0-5906-45F4-8CBB-1709FA153D44-low.png)

Text
:   Changes text location and other properties.

Specify New Text Insertion Point
:   Relocates the text.

Attribute Definitions
:   Changes the text and text properties of an attribute that is not part of a block.

Blocks
:   Changes the location or rotation of a block.

    Specifying a new location relocates the block. Pressing Enter leaves the block in its original location.

    ![](../images/GUID-561F9277-8F62-49CF-BED8-8A88698B3B68-low.png)

Properties

Modifies properties of existing objects.

NOTE:The Plotstyle option is displayed only when you are using named plot styles.

You can change several properties at a time. The Enter Property to Change prompt is redisplayed after each option is completed.

Color
:   Changes the color of the selected objects.

    For example, to change a color to red, enter *red* or *1*. If you enter *bylayer*, the object assumes the color of the layer on which it is located. If you enter *byblock*, the object inherits the color of the block of which it is a component.

    * *True Color.* Specifies a true color to be used for the selected object. The integer values range from 0 to 255 seperated by commas.
    * *Color Book.* Specifies a color from a loaded color book to be used for the selected object.

Elev
:   Changes the *Z*-axis elevation of 2D objects.

    You can change the elevation of an object only if all its points have the same *Z* value.

    ![](../images/GUID-129AF2A4-B2F6-47AA-A701-593FE91C7ADF-low.png)

Layer
:   Changes the layer of the selected objects.

Ltype
:   Changes the linetype of the selected objects.

    If the new linetype is not loaded, the program tries to load it from the standard linetype library file,  *acad.lin* . If this procedure fails, use [LINETYPE](LINETYPE-Command.md) to load the linetype.

    ![](../images/GUID-69DA2F3D-2858-4D8B-8D45-854C48DF67C8-low.png)

Ltscale
:   Changes the linetype scale factor of the selected objects.

Lweight
:   Changes the lineweight of the selected objects. Lineweight values are predefined values. If you enter a value that is not
    a predefined value, the closest predefined lineweight is assigned to the selected objects.

Thickness
:   Changes the *Z*-direction thickness of 2D objects.

    Changing the thickness of a 3D polyline, dimension, or layout viewport object has no effect.

    ![](../images/GUID-3AC9C256-6316-4A23-9E65-1A96C446298C-low.png)

Transparency
:   Changes the transparency level of selected objects.

    Set the transparency to ByLayer or ByBlock, or enter a value from 0 to 90.

Material
:   Changes the material of the selected objects if a material is attached.

Annotative
:   Changes the Annotative property of the selected objects.

#### Related Concepts

* [Overview of Object Properties](Overview-of-Object-Properties.md)

#### Related Information

* [Display and Change the Properties of Objects](Display-and-Change-the-Properties-of-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*