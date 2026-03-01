# vl-doc-ref (AutoLISP)

Retrieves the value of a variable from the current document's namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-doc-ref 'symbol)
```

*'symbol*
:   *Type:* Symbol

    A symbol naming a variable.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

The value of the variable identified by
*symbol*.

## Remarks

This function can be used by a separate-namespace application to retrieve the value of a variable from the current document's
namespace.

## Examples

```
(vl-doc-ref 'foobar)
"Rinky dinky stinky"
```

#### Related References

* [setq (AutoLISP)](setq-AutoLISP.md)
* [vl-doc-set (AutoLISP)](vl-doc-set-AutoLISP.md)
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)
* [vl-bb-ref (AutoLISP)](vl-bb-ref-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)
* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*