# rotate3d (AutoLISP/External Function)

Rotates an object about an arbitrary 3D axis

*Supported Platforms:* AutoCAD for Windows and Mac OS only; not available in AutoCAD LT

*Prerequisites:*The Geom3d ObjectARX application must be loaded before the function can be called,
(arxload "geom3d").

## Signature

```
(rotate3d args ...)
```

*args*
:   *Type:* String, List, Ename (entity name), or nil

    The order, number, and type of arguments for the
    rotate3d function are the same as if you were using the AutoCAD ROTATE3D command.

    A null response (a user pressing Enter) can be indicated by specifying
    nil or an empty string ("").

## Return Values

*Type:* T or nil

If successful,
rotate3d returns
T; otherwise it returns
nil.

## Examples

The following example rotates the selected objects 30 degrees about the axis specified by points
*p1* and
*p2*.

```
(setq ss (ssget))
(setq p1 (getpoint "\
Point1: "))
(setq p2 (getpoint "\
Point2: "))
(rotate3d ss p1 p2 30)
```

AutoLISP support for the
rotate3d function is implemented with the use of the SAGET library.

#### Related References

* [Externally Defined Commands (AutoLISP)](Externally-Defined-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*