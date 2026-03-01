# /= (not Equal to) (AutoLISP)

Compares arguments for numerical inequality

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(/= numstr [numstr ...])
```

*numstr*
:   *Type:* Integer, Real, or String

    A number or string.

## Return Values

*Type:* T or nil

T, if no two successive arguments are the same in value; otherwise
nil. If only one argument is supplied,
T is returned.

NOTE:The behavior of
/= does not quite conform to other LISP dialects. The standard behavior is to return
T if no two arguments in the list have the same value. In AutoLISP,
/= returns
T if no
*successive* arguments have the same value; see the examples that follow.

## Examples

```
(/= 10 20)
T

(/= "you" "you")
nil

(/= 5.43 5.44)
T

(/= 10 20 10 20 20)
nil

(/= 10 20 10 20)
T
```

NOTE:In the last example, although there are two arguments in the list with the same value, they do not follow one another; thus/= evaluates to
T.

#### Related References

* [not (AutoLISP)](not-AutoLISP.md)
* [null (AutoLISP)](null-AutoLISP.md)

#### Related Concepts

* [= (equal to) (AutoLISP)](=-equal-to-AutoLISP.md)
* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*