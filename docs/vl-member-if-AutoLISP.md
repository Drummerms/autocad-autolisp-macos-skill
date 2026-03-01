# vl-member-if (AutoLISP)

Determines if the predicate is true for one of the list members

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-member-if predicate-function lst)
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

A list, starting with the first element that passes the test and containing all elements following this in the original argument.
If none of the elements passes the test condition,
vl-member-if returns
nil.

## Remarks

The
vl-member-if function passes each element in
*lst* to the function specified in
*predicate-function*. If
*predicate-function* returns a non-nil value,
vl-member-if returns the rest of the list in the same manner as the
member function.

## Examples

The following command draws a line:

```
(command "._line" '(0 10) '(30 50) nil)
nil
```

The following command uses
vl-member-if to return association lists describing an entity, if the entity is a line:

```
(vl-member-if
  '(lambda (x) (= (cdr x) "AcDbLine"))
   (entget (entlast)))
((100 . "AcDbLine") (10 0.0 10.0 0.0) (11 30.0 50.0 0.0) (210 0.0 0.0 1.0))
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [vl-member-if-not (AutoLISP)](vl-member-if-not-AutoLISP.md)
* [vl-remove-if (AutoLISP)](vl-remove-if-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*