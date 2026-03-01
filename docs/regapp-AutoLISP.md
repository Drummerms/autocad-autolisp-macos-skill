# regapp (AutoLISP)

Registers an application name with the current AutoCAD drawing in preparation for using extended object data

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(regapp application)
```

*application*
:   *Type:* String

    Application name. The name must be a valid symbol table name.

## Return Values

*Type:* String

If an application of the same name has already been registered, this function returns
nil; otherwise it returns the name of the application.

If registered successfully, the application name is entered into the APPID symbol table. This table maintains a list of the
applications that are using extended data in the drawing.

## Examples

```
(regapp "ADESK_4153322344")
"ADESK_4153322344"

(regapp "DESIGNER-v2.1-124753")
"DESIGNER-v2.1-124753"
```

NOTE:It is recommended that you pick a unique application name. One way of ensuring this is to adopt a naming scheme that uses
the company or product name and a unique number (like your telephone number or the current date/time). The product version
number can be included in the application name or stored by the application in a separate integer or real-number field; for
example,
(1040 2.1).

#### Related References

* [xdroom (AutoLISP)](xdroom-AutoLISP.md)
* [xdsize (AutoLISP)](xdsize-AutoLISP.md)

#### Related Concepts

* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*