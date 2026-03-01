# vl-symbol-value (AutoLISP)

Returns the current value bound to a symbol

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-symbol-value symbol)
```

*symbol*
:   *Type:* Symbol

    Any LISP symbol.

## Return Values

*Type:* Integer, Real, String, List, File, Ename (entity name), T, or nil

The value of
*symbol*, after evaluation.

## Remarks

This function is equivalent to the
eval function, but does not call the LISP evaluator.

## Examples

```
(vl-symbol-value 't)
T

(vl-symbol-value 'PI)
3.14159

(progn (setq sym 'PAUSE) (vl-symbol-value sym))
"\\"
```

#### Related References

* [vl-symbol-name (AutoLISP)](vl-symbol-name-AutoLISP.md)
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