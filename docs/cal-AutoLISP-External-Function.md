# cal (AutoLISP/External Function)

Invokes the on-line geometry calculator and returns the value of the evaluated expression

*Supported Platforms:* AutoCAD for Windows and Mac OS only; not available in AutoCAD LT

*Prerequisites:*The GeomCal ObjectARX application must be loaded before the function can be called,
(arxload "geomcal").

## Signature

```
(c:cal expression)
```

*expression*
:   *Type:* String

    A quoted string.

    See the AutoCAD CAL command for a description of allowable expressions.

## Return Values

*Type:* Integer, Real, List, or nil

The result of the expression.

## Examples

The following example uses
cal in an AutoLISP expression with the
trans function:

```
(trans (c:cal "[1,2,3]+MID") 1 2)
>> Select entity for MID snap:
(20.0465 16.0369 3.0)
```

#### Related References

* [Externally Defined Commands (AutoLISP)](Externally-Defined-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*