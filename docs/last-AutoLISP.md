# last (AutoLISP)

Returns the last element in a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(last lst)
```

*lst*
:   *Type:* List

    A list of one or more elements.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

An atom or a list.

## Examples

```
(last '(a b c d e))
E

(last '(a b c (d e)))
(D E)
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [car (AutoLISP)](car-AutoLISP.md)
* [cdr (AutoLISP)](cdr-AutoLISP.md)
* [reverse (AutoLISP)](reverse-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*