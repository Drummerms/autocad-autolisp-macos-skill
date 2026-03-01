# foreach (AutoLISP)

Evaluates expressions for all members of a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(foreach name list [expr...])
```

*name*
:   *Type:* Symbol

    Variable that each element in the list will be assigned to.

*list*
:   *Type:* List

    List to be stepped through and evaluated.

*expr*
:   *Type:* List

    Expression to be evaluated for each element in
    *list*.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

The result of the last
*expr* evaluated. If no
*expr* is specified,
foreach returns
nil.

## Remarks

The
foreach function steps through a list, assigning each element in the list to a variable, and evaluates each expression for every
element in the list. Any number of expressions can be specified.

## Examples

Print each element in a list:

```
(foreach n '(a b c) (print n))
A
B
C C
```

foreach prints each element in the list and returns
C, the last element. This command is equivalent to the following sequence of commands, except that
foreach returns the result of only the last expression evaluated:

```
(print a)
(print b)
(print c)
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*