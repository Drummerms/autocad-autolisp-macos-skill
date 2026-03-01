# eq (AutoLISP)

Determines whether two expressions are identical

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(eq expr1 expr2)
```

*expr1*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    The expression to be compared.

*expr2*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    The expression to compare with
    *expr1*.

## Return Values

*Type:* T or nil

T if the two expressions are identical; otherwise
nil.

## Remarks

The
eq function determines whether
*expr1* and
*expr2* are bound to the same object (by
setq, for example).

## Examples

Given the following assignments:

```
(setq f1 '(a b c))
(setq f2 '(a b c))
(setq f3 f2)
```

Compare
f1 and
f3:

```
(eq f1 f3)
nil
```

eq returns
nil because
f1 and
f3, while containing the same value, do not refer to the same list.

Compare
f3 and
f2:

```
(eq f3 f2)
T
```

eq returns
T because
f3 and
f2 refer to the same list.

#### Related References

* [equal (AutoLISP)](equal-AutoLISP.md)

#### Related Concepts

* [= (equal to) (AutoLISP)](=-equal-to-AutoLISP.md)
* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*