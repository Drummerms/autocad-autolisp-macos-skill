# osnap (AutoLISP)

Returns a 3D point that is the result of applying an Object Snap mode to a specified point

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(osnap pt mode)
```

*pt*
:   *Type:* List

    A point.

*mode*
:   *Type:* String

    One or more valid Object Snap identifiers, such as
    mid,
    cen, and so on, separated by commas.

## Return Values

*Type:* List or nil

A point; otherwise
nil, if the pick did not return an object (for example, if there is no geometry under the pick aperture, or if the geometry is
not applicable to the selected object snap mode). The point returned by
osnap depends on the current 3D view, the AutoCAD entity around
*pt*, and the setting of the AutoCAD APERTURE system variable.

## Remarks

Starting with AutoCAD 2016-based products, the
qui mode is no longer valid. Using the
qui mode results in a value of
nil to be returned, even if other modes are specified.

## Examples

```
(setq pt1 (getpoint))
(11.8637 3.28269 0.0)

(setq pt2 (osnap pt1 "_end,_int"))
(12.1424 3.42181 0.0)
```

#### Related References

* [inters (AutoLISP)](inters-AutoLISP.md)
* [polar (AutoLISP)](polar-AutoLISP.md)

#### Related Concepts

* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*