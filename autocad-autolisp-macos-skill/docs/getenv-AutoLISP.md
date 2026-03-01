# getenv (AutoLISP)

Returns the string value assigned to a system environment variable

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getenv variable-name)
```

*variable-name*
:   *Type:* String

    A string specifying the name of the variable to be read. Environment variable names must be spelled and cased exactly as they
    are stored in the system registry.

## Return Values

*Type:* String or nil

A string representing the value assigned to the specified system variable. If the variable does not exist,
getenv returns
nil.

## Examples

Assume the system environment variable
ACAD is set to
*/acad/support* and there is no variable named
NOSUCH.

```
(getenv "ACAD")
"/acad/support"

(getenv "NOSUCH")
nil
```

Assume that the
MaxArray environment variable is set to 10000:

```
(getenv "MaxArray")
"10000"
```

#### Related References

* [setenv (AutoLISP)](setenv-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*