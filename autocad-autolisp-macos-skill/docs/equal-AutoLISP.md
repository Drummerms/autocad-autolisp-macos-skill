# equal (AutoLISP)

Determines whether two expressions are equal

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(equal expr1 expr2 [fuzz])
```

*expr1*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    The expression to be compared.

*expr2*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    The expression to compare with
    *expr1*.

*fuzz*
:   *Type:* Integer or Real

    A real number defining the maximum amount by which
    *expr1* and
    *expr2* can differ and still be considered equal.

## Return Values

*Type:* T or nil

T if the two expressions are equal (evaluate to the same value); otherwise
nil.

## Remarks

When comparing two real numbers (or two lists of real numbers, as in points), the two identical numbers can differ slightly
if different methods are used to calculate them. You can specify a
*fuzz* amount to compensate for the difference that may result from the different methods of calculation.

Comparing the eq and equal Functions
:   If the
    eq function finds that two lists or atoms are the same, the
    equal function also finds them to be the same.

    Any
    *atoms* that the
    equal function determines to be the same are also found equivalent by
    eq. However, two
    *lists* that
    equal determines to be the same may be found to be different according to the
    eq function.

## Examples

Given the following assignments:

```
(setq f1 '(a b c))
(setq f2 '(a b c))
(setq f3 f2)
(setq a 1.123456)
(setq b 1.123457)
```

Compare
f1 to
f3:

```
(equal f1 f3)
T
```

Compare
f3 to
f2:

```
(equal f3 f2)
T
```

Compare
a to
b:

```
(equal a b)
nil
```

The
a and
b variables differ by .000001. Compare
a to
b:, with
*fuzz* argument of .000001:

```
(equal a b 0.000001)
T
```

The
a and
b variables differ by an amount equal to the specified
*fuzz* factor, so
equal considers the variables equal.

#### Related References

* [eq (AutoLISP)](eq-AutoLISP.md)

#### Related Concepts

* [= (equal to) (AutoLISP)](=-equal-to-AutoLISP.md)
* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*