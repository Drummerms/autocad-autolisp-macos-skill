# vl-registry-delete (AutoLISP)

Deletes the specified key from the Windows Registry or property list file on Mac OS

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(vl-registry-delete reg-key [val-name])
```

*reg-key*
:   *Type:* String

    Windows registry key or property list file key on Mac OS.

*val-name*
:   *Type:* String

    Value of the
    *reg-key* entry.

## Return Values

*Type:* T or nil

T if successful; otherwise
nil.

## Remarks

If *val-name* is supplied and is not
nil, the specified value will be purged from the registry or property list file. If
*val-name*is absent or
nil, the function deletes the specified key and all of its values.

## Examples

```
(vl-registry-write "HKEY_CURRENT_USER\\Test" "" "test data")
"test data"

(vl-registry-read "HKEY_CURRENT_USER\\Test")
"test data"

(vl-registry-delete "HKEY_CURRENT_USER\\Test")
T
```

NOTE:This function cannot delete a key that has subkeys. To delete a subkey you must use
vl-registry-descendents to enumerate all subkeys and delete all of them.

#### Related References

* [vl-registry-descendents (AutoLISP)](vl-registry-descendents-AutoLISP.md)
* [vl-registry-read (AutoLISP)](vl-registry-read-AutoLISP.md)
* [vl-registry-write (AutoLISP)](vl-registry-write-AutoLISP.md)
* [vlax-machine-product-key (AutoLISP/ActiveX)](vlax-machine-product-key-AutoLISP-ActiveX.md)
* [vlax-product-key (AutoLISP/ActiveX)](vlax-product-key-AutoLISP-ActiveX.md)
* [vlax-user-product-key (AutoLISP/ActiveX)](vlax-user-product-key-AutoLISP-ActiveX.md)

#### Related Concepts

* [Windows Registry and Property List File Functions Reference (AutoLISP)](Windows-Registry-and-Property-List-File-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*