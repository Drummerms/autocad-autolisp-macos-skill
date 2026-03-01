# acet-ini-set (AutoLISP/Express Tools)

Writes data to an INI file.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-ini-set inifile section [key [value]])
```

*inifile*
:   *Type:* String

    Name of the INI file to modify.

*section*
:   *Type:* String

    A string containing the name of the section for the given data. If the section does not exist, it will be created.

*key*
:   *Type:* String

    A string containing the name of the key to be associated with a value. If the key does not exist in the given section, it
    will be created. If this parameter is not given, the entire section (including all entries within the section) will be deleted.

*value*
:   *Type:* String

    A string to be assigned to key. If this parameter is not given, the key will be deleted.

## Return Values

*Type:* T

T if successful.

## Remarks

For more information, see the
WritePrivateProfileString() Win32 function.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*