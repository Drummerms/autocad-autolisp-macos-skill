# tablet (AutoLISP)

Retrieves and sets digitizer (tablet) calibrations

*Supported Platforms:* Windows only

## Signature

```
(tablet code [row1 row2 row3 direction])
```

*code*
:   *Type:* Integer

    One of the following:

    *0* -- Return the current digitizer calibration. In this case, the remaining arguments must be omitted.

    *1* -- Set the calibration according to the arguments that follow. In this case, you must provide the new calibration settings
    (*row1,**row2,**row3,* and *direction*).

*row1, row2, row3*
:   *Type:* List

    Three 3D points. These three arguments specify the three rows of the tablet's transformation matrix.

    The third element in *row3* (*Z*) should always equal 1: tablet returns it as 1 even if you specify a different value in *row3*.

*direction*
:   *Type:* List

    One 3D point. This is the vector (expressed in the world coordinate system, or WCS) that is normal to the plane that represents
    the surface of the tablet.

    If the specified *direction* isn't normalized, tablet corrects it, so the *direction* it returns when you set the calibration may differ from the value you passed.

## Return Values

*Type:* Integer or nil

If tablet fails, it returns nil and sets the AutoCAD ERRNO system variable to a value that indicates the reason for the failure. This can happen if the digitizer
is not a tablet.

## Examples

A very simple transformation that can be established with tablet is the identity transformation:

```
(tablet 1 '(1 0 0) '(0 1 0) '(0 0 1) '(0 0 1))
```

With this transformation in effect, AutoCAD will receive, effectively, raw digitizer coordinates from the tablet. For example,
if you pick the point with digitizer coordinates (5000,15000), AutoCAD will see it as the point in your drawing with those
same coordinates.

The AutoCAD TABMODE system variable allows AutoLISP routines to toggle the tablet on and off.

#### Related References

* [grread (AutoLISP)](grread-AutoLISP.md)

#### Related Concepts

* [Device Access Functions Reference (AutoLISP)](Device-Access-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*