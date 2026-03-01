# client\_data\_tile (AutoLISP/DCL)

Associates application-managed data with a dialog box tile

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(client_data_tile key clientdata)
```

*key*
:   *Type:* String

    Value that specifies a tile. This argument is case-sensitive.

*clientdata*
:   *Type:* String

    Value to be associated with the
    *key* tile. An action expression or callback function can refer to the string as
    $data.

## Return Values

Always returns
nil.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related Concepts

* [Application-Specific Data-Handling Function Reference (AutoLISP/DCL)](Application-Specific-Data-Handling-Function-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*