# getpoint (AutoLISP)

Pauses for user input of a point, and returns that point

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getpoint [pt] [msg])
```

*pt*
:   *Type:* List

    A 2D or 3D base point in the current UCS.

    NOTE:getpoint will accept a single integer or real number as the
    *pt* argument, and use the AutoCAD direct distance entry mechanism to determine a point. This mechanism uses the value of the
    AutoCAD LASTPOINT system variable as the starting point, the
    *pt* input as the distance, and the current cursor location as the direction from LASTPOINT. The result is a point that is the
    specified number of units away from LASTPOINT in the direction of the current cursor location.

*msg*
:   *Type:* String

    Message to be displayed to prompt the user.

## Return Values

*Type:* List or nil

A 3D point, expressed in terms of the current UCS.

## Remarks

The user can specify a point by pointing or by entering a coordinate in the current units format. If the
*pt* argument is present, AutoCAD draws a rubber-band line from that point to the current crosshairs position.

The user cannot enter another AutoLISP expression in response to a
getpoint request.

## Examples

```
(setq p (getpoint))
(setq p (getpoint "Where? "))
(setq p (getpoint '(1.5 2.0) "Second point: "))
```

#### Related References

* [getcorner (AutoLISP)](getcorner-AutoLISP.md)
* [polar (AutoLISP)](polar-AutoLISP.md)
* [inters (AutoLISP)](inters-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*