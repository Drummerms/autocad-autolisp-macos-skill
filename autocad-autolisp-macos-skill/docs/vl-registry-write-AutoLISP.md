# vl-registry-write (AutoLISP)

Creates a key in the Windows Registry or property list file on Mac OS

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(vl-registry-write reg-key [val-name val-data])
```

*reg-key*
:   *Type:* String

    Windows registry key or property list file key on Mac OS.

    NOTE:You cannot use
    vl-registry-write for HKEY\_USERS or KEY\_LOCAL\_MACHINE.

*val-name*
:   *Type:* String

    Value name for the key.

*val-data*
:   *Type:* String

    Data for the value name.

## Return Values

*Type:* String or nil

vl-registry-write returns
*val-data*, if successful; otherwise
nil.

## Remarks

If
*val-name* is not supplied or is
nil, a default value for the key is written. If
*val-name* is supplied and
*val-data* is not specified, an empty string is stored.

## Examples

```
(vl-registry-write "HKEY_CURRENT_USER\\Test" "" "test data")
"test data"

(vl-registry-read "HKEY_CURRENT_USER\\Test")
"test data"
```

#### Related References

* [vl-registry-delete (AutoLISP)](vl-registry-delete-AutoLISP.md)
* [vl-registry-descendents (AutoLISP)](vl-registry-descendents-AutoLISP.md)
* [vl-registry-read (AutoLISP)](vl-registry-read-AutoLISP.md)
* [vlax-machine-product-key (AutoLISP/ActiveX)](vlax-machine-product-key-AutoLISP-ActiveX.md)
* [vlax-product-key (AutoLISP/ActiveX)](vlax-product-key-AutoLISP-ActiveX.md)
* [vlax-user-product-key (AutoLISP/ActiveX)](vlax-user-product-key-AutoLISP-ActiveX.md)

#### Related Concepts

* [Windows Registry and Property List File Functions Reference (AutoLISP)](Windows-Registry-and-Property-List-File-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*