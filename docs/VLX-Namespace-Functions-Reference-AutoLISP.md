# VLX Namespace Functions Reference (AutoLISP)

The VLX namespace functions listed below apply to separate-namespace VLX applications. These functions allow separate-namespace
VLX functions to be accessible from a document namespace, enable the retrieval and updating of variables in the associated
document namespace, and provide error-handling routines for separate-namespace VLX functions.

| VLX namespace functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(vl-arx-import [ function | application])](vl-arx-import-AutoLISP.md) | Imports ADS-DEFUN functions into a separate-namespace VLX | ✓ | ✓ | / - supported, but behavior is different than on Windows | -- | / - supported, but behavior is different than on Windows |
| [(vl-doc-export 'function)](vl-doc-export-AutoLISP.md) | Makes a function loaded in a VLX namespace available to the current document | ✓ | ✓ | / - supported, but behavior is different than on Windows | -- | / - supported, but behavior is different than on Windows |
| [(vl-doc-import ['function | application])](vl-doc-import-AutoLISP.md) | Imports a function that was previously exported from another separate-namespace VLX | ✓ | ✓ | / - supported, but behavior is different than on Windows | -- | / - supported, but behavior is different than on Windows |
| [(vl-doc-ref symbol)](vl-doc-ref-AutoLISP.md) | Retrieves the value of a variable from the namespace of the associated document | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-doc-set symbol value)](vl-doc-set-AutoLISP.md) | Sets the value of a variable in the associated document's namespace | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-exit-with-error "msg")](vl-exit-with-error-AutoLISP.md) | Passes control from a VLX error handler to the \*error\* function of the associated document namespace | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-exit-with-value value)](vl-exit-with-value-AutoLISP.md) | Returns a value to the document namespace from which the VLX was invoked | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-list-exported-functions [“appname”])](vl-list-exported-functions-AutoLISP-Visual-LISP-IDE.md) | Lists all functions exported by the specified application, or all exported functions if no application is specified | ✓ | ✓ | / - supported, but does not affect the program | -- | / - supported, but does not affect the program |
| [(vl-list-loaded-vlx)](vl-list-loaded-vlx-AutoLISP.md) | Returns a list of all separate-namespace VLX files associated with the current document | ✓ | ✓ | / - supported, but does not affect the program | -- | / - supported, but does not affect the program |
| [(vl-unload-vlx "appname")](vl-unload-vlx-AutoLISP.md) | Unloads a VLX that is loaded in its own namespace (a separate-namespace VLX) | ✓ | ✓ | / - supported, but does not affect the program | -- | / - supported, but does not affect the program |
| [(vl-vlx-loaded-p "appname")](vl-vlx-loaded-p-AutoLISP.md) | Determines whether a VLX is loaded in its own namespace | ✓ | ✓ | / - supported, but does not affect the program | -- | / - supported, but does not affect the program |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*