# vl-unload-vlx (AutoLISP)

Unload a VLX application that is loaded in its own namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-unload-vlx appname)
```

*appname*
:   *Type:* String

    Name of a VLX application that is loaded in its own namespace. Do not include the
    *.vlx* extension.

## Return Values

*Type:* T or error

T if successful; otherwise
vl-unload-vlx results in an error.

## Remarks

The
vl-unload-vlx function does not unload VLX applications that are loaded in the current document's namespace.

VLX files are supported on Windows only.

NOTE:This function is supported on Mac OS and Web, but does not affect the program.

## Examples

Assuming that
*vlxns* is an application that is loaded in its own namespace, the following command unloads
*vlxns*:

```
(vl-unload-vlx "vlxns")
T
```

Try unloading
*vlxns* again:

```
(vl-unload-vlx "vlxns")
; *** ERROR: LISP Application is not found VLXNS
```

The
vl-unload-vlx command fails this time, because the application was not loaded.

#### Related References

* [load (AutoLISP)](load-AutoLISP.md)
* [autoload (AutoLISP)](autoload-AutoLISP.md)
* [vl-list-exported-functions (AutoLISP/Visual LISP IDE)](vl-list-exported-functions-AutoLISP-Visual-LISP-IDE.md)
* [vl-vlx-loaded-p (AutoLISP)](vl-vlx-loaded-p-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*