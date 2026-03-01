# grdraw (AutoLISP)

Draws a vector between two points, in the current viewport

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(grdraw from to color [highlight])
```

*from*
:   *Type:* List

    2D or 3D points (lists of two or three reals) specifying one endpoint of the vector in terms of the current UCS. AutoCAD clips
    the vector to fit the screen.

*to*
:   *Type:* List

    2D or 3D points (lists of two or three reals) specifying the other endpoint of the vector in terms of the current UCS. AutoCAD
    clips the vector to fit the screen.

*color*
:   *Type:* Integer

    Color used to draw the vector. A -1 signifies
    *XOR ink*, which complements anything it draws over and which erases itself when overdrawn.

*highlight*
:   *Type:* Integer

    Other than zero, indicates that the vector is to be drawn using the default highlighting method of the display device (usually
    dashed).

    If
    *highlight* is omitted or is zero,
    grdraw uses the normal display mode.

## Return Values

*Type:* nil

Always returns
nil.

## Examples

N/A

#### Related References

* [grvecs (AutoLISP)](grvecs-AutoLISP.md)
* [grclear (AutoLISP)](grclear-AutoLISP.md)
* [redraw (AutoLISP)](redraw-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*