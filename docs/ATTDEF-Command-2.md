# -ATTDEF (Command)

## List of Prompts

The following prompts are displayed.

Current attribute modes: Invisible=*current* Constant=*current* Verify=*current* Preset=*current* Lock position=*current* Annotative =*current* Multiple line =*current*

Enter an option to change [Invisible/Constant/Verify/Preset/Lock position/Annotative/Multiple lines] <done>:

Enter attribute tag name: *Enter any characters except spaces or exclamation points*

Enter attribute value:
*Enter the appropriate text or press*Enter *(this prompt is displayed only if you turned on Constant mode)*

Enter attribute prompt:
*Enter the text for the prompt line or press* Enter
*(this prompt is not displayed if you turned on Constant mode)*

Enter default attribute value:
*Enter the appropriate text or press*Enter *(this prompt is not displayed if you turned on Constant mode)*

Specify location of multiline attribute:
*Specify a point* *(this prompt is displayed only if you turned on Multiple line mode)*

Specify opposite corner:
*Specify a point or enter an option (this prompt is displayed only if you turned on Multiple line mode)*

Attribute Modes

The current value line indicates the current settings for each attribute mode (either Y for on or N for off). Entering
*i*,
*c*,
*v*,
*p*,
*l*,
*a*, or
*m* toggles the modes on or off. Press Enter when you have finished adjusting the mode settings. The AFLAGS system variable stores
the current mode settings and can be used to set the default modes.

Invisible
:   Specifies that attribute values are displayed when you insert the block. ATTDISP overrides Invisible mode.

Constant
:   Gives attributes a fixed value for block insertions.

Verify
:   Prompts for verification that the attribute value is correct when you insert the block.

Preset
:   Sets the attribute to its default value when you insert a block containing a preset attribute.

Lock Position
:   Locks the location of the attribute within the block reference. When unlocked, the attribute can be moved relative to the
    rest of the block using grip editing, and multiline attributes can be resized.

    NOTE:In a dynamic block, an attribute's position must be locked for it to be included in an action's selection set.

Annotative
:   Specifies that the attribute is annotative.

Multiple Lines
:   Specifies that the attribute value can contain multiple lines of text. When this option is selected, you can specify a boundary
    width for the attribute.

Attribute Tag Name

Specifies the attribute tag, which identifies each occurrence of an attribute in the drawing. The tag can contain any characters
except spaces or exclamation marks (!). Lowercase letters are automatically changed to uppercase.

Attribute Prompt

Specifies the prompt that is displayed when you insert a block containing this attribute definition. If you press Enter, the
attribute tag is used as the prompt. If you turn on Constant mode, this prompt is not displayed.

NOTE:For single-line attributes, you can enter up to 256 characters. If you need leading blanks in the prompt or the default value,
start the string with a backslash (\). To make the first character a backslash, start the string with two backslashes.

Default Attribute Value

Specifies the default attribute value. The default attribute value appears when a block is inserted into your drawing. A default
value is not required. If you turn on Constant mode, the Attribute Value prompt is displayed instead.

When Multiple Line mode is off, -ATTDEF then displays the same prompts as the TEXT command, using the attribute tag instead
of requesting a text string.

Current text style: "Standard" Text height: 0.2000

Specify start point of text or [Justify/Style]:
*Enter an option or press* Enter

Specify paper text height <*current*>:
*Specify a height, or press*Enter

The Specify Paper Text Height prompt is displayed only if the current text style is annotative.

For a description of each option, see the TEXT command.

NOTE:For single-line attributes, you can enter up to 256 characters. If you need leading blanks in the prompt or the default value,
start the string with a backslash (\). To make the first character a backslash, start the string with two backslashes.

When Multiple Line mode is on, -ATTDEF then displays several of the prompts used by the MTEXT command. For a description of
each option, see the MTEXTcommand.

Attribute Value (Constant Mode)

Specifies the value for a constant attribute. This prompt is displayed only if you turn on Constant mode.

ATTDEF then displays the same prompts as the TEXT command, using the attribute tag instead of requesting a text string. For
a description of each option, see the TEXT command.

When Multiple Line mode is on, -ATTDEF then displays several of the prompts used by the MTEXT command. For a description of
each option, see the MTEXT command.

Location of Multiline Attribute (Multiple Line Mode)

Specifies the first corner of the bounding box for the multiple-line text. This location is used as the starting point for
the attribute.

Opposite Corner (Multiple Line Mode)

As you drag the pointing device to specify the opposite corner, a rectangle is displayed to show the location and width of
the multiple-line text. The arrow within the rectangle indicates the direction of the text flow.

#### Related References

* [ATTDEF (Command)](ATTDEF-Command.md)
* [AFLAGS (System Variable)](AFLAGS-System-Variable.md)
* [ATTDISP (Command)](ATTDISP-Command.md)
* [TEXT (Command)](TEXT-Command.md)
* [MTEXT (Command)](MTEXT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*