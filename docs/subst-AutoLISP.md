# subst (AutoLISP)

Searches a list for an old item and returns a copy of the list with a new item substituted in place of every occurrence of
the old item

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(subst newitem olditem lst)
```

*newitem*
:   *Type:* Integer, Real, String, List, Symbol, Ename (entity name), T, or nil

    An atom or list.

*olditem*
:   *Type:* Integer, Real, String, List, Symbol, Ename (entity name), T, or nil

    An atom or list.

*lst*
:   *Type:* List

    A list.

## Return Values

A list, with
*newitem* replacing all occurrences of
*olditem*. If
*olditem* is not found in
*lst*,
subst returns
*lst* unchanged.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## Examples

```
(setq sample '(a b (c d) b))
(A B (C D) B)

(subst 'qq 'b sample)
(A QQ (C D) QQ)

(subst 'qq 'z sample)
(A B (C D) B)

(subst 'qq '(c d) sample)
(A B QQ B)

(subst '(qq rr) '(c d) sample)
(A B (QQ RR) B)

(subst '(qq rr) 'z sample)
(A B (C D) B)
```

When used in conjunction with
assoc,
subst provides a convenient means of replacing the value associated with one key in an association list, as demonstrated by the
following function calls.

Set variable
who to an association list:

```
(setq who '((first john) (mid q) (last public)))
((FIRST JOHN) (MID Q) (LAST PUBLIC))
```

The following sets
old to (FIRST JOHN) and
new to (FIRST J):

```
(setq old (assoc 'first who) new '(first j))
(FIRST J)
```

Finally, replace the value of the first item in the association list:

```
(subst new old who)
((FIRST J) (MID Q) (LAST PUBLIC))
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [cons (AutoLISP)](cons-AutoLISP.md)
* [assoc (AutoLISP)](assoc-AutoLISP.md)
* [entmod (AutoLISP)](entmod-AutoLISP.md)
* [vl-string-subst (AutoLISP)](vl-string-subst-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*