# solprof (AutoLISP/External Function)

Creates profile images of three-dimensional solids

*Supported Platforms:* AutoCAD for Windows and Mac OS only; not available in AutoCAD LT

*Prerequisites:*The AcSolids ObjectARX application must be loaded before the function can be called,
(arxload "acsolids"). Earlier releases might require you to load the
*acsolids.arx* or
*solids.arx* file.

## Signature

```
(c:solprof args ...)
```

*args*
:   *Type:* String or Ename (entity name)

    The order, number, and type of arguments are the same as those specified when using the AutoCAD SOLPROF command.

## Return Values

*Type:* nil or error

If successful,
solprof returns
nil; otherwise an error occurs.

## Examples

```
(setq ss (ssget))
(c:solprof ss "y" "y" "n")
nil
```

#### Related References

* [Externally Defined Commands (AutoLISP)](Externally-Defined-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*