# vl-every (AutoLISP)

Checks whether the predicate is true for every element combination

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-every predicate-function list [list ...])
```

*predicate-function*
:   *Type:* Subroutine or Symbol

    The test function. This can be any function that accepts as many arguments as there are lists provided with
    vl-every, and returns
    T on any user-specified condition. The
    *predicate-function* value can take one of the following forms:

    * A symbol (function name)
    * '(LAMBDA (A1 A2) ...)
    * (FUNCTION (LAMBDA (A1 A2) ...))

*list*
:   *Type:* List

    A list to be tested.

## Return Values

*Type:* T or nil

T, if
*predicate-function* returns a non-nil value for every element combination; otherwise
nil.

## Remarks

Thevl-every function passes the first element of each supplied list as an argument to the test function, followed by the next element
from each list, and so on. Evaluation stops as soon as one of the lists runs out.

## Examples

Check whether there are any empty files in the current directory:

```
(vl-every
'(lambda (fnm) (> (vl-file-size fnm) 0))
   (vl-directory-files nil nil 1))
T
```

Check whether the list of numbers in
nlst is ordered by
'<=:

```
(setq nlst (list 0 2 pi pi 4))
(0 2 3.14159 3.14159 4)

(vl-every '<= nlst (cdr nlst))
T
```

Compare the results of the following expressions:

```
(vl-every '= '(1 2) '(1 3))
nil

(vl-every '= '(1 2) '(1 2 3))
T
```

The first expression returned
nil because
vl-every compared the second element in each list and they were not numerically equal. The second expression returned
T because
vl-every stopped comparing elements after it had processed all the elements in the shorter list (1 2), at which point the lists were
numerically equal. If the end of a list is reached,
vl-every returns a non-nil value.

The following example demonstrates the result when
vl-every evaluates one list that contains integer elements and another list that is
nil:

```
(setq alist (list 1 2 3 4))
(1 2 3 4)

(setq junk nil)
nil

(vl-every '= junk alist)
T
```

The return value is
T because
vl-every responds to the
nil list as if it has reached the end of the list (even though the predicate has not yet been applied to any elements). And since
the end of a list has been reached,
vl-every returns a non-nil value.

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*