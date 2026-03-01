# vl-catch-all-error-p (AutoLISP)

Determines whether an argument is an error object returned from
*vl-catch-all-apply*

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-catch-all-error-p arg)
```

*arg*
:   *Type:* Integer, Real, String, List, Subroutine, Ename (entity name), T, nil, or catch-all-apply-error

    Any argument.

## Return Values

*Type:* T or nil

T, if the supplied argument is an error object returned from
vl-catch-all-apply; otherwise
nil.

## Examples

Divide by zero using
vl-catch-all-apply:

```
(setq catchit (vl-catch-all-apply '/ '(50 0)))
#<%catch-all-apply-error%>
```

Use
vl-catch-all-error-p to determine if the value returned by
vl-catch-all-apply is an error object:

```
(vl-catch-all-error-p catchit)
T
```

#### Related References

* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)
* [vl-catch-all-error-message (AutoLISP)](vl-catch-all-error-message-AutoLISP.md)
* [apply (AutoLISP)](apply-AutoLISP.md)
* [\*error\* (AutoLISP)](error-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*