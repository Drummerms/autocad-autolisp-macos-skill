# angtos (AutoLISP)

Converts an angular value in radians into a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(angtos angle [unit [precision]])
```

*angle*
:   *Type:* Integer or Real

    A number, in radians.

*unit*
:   *Type:* Integer

    An integer that specifies the angular units. If
    *unit* is omitted,
    angtos uses the current value of the AutoCAD AUNITS system variable. The following
    *unit*s may be specified:

    *0* -- Degrees

    *1* -- Degrees/minutes/seconds

    *2* -- Grads

    *3* -- Radians

    *4* -- Surveyor's units

*precision*
:   *Type:* Integer

    Specifies the number of decimal places of precision to be returned. If omitted,
    angtos uses the current setting of the AutoCAD AUPREC system variable.

## Return Values

*Type:* String or nil

A string, if successful; otherwise
nil.

## Remarks

The
angtos function takes
*angle* and returns it edited into a string according to the settings of
*unit* and
*precision*, the AutoCAD UNITMODE and DIMZIN system variables.

The
angtos function accepts a negative
*angle* argument, but always reduces it to a positive value between zero and 2 pi radians before performing the specified conversion.

The UNITMODE system variable affects the returned string when surveyor's units are selected (a
*unit* value of 4). If UNITMODE = 0, spaces are included in the string (for example, “N 45d E”); if UNITMODE = 1, no spaces are
included in the string (for example, “N45dE”).

## Examples

```
(angtos 0.785398 0 4)
"45.0000"

(angtos -0.785398 0 4)
"315.0000"

(angtos -0.785398 4)
"S 45d E"
```

NOTE:Routines that use the
angtos function to display arbitrary angles (those not relative to the value of AutoCAD ANGBASE system variable) should check and
consider the value of ANGBASE.

#### Related References

* [angtof (AutoLISP)](angtof-AutoLISP.md)
* [angle (AutoLISP)](angle-AutoLISP.md)

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*