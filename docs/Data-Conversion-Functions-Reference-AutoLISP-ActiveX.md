# Data Conversion Functions Reference (AutoLISP/ActiveX)

NOTE:ActiveX support in AutoLISP is limited to Windows only; not available on Mac OS or Web.

The following table provides summary descriptions of the AutoLISP ActiveX data conversion functions.

| Data conversion functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(vlax-3D-point list)](vlax-3D-point-AutoLISP-ActiveX.md) | Creates an ActiveX-compatible 3D point structure | ✓ | ✓ | -- | -- | -- |
| [(vlax-ename->vla-object entname)](vlax-ename-vla-object-AutoLISP-ActiveX.md) | Transforms entity to VLA-object | ✓ | ✓ | -- | -- | -- |
| [(vlax-make-safearray type '(l-bound . u-bound) ['( l-bound . u-bound) ...])](vlax-make-safearray-AutoLISP-ActiveX.md) | Creates a safearray | ✓ | ✓ | -- | -- | -- |
| [(vlax-make-variant value type)](vlax-make-variant-AutoLISP-ActiveX.md) | Creates a variant data type | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-fill var 'element-values)](vlax-safearray-fill-AutoLISP-ActiveX.md) | Stores elements in a safearray | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-get-dim var)](vlax-safearray-get-dim-AutoLISP-ActiveX.md) | Returns the number of dimensions in a safearray object | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-get-element var element)](vlax-safearray-get-element-AutoLISP-ActiveX.md) | Returns an element from an array | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-get-l-bound var dim)](vlax-safearray-get-l-bound-AutoLISP-ActiveX.md) | Returns the lower boundary (starting index) of a dimension of an array | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-get-u-bound var dim)](vlax-safearray-get-u-bound-AutoLISP-ActiveX.md) | Returns the upper boundary (end index) of a dimension of an array | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-put-element var element value)](vlax-safearray-put-element-AutoLISP-ActiveX.md) | Adds or updates an element in an array | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray-type var)](vlax-safearray-type-AutoLISP-ActiveX.md) | Returns the data type of a safearray | ✓ | ✓ | -- | -- | -- |
| [(vlax-safearray->list var)](vlax-safearray-list-AutoLISP-ActiveX.md) | Returns the elements of a safearray in list form | ✓ | ✓ | -- | -- | -- |
| [(vlax-tmatrix list)](vlax-tmatrix-AutoLISP-ActiveX.md) | Returns a suitable representation for a 4 x 4 transformation matrix to be used in VLA methods | ✓ | ✓ | -- | -- | -- |
| [(vlax-variant-change-type var type)](vlax-variant-change-type-AutoLISP-ActiveX.md) | Returns the value of a variant after changing it from one data type to another | ✓ | ✓ | -- | -- | -- |
| [(vlax-variant-type var)](vlax-variant-type-AutoLISP-ActiveX.md) | Returns the data type of a variant | ✓ | ✓ | -- | -- | -- |
| [(vlax-variant-value var)](vlax-variant-value-AutoLISP-ActiveX.md) | Returns the value of a variant | ✓ | ✓ | -- | -- | -- |
| [(vlax-vla-object->ename obj)](vlax-vla-object-ename-AutoLISP-ActiveX.md) | Transforms a VLA-object to an AutoLISP entity | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*