# About Text in Custom Linetypes

Characters from text fonts can be included in linetypes.

Linetypes with embedded characters can denote utilities, boundaries, contours, and so on. As with simple linetypes, lines
are dynamically drawn as you specify the vertices. Characters embedded in lines are always displayed completely; they are
never trimmed.

Linetype pattern descriptors that include embedded characters is similar to that for simple linetypes.

For example, a linetype called HOT\_WATER\_SUPPLY is defined as

```
*HOT_WATER_SUPPLY,---- HW ---- HW ---- HW ---- HW ---- HW ----
A,.5,-.2,["HW",STANDARD,S=.1,U=0.0,X=-0.1,Y=-.05],-.2
```

This indicates a repeating pattern starting with a dash 0.5 drawing units long, a space 0.2 drawing units long, the characters
*HW* with some scale and placement parameters, and another space 0.2 drawing units long. The text characters come from the text
font assigned to the STANDARD text style at a scale of 0.1, an upright rotation of 0 degrees, an *X* offset of -0.1, and a *Y* offset of -0.05. This pattern continues for the length of the line, ending with a dash 0.5 drawing units long. The linetype
would be displayed as shown below.

![](../images/GUID-2CAD0D40-2A0B-4657-93E3-67A75700333D-low.png)

Notice that the total space length is 0.2 + 0.2 = 0.4 and that the text origin is offset -.01 units in the *X* direction from the end of the first upstroke. An equivalent linetype would be

```
*HOT_WATER_SUPPLY,---- HW ---- HW ---- HW ---- HW ---- HW ----
A,.5,-.1,["HW",STANDARD,S=.1,U=0.0,X=0.0,Y=-.05],-.3
```

The total space length is still 0.1 + 0.3 = 0.4, but the text origin is not offset in the *X* direction.

## Character Descriptor Format

The format for adding text characters in a linetype description is as follows:

```
["text_string",text_style_name,scale,rotation,xoffset,yoffset]
```

Scale, rotation, x-offset, and y-offset values must be expressed as signed decimal numbers such as 1, -17, and 0.01.

*Text string*
:   The characters to display in the linetype.

*Text style name*
:   The name of the text style to be used. If no text style is specified, the currently defined style is used.

    NOTE:Embedded text characters are associated with a text style in the drawing. Any text styles associated with a linetype must
    exist in the drawing before you load the linetype.

*Scale*
:   The scale factor to be used for the text style relative to the scale of the linetype. The scale factor provided must be prefixed
    with S=, for example S=.5 indicates a scale factor of 0.5. The height of the text style is multiplied by the scale factor. If the height of the text
    style is 0, the value for S=value alone is used as the height.

*Rotation*
:   The rotation angle of the characters to be displayed in the linetype. The rotation angle must be prefixed with U=, R=, or A=.

    * U= specifies upright or easy-to-read text.
    * R= specifies relative or tangential rotation with respect to the line.
    * A= specifies absolute rotation of the text with respect to the origin; that is, all text has the same rotation regardless of
      its position relative to the line.

    The value can be appended with a

    * d for degrees (degrees is the default value)
    * r for radians
    * g for grads

    The following illustration is of a linetype defined with an upright rotation.

    ![](../images/GUID-4282CB3D-8181-45E3-8856-0B45754B2E2D-low.png)

    If rotation is omitted, 0 relative rotation is used. Rotation is centered between the baseline and the nominal cap height.

    NOTE:Drawings containing legacy linetypes that do not use the U (upright) rotation flag can be updated to the latest linetype definition
    by reloading the linetype from the LIN files. Custom linetypes can be updated by changing the R (rotation) flag to the U (upright)
    flag prior to reloading a linetype definition.

*X-offset*
:   The shift of the text on the *X* axis of the linetype, which is along the line. The offset provided must be prefixed with X=, for example X=.1 indicates an offset of 0.1. If an offset is omitted or is 0, the text is elaborated with no offset. Use this field to control
    the distance between the text and the previous pen-up or pen-down stroke. This value is not scaled by the scale factor defined
    by S=value, but it is scaled to the linetype.

*Y-offset*
:   The shift of the text in the *Y* axis of the linetype, which is at a 90-degree angle to the line. The offset provided must be prefixed with Y=, for example Y=.1 indicates an offset of 0.1. If an offset is omitted or is 0, the text is elaborated with no offset. Use this field to control
    the vertical alignment of the text with respect to the line. This value is not scaled by the scale factor defined by S=value, but it is scaled to the linetype.

#### Topics in this section

* [To Include Text in Custom Linetypes](To-Include-Text-in-Custom-Linetypes.md)

#### Related Tasks

* [To Include Text in Custom Linetypes](To-Include-Text-in-Custom-Linetypes.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Simple Custom Linetypes](About-Simple-Custom-Linetypes.md)
* [About Custom Linetypes and Linetype Definitions](About-Custom-Linetypes-and-Linetype-Definitions.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*