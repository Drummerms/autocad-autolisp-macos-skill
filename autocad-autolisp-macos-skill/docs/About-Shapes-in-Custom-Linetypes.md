# About Shapes in Custom Linetypes

A complex linetype can contain embedded shapes that are saved in shape files. Complex linetypes can denote utilities, boundaries,
contours, and so on.

As with simple linetypes, complex lines are dynamically drawn as the user specifies vertices. Shapes and text objects embedded
in lines are always displayed completely; they are never trimmed.

Linetype pattern descriptors that include shape objects is similar to that for simple linetypes.

The syntax for shape object descriptors in a linetype description is as follows:

```
[shape_name,shape_filename] or [shape_name,shape_filename,transform]
```

where
 *transform*  is optional and can be any series of the following (each preceded by a comma):

R=##
Relative rotation

A=##
Absolute rotation

U=##
Upright rotation

S=##
Scale

X=##
 *X* offset

Y=##
 *Y* offset

In this syntax,
## is a signed decimal number (1, -17, 0.01, and so on), the rotation is in degrees, and the remaining options are in linetype-scaled
drawing units. The preceding
 *transform*  letters, if they are used, must be followed by an equal sign and a number.

The following linetype definition defines a linetype named CON1LINE that is composed of a repeating pattern of a line segment,
a space, and the embedded shape CON1 from the
*ep.shx* file. (Note that the
*ep.shx* file must be in the support path for the following example to work properly.)

```
*CON1LINE, --- [CON1] --- [CON1] --- [CON1]
A,1.0,-0.25,[CON1,ep.shx],-1.0
```

Except for the code enclosed in square brackets, everything is consistent with the definition of a simple linetype.

As previously described, a total of six fields can be used to define a shape as part of a linetype. The first two are mandatory
and position-dependent; the next four are optional and can be ordered arbitrarily. The following two examples demonstrate
various entries in the shape definition field.

```
[CAP,ep.shx,S=2,R=10,X=0.5]
```

The code above draws the
CAP shape defined in the
*ep.shx* shape file with a scale of two times the unit scale of the linetype, a tangential rotation of 10 degrees in a counterclockwise
direction, and an
*X* offset of 0.5 drawing units before shape elaboration takes place.

```
[DIP8,pd.shx,X=0.5,Y=1,R=0,S=1]
```

The code above draws the
DIP8 shape defined in the
*pd.shx* shape file with an
*X* offset of 0.5 drawing units before shape drawing takes place, and a
*Y* offset of one drawing unit above the linetype, with 0 rotation and a scale equal to the unit scale of the linetype.

### Character Descriptor Format

The format for adding a shape to a linetype description is as follows:

```
[shape_name,shape_filename,scale,rotate,xoffset,yoffset]
```

Scale, rotation, x-offset, and y-offset values must be expressed as signed decimal numbers such as 1, -17, and 0.01.

*Shape name*
:   The name of the shape to be drawn. This field must be included. If it is omitted, the linetype definition fails. If
     *shape\_name*  does not exist in the specified shape file, the linetype is loaded and can be used but without the embedded shape.

*Shape filename*
:   The name of a compiled shape definition (SHX) file. If it is omitted, the linetype definition fails. If
     *shape\_filename*  is unqualified (that is, no path is specified), the support paths of the program are searched for the file. If
     *shape\_filename*  is fully qualified and not found at that location, the path is removed and the support paths of the program are searched
    for the file. If the file is not found, the linetype is loaded and can be used but without the embedded shape.

*Scale*
:   The scale factor to be used for the shape by which the shape's internally defined scale is multiplied. The scale factor provided
    must be prefixed with
    S=, for example
    S=.5 indicates a scale factor of 0.5. If the shape's internally defined scale is 0, the
    S= *value*  alone is used as the scale.

*Rotate*
:   The rotation angle of the shape to be displayed in the linetype. The rotation angle must be prefixed with
    U=,
    R=, or
    A=.

    * U= specifies upright or easy-to-read text.
    * R= specifies relative or tangential rotation with respect to the line.
    * A= specifies absolute rotation of the text with respect to the origin; that is, all text has the same rotation regardless of
      its position relative to the line.

    NOTE:Drawings containing legacy linetypes that do not use the U (upright) rotation flag can be updated to the latest linetype definition
    by reloading the linetype from the LIN files. Custom linetypes can be updated by changing the R (rotation) flag to the U (upright)
    flag prior to reloading a linetype definition.

*X-offset*
:   The shift of the shape in the
    *X* axis of the linetype computed from the end of the linetype definition vertex. The offset provided must be prefixed with
    X=, for example
    X=.1 indicates an offset of 0.1. If an offset is omitted or is 0, the shape is elaborated with no offset. Include this field if
    you want a continuous line with shapes. This value is not scaled by the scale factor defined by
    S=value.

*Y-offset*
:   The shift of the shape in the
    *Y* axis of the linetype computed from the end of the linetype definition vertex. The offset provided must be prefixed with
    Y=, for example
    Y=.1 indicates an offset of 0.1. If an offset is omitted or is 0, the shape is elaborated with no offset. Include this field if
    you want a continuous line with shapes. This value is not scaled by the scale factor defined by
    S=value.

#### Related Tasks

* [To Include Text in Custom Linetypes](To-Include-Text-in-Custom-Linetypes.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Simple Custom Linetypes](About-Simple-Custom-Linetypes.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*