# getcorner (AutoLISP)

Pauses for user input of a rectangle's second corner

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getcorner pt [msg])
```

*pt*
:   *Type:* List

    A point to be used as the base point.

*msg*
:   *Type:* String

    Message to be displayed to prompt the user.

## Return Values

*Type:* List or nil

The
getcorner function returns a point in the current UCS, similar to
getpoint. If the user supplies a 3D point, its
*Z* coordinate is ignored. The current elevation is used as the
*Z* coordinate.

## Remarks

The
getcorner function takes a base point argument, based on the current UCS, and draws a rectangle from that point as the user moves the
crosshairs on the screen.

The user cannot enter another AutoLISP expression in response to a
getcorner request.

## Examples

```
(getcorner '(7.64935 6.02964 0.0))
(17.2066 1.47628 0.0)

(getcorner '(7.64935 6.02964 0.0) "\
Pick a corner")
Pick a corner(15.9584 2.40119 0.0)
```

#### Related References

* [getpoint (AutoLISP)](getpoint-AutoLISP.md)
* [polar (AutoLISP)](polar-AutoLISP.md)
* [inters (AutoLISP)](inters-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*