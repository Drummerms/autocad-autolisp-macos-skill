# vl-symbolp (AutoLISP)

Identifies whether or not a specified object is a symbol

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-symbolp object)
```

*object*
:   *Type:* Integer, Real, String, List, File, Symbol, Ename (entity name), T, or nil

    Any LISP object.

## Return Values

*Type:* T or nil

T if
*object* is a symbol; otherwise
nil.

## Examples

```
(vl-symbolp t)
T

(vl-symbolp nil)
nil

(vl-symbolp 1)
nil

(vl-symbolp (list 1))
nil
```

#### Related References

* [vl-symbol-value (AutoLISP)](vl-symbol-value-AutoLISP.md)
* [vl-symbol-name (AutoLISP)](vl-symbol-name-AutoLISP.md)
* [setq (AutoLISP)](setq-AutoLISP.md)
* [vl-bb-set (AutoLISP)](vl-bb-set-AutoLISP.md)
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)
* [vl-doc-set (AutoLISP)](vl-doc-set-AutoLISP.md)
* [defun (AutoLISP)](defun-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*