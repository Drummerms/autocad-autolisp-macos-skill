# vl-list-exported-functions (AutoLISP/Visual LISP IDE)

Lists exported functions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-list-exported-functions [appname])
```

*appname*
:   *Type:* String

    Name of a loaded VLX application. Do
    *not* include the
    *.vlx* extension.

## Return Values

*Type:* List

A list of strings naming exported functions; otherwise
nil, if there are no functions exported from the specified VLX. If
*appname* is omitted or is
nil,
vl-list-exported-functions returns a list of all exported functions (for example,
*c:* functions) except those exported from VLX namespaces.

## Remarks

VLX files are supported on Windows only.

NOTE:This function is supported on Mac OS and Web, but does not affect the program.

## Examples

```
(vl-list-exported-functions "whichexpns")
("WHICHNAMESPACE")
```

#### Related References

* [load (AutoLISP)](load-AutoLISP.md)
* [vl-load-all (AutoLISP)](vl-load-all-AutoLISP.md)
* [vl-unload-vlx (AutoLISP)](vl-unload-vlx-AutoLISP.md)
* [vl-vlx-loaded-p (AutoLISP)](vl-vlx-loaded-p-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*