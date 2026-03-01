# vl-catch-all-apply (AutoLISP)

Passes a list of arguments to a specified function and traps any exceptions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-catch-all-apply 'function list)
```

*'function*
:   *Type:* Symbol

    A function. The
    *function* argument can be either a symbol identifying a
    defun or
    lambda expression.

*list*
:   *Type:* List

    A list containing arguments to be passed to the function.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, nil, or catch-all-apply-error

The result of the function call, if successful. If an error occurs,
vl-catch-all-apply returns an error object.

## Examples

If the function invoked by
vl-catch-all-apply completes successfully, it is the same as using
apply, as the following examples show:

```
(setq catchit (apply '/ '(50 5)))
10

(setq catchit (vl-catch-all-apply '/ '(50 5)))
10
```

The benefit of using
vl-catch-all-apply is that it allows you to intercept errors and continue processing. See what happens when you try to divide by zero using
apply:

```
(setq catchit (apply '/ '(50 0)))
; error: divide by zero
```

When you use
apply, an exception occurs and an error message displays. Here is the same operation using
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

* [vl-catch-all-error-message (AutoLISP)](vl-catch-all-error-message-AutoLISP.md)
* [vl-catch-all-error-p (AutoLISP)](vl-catch-all-error-p-AutoLISP.md)
* [apply (AutoLISP)](apply-AutoLISP.md)
* [\*error\* (AutoLISP)](error-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*