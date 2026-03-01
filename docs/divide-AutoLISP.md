# / (divide) (AutoLISP)

Divides the first number by the product of the remaining numbers and returns the quotient

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(/ [number number ...])
```

**number**
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* Integer or Real

The result of the division. If you supply more than two
*number* arguments, this function divides the first number by the product of the second through the last numbers, and returns the
final quotient. If you supply one
*number* argument, this function returns the result of dividing it by one; it returns the number. Supplying no arguments returns 0.

## Examples

```
(/ 100 2)
50

(/ 100 2.0)
50.0

(/ 100 20.0 2)
2.5

(/ 100 20 2)
2

(/ 4)
4
```

#### Related References

* [\* (multiply) (AutoLISP)](multiply-AutoLISP.md)
* [rem (AutoLISP)](rem-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)
* [About Number Handling (AutoLISP)](About-Number-Handling-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*