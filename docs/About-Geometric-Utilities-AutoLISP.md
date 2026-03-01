# About Geometric Utilities (AutoLISP)

A group of functions allows applications to obtain pure geometric information and geometric data from the drawing.

The following lists some of the commonly used geometric related functions:

* angle – Returns the angle, in radians, between a line and the *X* axis (of the current UCS).
* distance – Returns the distance between two points.
* polar – Locates a point by means of polar coordinates (relative to an initial point).
* inters – Locates the intersection point of two lines.
* osnap – Returns a 3D point that is the result of applying an Object Snap mode to a specified point.
* textbox – Measures a specified text object, and returns the diagonal coordinates of the bounding box that encloses the text.

The following code example demonstrates calls to the geometric utility functions:

```
(setq pt1 '(3.0 6.0 0.0))
(setq pt2 '(5.0 2.0 0.0))
(setq base '(1.0 7.0 0.0))
(setq rads (angle pt1 pt2))   ; Angle in XY plane of current UCS - value
                              ; is returned in radians

(setq len (distance pt1 pt2)) ; Distance in 3D space
(setq endpt (polar base rads len))
```

The call to polar sets endpt to a point that is the same distance from (1,7) as pt1 is from pt2, and at the same angle from the *X* axis as the angle between pt1 and pt2.

#### Topics in this section

* [About Object Snaps (AutoLISP)](About-Object-Snaps-AutoLISP.md)

  The osnap function can find a point by using one of the AutoCAD Object Snap modes.
* [About Getting the Extents of Text (AutoLISP)](About-Getting-the-Extents-of-Text-AutoLISP.md)

  The textbox function returns the diagonal coordinates of a box that encloses text.

#### Related Concepts

* [About Object Snaps (AutoLISP)](About-Object-Snaps-AutoLISP.md)
* [About Getting the Extents of Text (AutoLISP)](About-Getting-the-Extents-of-Text-AutoLISP.md)
* [About Angular Conversion (AutoLISP)](About-Angular-Conversion-AutoLISP.md)
* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)
* [About Integers (AutoLISP)](About-Integers-AutoLISP.md)
* [About Reals (AutoLISP)](About-Reals-AutoLISP.md)
* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*