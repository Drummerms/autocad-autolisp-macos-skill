# acet-ui-txted (AutoLISP/Express Tools)

Displays a multiline text editing dialog.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-ui-txted [text [caption [note]]])
```

text
:   *Type:* String

    If provided, a text string to be displayed as the initial contents. Lines can be separated with "\r\
    " sequences.

caption
:   *Type:* String

    If provided, text to be used as the dialog caption.

note
:   *Type:* String

    If provided, an additional text string to be displayed above the text editing control.

## Return Values

*Type:* String or
nil

A string containing the text contents if the user presses the OK button, or
nil if the user presses the Cancel button.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*