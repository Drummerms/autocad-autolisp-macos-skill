# align (AutoLISP/External Function)

Translates and rotates objects, allowing them to be aligned with other objects

*Supported Platforms:* Windows and Mac OS only

*Prerequisites:*The Geom3d ObjectARX application must be loaded before the function can be called,
(arxload "geom3d").

## Signature

```
(align args ...)
```

*args*
:   *Type:* String, List, Ename (entity name), or nil

    The order, number, and type of arguments for the
    align function are the same as if you were using the AutoCAD ALIGN command.

    A null response (a user pressing Enter) can be indicated by specifying
    nil or an empty string ("").

## Return Values

*Type:* T or nil

If successful,
align returns
T; otherwise it returns
nil.

## Examples

The following example specifies two pairs of source and destination points, which perform a 2D move and does not scale the
objects based on alignment points:

```
(setq ss (ssget))
(setq s1 (getpoint "\
Source1: "))
(setq d1 (getpoint s1 "\
Destination1: "))
(setq s2 (getpoint "\
Source2: "))
(setq d2 (getpoint s2 "\
Destination2: "))
(align ss s1 d1 s2 d2 "" "n")
T
```

#### Related References

* [Externally Defined Commands (AutoLISP)](Externally-Defined-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*