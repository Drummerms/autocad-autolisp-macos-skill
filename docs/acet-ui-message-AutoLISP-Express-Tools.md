# acet-ui-message (AutoLISP/Express Tools)

Displays a message box.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-ui-message message [caption [type]])
```

message
:   *Type:* String

    A text string containing the message to display. Multiple lines may be separated by ' ' characters.

caption
:   *Type:* String

    If provided, the caption for the dialog. Defaults to "Error".

type
:   *Type:* Integer

    If provided, a bitmap of various flags used to achieve different effects.

    The following type flags are available:

    Base types

    * 0 =
      Acet:OK
    * 1 =
      Acet:OKCANCEL
    * 2 =
      Acet:ABORTRETRYIGNORE
    * 3 =
      Acet:YESNOCANCEL
    * 4 =
      Acet:YESNO
    * 5 =
      Acet:RETRYCANCEL

    Icons

    * 16 =
      Acet:ICONSTOP
    * 32 =
      Acet:ICONQUESTION
    * 48 =
      Acet:ICONWARNING
    * 64 =
      Acet:ICONINFORMATION

    Default buttons

    * 0 =
      Acet:DEFBUTTON1
    * 256 =
      Acet:DEFBUTTON2
    * 512 =
      Acet:DEFBUTTON3
    * 768 =
      Acet:DEFBUTTON4

## Return Values

*Type:* Integer

Returns one of the following values:

* 1 =
  Acet:IDOK
* 2 =
  Acet:IDCANCEL
* 3 =
  Acet:IDABORT
* 4 =
  Acet:IDRETRY
* 5 =
  Acet:IDIGNORE
* 6 =
  Acet:IDYES
* 7 =
  Acet:IDNO
* 8 =
  Acet:IDCLOSE
* 9 =
  Acet:IDHELP

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*