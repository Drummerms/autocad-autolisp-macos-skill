# getdist (AutoLISP)

Pauses for user input of a distance

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getdist [pt] [msg])
```

*pt*
:   *Type:* List

    A 2D or 3D point to be used as the base point in the current UCS. If
    *pt* is provided, the user is prompted for the second point.

*msg*
:   *Type:* String

    Message to be displayed to prompt the user. If no string is supplied, AutoCAD does not display a message.

## Return Values

*Type:* Real or nil

A numeric value. If a 3D point is provided, the returned value is a 3D distance. However, setting the 64-bit of the
initget function instructs
getdist to ignore the
*Z* component of 3D points and to return a 2D distance.

## Remarks

The user can specify the distance by selecting two points, or by specifying just the second point, if a base point is provided.
The user can also specify a distance by entering a number in the AutoCAD current distance units format. Although the current
distance units format might be in feet and inches (architectural), the
getdist function always returns the distance as a real.

The
getdist function draws a rubber-band line from the first point to the current crosshairs position to help the user visualize the
distance.

The user cannot enter another AutoLISP expression in response to a
getdist request.

## Examples

```
(setq dist (getdist))
(setq dist (getdist '(1.0 3.5)))
(setq dist (getdist "How far "))
(setq dist (getdist '(1.0 3.5) "How far? "))
```

#### Related References

* [getpoint (AutoLISP)](getpoint-AutoLISP.md)
* [distance (AutoLISP)](distance-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*