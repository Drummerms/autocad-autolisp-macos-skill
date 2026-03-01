# vl-exit-with-error (AutoLISP)

Passes control from an error handler to the \*error\* function of the calling namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-exit-with-error msg)
```

*msg*
:   *Type:* String

    Message displayed to the user.

## Return Values

*Type:* None

None

## Remarks

This function is used by applications that run in their own namespace. When
vl-exit-with-error executes, it calls the
\*error\* function, the stack is unwound, and control returns to a command prompt.

## Examples

The following code illustrates the use of
vl-exit-with-error to pass a string to the
\*error\* function of the calling namespace:

```
(defun *error* (msg)
  ... ; processing in VLX namespace/execution context
(vl-exit-with-error (strcat "My application bombed! " msg)))
```

#### Related References

* [vl-exit-with-value (AutoLISP)](vl-exit-with-value-AutoLISP.md)
* [\*error\* (AutoLISP)](error-AutoLISP.md)
* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*