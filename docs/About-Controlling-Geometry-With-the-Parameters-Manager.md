# About Controlling Geometry With the Parameters Manager

The Parameters Manager lists dimensional constraint parameters, reference parameters, and user variables, which you can also
create, edit, and organize.

You can easily create, modify, and delete parameters from the Parameters Manager, which supports the following operations:

* Click the name of a dimensional constraint parameter to highlight the constraint in the drawing.
* Double-click a name or expression to edit it.
* Right-click and click Delete to remove a dimensional constraint parameter or user variable.
* Click a column heading to sort the list of parameters by name, expression, or value.

## Use Operators in Expressions

Dimensional constraint parameters and user variables support the following operators within expressions:

| Operator | Description |
| + | Addition |
| - | Subtraction or unary negation |
| % | Floating point modulo |
| \* | Multiplication |
| / | Division |
| ^ | Exponentiation |
| ( ) | Parenthesis, expression delimiter |
| . | Decimal separator |

NOTE:With imperial units, the Parameters Manager interprets a minus or a dash (-) as a unit separator rather than a subtraction
operation. To specify subtraction, include at least one space before or after the minus sign. For example, to subtract 9"
from 5', enter *5' -9"* rather than *5'-9"*.

## Understand Precedence in Expressions

Expressions are evaluated according to the following standard mathematical rules of precedence:

1. Expressions in parentheses first, starting with the innermost set
2. Operators in standard order: (1) unary negation, (2) exponents, (3) multiplication and division, and (4) addition and subtraction
3. Operators of equal precedence from left to right

## Functions Supported in Expressions

The following functions are available for use in expressions:

| Function | Syntax |
| Cosine | cos(*expression*) |
| Sine | sin(*expression*) |
| Tangent | tan(*expression*) |
| Arc cosine | acos(*expression*) |
| Arc sine | asin(*expression*) |
| Arc tangent | atan(*expression*) |
| Hyperbolic cosine | cosh(*expression*) |
| Hyperbolic sine | sinh(*expression*) |
| Hyperbolic tangent | tanh(*expression*) |
| Arc hyperbolic cosine | acosh(*expression*) |
| Arc hyperbolic sine | asinh(*expression*) |
| Arc hyperbolic tangent | atanh(*expression*) |
| Square root | sqrt(*expression*) |
| Signum function (-1,0,1) | sign(*expression*) |
| Round to nearest integer | round(*expression*) |
| Truncate decimal | trunc(*expression*) |
| Round down | floor(*expression*) |
| Round up | ceil(*expression*) |
| Absolute value | abs(*expression*) |
| Largest element in array | max(*expression1*;*expression2*) |
| Smallest element in array | min(*expression1*;*expression2*) |
| Degrees to radians | d2r(*expression*) |
| Radians to degrees | r2d(*expression*) |
| Logarithm, base *e* | ln(*expression*) |
| Logarithm, base 10 | log(*expression*) |
| Exponent, base e | exp(*expression*) |
| Exponent, base 10 | exp10(*expression*) |
| Power function | pow(*expression1*;*expression2*) |
| Random decimal, 0-1 | Random |

In addition to these functions, the constants Pi and *e* are also available for use in expressions.

#### Related Tasks

* [To Modify a User Parameter in the Parameters Manager](To-Modify-a-User-Parameter-in-the-Parameters-Manager.md)
* [To Include a Function in an Expression in the Parameters Manager](To-Include-a-Function-in-an-Expression-in-the-Parameters-Manager.md)
* [To Reference a Variable Within an Expression in the Parameters Manager](To-Reference-a-Variable-Within-an-Expression-in-the-Parameters-Manager.md)
* [To Select a Constrained Object Associated With a User Parameter](To-Select-a-Constrained-Object-Associated-With-a-User-Parameter.md)

#### Related Concepts

* [About Parametric Formulas and Equations](About-Parametric-Formulas-and-Equations.md)

#### Related Information

* [About Parametric Drawing](About-Parametric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*