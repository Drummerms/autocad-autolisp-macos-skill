# vl-member-if-not (AutoLISP)

Determines if the predicate is nil for one of the list members

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-member-if-not predicate-function lst)
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

A list, starting with the first element that fails the test and containing all elements following this in the original argument.
If none of the elements fails the test condition,
vl-member-if-not returns
nil.

## Remarks

The
vl-member-if-not function passes each element in
*lst* to the function specified in
*predicate-function*. If the function returns
nil,
vl-member-if-not returns the rest of the list in the same manner as the
member function.

## Examples

```
(vl-member-if-not 'atom '(1 "Str" (0 . "line") nil t))
((0 . "line") nil T)
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [vl-member-if (AutoLISP)](vl-member-if-AutoLISP.md)
* [vl-remove-if-not (AutoLISP)](vl-remove-if-not-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*