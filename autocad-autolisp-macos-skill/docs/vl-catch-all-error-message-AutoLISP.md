# vl-catch-all-error-message (AutoLISP)

Returns a string from an error object

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-catch-all-error-message error-obj)
```

*error-obj*
:   *Type:* catch-all-apply-error

    An error object returned by
    vl-catch-all-apply.

## Return Values

*Type:* String

A textual value containing an error message.

## Examples

Divide by zero using
vl-catch-all-apply:

```
(setq catchit (vl-catch-all-apply '/ '(50 0)))
#<%catch-all-apply-error%>
```

The
vl-catch-all-apply function traps the error and returns an error object. Use
vl-catch-all-error-message to see the error message contained in the error object:

```
(vl-catch-all-error-message catchit)
"divide by zero"
```

#### Related References

* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)
* [vl-catch-all-error-p (AutoLISP)](vl-catch-all-error-p-AutoLISP.md)
* [apply (AutoLISP)](apply-AutoLISP.md)
* [\*error\* (AutoLISP)](error-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*