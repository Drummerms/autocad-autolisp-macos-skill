# textbox (AutoLISP)

Measures a specified text object, and returns the diagonal coordinates of a box that encloses the text

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(textbox elist)
```

*elist*
:   *Type:* List

    An entity definition list defining a text object, in the format returned by
    entget.

    If fields that define text parameters other than the text itself are omitted from
    *elist*, the current (or default) settings are used.

    The minimum list accepted by
    textbox is that of the text itself.

## Return Values

*Type:* List or nil

A list of two points, if successful; otherwise
nil.

The points returned by
textbox describe the bounding box of the text object as if its insertion point is located at (0,0,0) and its rotation angle is 0.
The first list returned is generally the point (0.0 0.0 0.0) unless the text object is oblique or vertical, or it contains
letters with descenders (such as
*g* and
*p*). The value of the first point list specifies the offset from the text insertion point to the lower-left corner of the smallest
rectangle enclosing the text. The second point list specifies the upper-right corner of that box. Regardless of the orientation
of the text being measured, the point list returned always describes the lower-left and upper-right corners of this bounding
box.

## Examples

The following command supplies the text and accepts the current defaults for the remaining parameters:

```
(textbox '((1 . "Hello world.")))
((0.000124126 -0.00823364 0.0) (3.03623 0.310345 0.0))
```

#### Related Concepts

* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*