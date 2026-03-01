# Attribute Definition Dialog Box

Defines the mode; attribute tag, prompt, and value; insertion point; and text settings for an attribute.

ATTDEF (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Define Attribute.
![](../images/GUID-59191139-7C55-482E-8248-032FA31D2056-low.png)

![](../images/GUID-E045445E-A50F-4B45-A092-6BB14BD19B09-low.png)

## List of Options

The following options are displayed.

Attribute

Sets attribute data.

Tag
:   Identifies each occurrence of an attribute in the drawing. Enter the attribute tag using any combination of characters except
    spaces. Lowercase letters are automatically changed to uppercase.

Prompt
:   Specifies the prompt that is displayed when you insert a block containing this attribute definition. If you do not enter a
    prompt, the attribute tag is used as a prompt. If you select Constant in the Attribute Options area under Advanced Options,
    the Prompt option is not available.

Default
:   Specifies the default attribute value.

Insert Field Button
:   Displays the
    [Field dialog box](GUID-1B6DD22B-10D1-44ED-BAA2-E6D79FE52327.htm#WSC30CD3D5FAA8F6D8B82368FFC2D60192-7FFF). You can insert a field as all or part of the value for an attribute.

    This button is available when you are not creating a multiline attribute. If you are creating a multiline attribute, right-click
    in the multiline in-place text editor and choose Field.

Multiline Editor Button
:   When Multiple Line mode is selected, displays an in-place text editor with a text formatting toolbar and ruler. Depending
    on the setting of the ATTIPE system variable, the Text Formatting toolbar displayed is either the abbreviated version, or
    the full version.

    For more information, see the
    [In-Place Text Editor](In-Place-Text-Editor.md).

    NOTE:Several options in the full In-Place Text Editor are grayed out to preserve compatibility with single-line attributes.

Text Settings

Sets the justification, style, height, and rotation of the attribute text.

Text Style
:   Specifies a predefined text style for the attribute text. Currently loaded text styles are displayed. To load or create a
    text style, see STYLE.

Justification
:   Specifies the justification of the attribute text. See TEXT for a description of the justification options.

Annotative
:   Specifies that the attribute is annotative. If the block is annotative, the attribute will match the orientation of the block.
    Click the information icon to learn more about annotative objects.

Text Height
:   Specifies the height of the attribute text. Enter a value, or choose Height to specify a height with your pointing device.
    The height is measured from the origin to the location you specify. If you select a text style that has fixed height (anything
    other than 0.0), or if you select Align in the Justification list, the Height option is not available.

Text Rotation
:   Specifies the rotation angle of the attribute text. Enter a value, or choose Rotation to specify a rotation angle with your
    pointing device. The rotation angle is measured from the origin to the location you specify. If you select Align or Fit in
    the Justification list, the Rotation option is not available.

Multiline Text Width
:   Specifies the maximum length of the lines of text in a multiple-line attribute before wrapping to the next line. A value of
    0.000 means that there is no restriction on the length of a line of text.

    Not available for single-line attributes.

Advanced Options

Contains options to set the behavior and insertion position for the attribute.

Attribute Options

Sets options for attribute values associated with a block when you insert the block in a drawing.

The default values are stored in the AFLAGS system variable. Changing the AFLAGS setting affects the default mode for new
attribute definitions and does not affect existing attribute definitions.

Invisible
:   Specifies that attribute values are not displayed or printed when you insert the block. ATTDISP overrides Invisible mode.

Constant
:   Gives attributes a fixed value for block insertions.

Verify
:   Prompts you to verify that the attribute value is correct when you insert the block.

Preset
:   Sets the attribute to its default value when you insert a block containing a preset attribute.

Lock Location
:   Locks the location of the attribute within the block reference. When unlocked, the attribute can be moved relative to the
    rest of the block using grip editing, and multiline attributes can be resized.

Multiple Lines
:   Specifies that the attribute value can contain multiple lines of text. When this option is selected, you can specify a boundary
    width for the attribute.

NOTE:In a dynamic block, an attribute's position must be locked for it to be included in an action's selection set.

Insertion Point

Specifies the location for the attribute. Enter coordinate values or select Specify On-screen and use the pointing device
to specify the placement of the attribute in relation to the objects that it will be associated with.

Specify On-Screen

Displays a Start Point prompt when the dialog box closes. Use the pointing device to specify the placement of the attribute
in relation to the objects that it will be associated with.

Input Coordinates

Specifies the coordinates to use for the attribute’s insertion point.

X
:   Specifies the
    *X* coordinate of the attribute's insertion point.

Y
:   Specifies the
    *Y* coordinate of the attribute's insertion point.

Z
:   Specifies the
    *Z* coordinate of the attribute's insertion point.

#### Related References

* [ATTDEF (Command)](ATTDEF-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*