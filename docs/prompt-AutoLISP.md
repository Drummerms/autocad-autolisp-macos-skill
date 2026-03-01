# prompt (AutoLISP)

Displays a string on your screen's prompt area

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(prompt msg)
```

*msg*
:   *Type:* String

    Message to be displayed to the user.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

On dual-screen AutoCAD configurations,
prompt displays
*msg* on both screens and is, therefore, preferable to
princ.

## Examples

```
(prompt "New value: ")
New value: nil
```

#### Related References

* [prin1 (AutoLISP)](prin1-AutoLISP.md)
* [princ (AutoLISP)](princ-AutoLISP.md)
* [print (AutoLISP)](print-AutoLISP.md)
* [alert (AutoLISP)](alert-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*