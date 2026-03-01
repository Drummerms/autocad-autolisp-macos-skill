# \*error\* (AutoLISP)

A user-definable error-handling function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(*error* string)
```

*string*
:   *Type:* String

    A textual string that contains a description of the error and is passed by AutoCAD.

## Return Values

*Type:* N/A

This function does not return, except when using
vl-exit-with-value.

## Remarks

If
\*error\* is not
nil, it is executed as a function whenever an AutoLISP error condition exists.

Your
\*error\* function can include calls to the
command function without arguments (for example,
(command)). This will cancel a previous AutoCAD command called with the
command function.

## Examples

The following function does the same thing that the AutoLISP standard error handler does. It prints the text “error: ” followed
by a description:

```
(defun *error* (msg)
  (princ "error: ")
  (princ msg)
 (princ)
)
```

#### Related References

* [exit (AutoLISP)](exit-AutoLISP.md)
* [quit (AutoLISP)](quit-AutoLISP.md)
* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)
* [vl-exit-with-error (AutoLISP)](vl-exit-with-error-AutoLISP.md)
* [vl-exit-with-value (AutoLISP)](vl-exit-with-value-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*