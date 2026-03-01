# vl-acad-defun (AutoLISP)

Defines an AutoLISP function symbol as an external subroutine

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-acad-defun 'symbol)
```

symbol
:   *Type:* Subroutine or Symbol

    A symbol identifying a function.

## Return Values

*Type:* Integer

A numeric value.

## Remarks

If a function does not have the
c: prefix, and you want to be able to invoke this function from an external ObjectARX application, you can use
vl-acad-defun to make the function accessible.

## Examples

None

#### Related References

* [vl-acad-undefun (AutoLISP)](vl-acad-undefun-AutoLISP.md)
* [defun (AutoLISP)](defun-AutoLISP.md)
* [vlax-add-cmd (AutoLISP/ActiveX)](vlax-add-cmd-AutoLISP-ActiveX.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*