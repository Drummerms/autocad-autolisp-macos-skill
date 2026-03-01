# getangle (AutoLISP)

Pauses for user input of an angle, and returns that angle in radians

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getangle [pt] [msg])
```

*pt*
:   *Type:* List

    A 2D base point in the current UCS.

    The
    *pt* argument, if specified, is assumed to be the first of two points, so the user can show AutoLISP the angle by pointing to
    one other point. You can supply a 3D base point, but the angle is always measured in the current construction plane.

*msg*
:   *Type:* String

    Message to be displayed to prompt the user.

## Return values

*Type:* Real or nil

The angle specified by the user, in radians.

The
getangle function measures angles with the zero-radian direction (set by the AutoCAD ANGBASE system variable) with angles increasing
in the counterclockwise direction. The returned angle is expressed in radians with respect to the current construction plane
(the
*XY* plane of the current UCS, at the current elevation).

## Remarks

Users can specify an angle by entering a number in the AutoCAD current angle units format. Although the current angle units
format might be in degrees, grads, or some other unit, this function always returns the angle in radians. The user can also
show AutoLISP the angle by pointing to two 2D locations in the drawing area. AutoCAD draws a rubber-band line from the first
point to the current crosshairs position to help you visualize the angle.

It is important to understand the difference between the input angle and the angle returned by
getangle. Angles that are passed to
getangle are based on the current settings of the AutoCAD ANGDIR and ANGBASE system variables. However, once an angle is provided,
it is measured in a counterclockwise direction (ignoring ANGDIR) with zero radians as the current setting of ANGBASE.

The user cannot enter another AutoLISP expression as the response to a
getangle request.

## Examples

The following code examples show how different arguments can be used with
getangle:

```
(setq ang (getangle))
(setq ang (getangle '(1.0 3.5)))
(setq ang (getangle "Which way? "))
(setq ang (getangle '(1.0 3.5) "Which way? "))
```

#### Related References

* [getorient (AutoLISP)](getorient-AutoLISP.md)
* [angle (AutoLISP)](angle-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*