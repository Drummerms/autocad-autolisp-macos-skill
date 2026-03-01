# vl-remove-if-not (AutoLISP)

Returns all elements of the supplied list that pass the test function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-remove-if-not predicate-function lst)
```

*predicate-function*
:   *Type:* Subroutine or Symbol

    The test function. This can be any function that accepts a single argument and returns
    T for any user-specified condition. The
    *predicate-function* value can take one of the following forms:

    * A symbol (function name)
    * '(LAMBDA (A1 A2) ...)
    * (FUNCTION (LAMBDA (A1 A2) ...))

*lst*
:   *Type:* List

    A list to be tested.

## Return Values

*Type:* List or nil

A list containing all elements of
*lst* for which
*predicate-function* returns a non-nil value

## Examples

```
(vl-remove-if-not 'vl-symbolp (list pi t 0 "abc"))
(T)
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [vl-remove-if (AutoLISP)](vl-remove-if-AutoLISP.md)
* [vl-remove (AutoLISP)](vl-remove-AutoLISP.md)
* [vl-member-if-not (AutoLISP)](vl-member-if-not-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*