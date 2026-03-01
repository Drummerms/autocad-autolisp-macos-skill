# rtos (AutoLISP)

Converts a number into a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(rtos number [mode [precision]])
```

*number*
:   *Type:* Integer or Real

    A numeric value.

*mode*
:   *Type:* Integer

    Linear units mode. The
    *mode* corresponds to the values allowed for the AutoCAD LUNITS system variable.

    The mode can be one of the following numbers:

    *1* -- Scientific

    *2* -- Decimal

    *3* -- Engineering (feet and decimal inches)

    *4* -- Architectural (feet and fractional inches)

    *5* -- Fractional

*precision*
:   *Type:* Integer

    Precision used to format the returned value.

## Return Values

*Type:* String

Formatted numeric value.

The AutoCAD UNITMODE system variable affects the returned string when engineering, architectural, or fractional units are
selected (*mode* values 3, 4, or 5).

## Remarks

The
rtos function returns a string that is the representation of
*number* according to the settings of
*mode*,
*precision*, and the AutoCAD UNITMODE, DIMZIN, LUNITS, and LUPREC system variables.

The
*mode* and
*precision* arguments correspond to the AutoCAD LUNITS and LUPREC system variables. If you omit the arguments,
rtos uses the current settings of LUNITS and LUPREC.

## Examples

Set variable
x:

```
(setq x 17.5)
17.5
```

Convert the value of
x to a string in scientific format, with a precision of 4:

```
(setq fmtval (rtos x 1 4))
"1.7500E+01"
```

Convert the value of
x to a string in decimal format, with 2 decimal places:

```
(setq fmtval (rtos x 2 2))
"17.50"
```

Convert the value of
x to a string in engineering format, with a precision of 2:

```
(setq fmtval (rtos x 3 2))
"1'-5.50\""
```

Convert the value of
x to a string in architectural format:

```
(setq fmtval (rtos x 4 2))
"1'-5 1/2\""
```

Convert the value of
x to a string in fractional format:

```
(setq fmtval (rtos x 5 2))
"17 1/2"
```

Setting AutoCAD UNITMODE system variable to 1 causes units to be displayed as entered. This affects the values returned by
rtos for engineering, architectural, and fractional formats, as shown in the following examples:

```
(setvar "unitmode" 1)
1

(setq fmtval (rtos x 3 2))
"1'5.50\""

(setq fmtval (rtos x 4 2))
"1'5-1/2\""

(setq fmtval (rtos x 5 2))
"17-1/2"
```

#### Related References

* [atof (AutoLISP)](atof-AutoLISP.md)
* [angtos (AutoLISP)](angtos-AutoLISP.md)

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*