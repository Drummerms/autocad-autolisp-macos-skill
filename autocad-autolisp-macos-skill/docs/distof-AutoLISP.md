# distof (AutoLISP)

Converts a string that represents a real (floating-point) value into a real value

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(distof str [mode])
```

*str*
:   *Type:* String

    A string to be converted. The argument must be a string that
    distof can parse correctly according to the units specified by
    *mode*. It can be in the same form that
    rtos returns, or in a form that AutoCAD allows for keyboard entry.

*mode*
:   *Type:* Integer

    The units in which the string is currently formatted. The
    *mode* corresponds to the values allowed for the AutoCAD LUNITS system variable. Specify one of the following numbers for
    *mode*:

    *1* -- Scientific

    *2* -- Decimal

    *3* -- Engineering (feet and decimal inches)

    *4* -- Architectural (feet and fractional inches)

    *5* -- Fractional

## Return Values

*Type:* Real

A real number, if successful; otherwise
nil.

NOTE:The
distof function treats modes 3 and 4 the same. That is, if
*mode* specifies 3 (engineering) or 4 (architectural) units, and
*string* is in either of these formats,
distof returns the correct real value.

## Remarks

The
distof and
rtos functions are complementary. If you pass
distof a string created by
rtos,
distof is guaranteed to return a valid value, and vice versa (assuming the mode values are the same).

## Examples

None

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*