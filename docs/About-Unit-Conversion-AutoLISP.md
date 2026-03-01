# About Unit Conversion (AutoLISP)

Values that represent distances, volumes, or other forms of measurement can be converted from one real-world unit to another.

The *acad.unt* file defines various conversions between real-world units such as miles to kilometers, Fahrenheit to Celsius, and so on.
The function cvunit takes a value expressed in one system of units and returns the equivalent value in another system. The two systems of units
are specified by strings containing expressions of units defined in *acad.unt*. The cvunit function does not convert measurements of the same type. For example, it does not convert inches into grams.

The first time cvunit converts to or from a unit during a drawing editor session, it must look up the string that specifies the unit in *acad.unt*. If your routine has many values to convert from one system of units to another, it is more efficient to convert the value
1.0 by a single call to cvunit and then use the returned value as a scale factor in subsequent conversions. This works for all units defined in *acad.unt* except temperature scales, which involve an offset as well as a scale factor.

The following example code converts a value in inches to centimeters:

```
(cvunit 1.0 "inch" "cm")
2.54
```

The following example code converts a value from Fahrenheit to Celsius:

```
(cvunit 32 "fahrenheit" "celsius")
3.46317e-009
```

The value returned after converting from Fahrenheit to Celsius is not exactly 0.0, you can use rtos to control the precision of the value returned by cvunit. If you still need a real value, you can convert the string returned by rtos with atof.

```
(setq temp (cvunit 32 "fahrenheit" "celsius"))
3.46317e-009

(setq temp (rtos temp 2 2))
"0.00"

(setq temp (atof temp))
0.0
```

#### Topics in this section

* [Example: Convert Inches to Meters (AutoLISP)](Example-Convert-Inches-to-Meters-AutoLISP.md)

  This example demonstrates how a user-specified distance in inches can be converted to meters with the cvunit function.
* [Unit Definition File Reference (AutoLISP)](Unit-Definition-File-Reference-AutoLISP.md)

  The AutoCAD unit definition file, acad.unt, allows you to define the factors to convert data one set of units to another set
  of units.

#### Related Concepts

* [Unit Definition File Reference (AutoLISP)](Unit-Definition-File-Reference-AutoLISP.md)
* [Example: Convert Inches to Meters (AutoLISP)](Example-Convert-Inches-to-Meters-AutoLISP.md)
* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*