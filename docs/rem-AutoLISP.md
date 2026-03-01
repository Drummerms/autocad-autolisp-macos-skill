# rem (AutoLISP)

Divides the first number by the second, and returns the remainder

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(rem [number number ...])
```

*number*
:   *Type:* Integer or Real

    Any number.

## Return Values

*Type:* Integer or Real

A number. If any
*number* argument is a real,
rem returns a real; otherwise,
rem returns an integer. If no arguments are supplied,
rem returns 0. If a single
*number* argument is supplied,
rem returns
*number*.

## Remarks

If you provide more than two numbers, numbers are evaluated from left to right. For example, if you supply three numbers,
rem divides the first number by the second, then takes the result and divides it by the third number, returning the remainder
of that operation.

## Examples

```
(rem 42 12)
6

(rem 12.0 16)
12.0

(rem 26 7 2)
1
```

#### Related References

* [/ (divide) (AutoLISP)](divide-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*