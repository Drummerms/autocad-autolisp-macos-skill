# vl-list-loaded-vlx (AutoLISP)

Returns a list of all separate-namespace VLX files associated with the current document

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-list-loaded-vlx)
```

No arguments.

## Return Values

*Type:* List or nil

A list of symbols identifying separate-namespace VLX applications associated with the current AutoCAD document; otherwise
nil, if there are no VLX applications associated with the current document.

The
vl-list-loaded-vlx function does not identify VLX applications that are loaded in the current document's namespace.

## Remarks

VLX files are supported on Windows only.

NOTE:This function is supported on Mac OS and Web, but does not affect the program.

## Examples

Test for loaded VLX files associated with the current AutoCAD document:

```
(vl-list-loaded-vlx)
nil
```

No VLX files are associated with the current document.

Load two VLX files; both VLX applications have been compiled to run in their own namespace:

```
(load "c:/my documents/visual lisp/examples/foo1.vlx")
nil

(load "c:/my documents/visual lisp/examples/foo2.vlx")
nil
```

Test for loaded VLX files associated with the current AutoCAD document:

```
(vl-list-loaded-vlx)
(FOO1 FOO2)
```

The two VLX files just loaded are identified by
vl-list-loaded-vlx.

Load a VLX that was compiled to run in a document's namespace:

```
(load "c:/my documents/visual lisp/examples/foolocal.vlx")
nil
```

Test for loaded VLX files:

```
(vl-list-loaded-vlx)
(FOO1 FOO2))
```

The last VLX loaded (*foolocal.vlx*) is not returned by
vl-list-loaded-vlx because the application was loaded into the document's namespace; the VLX does not have its own namespace.

#### Related References

* [vl-unload-vlx (AutoLISP)](vl-unload-vlx-AutoLISP.md)
* [vl-vlx-loaded-p (AutoLISP)](vl-vlx-loaded-p-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*