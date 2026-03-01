# vl-acad-undefun (AutoLISP)

Undefines an AutoLISP function symbol so it is no longer available to ObjectARX applications

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-acad-undefun 'symbol)
```

symbol
:   *Type:* Subroutine or Symbol

    A symbol identifying a function.

## Return Values

*Type:* Integer or nil

A numeric value if successful;
nil if unsuccessful (for example, the function was not defined in AutoLISP).

## Remarks

You can use
vl-acad-undefun to undefine a
c: function or a function that was exposed by
vl-acad-defun.

## Examples

None

#### Related References

* [vl-acad-defun (AutoLISP)](vl-acad-defun-AutoLISP.md)
* [defun (AutoLISP)](defun-AutoLISP.md)
* [vlax-add-cmd (AutoLISP/ActiveX)](vlax-add-cmd-AutoLISP-ActiveX.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*