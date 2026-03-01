# vl-some (AutoLISP)

Checks whether the predicate is not nil for one element combination

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-some predicate-function lst [lst ...])
```

*predicate-function*
:   *Type:* Subroutine or Symbol

    The test function. This can be any function that accepts as many arguments as there are lists provided with
    vl-some, and returns
    T on a user-specified condition. The
    *predicate-function* value can take one of the following forms:

    * A symbol (function name)
    * '(LAMBDA (A1 A2) ...)
    * (FUNCTION (LAMBDA (A1 A2) ...))

*lst*
:   *Type:* List

    A list to be tested.

## Return Values

*Type:* List or nil

The predicate value, if
*predicate-function* returned a value other than
nil; otherwise
nil.

## Remarks

The
vl-some function passes the first element of each supplied list as an argument to the test function, then the next element from each
list, and so on. Evaluation stops as soon as the predicate function returns a non-nil value for an argument combination, or until all elements have been processed in one of the lists.

## Examples

The following example checks whether
nlst (a number list) has equal elements in sequence:

```
(setq nlst (list 0 2 pi pi 4))
(0 2 3.14159 3.14159 4)

(vl-some '= nlst (cdr nlst))
T
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*