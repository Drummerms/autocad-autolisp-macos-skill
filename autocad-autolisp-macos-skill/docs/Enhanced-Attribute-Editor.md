# Enhanced Attribute Editor

Lists the attributes in a selected block instance and displays the properties of each attribute.

## Summary

The Enhanced Attribute Editor contains the following tabs:

* Attribute
* Text Options
* Properties

## List of Options

The following options are displayed.

Block
:   Name of the block whose attributes you are editing.

Tag
:   Tag identifying the attribute.

Select Block
:   Temporarily closes the dialog box while you select a block with your pointing device.

Attribute Tab (Enhanced Attribute Editor)

Displays the tag, prompt, and value assigned to each attribute. You can change only the attribute value.

![](../images/GUID-14AB716E-A412-433B-BE44-D5504D341922-low.png)

List
:   Lists the attributes in the selected block instance and displays the tag, prompt, and value for each attribute.

Value
:   Assigns a new value to the selected attribute.

    Single-line attributes include a button to insert a field. When clicked, the
    [Insert Field dialog box](Insert-Field-Dialog-Box.md) is displayed.

    Multiple-line attributes include a button with an ellipsis. Click to open the
    [In-Place Text Editor](In-Place-Text-Editor.md) with the ruler. Depending on the setting of the
    [ATTIPE](ATTIPE-System-Variable.md) system variable, the Attribute Editor visor displayed is either the abbreviated version, or the full version

Text Options Tab (Enhanced Attribute Editor)

Sets the properties that define the way an attribute's text is displayed in the drawing. Change the color of attribute text
on the Properties tab.

![](../images/GUID-28ADACA5-ED68-4A07-83B0-C3694FBC19B3-low.png)

Rotation
:   Specifies the rotation angle of the attribute text.

Oblique Angle
:   Specifies the angle that the attribute text is slanted away from its vertical axis. Not available for multiple-line attributes.

Height
:   Specifies the height of the attribute text.

Width Factor
:   Sets the character spacing for the attribute text. Entering a value less than
    *1.0* condenses the text. Entering a value greater than
    *1.0* expands it.

Multiline Text Width
:   Specifies the maximum length of the lines of text in a multiple-line attribute before wrapping to the next line. A value of
    0.000 means that there is no restriction on the length of a line of text. Not available for single-line attributes.

Text Style
:   Specifies the text style for the attribute text. Default values for this text style are assigned to the text properties displayed
    in this dialog box.

Backwards
:   Specifies whether or not the attribute text is displayed backwards. Not available for multiple-line attributes.

Upside Down
:   Specifies whether or not the attribute text is displayed upside down. Not available for multiple-line attributes.

Annotative
:   Specifies that the attribute is annotative. Click the information icon to learn more about annotative objects.

Justification
:   Specifies how the attribute text is justified (left-, center-, or right-justified).

Properties Tab (Enhanced Attribute Editor)

Defines the layer that the attribute is on and the lineweight, linetype, and color for the attribute text. If the drawing
uses plot styles, you can assign a plot style to the attribute using the Properties tab.

![](../images/GUID-C27E8640-F45E-4200-A707-848187722B63-low.png)

Layer
:   Specifies the layer that the attribute is on.

Linetype
:   Specifies the linetype of the attribute.

Color
:   Specifies the color of the attribute.

Lineweight
:   Specifies the lineweight of the attribute.

    Changes you make to this option are not displayed if the
    [LWDISPLAY](LWDISPLAY-System-Variable.md) system variable is off.

Plot Style
:   Specifies the plot style of the attribute.

    If the current drawing uses color-dependent plot styles, the Plot Style list is not available.

#### Related References

* [EATTEDIT (Command)](EATTEDIT-Command.md)

#### Related Concepts

* [About Modifying the Data in Block Attributes](About-Modifying-the-Data-in-Block-Attributes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*