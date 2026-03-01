# if (AutoLISP)

Conditionally evaluates expressions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(if testexpr thenexpr [elseexpr])
```

*testexpr*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Expression to be tested.

*thenexpr*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Expression evaluated if
    *testexpr* is not
    nil.

*elseexpr*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Expression evaluated if
    *testexpr* is
    nil.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

The
if function returns the value of the selected expression. If
*elseexpr* is missing and
*testexpr* is
nil, then it returns
nil.

## Examples

```
(if (= 1 3) "YES!!" "no.")
"no."

(if (= 2 (+ 1 1)) "YES!!")
"YES!!"

(if (= 2 (+ 3 4)) "YES!!")
nil
```

#### Related References

* [cond (AutoLISP)](cond-AutoLISP.md)
* [progn (AutoLISP)](progn-AutoLISP.md)
* [not (AutoLISP)](not-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*