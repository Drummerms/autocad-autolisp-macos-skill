# setcfg (AutoLISP)

Obsolete. Writes application data to the AppData section of the
 *acad20xx.cfg* file

NOTE:This function might be removed in a future release. As an alternative, use the
vl-registry-write function to store application data in the Windows Registry on Windows or property list file on Mac OS.

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(setcfg cfgname cfgval)
```

*cfgname*
:   *Type:* String

    Section and parameter to set with the value of
    *cfgval*. The
    *cfgname* argument must be a string of the following form:

    AppData/*application\_name*/*section\_name*/.../*param\_name*

    The string can be up to 496 characters long.

*cfgval*
:   *Type:* String

    Application data. The string can be up to 512 characters in length. Larger strings are accepted by
    setcfg, but cannot be returned by
    getcfg.

## Return Values

If successful,
setcfg returns
*cfgval*. If
*cfgname* is not valid,
setcfg returns
nil.

## Examples

The following code sets the WallThk parameter in the AppData/ArchStuff section to 8, and returns the string “8”:

```
(setcfg "AppData/ArchStuff/WallThk" "8")
"8"
```

#### Related References

* [getcfg (AutoLISP)](getcfg-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*