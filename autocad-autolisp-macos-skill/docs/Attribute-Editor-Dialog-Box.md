# Attribute Editor Dialog Box

Allows you to edit attributes for a block definition.

BATTMAN (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Block attribute Manager
![](../images/GUID-29956DF2-A40C-4FF8-943C-CA1DBA0F5B9D-low.png):
Select a block ![](../images/ac.menuaro.gif) Double-click an attribute.

## List of Options

The following options are displayed.

Block Name
:   Displays the name of the block whose attributes are to be edited.

Attribute Tab (Attribute Editor Dialog Box)

Defines how a value is assigned to an attribute and whether or not the assigned value is visible in the drawing area, and
sets the string that prompts users to enter a value. The Attribute tab also displays the tag name that identifies the attribute.

![](../images/GUID-C8AB8D4B-24F7-459C-8A6C-240BFE16143E-low.png)

Tag

Sets the identifier assigned to the attribute.

Prompt

Sets the text for the prompt that is displayed when you insert the block.

Default

Sets the default value assigned to the attribute when you insert the block.

Options

Mode options determine whether and how attribute text appears.

Invisible
:   Displays or hides the attribute in the drawing area. If selected, hides the attribute value in the drawing area. If cleared,
    displays the attribute value.

Constant
:   Identifies whether the attribute is set to its default value. You cannot change this property. If a check mark is shown in
    the check box, the attribute is set to its default value and cannot be changed. If the check box is empty, you can assign
    a value to the attribute.

Verify
:   Turns value verification on and off. If selected, prompts you to verify the values you assign to the attribute when inserting
    a new instance of the block. If this option is cleared, verification is not performed.

Preset
:   Turns default value assignment on and off. If selected, sets the attribute to its default value when the block is inserted.
    If cleared, ignores the attribute's default value and prompts you to enter a value when inserting the block.

Lock Location
:   Locks the location of the attribute within the block reference. When unlocked, the attribute can be moved relative to the
    rest of the block using grip editing, and multiline attributes can be resized.

Multiple Lines
:   Indicates whether the attribute was defined as a Multiple Lines attribute and can contain multiple lines of text.

Text Options Tab (Attribute Editor Dialog Box)

Sets the properties that define the way an attribute's text is displayed in the drawing. Change the color of attribute text
on the Properties tab.

![](../images/GUID-8E09163A-AE3B-431D-8FB3-5B9F19DD7260-low.png)

Rotation
:   Specifies the rotation angle of the attribute text.

Oblique Angle
:   Specifies the angle that attribute text is slanted away from its vertical axis.

Height
:   Specifies the height of the attribute text.

Width Factor
:   Sets the character spacing for attribute text. Entering a value less than
    *1.0* condenses the text. Entering a value greater than
    *1.0* expands it.

Multiline Text Width
:   Specifies the maximum length of the lines of text in a multiple-line attribute before wrapping to the next line. A value of
    0.000 means that there is no restriction on the length of a line of text. Not available for single-line attributes.

Text Style
:   Specifies the text style for attribute text. Default values for this text style are assigned to the text properties displayed
    in this dialog box.

Backwards
:   Specifies whether or not the text is displayed backwards.

Upside Down
:   Specifies whether or not the text is displayed upside down.

Annotative
:   Specifies that the attribute is annotative.

Justification
:   Specifies how attribute text is justified.

Properties Tab (Attribute Editor Dialog Box)

Defines the layer that the attribute is on and the color, lineweight, and linetype for the attribute's line. If the drawing
uses plot styles, you can assign a plot style to the attribute using the Properties tab.

![](../images/GUID-90660710-13BA-4609-AB6B-8C1017595248-low.png)

Layer
:   Specifies the layer that the attribute is on.

Linetype
:   Specifies the linetype of attribute text.

Color
:   Specifies the attribute's text color.

Lineweight
:   Specifies the lineweight of attribute text.

    Changes you make to this option are not displayed if the
    [LWDISPLAY](LWDISPLAY-System-Variable.md) system variable is off.

Plot Style
:   Specifies the plot style of the attribute.

    If the current drawing uses color-dependent plot styles, the Plot Style list is not available.

#### Related References

* [BATTMAN (Command)](BATTMAN-Command.md)

#### Related Concepts

* [About Modifying Block Attribute Definitions](About-Modifying-Block-Attribute-Definitions.md)

#### Related Information

* [Block Attribute Manager](Block-Attribute-Manager.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*