# vl-bb-set (AutoLISP)

Sets a variable in the blackboard namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-bb-set 'symbol value)
```

*'symbol*
:   *Type:* Symbol

    A symbol naming the variable to be set.

*value*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Any value, except a function.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

The
*value* you assigned to
*symbol*.

## Examples

```
(vl-bb-set 'foobar "Root toot toot")
"Root toot toot"

(vl-bb-ref 'foobar)
"Root toot toot"
```

#### Related References

* [setq (AutoLISP)](setq-AutoLISP.md)
* [vl-bb-ref (AutoLISP)](vl-bb-ref-AutoLISP.md)
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)
* [vl-doc-set (AutoLISP)](vl-doc-set-AutoLISP.md)

#### Related Concepts

* [Namespace Communication Functions Reference (AutoLISP)](Namespace-Communication-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*