# acet-ui-pickdir (AutoLISP/Express Tools)

Displays a directory selection dialog.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-ui-pickdir [message [startDir [caption]]])
```

message
:   *Type:* String

    If provided, a message to be displayed in the space above the directory tree control.

startDir
:   *Type:* String

    If provided, the initial directory to be selected.

caption
:   *Type:* String

    If provided, the dialog caption.

## Return Values

*Type:* String or
nil

A string containing the name of the selected directory, or
nil if the dialog was canceled.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*