# About Object Snaps (AutoLISP)

The osnap function can find a point by using one of the AutoCAD Object Snap modes.

You pass the function a three element list that represents a 3D point; if you want to specify a 2D point, set the *Z* axis to a value of 0 (zero). Snap modes are specified using a string value; multiple Snap modes can be specified by using
a comma delimiter.

The following example code looks for the midpoint of an object near pt1:

```
(setq pt2 (osnap pt1 "_midp"))
```

The following example code looks for the midpoint, the endpoint, or the center of an object nearest pt1:

```
(setq pt2 (osnap pt1 "_midp,_endp,_center"))
```

NOTE:It is recommended to always add an underscore (\_) in front of each Snap mode; this will help your program to work as expected
when executed on an AutoCAD release other than the English language release.

In both examples, pt2 is set to the snap point if one is found that fulfills the osnap requirements. If more than one snap point fulfills the requirements,
the point is selected based on the setting of the AutoCAD SORTENTS system variable. Otherwise, pt2 is set to nil.

NOTE:The AutoCAD APERTURE system variable determines the allowable proximity of a selected point to an object when you use Object
Snap.

#### Related Concepts

* [About Geometric Utilities (AutoLISP)](About-Geometric-Utilities-AutoLISP.md)
* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)
* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*