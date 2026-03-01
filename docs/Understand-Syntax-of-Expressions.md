# Understand Syntax of Expressions

CAL evaluates expressions according to standard mathematical rules of precedence:

* Expressions in parentheses first, starting with the innermost set
* Operators in standard order: exponents first, multiplication and division second, and addition and subtraction last
* Operators of equal precedence from left to right

## Numeric Expressions

Numeric expressions are real integer numbers and functions combined with the operators in the following table.

| Numeric operators | |
| Operator | Operation |
| ( ) | Groups expressions |
| ^ | Indicates exponentiation |
| \* , / | Multiplies, divides |
| +, - | Adds, subtracts |

The following are examples of numeric expressions:

*3*

*3 + 0.6*

*(5.8^2) + PI*

## Vector Expressions

A vector expression is a collection of points, vectors, numbers, and functions combined with the operators in the following
table.

| Vector operators | |
| Operator | Operation |
| ( ) | Groups expressions |
| & | Determines the vector product of vectors (as a vector)  [a,b,c]&[x,y,z] = [ (b\*z) - (c\*y) , (c\*x) - (a\*z) , (a\*y) - (b\*x) ] |
| \* | Determines the scalar product of vectors (as a real number)  [a,b,c]\*[x,y,z] = ax + by + cz |
| \*, / | Multiplies, divides a vector by a real number  a\*[x,y,z] = [a\*x,a\*y,a\*z] |
| + , - | Adds, subtracts vectors (points)  [a,b,c] + [x,y,z] = [a+x,b+y,c+z] |

The following are examples of vector expressions:

*A+[1,2,3]* provides the point located [1,2,3] units relative to point A.

The expression

*[2<45<45] + [2<45<0]* - *[1.02, 3.5, 2]*

adds two points and subtracts a third point. The first two points are expressed in spherical coordinates.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*