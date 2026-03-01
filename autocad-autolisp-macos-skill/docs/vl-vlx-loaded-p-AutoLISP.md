# vl-vlx-loaded-p (AutoLISP)

Determines whether a separate-namespace VLX is currently loaded

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-vlx-loaded-p appname)
```

*appname*
:   *Type:* String

    Name of a VLX application.

## Return Values

*Type:* T or nil

T if the application is loaded,
nil if it is not loaded.

## Remarks

VLX files are supported on Windows only.

NOTE:This function is supported on Mac OS and Web, but does not affect the program.

## Examples

Check to see if the
*vlxns* application is loaded in its own namespace:

```
(vl-vlx-loaded-p "vlxns")
nil
```

The application is not loaded in its own namespace.

Now load
*vlxns*:

```
(load "vlxns.vlx")
nil
```

Check to see if the
*vlxns* application loaded successfully:

```
(vl-vlx-loaded-p "vlxns")
T
```

This example assumes
*vlxns* was defined to run in its own namespace. If the application was not defined to run in its own namespace, it would load into
the current document's namespace and
vl-vlx-loaded-p would return
nil.

#### Related References

* [load (AutoLISP)](load-AutoLISP.md)
* [autoload (AutoLISP)](autoload-AutoLISP.md)
* [vl-list-exported-functions (AutoLISP/Visual LISP IDE)](vl-list-exported-functions-AutoLISP-Visual-LISP-IDE.md)
* [vl-unload-vlx (AutoLISP)](vl-unload-vlx-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*