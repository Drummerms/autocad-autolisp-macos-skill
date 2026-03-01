# atan (AutoLISP)

Returns the arctangent of a number in radians

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(atan num1 [num2])
```

*num1*
:   *Type:* Integer or Real

    A numeric value.

*num2*
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* Real

The arctangent of
*num1*, in radians, if only
*num1* is supplied. If you supply both
*num1* and
*num2* arguments,
atan returns the arctangent of
*num1*/*num2*, in radians. If
*num2* is zero, it returns an angle of plus or minus 1.570796 radians (+90 degrees or -90 degrees), depending on the sign of*num1*. The range of angles returned is -pi/2 to +pi/2 radians.

## Examples

```
(atan 1)
0.785398

(atan 1.0)
0.785398

(atan 0.5)
0.463648

(atan -1.0)
-0.785398

(atan 2.0 3.0)
0.588003

(atan 2.0 -3.0)
2.55359

(atan 1.0 0.0)
1.5708
```

#### Related References

* [cos (AutoLISP)](cos-AutoLISP.md)
* [sin (AutoLISP)](sin-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*