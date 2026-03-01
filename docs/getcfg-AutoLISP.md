# getcfg (AutoLISP)

Obsolete. Retrieves application data from the AppData section of the
 *acad20xx.cfg* file

NOTE:This function might be removed in a future release. As an alternative, use the
vl-registry-read function to retrieve application data from the Windows Registry on Windows or property list file on Mac OS.

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getcfg cfgname)
```

*cfgname*
:   *Type:* String

    Section name and parameter value to retrieve (maximum length of 496 characters).

The
*cfgname* argument must be a string of the following form:

```
"AppData/application_name/section_name/.../param_name"
```

## Return Values

*Type:* String or nil

Application data, if successful. If
*cfgname* is not valid,
getcfg returns
nil.

## Examples

Assuming the WallThk parameter in the AppData/ArchStuff section has a value of 8, the following command retrieves that value:

```
(getcfg "AppData/ArchStuff/WallThk")
"8"
```

#### Related References

* [setcfg (AutoLISP)](setcfg-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*