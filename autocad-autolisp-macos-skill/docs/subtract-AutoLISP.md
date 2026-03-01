# - (subtract) (AutoLISP)

Subtracts the second and following numbers from the first and returns the difference

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(- [number number ...])
```

*number*
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* Integer or Real

The result of the subtraction. If you supply more than two
*number* arguments, this function returns the result of subtracting the sum of the second through the last numbers from the first
number. If you supply only one
*number* argument, this function subtracts the number from zero, and returns a negative number. Supplying no arguments returns 0.

## Examples

```
(- 50 40)
10

(- 50 40.0)
10.0

(- 50 40.0 2.5)
7.5

(- 8)
-8
```

#### Related References

* [+ (add) (AutoLISP)](+-add-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)
* [About Number Handling (AutoLISP)](About-Number-Handling-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*