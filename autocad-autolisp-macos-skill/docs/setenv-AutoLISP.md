# setenv (AutoLISP)

Sets a system environment variable to a specified value

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(setenv varname value)
```

*varname*
:   *Type:* String

    Name of the environment variable to be set. Environment variable names must be spelled and cased exactly as they are stored
    in the system registry.

*value*
:   *Type:* String

    Value to set
    *varname* to.

## Return Values

*Type:* String

Value provided with the
*value* argument.

## Examples

The following command sets the value of the
MaxArray environment variable to 10000:

```
(setenv "MaxArray" "10000")
"10000"
```

Note that changes to settings might not take effect until the next time AutoCAD is started.

#### Related References

* [getenv (AutoLISP)](getenv-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*