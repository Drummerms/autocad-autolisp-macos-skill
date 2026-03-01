# while (AutoLISP)

Evaluates a test expression, and if it is not nil, evaluates other expressions; repeats this process until the test expression
evaluates to nil

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(while testexpr [expr ...])
```

*testexpr*
:   *Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

    The expression containing the test condition.

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

    One or more expressions to be evaluated until
    *testexpr* is
    nil.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

The most recent value of the last
*expr*.

## Remarks

The
while function continues until
*testexpr* is
nil.

## Examples

The following code calls user function
some-func ten times, with
test set to 1 through 10. It then returns 11, which is the value of the last expression evaluated:

```
(setq test 1)
(while (<= test 10)
  (some-func test)
  (setq test (1+ test))
)
```

#### Related References

* [repeat (AutoLISP)](repeat-AutoLISP.md)
* [foreach (AutoLISP)](foreach-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*