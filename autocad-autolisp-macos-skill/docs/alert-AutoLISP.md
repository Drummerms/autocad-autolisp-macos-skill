# alert (AutoLISP)

Displays a dialog box containing an error or warning message

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(alert msg)
```

*msg*
:   *Type:* String

    The message to display in the alert box.

## Return Values

*Type:* nil

Always returns
nil.

## Examples

Display a message in an alert box:

```
(alert "That function is not available.")
```

Display a multiple line message, by using the newline character in
*string*:

```
(alert "That function\
is not available.")
```

NOTE:Line length and the number of lines in an alert box are platform, device, and window dependent. AutoCAD truncates any string
that is too long to fit inside an alert box.

#### Related References

* [prompt (AutoLISP)](prompt-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*