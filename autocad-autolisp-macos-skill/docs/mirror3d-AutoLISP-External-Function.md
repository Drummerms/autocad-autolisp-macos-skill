# mirror3d (AutoLISP/External Function)

Reflects selected objects about a user-specified plane

*Supported Platforms:* AutoCAD for Windows and Mac OS only; not available in AutoCAD LT

*Prerequisites:*The Geom3d ObjectARX application must be loaded before the function can be called,
(arxload "geom3d").

## Signature

```
(mirror3d args ...)
```

*args*
:   *Type:* String, List, Ename (entity name), or nil

    The order, number, and type of arguments for the
    mirror3d function are the same as if you were using the AutoCAD MIRROR3D command.

    A null response (a user pressing Enter) can be indicated by specifying
    nil or an empty string ("").

## Return Values

*Type:* T or nil

If successful,
mirror3d returns
T; otherwise it returns
nil.

## Examples

The following example mirrors the selected objects about the
*XY* plane that passes through the point 0,0,5, and then deletes the old objects:

```
(setq ss (ssget))
(mirror3d ss "XY" '(0 0 5) "Y")
T
```

#### Related References

* [Externally Defined Commands (AutoLISP)](Externally-Defined-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*