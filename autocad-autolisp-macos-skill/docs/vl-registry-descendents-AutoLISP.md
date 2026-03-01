# vl-registry-descendents (AutoLISP)

Returns a list of subkeys or value names for the specified key of the Windows Registry or property list file on Mac OS

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(vl-registry-descendents reg-key [val-names])
```

*reg-key*
:   *Type:* String

    Windows registry key or property list file key on Mac OS.

*val-names*
:   *Type:* String

    Values for the
    *reg-key* entry.

## Return Values

*Type:* List or nil

A list of strings, if successful; otherwise
nil.

## Remarks

If
*val-names* is supplied and is not
nil, the specified value names will be listed from the registry. If
*val-name* is absent or
nil, the function displays all subkeys of
*reg-key*.

## Examples

```
(vl-registry-descendents "HKEY_LOCAL_MACHINE\\SOFTWARE")
("Description" "Program Groups" "ORACLE" "ODBC" "Netscape" "Microsoft")
```

#### Related References

* [vl-registry-delete (AutoLISP)](vl-registry-delete-AutoLISP.md)
* [vl-registry-read (AutoLISP)](vl-registry-read-AutoLISP.md)
* [vl-registry-write (AutoLISP)](vl-registry-write-AutoLISP.md)
* [vlax-machine-product-key (AutoLISP/ActiveX)](vlax-machine-product-key-AutoLISP-ActiveX.md)
* [vlax-product-key (AutoLISP/ActiveX)](vlax-product-key-AutoLISP-ActiveX.md)
* [vlax-user-product-key (AutoLISP/ActiveX)](vlax-user-product-key-AutoLISP-ActiveX.md)

#### Related Concepts

* [Windows Registry and Property List File Functions Reference (AutoLISP)](Windows-Registry-and-Property-List-File-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*