# angtof (AutoLISP)

Converts a string representing an angle into a real (floating-point) value in radians

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(angtof string [units])
```

*string*
:   *Type:* String

    Formatted angular string that
    angtof can parse correctly to the specified
    *unit*. It can be in the same form that
    angtos returns, or in a form that AutoCAD allows for keyboard entry.

*units*
:   *Type:* Integer

    Specifies the units in which the string is formatted. The value should correspond to values allowed for the AutoCAD AUNITS
    system variable. If
    *unit* is omitted,
    angtof uses the current value of AUNITS. The following
    *unit*s may be specified:

    *0* -- Degrees

    *1* -- Degrees/minutes/seconds

    *2* -- Grads

    *3* -- Radians

    *4* -- Surveyor's units

## Return Values

*Type:* Real

A real value, if successful; otherwise
nil.

The
angtof and
angtos functions are complementary: if you pass
angtof a string created by
angtos,
angtof is guaranteed to return a valid value, and vice versa (assuming the
*unit* values match).

## Examples

```
(angtof "45.0000")
0.785398

(angtof "45.0000" 3)
1.0177
```

#### Related References

* [angtos (AutoLISP)](angtos-AutoLISP.md)
* [angle (AutoLISP)](angle-AutoLISP.md)

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*