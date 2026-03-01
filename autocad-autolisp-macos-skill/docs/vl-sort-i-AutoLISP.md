# vl-sort-i (AutoLISP)

Sorts the elements in a list according to a given compare function, and returns the element index numbers

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-sort-i lst comparison-function)
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

A list containing the index values of the elements of
*lst*, sorted in the order specified by
*comparison-function*. Duplicate elements will be retained in the result.

## Examples

Sort a list of characters in descending order:

```
(vl-sort-i '("a" "d" "f" "c") '>)
(2 1 3 0)
```

The sorted list order is “f” “d” “c” “a”; “f” is the 3rd element (index 2) in the original list, “d” is the 2nd element (index
1) in the list, and so on.

Sort a list of numbers in ascending order:

```
(vl-sort-i '(3 2 1 3) '<)
(2 1 3 0)
```

Note that both occurrences of 3 are accounted for in the result list.

Sort a list of 2D points by
*Y* coordinate:

```
(vl-sort-i '((1 3) (2 2) (3 1))
         (function (lambda (e1 e2)
                (< (cadr e1) (cadr e2)))))
(2 1 0)
```

Sort a list of symbols:

```
(vl-sort-i
   '(a d c b a)
   '(lambda (s1 s2)
    (< (vl-symbol-name s1) (vl-symbol-name s2))))
(4 0 3 2 1)
```

Note that both
a's are accounted for in the result list.

#### Related References

* [vl-sort (AutoLISP)](vl-sort-AutoLISP.md)
* [acad\_strlsort (AutoLISP)](acad_strlsort-AutoLISP.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*