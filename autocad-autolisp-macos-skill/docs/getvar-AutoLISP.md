# getvar (AutoLISP)

Retrieves the value of an AutoCAD system variable

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getvar varname)
```

*varname*
:   *Type:* String

    Names of a system variable.

    See the product's Help system for a list of current AutoCAD system variables.

## Return Values

*Type:* Integer, Real, String, List, or nil

The value of the system variable; otherwise
nil, if
*varname* is not a valid system variable.

## Examples

Get the current value of the fillet radius:

```
(getvar 'FILLETRAD)
0.25
```

#### Related References

* [setvar (AutoLISP)](setvar-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*