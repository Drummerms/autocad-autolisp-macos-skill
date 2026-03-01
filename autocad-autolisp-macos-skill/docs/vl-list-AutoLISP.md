# vl-list\* (AutoLISP)

Constructs and returns a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-list* object [object ...])
```

*object*
:   *Type:* Integer, Real, String, List, File, Symbol, Ename (entity name), T, or nil

    Any LISP object.

## Return Values

The
vl-list\* function is similar to
list, but it will place the last
*object* in the final
cdr of the result list. If the last argument to
vl-list\* is an atom, the result is a dotted list. If the last argument is a list, its elements are appended to all previous arguments
added to the constructed list. The possible return values from
vl-list\* are

* An atom, if a single atom
  *object* is specified.
* A dotted pair, if all
  *object* arguments are atoms.
* A dotted list, if the last argument is an atom and neither of the previous conditions is true.
* A list, if none of the previous statements is true.

## Examples

```
(vl-list* 1)
1

(vl-list* 0 "text")
(0 . "TEXT")

(vl-list* 1 2 3)
(1 2 . 3)

(vl-list* 1 2 '(3 4))
(1 2 3 4)
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [append (AutoLISP)](append-AutoLISP.md)
* [listp (AutoLISP)](listp-AutoLISP.md)
* [vl-every (AutoLISP)](vl-every-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*