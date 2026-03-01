# vports (AutoLISP)

Returns a list of viewport descriptors for the current viewport configuration

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vports)
```

No arguments.

## Return Values

*Type:* List

One or more viewport descriptor lists consisting of the viewport identification number and the coordinates of the viewport's
lower-left and upper-right corners.

If the AutoCAD TILEMODE system variable is set to 1 (on), the returned list describes the viewport configuration created with
the AutoCAD VPORTS command. The corners of the viewports are expressed in values between 0.0 and 1.0, with (0.0, 0.0) representing
the lower-left corner of the display screen's graphics area, and (1.0, 1.0) the upper-right corner. If TILEMODE is 0 (off),
the returned list describes the viewport objects created with the AutoCAD MVIEW command. The viewport object corners are expressed
in paper space coordinates. Viewport number 1 is always paper space when TILEMODE is off.

## Examples

Given a single-viewport configuration with TILEMODE on, the
vports function might return the following:

```
((1 (0.0 0.0) (1.0 1.0)))
```

Given four equal-sized viewports located in the four corners of the screen when TILEMODE is on, the
vports function might return the following lists:

```
((5 (0.5 0.0) (1.0 0.5))
 (2 (0.5 0.5) (1.0 1.0))
 (3 (0.0 0.5) (0.5 1.0))
 (4 (0.0 0.0) (0.5 0.5)))
```

The current viewport's descriptor is always first in the list. In the previous example, viewport number 5 is the current viewport.

#### Related References

* [entget (AutoLISP)](entget-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*