# vl-load-com (AutoLISP/ActiveX)

Loads the extended AutoLISP functions related to ActiveX support

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vl-load-com)
```

No arguments.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

This function loads the extended functions that implement ActiveX and AutoCAD reactor support for AutoLISP, and also provide
ActiveX utility and data conversion, dictionary handling, and curve measurement functions.

If the extensions are already loaded,
vl-load-com does nothing.

## Examples

```
(vl-load-com)
```

#### Related References

* [vl-load-reactors (AutoLISP/ActiveX)](vl-load-reactors-AutoLISP-ActiveX.md)

#### Related Concepts

* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*