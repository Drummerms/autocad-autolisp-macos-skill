# About Simple Custom Linetypes

You can define a custom linetype with different patterns of dots, spaces, and dashes by creating or editing a linetype definition
(LIN) file using a text editor. Once defined, you can load and use the custom linetype in any drawing file.

Each linetype is defined on two lines in a linetype definition file. The first line contains the linetype name and an optional
description. The second line is the code that defines the actual linetype pattern.

The second line must begin with the letter A (alignment), followed by a list of pattern descriptors that define pen-up lengths
(spaces), pen-down lengths (dashes), and dots. You can include comments in a LIN file by beginning the line with a semicolon
(;).

## Linetype Definition Format

The format of the linetype definition is

```
*linetype_name,description
A,descriptor1,descriptor2, ...
```

For example, a linetype called DASHDOT is defined as

```
*DASHDOT,Dash dot __ . __ . __ . __ . __ . __ . __ . __
A,.5,-.25,0,-.25
```

The example indicates a repeating pattern starting with a dash 0.5 drawing units long, a space 0.25 drawing units long, a
dot, and another space 0.25 drawing units long. This pattern continues for the length of the line, ending with a dash 0.5
drawing units long. The linetype would be displayed as shown below.

\_\_ . \_\_ . \_\_ . \_\_ . \_\_ . \_\_ . \_\_ . \_\_

LIN files must be saved in the ASCII format and use a .*lin* file extension.

*Linetype Name*
:   The linetype name field must begin with an asterisk (\*) and should provide a unique, descriptive name for the linetype.

*Description*
:   The description of the linetype should help you visualize the linetype when you edit the LIN file. The description is also
    displayed in the Linetype Manager and in the Load or Reload Linetypes dialog box.

    The description is optional and can include

    * A simple representation of the linetype pattern using ASCII text
    * An expanded description of the linetype
    * A comment such as "Use this linetype for hidden lines"

    If you omit the description, do not insert a comma after the linetype name. A description cannot exceed 47 characters.

*Alignment Field (A)*
:   The alignment field specifies the action for pattern alignment at the ends of individual lines, circles, and arcs. The program
    supports only A-type alignment, which guarantees that the endpoints of lines and arcs start and stop with a dash. You must
    specify A-type alignment by entering *A* in the alignment field.

    For example, suppose you create a linetype called CENTRAL that displays the repeating dash-dot sequence commonly used as a
    centerline. The program adjusts the dash-dot sequence on an individual line so that dashes and line endpoints coincide. The
    pattern fits the line so that at least half of the first dash begins and ends the line. If necessary, the first and last dashes
    are lengthened. If a line is too short to hold even one dash-dot sequence, a continuous line between the endpoints is drawn.
    For arcs, the pattern is adjusted so that dashes are drawn at the endpoints. For circles and other objects without endpoints,
    the dash-dot sequence is adjusted to provide a reasonable display.

*Pattern Descriptors*
:   Each pattern descriptor field specifies the length of segments making up the linetype, separated by commas (no spaces are
    allowed):

    * A positive decimal number denotes a pen-down (dash) segment of that length.
    * A negative decimal number denotes a pen-up (space) segment of that length.
    * A dash length of 0 draws a dot.

    You can enter up to 12 dash-length specifications per linetype, provided they fit on one 80-character line in the LIN file.
    You need to include only one complete repetition of the linetype pattern defined by pattern descriptors. When the linetype
    is drawn, the application uses the first pattern descriptor for the starting and ending dashes. Between the starting and ending
    dashes, the pattern dash specifications are drawn sequentially, beginning with the second dash specification and restarting
    the pattern with the first dash specification when required.

    A-type alignment requires that the first dash length be 0 or greater (a pen-down segment). The second dash length should be
    less than 0 if you need a pen-up segment and more than 0 if you are creating a continuous linetype. You must have at least
    two dash specifications for A-type alignment.

#### Topics in this section

* [To Add a Simple Linetype to an LIN File](To-Add-a-Simple-Linetype-to-an-LIN-File.md)
* [To Create a Simple Linetype From the Command Prompt](To-Create-a-Simple-Linetype-From-the-Command-Prompt.md)

#### Related Tasks

* [To Create a Simple Linetype From the Command Prompt](To-Create-a-Simple-Linetype-From-the-Command-Prompt.md)
* [To Add a Simple Linetype to an LIN File](To-Add-a-Simple-Linetype-to-an-LIN-File.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Custom Linetypes and Linetype Definitions](About-Custom-Linetypes-and-Linetype-Definitions.md)
* [About Text in Custom Linetypes](About-Text-in-Custom-Linetypes.md)
* [About Shapes in Custom Linetypes](About-Shapes-in-Custom-Linetypes.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*