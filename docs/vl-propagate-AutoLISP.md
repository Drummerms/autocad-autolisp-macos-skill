# vl-propagate (AutoLISP)

Copies the value of a variable into all open document namespaces (and sets its value in any subsequent drawings opened during
the current AutoCAD session)

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-propagate 'symbol)
```

*symbol*
:   *Type:* Symbol

    A symbol naming an AutoLISP variable.

## Return Values

*Type:* nil

Always returns
nil.

## Examples

```
(vl-propagate 'radius)
nil
```

#### Related References

* [setq (AutoLISP)](setq-AutoLISP.md)
* [vl-bb-ref (AutoLISP)](vl-bb-ref-AutoLISP.md)
* [vl-bb-set (AutoLISP)](vl-bb-set-AutoLISP.md)

#### Related Concepts

* [Namespace Communication Functions Reference (AutoLISP)](Namespace-Communication-Functions-Reference-AutoLISP.md)
* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*