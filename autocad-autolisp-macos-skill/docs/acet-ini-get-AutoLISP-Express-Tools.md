# acet-ini-get (AutoLISP/Express Tools)

Retrieves data from an INI file.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-ini-get inifile [section [key [default]]])
```

*inifile*
:   *Type:* String

    Name of the INI file to search.

*section*
:   *Type:* String

    Section name within the INI file.

*key*
:   *Type:* String

    Key name within the section.

*default*
:   *Type:* String

    Default value to return if key cannot be located.

## Return Values

*Type:* List, string, or
nil

The return value depends on the parameters provided. If only
*inifile* is given, this function returns a list of section names (or
nil if
*inifile* cannot be opened). If a section name is given, a list of key names will be returned. If a key is given, returns the value
associated with the key (or default, if the key cannot be located). Returns
nil if no information can be found.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*