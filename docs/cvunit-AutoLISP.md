# cvunit (AutoLISP)

Converts a value from one unit of measurement to another

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(cvunit value from-unit to-unit)
```

*value*
:   *Type:* Integer, Real, or List

    The numeric value or point list (2D or 3D point) to be converted.

*from-unit*
:   *Type:* String

    The unit that
    *value* is being converted from.

*to-unit*
:   *Type:* String

    The unit that
    *value* is being converted to.

## Return Values

*Type:* Real, List, or nil

The converted value, if successful; otherwise
nil, if either unit name is unknown or not found in the
*acad.unt* file (or
*acadlt.unt* file in AutoCAD LT), or if the two units are incompatible (for example, trying to convert grams into years).

## Remarks

The
*from-unit* and
*to-unit* arguments can name any unit type found in the
*acad.unt* file (or
*acadlt.unt* file in AutoCAD LT).

## Examples

```
(cvunit 1 "minute" "second")
60.0

(cvunit 1 "gallon" "furlong")
nil

(cvunit 1.0 "inch" "cm")
2.54

(cvunit 1.0 "acre" "sq yard")
4840.0

(cvunit '(1.0 2.5) "ft" "in")
(12.0 30.0)

(cvunit '(1 2 3) "ft" "in")
(12.0 24.0 36.0)
```

NOTE:If you have several values to convert in the same manner, it is more efficient to convert the value 1.0 once and then apply
the resulting value as a scale factor in your own function or computation. This works for all predefined units except temperature,
where an offset is involved as well.

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*