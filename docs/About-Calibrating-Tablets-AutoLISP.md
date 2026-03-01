# About Calibrating Tablets (AutoLISP)

Digitizing tablets can be calibrated using the TABLET command or with the AutoLISP tablet function.

IMPORTANT:Tablet support is limited to Windows only.

The tablet function enables applications to manage calibration settings directly and by saving those settings for future use. The first
argument to the tablet function is an integer *code*. If *code* is equal to 0, the function returns the current calibration. If code is equal to 1, the calibration is set according to the
remaining arguments. Calibrations are expressed as four 3D points (in addition to the *code*).

The first three points—*row1*, *row2*, and *row3*—are the three rows of the tablet's transformation matrix. The fourth point, *direction*, is a vector that is normal to the plane in which the tablet's surface is assumed to lie (expressed in WCS, the World Coordinate
System). When the calibration is set with the TABLET command, the tablet's surface is assumed to lie in the *XY* plane of the current UCS.

NOTE:The TABMODE system variable controls whether Tablet mode is turned on (1) or off (0). You can control it by using the setvar function.

The following code retrieves the current tablet calibration and stores it in the variable tcal:

```
(defun C:TABGET ()
  (setq tcal (tablet 0))
  (if tcal
    (princ
      (strcat "\
Configuration saved, "
              "use TABSET to retrieve calibration."
      )
    )
    (princ "\
Calibration not obtainable ")
  )
 (princ)
)
```

If the TABGET command was successful, the tcal variable now contains a list returned by the tablet function. This list might appear as follows:

```
(1 (0.00561717 -0.000978942 -7.5171)
  (0.000978942 0.00561717 -9.17308)
  (0.0 0.0 1.0)
  (0.0 0.0 1.0)
)
```

To reset the calibration to the values retrieved by the preceding routine, you can use the following code:

```
(defun C:TABSET ()
  (if (not (apply 'tablet tcal))
    (princ "\
Unable to reset calibration. ")
    (progn
      (princ "\
Tablet calibration reset. ")
      (setvar "tabmode" 1)
      (if (= (getvar "tabmode") 0)
        (princ "\
Unable to turn on tablet mode ")
      )
    )
  )
 (princ)
)
```

## Defining the Transformation Matrix for a Tablet

Arguments *row1*, *row2*, and *row3* are passed as a 3×3 transformation matrix which is meant to transform a 2D point. The 2D point is expressed as a column vector
in homogeneous coordinates (by appending 1.0 as the third element), so the transformation looks like this:

![](../images/GUID-DACFA669-4BF0-4BA9-9D66-BCD185BE2DEC-low.png)

The calculation of a point is similar to the 3D case. AutoCAD transforms the point by using the following formulas:

![](../images/GUID-24C35C46-A129-4A7A-8AA6-8221E3B6C3C9-low.png)

The resulting vector from the transformation can be turned back into a 2D point by dividing the first two (X',Y') components
by the third component (the scale factor D') yielding. The resulting 2D point looks like (X'/D',Y'/D').

For projective transformations, the most general case, tablet does the full calculation. But for affine and orthogonal transformations, M 20  and M 21  are both 0, so D' would be 1.0. The calculation of D' and the division are omitted; the resulting 2D point is simply (X',Y').

As the previous paragraph implies, an affine transformation is a special, uniform case of a projective transformation. An
orthogonal transformation is a special case of an affine transformation: not only are M 20  and M 21  zero, but M 00  = M 11  and M 10  = -M 01 .

NOTE:When you set a calibration, the list returned does not equal the list provided if the *direction* is not normalized. AutoCAD normalizes the direction vector before it returns it. Also, it ensures the third element in the
third column (*row3*[Z]) is equal to 1. This situation should not arise if you set the calibration by using values retrieved from AutoCAD by means
of tablet. However, it can happen if your program calculates the transformation itself.

#### Related Concepts

* [About Controlling Menus (AutoLISP)](About-Controlling-Menus-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)
* [About Configuration Files (AutoLISP)](About-Configuration-Files-AutoLISP.md)
* [Device Access Functions Reference (AutoLISP)](Device-Access-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*