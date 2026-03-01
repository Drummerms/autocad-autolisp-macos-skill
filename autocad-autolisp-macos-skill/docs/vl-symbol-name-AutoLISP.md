# vl-symbol-name (AutoLISP)

Returns a string containing the name of a symbol

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-symbol-name symbol)
```

*symbol*
:   *Type:* Symbol

    Any LISP symbol.

## Return Values

*Type:* String or error

A string containing the name of the supplied symbol argument, in uppercase.

## Examples

```
(vl-symbol-name 'S::STARTUP)
"S::STARTUP"

(progn (setq sym 'my-var) (vl-symbol-name sym))
"MY-VAR"

(vl-symbol-name 1)
; *** ERROR: bad argument type: symbolp 1
```

#### Related References

* [vl-symbol-value (AutoLISP)](vl-symbol-value-AutoLISP.md)
* [vl-symbolp (AutoLISP)](vl-symbolp-AutoLISP.md)
* [setq (AutoLISP)](setq-AutoLISP.md)
* [vl-bb-set (AutoLISP)](vl-bb-set-AutoLISP.md)
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)
* [vl-doc-set (AutoLISP)](vl-doc-set-AutoLISP.md)
* [defun (AutoLISP)](defun-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*