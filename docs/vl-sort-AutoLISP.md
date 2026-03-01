# vl-sort (AutoLISP)

Sorts the elements in a list according to a given compare function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-sort lst comparison-function)
```

*lst*
:   *Type:* List

    Any list to sort.

*comparison-function*
:   *Type:* Subroutine or Symbol

    A comparison function. This can be any function that accepts two arguments and returns
    T (or any non-nil value) if the first argument precedes the second in the sort order. The
    *comparison-function* value can take one of the following forms:

    * A symbol (function name)
    * '(LAMBDA (A1 A2) ...)
    * (FUNCTION (LAMBDA (A1 A2) ...))

## Return Values

*Type:* List

A list containing the elements of
*lst* in the order specified by
*comparison-function*. Duplicate elements may be eliminated from the list.

## Examples

Sort a list of numbers:

```
(vl-sort '(3 2 1 3) '<)
(1 2 3)
```

Note that the result list contains only one 3.

Sort a list of 2D points by
*Y* coordinate:

```
(vl-sort '((1 3) (2 2) (3 1))
             (function (lambda (e1 e2)
                         (< (cadr e1) (cadr e2)))))
((3 1) (2 2) (1 3))
```

Sort a list of symbols:

```
(vl-sort
   '(a d c b a)
   '(lambda (s1 s2)
    (< (vl-symbol-name s1) (vl-symbol-name s2))))
(A B C D)       ;  Note that only one A remains in the result list
```

#### Related References

* [vl-sort-i (AutoLISP)](vl-sort-i-AutoLISP.md)
* [acad\_strlsort (AutoLISP)](acad_strlsort-AutoLISP.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*