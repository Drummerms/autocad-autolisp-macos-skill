# atoms-family (AutoLISP)

Returns a list of the currently defined symbols

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(atoms-family format [symlist])
```

*format*
:   *Type:* Integer

    An integer value of 0 or 1 that determines the format in which
    atoms-family returns the symbol names:

    *0* -- Return the symbol names as a list

    *1* -- Return the symbol names as a list of strings

*symlist*
:   *Type:* List

    A list of strings that specify the symbol names you want
    atoms-family to search for.

## Return Values

*Type:* List

A list of symbols. If you specify
symlist, then
atoms-family returns the specified symbols that are currently defined, and returns
nil for those symbols that are not defined.

## Examples

```
(atoms-family 0)
(BNS_PRE_SEL FITSTR2LEN C:AI_SPHERE ALERT DEFUN C:BEXTEND REM_GROUP
 B_RESTORE_SYSVARS BNS_CMD_EXIT LISPED FNSPLITL...)
```

The following code verifies that the symbols
CAR,
CDR, and
XYZ are defined, and returns the list as strings:

```
(atoms-family 1 '("CAR" "CDR" "XYZ"))
("CAR" "CDR" nil)
```

The return value shows that the symbol
XYZ is not defined.

#### Related References

* [atom (AutoLISP)](atom-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*