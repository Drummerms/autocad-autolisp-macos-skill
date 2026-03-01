# acet-ui-status (AutoLISP/Express Tools)

Displays a modeless status dialog.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-ui-status [message [caption]])
```

message
:   *Type:* String

    If provided, a text string to be displayed in the dialog.

caption
:   *Type:* String

    If provided, a text string to be used as the dialog caption.

NOTE:If no arguments are provided, the dialog is hidden.

## Return Values

*Type:* nil

Returns
nil.

## Remarks

The status dialog may be moved by the user. It will remember it's position and contents during the current session.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*