# Windows Registry and Property List File Functions Reference (AutoLISP)

Windows Registry and property list (PLIST) file functions query and update the Windows Registry on Windows or property list
files on Mac OS.

| Windows Registry and Property List File functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(vl-registry-delete reg-key [val-name])](vl-registry-delete-AutoLISP.md) | Deletes the specified key from the Windows Registry or property list file on Mac OS | ✓ | ✓ | ✓ | -- | -- |
| [(vl-registry-descendents reg-key [val-names])](vl-registry-descendents-AutoLISP.md) | Returns a list of subkeys or value names for the specified key of the Windows Registry or property list file on Mac OS | ✓ | ✓ | ✓ | -- | -- |
| [(vl-registry-read reg-key [val-name])](vl-registry-read-AutoLISP.md) | Returns data stored by a specific key/value pair in the Windows Registry or property list file on Mac OS | ✓ | ✓ | ✓ | -- | -- |
| [(vl-registry-write reg-key [val-name val-data])](vl-registry-write-AutoLISP.md) | Creates a key in the Windows Registry or property list file on Mac OS | ✓ | ✓ | ✓ | -- | -- |
| [(vlax-machine-product-key)](vlax-machine-product-key-AutoLISP-ActiveX.md) | Returns the AutoCAD Windows Registry path in the HKLM (HKEY\_LOCAL\_MACHINE)  NOTE:Available on Windows only and requires a call to the vl-load-com function. | ✓ | ✓ | -- | -- | -- |
| [(vlax-product-key)](vlax-product-key-AutoLISP-ActiveX.md) | Returns the AutoCAD Windows Registry path (Obsolete)  NOTE:Use the vlax-machine-product-key function instead. | ✓ | ✓ | -- | -- | -- |
| [(vlax-user-product-key)](vlax-user-product-key-AutoLISP-ActiveX.md) | Returns the AutoCAD Windows registry path in the HKCU (HKEY\_CURRENT\_USER)  NOTE:Available on Windows only and requires a call to the vl-load-com function. | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*