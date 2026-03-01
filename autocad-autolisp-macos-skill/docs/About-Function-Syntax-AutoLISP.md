# About Function Syntax (AutoLISP)

Reference topics in the documentation use a consistent convention to describe the proper syntax for an AutoLISP function.

The syntax used is as follows:

![](../images/GUID-202C8A5F-A654-49FC-83C3-8EAA10E9F286-low.png)

In this example, the foo function has one required argument, *string* of the string data type, and one or more optional arguments of numeric value for *number*. The *number* arguments can be of the integer or real data types. Frequently, the name of the argument indicates the expected data type.
The examples in the following table show both valid and invalid calls to the foo function.

| Valid and invalid function call examples | |
| Valid calls | Invalid calls |
| (foo "catch") | (foo 44 13) |
| (foo "catch" 22) | (foo "fi" "foe" 44 13) |
| (foo "catch" 22 31) | (foo) |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Formatting and Spaces in Code (AutoLISP)](About-Formatting-and-Spaces-in-Code-AutoLISP.md)
* [About Symbols and Variables (AutoLISP)](About-Symbols-and-Variables-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*