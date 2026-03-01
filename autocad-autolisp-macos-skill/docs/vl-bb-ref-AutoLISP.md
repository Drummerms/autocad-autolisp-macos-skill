# vl-bb-ref (AutoLISP)

Returns the value of a variable from the blackboard namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-bb-ref 'variable)
```

*'variable*
:   *Type:* Symbol

    A symbol identifying the variable to be retrieved.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

The value of the
*variable* named by symbol.

## Examples

Set a variable in the blackboard:

```
(vl-bb-set 'foobar "Root toot toot")
"Root toot toot"
```

Use
vl-bb-ref to retrieve the value of
foobar from the blackboard:

```
(vl-bb-ref 'foobar)
"Root toot toot"
```

#### Related References

* [setq (AutoLISP)](setq-AutoLISP.md)
* [vl-bb-set (AutoLISP)](vl-bb-set-AutoLISP.md)
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)
* [vl-doc-ref (AutoLISP)](vl-doc-ref-AutoLISP.md)

#### Related Concepts

* [Namespace Communication Functions Reference (AutoLISP)](Namespace-Communication-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*