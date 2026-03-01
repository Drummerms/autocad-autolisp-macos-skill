# acet-help-trap (AutoLISP/Express Tools)

Installs a F1 key monitor.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-help-trap command [topic [file]])
```

*command*
:   *Type:* String

    The name of the command to monitor, as would be passed to
    (setfunhelp).

*topic*
:   *Type:* String

    The topic name in the help file. If this argument is nil or not supplied, any help trap attached to command will be released.

*file*
:   *Type:* String

    The name of the help file to use. If not provided,
    *acet.chm* is used.

## Return Values

*Type:* T

T if successful.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*