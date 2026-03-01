# getcname (AutoLISP)

Retrieves the localized or English name of an AutoCAD command

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getcname cname)
```

*cname*
:   *Type:* String

    The localized or underscored English command name; must be 64 characters or less in length.

## Return Values

If
*cname* is not preceded by an underscore (assumed to be the localized command name),
getcname returns the underscored English command name. If
*cname* is preceded by an underscore,
getcname returns the localized command name. This function returns
nil if
*cname* is not a valid command name.

## Examples

In a French version of AutoCAD, the following is True.

```
(getcname "ETIRER")
"_STRETCH"

(getcname "_STRETCH")
"ETIRER"
```

#### Related References

* [command (AutoLISP)](command-AutoLISP.md)
* [command-s (AutoLISP)](command-s-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*