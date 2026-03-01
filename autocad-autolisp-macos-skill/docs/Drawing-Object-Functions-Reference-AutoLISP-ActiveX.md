# Drawing Object Functions Reference (AutoLISP/ActiveX)

NOTE:ActiveX support in AutoLISP is limited to Windows only; not available on Mac OS or Web.

The following table provides summary descriptions of the AutoLISP functions for handling drawing objects.

| Functions for handling drawing objects | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(vlax-create-object "prog-id")](vlax-create-object-AutoLISP-ActiveX.md) | Creates a new instance of an ActiveX object | ✓ | -- | -- | -- | -- |
| [(vlax-dump-object obj)](vlax-dump-object-AutoLISP-ActiveX.md) | Lists an object's methods and properties | ✓ | ✓ | -- | -- | -- |
| [(vlax-erased-p obj)](vlax-erased-p-AutoLISP-ActiveX.md) | Determines whether an object was erased | ✓ | ✓ | -- | -- | -- |
| [(vlax-get-acad-object)](vlax-get-acad-object-AutoLISP-ActiveX.md) | Retrieves the top-level AutoCAD application object for the current AutoCAD session | ✓ | ✓ | -- | -- | -- |
| [(vlax-get-object "prog-id")](vlax-get-object-AutoLISP-ActiveX.md) | Returns a running instance of an ActiveX object | ✓ | -- | -- | -- | -- |
| [(vlax-get-or-create-object "prog-id")](vlax-get-or-create-object-AutoLISP-ActiveX.md) | Returns a running instance of an ActiveX object, if one exists, otherwise starts a new instance of the object | ✓ | -- | -- | -- | -- |
| [(vlax-import-type-library :tlb-filename filename [ :methods-prefix mprefix :properties-prefix pprefix :constants-prefix cprefix])](vlax-import-type-library-AutoLISP-ActiveX.md) | Imports information from a type library | ✓ | -- | -- | -- | -- |
| [(vlax-method-applicable-p obj method)](vlax-method-applicable-p-AutoLISP-ActiveX.md) | Determines whether an object supports a particular method | ✓ | ✓ | -- | -- | -- |
| [(vlax-object-released-p obj)](vlax-object-released-p-AutoLISP-ActiveX.md) | Determines whether an object has been released | ✓ | ✓ | -- | -- | -- |
| [(vlax-read-enabled-p obj)](vlax-read-enabled-p-AutoLISP-ActiveX.md) | Determines whether an object can be read | ✓ | ✓ | -- | -- | -- |
| [(vlax-release-object obj)](vlax-release-object-AutoLISP-ActiveX.md) | Releases a drawing object | ✓ | ✓ | -- | -- | -- |
| [(vlax-typeinfo-available-p obj)](vlax-typeinfo-available-p-AutoLISP-ActiveX.md) | Determines whether type library information is present for the specified type of object | ✓ | ✓ | -- | -- | -- |
| [(vlax-write-enabled-p obj)](vlax-write-enabled-p-AutoLISP-ActiveX.md) | Determines whether an AutoCAD drawing object can be modified | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*