# vlax-product-key (AutoLISP/ActiveX)

Returns the AutoCAD Windows registry path

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-product-key)
```

No arguments.

## Return Values

*Type:* String

A value containing the AutoCAD registry path.

## Remarks

The AutoCAD registry path can be used to register an application for demand loading.

## Examples

```
(vlax-product-key)
"Software\\Autodesk\\AutoCAD\\R25.1\\ACAD-9101:409"
```

#### Related References

* [vlax-machine-product-key (AutoLISP/ActiveX)](vlax-machine-product-key-AutoLISP-ActiveX.md)
* [vlax-user-product-key (AutoLISP/ActiveX)](vlax-user-product-key-AutoLISP-ActiveX.md)
* [vl-registry-delete (AutoLISP)](vl-registry-delete-AutoLISP.md)
* [vl-registry-descendents (AutoLISP)](vl-registry-descendents-AutoLISP.md)
* [vl-registry-read (AutoLISP)](vl-registry-read-AutoLISP.md)
* [vl-registry-write (AutoLISP)](vl-registry-write-AutoLISP.md)

#### Related Concepts

* [Windows Registry and Property List File Functions Reference (AutoLISP)](Windows-Registry-and-Property-List-File-Functions-Reference-AutoLISP.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*