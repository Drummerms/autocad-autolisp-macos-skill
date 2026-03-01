# showhtmlmodalwindow (AutoLISP)

Displays a modal dialog box with a specified URI (Uniform Resource Identifier)

*Supported Platforms:* Windows only

## Signature

```
(showhtmlmodalwindow uri)
```

*uri*
:   *Type:* String

    URI of the page to be loaded into the dialog box.

    The page that the URI references can utilize the AutoCAD JavaScript API.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

Both the current size and position of the dialog box is automatically persisted between sessions.

## Examples

The following example displays the AutoCAD Developer Center.

```
(showhtmlmodalwindow "https://www.autodesk.com/developautocad")
```

#### Related References

* [startapp (AutoLISP)](startapp-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*