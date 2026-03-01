# member (AutoLISP)

Searches a list for an occurrence of an expression and returns the remainder of the list, starting with the first occurrence
of the expression

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(member expr lst)
```

*expr*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    The expression to be searched for.

*lst*
:   *Type:* List

    The list in which to search for
    *expr*.

## Return Values

*Type:* List or nil

A list; otherwise
nil, if there is no occurrence of
*expr* in
*lst*.

## Examples

```
(member 'c '(a b c d e))
(C D E)

(member 'q '(a b c d e))
nil
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [vl-member-if-not (AutoLISP)](vl-member-if-not-AutoLISP.md)
* [vl-member-if (AutoLISP)](vl-member-if-AutoLISP.md)
* [vl-remove-if-not (AutoLISP)](vl-remove-if-not-AutoLISP.md)
* [vl-remove-if (AutoLISP)](vl-remove-if-AutoLISP.md)
* [vl-remove (AutoLISP)](vl-remove-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*