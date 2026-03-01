# getorient (AutoLISP)

Pauses for user input of an angle, and returns that angle in radians

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getorient [pt] [msg])
```

*pt*
:   *Type:* List

    A 2D base point in the current UCS.

    The
    *pt* argument, if specified, is assumed to be the first of two points, so that the user can show AutoLISP the angle by pointing
    to one other point. You can supply a 3D base point, but the angle is always measured in the current construction plane.

*msg*
:   *Type:* String

    Message to be displayed to prompt the user.

## Return Values

*Type:* Real or nil

The angle specified by the user, in radians, with respect to the current construction plane.

## Remarks

The
getorient function measures angles with the zero-radian direction to the right (east) and angles that are increasing in the counterclockwise
direction. The angle input by the user is based on the current settings of the AutoCAD ANGDIR and ANGBASE system variables,
but once an angle is provided, it is measured in a counterclockwise direction, with zero radians being to the right (ignoring
ANGDIR and ANGBASE). Therefore, some conversion must take place if you select a different zero-degree base or a different
direction for increasing angles by using the AutoCAD UNITS command or the ANGBASE and ANGDIR system variables.

Use
getangle when you need a rotation amount (a relative angle). Use
getorient to obtain an orientation (an absolute angle).

The user cannot enter another AutoLISP expression as the response to a
getorient request.

## Examples

```
(setq pt1 (getpoint "Pick point: "))
(4.55028 5.84722 0.0)

(getorient pt1 "Pick point: ")
5.61582
```

#### Related References

* [getangle (AutoLISP)](getangle-AutoLISP.md)
* [angle (AutoLISP)](angle-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*