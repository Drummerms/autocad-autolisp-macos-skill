# About String Conversions (AutoLISP)

Numeric values can be converted to string values for use in output or textual data.

The following functions can be used to convert real and angle values to strings, and back:

* rtos – Converts a real number into a formatted string based on a specified linear units mode.
* distof – Converts a formatted string that represents a distance value into a real (floating-point) value.
* angtos – Converts an angular value in radians into a formatted string based on a specified angular units mode.
* angtof – Converts a formatted string representing an angle into a real (floating-point) value in radians.

## Converting Real Numbers to a String with Linear Units Format

The rtos function converts a real value to a string. The format of the result string can be specified using the arguments of the function,
or by the AutoCAD LUNITS and LUPREC system variables then when not provided. The AutoCAD DIMZIN system variable controls how
leading and trailing zeros are written to the result string.

The following example code demonstrates the use of rtos and the values returned (assuming the AutoCAD DIMZIN system variable equals 0). Precision (the third argument to rtos) is set to 4 places in the first call and 2 places in the others.

```
(setq x 17.5)
(setq str "\
Value formatted as ") (setq fmtval (rtos x 1 4)) ; Mode 1 = scientific
(princ (strcat str fmtval))
Value formatted as 1.7500E+01

(setq fmtval (rtos x 2 2)) ; Mode 2 = decimal
(princ (strcat str fmtval))
Value formatted as 17.50

(setq fmtval (rtos x 3 2)) ; Mode 3 = engineering
(princ (strcat str fmtval))
Value formatted as 1'-5.50"

(setq fmtval (rtos x 4 2)) ; Mode 4 = architectural
(princ (strcat str fmtval))
Value formatted as 1'-5 1/2"

(setq fmtval (rtos x 5 2)) ; Mode 5 = fractional
(princ (strcat str fmtval))
Value formatted as 17 ½
```

When the AutoCAD UNITMODE system variable is set to 1, units are displayed as entered, the string returned by rtos differs for engineering (mode equals 3), architectural (mode equals 4), and fractional (mode equals 5) units. For example,
the first two lines of the preceding sample output would be the same, but the last three lines would appear as follows:

```
Value formatted as 1'5.50"
Value formatted as 1'5-1/2"
Value formatted as 17-1/2''
```

## Converting Strings with Linear Units Format to Real Numbers

The distof (distance to floating point) function is the complement of rtos. All of the following calls return the same value: 17.5. (Note the use of the backslash (\) with modes 3 and 4.)

```
(distof "1.7500E+01" 1) ; Mode 1 = scientific
(distof "17.50" 2)      ; Mode 2 = decimal
(distof "1'-5.50\"" 3)  ; Mode 3 = engineering
(distof "1'-5 1/2\"" 4) ; Mode 4 = architectural
(distof "17 1/2" 5)     ; Mode 5 = fractional
```

When you have a string specifying a distance in feet and inches, you must precede the quotation mark with a backslash ( *\"* ) so it does not look like the end of the string. The preceding examples of distof demonstrates this action.

## Converting Real Numbers to a String with Angular Units Format

The angtos function converts an angular value to a string. The format of the result string can be specified using the arguments of the
function, or by the AutoCAD AUNITS and AUPREC system variables then when not provided. The AutoCAD DIMZIN system variable
controls how leading and trailing zeros are written to the result string.

Because the angtos function takes the AutoCAD ANGBASE system variable into consideration, the following example code always returns "0":

```
(angtos (getvar "angbase"))
```

There is no AutoLISP function that returns a string version (in the current mode/precision) of either the amount of rotation
of ANGBASE from true zero (East) or an arbitrary angle in radians.

The amount of rotation of ANGBASE from AutoCAD zero (East) or the size of an arbitrary angle can be found by doing one of
the following:

* Add the desired angle to the current ANGBASE, and then check to see if the absolute value of the result is greater than 2pi;
  (2 \* pi). If so, subtract 2pi;, if the result is negative, add 2pi;, then use the angtos function on the result.
* Store the value of ANGBASE in a temporary variable, set ANGBASE to 0, evaluate the angtos function, then set ANGBASE to its original value.

Subtracting the result of (atof (angtos 0)) from 360 degrees (2pi; radians or 400 grads) also yields the rotation of ANGBASE from 0.

The following example code demonstrates the use of angtos and the values returned (still assuming that DIMZIN equals 0). Precision (the third argument to angtos) is set to 0 places in the first call, 4 places in the next three calls, and 2 places in the last.

```
(setq ang 3.14159 str2 "\
Angle formatted as ")
(setq fmtval (angtos ang 0 0)) ; Mode 0 = degrees
(princ (strcat str2 fmtval))
Angle formatted as 180

(setq fmtval (angtos ang 1 4)) ; Mode 1 = deg/min/sec
(princ (strcat str2 fmtval))
Angle formatted as 180d0'0"

(setq fmtval (angtos ang 2 4)) ; Mode 2 = grads
(princ (strcat str2 fmtval)) ; displays Angle formatted as
200.0000g

(setq fmtval (angtos ang 3 4)) ; Mode 3 = radians
(princ (strcat str2 fmtval))
Angle formatted as 3.1416r

(setq fmtval (angtos ang 4 2)) ; Mode 4 = surveyor's
(princ (strcat str2 fmtval))
Angle formatted as W
```

The UNITMODE system variable also affects strings returned by angtos when it returns a string in surveyor's units (mode equals 4). If UNITMODE equals 0, the string returned can include spaces
(for example, "N 45d E"); if UNITMODE equals 1, the string contains no spaces (for example, "N45dE").

## Converting Strings with Angular Units Format to Real Numbers

The angtof function complements angtos, all of the following calls return the same value: 3.14159.

```
(angtof "180" 0)       ; Mode 0 = degrees
(angtof "180d0'0\"" 1) ; Mode 1 = deg/min/sec
(angtof "200.0000g" 2) ; Mode 2 = grads
(angtof "3.14159r" 3)  ; Mode 3 = radians
(angtof "W" 4)         ; Mode 4 = surveyor's
```

When you have a string specifying an angle in degrees, minutes, and seconds, you must precede the quotation mark with a backslash
( *\"* ) so it does not look like the end of the string. The preceding example of angtof demonstrates this action.

#### Related Concepts

* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)
* [About Control Characters in Strings (AutoLISP)](About-Control-Characters-in-Strings-AutoLISP.md)
* [About Angular Conversion (AutoLISP)](About-Angular-Conversion-AutoLISP.md)
* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*