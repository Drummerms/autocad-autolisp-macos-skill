# Equality and Conditional Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP equality and conditional functions.

| Equality and conditional functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(= numstr [numstr ...])](=-equal-to-AutoLISP.md) | Returns T if all arguments are numerically equal, and returns nil otherwise | ✓ | ✓ | ✓ | -- | ✓ |
| [(/= numstr [numstr ...])](=-not-Equal-to-AutoLISP.md) | Returns T if the arguments are not numerically equal, and nil if the arguments are numerically equal | ✓ | ✓ | ✓ | -- | ✓ |
| [(< numstr [numstr ...])](less-than-AutoLISP.md) | Returns T if each argument is numerically less than the argument to its right, and returns nil otherwise | ✓ | ✓ | ✓ | -- | ✓ |
| [(<= numstr [numstr ...])](=-less-than-or-equal-to-AutoLISP.md) | Returns T if each argument is numerically less than or equal to the argument to its right, and returns nil otherwise | ✓ | ✓ | ✓ | -- | ✓ |
| [(> numstr [numstr ...])](greater-than-AutoLISP.md) | Returns T if each argument is numerically greater than the argument to its right, and returns nil otherwise | ✓ | ✓ | ✓ | -- | ✓ |
| [(>= numstr [numstr ...])](=-greater-than-or-equal-to-AutoLISP.md) | Returns T if each argument is numerically greater than or equal to the argument to its right, and returns nil otherwise | ✓ | ✓ | ✓ | -- | ✓ |
| [(and [expr ...])](and-AutoLISP.md) | Returns the logical AND of a list of expressions | ✓ | ✓ | ✓ | -- | ✓ |
| [(boole func int1 [int2 ...])](boole-AutoLISP.md) | Serves as a general bitwise Boolean function | ✓ | ✓ | ✓ | -- | ✓ |
| [(cond [(test result ...) ...])](cond-AutoLISP.md) | Serves as the primary conditional function for AutoLISP | ✓ | ✓ | ✓ | -- | ✓ |
| [(eq expr1 expr2)](eq-AutoLISP.md) | Determines whether two expressions are identical | ✓ | ✓ | ✓ | -- | ✓ |
| [(equal expr1 expr2 [fuzz])](equal-AutoLISP.md) | Determines whether two expressions are equal | ✓ | ✓ | ✓ | -- | ✓ |
| [(if testexpr thenexpr [elseexpr])](if-AutoLISP.md) | Conditionally evaluates expressions | ✓ | ✓ | ✓ | -- | ✓ |
| [(or [expr ...])](or-AutoLISP.md) | Returns the logical OR of a list of expressions | ✓ | ✓ | ✓ | -- | ✓ |
| [(repeat int [expr ...])](repeat-AutoLISP.md) | Evaluates each expression a specified number of times, and returns the value of the last expression | ✓ | ✓ | ✓ | -- | ✓ |
| [(while testexpr [expr ...])](while-AutoLISP.md) | Evaluates a test expression, and if it is not nil, evaluates other expressions; repeats this process until the test expression evaluates to nil | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*