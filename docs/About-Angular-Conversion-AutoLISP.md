# About Angular Conversion (AutoLISP)

Angular values returned by most AutoLISP functions and those stored in a drawing are expressed in radians, while angular input
is commonly provided in degrees or another angular format than radians.

You can convert angular values directly with a combination of math functions, or use the
angtos and
angtof functions. The
angtos function converts an angular value expressed in radians to degrees or one of the other supported angular formats. This function
returns a string value. If you need a real (or floating point) value, you can use the
atof function to convert the string value that is returned by
angtos.

```
(setq half-PI (/ PI 2))
1.5708

(setq angstr (angtos half-PI 0 2))
"90.00"

(setq deg (atof angstr))
90.0
```

The
angtof function is the opposite of
angtos, it converts a string representing an angular value into a real (or floating point) value in radians.

```
(setq angstr (angtos 1.5708 1 6))
"90d0'0.76\""

(setq rad (angtof angstr 1))
1.5708
```

## Converting Radians to Degrees and Degrees to Radians with Math Functions

A more efficient method way to convert radians to degrees and degrees to radians than using the
angtos and
angtof functions is to use math functions.

The math formula to convert radians to degrees is:

```
(Radians / PI) * 180 = Degrees
```

In AutoLISP, the same can be achieved using the following function:

```
; Convert value in radians to degrees
(defun Radian->Degrees (nbrOfRadians)
  (* 180.0 (/ nbrOfRadians pi))
)
RADIAN->DEGREES

(Radian->Degrees PI)
180.0
```

The math formula to convert degrees to radians is:

```
(Degrees / 180) * PI = Radians
```

In AutoLISP, the same can be achieved using the following function:

```
; Convert value in degrees to radians
(defun Degrees->Radians (numberOfDegrees)
  (* pi (/ numberOfDegrees 180.0))
)
DEGREES->RADIANS

(Degrees->Radians 180.0)
3.14159
```

#### Related Concepts

* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Geometric Utilities (AutoLISP)](About-Geometric-Utilities-AutoLISP.md)
* [About Integers (AutoLISP)](About-Integers-AutoLISP.md)
* [About Reals (AutoLISP)](About-Reals-AutoLISP.md)
* [About Number Handling (AutoLISP)](About-Number-Handling-AutoLISP.md)
* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*