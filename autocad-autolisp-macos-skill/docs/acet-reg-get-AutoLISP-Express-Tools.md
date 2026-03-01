# acet-reg-get (AutoLISP/Express Tools)

Returns a value from the Registry.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-reg-get key [name])
```

key
:   *Type:* String

    Key name to retrieve.

name
:   *Type:* String

    If given, value name to retrieve.

## Return Values

*Type:* String or
nil

The selected value, or
nil if the entry cannot be located.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*