# cons (AutoLISP)

Adds an element to the beginning of a list, or constructs a dotted list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(cons new-first-element list-or-atom)
```

*new-first-element*
:   *Type:* Integer, Real, String, List, T, or nil

    Element to be added to the beginning of a list. This element can be an atom or a list.

*list-or-atom*
:   *Type:* Integer, Real, String, List, or T

    A list or an atom.

## Return Values

*Type:* List

The value returned depends on the data type of
*list-or-atom*. If
*list-or-atom* is a list,
cons returns that list with
*new-first-element* added as the first item in the list. If
*list-or-atom* is an atom,
cons returns a dotted pair consisting of
*new-first-element* and
*list-or-atom*.

## Examples

```
(cons 'a '(b c d))
(A B C D)

(cons '(a) '(b c d))
((A) B C D)

(cons 'a 2)
(A . 2)
```

#### Related References

* [assoc (AutoLISP)](assoc-AutoLISP.md)
* [entmod (AutoLISP)](entmod-AutoLISP.md)
* [subst (AutoLISP)](subst-AutoLISP.md)
* [vl-list-length (AutoLISP)](vl-list-length-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*