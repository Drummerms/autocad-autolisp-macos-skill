# grvecs (AutoLISP)

Draws multiple vectors in the drawing area

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(grvecs vlist [trans])
```

*vlist*
:   *Type:* List

    A vector list is composed of a series of optional color integers and two point lists. See below for details on how to format
    *vlist*.

*trans*
:   *Type:* List

    A transformation matrix used to change the location or proportion of the vectors defined in your vector list. This matrix
    is a list of four lists of four real numbers.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

The format for
*vlist* is as follows:

```
([color1] from1 to1 [color2] from2 to2 ...)
```

The color value applies to all succeeding vectors until
*vlist* specifies another color. AutoCAD colors are in the range 0-255. If the color value is greater than 255, succeeding vectors
are drawn in
*XOR ink*, which complements anything it draws over and which erases itself when overdrawn. If the color value is less than zero, the
vector is highlighted. Highlighting depends on the display device. Most display devices indicate highlighting by a dashed
line, but some indicate it by using a distinctive color.

A pair of point lists,
*from* and
*to*, specify the endpoints of the vectors, expressed in the current UCS. These can be 2D or 3D points. You must pass these points
as pairs—two successive point lists—or the
grvecs call will fail.

AutoCAD clips the vectors as required to fit on the screen.

## Examples

The following code draws five vertical lines in the drawing area, each a different color:

```
(grvecs '(1 (1 2)(1 5)       Draws a red line from (1,2) to (1,5)
          2 (2 2)(2 5)       Draws a yellow line from (2,2) to (2,5)
          3 (3 2)(3 5)       Draws a green line from (3,2) to (3,5)
          4 (4 2)(4 5)       Draws a cyan line from (4,2) to (4,5)
          5 (5 2)(5 5)       Draws a blue line from (5,2) to (5,5)
) )
```

The following matrix represents a uniform scale of 1.0 and a translation of 5.0,5.0,0.0. If this matrix is applied to the
preceding list of vectors, they will be offset by 5.0,5.0,0.0.

```
'((1.0 0.0 0.0 5.0)
   (0.0 1.0 0.0 5.0)
   (0.0 0.0 1.0 0.0)
   (0.0 0.0 0.0 1.0)
)
```

#### Related References

* [grdraw (AutoLISP)](grdraw-AutoLISP.md)
* [grclear (AutoLISP)](grclear-AutoLISP.md)
* [redraw (AutoLISP)](redraw-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*