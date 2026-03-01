# About Parametric Formulas and Equations

Formulas and equations can be represented either as expressions within dimensional constraint parameters or by defining user
variables. For example, the following illustration represents a design that constrains a circle to the center of the rectangle
with an area equal to that of the rectangle.

![](../images/GUID-02CD48B0-C023-436E-907E-76D791E5015A-low.png)

The *Length* and *Width* dimensional constraint parameters are set to constants. The *d1* and *d2* constraints are simple expressions that reference the *Length* and *Width*. The *Radius* dimensional constraint parameter is set to an expression that includes the square root function, parentheses to determine
the precedence of operations, the *Area* user variable, the division operator, and the constant, PI. These parameters can all be accessed in the Parameters Manager.

![](../images/GUID-E6C048D6-3A43-4514-A1FD-AE206F94FB24-low.png)

As you can see, part of the equation for determining the area of the circle is included in the Radius dimensional constraint
parameter and part was defined as a user variable. Alternatively, the entire expression, sqrt (Length \* Width / PI), could
have been assigned to the *Radius* dimensional constraint parameter, defined in a user variable, or some other combination.

## Protect Expressions in Dynamic Constraints

When a *dynamic dimensional constraint* references one or more parameters, the prefix *fx:* is added to the name of the constraint. This prefix is displayed only in the drawing. Its purpose is to help you to avoid
accidentally overwriting parameters and formulas when the *dimension name format* is set to *Value* or *Name*, which suppresses the display of the parameters and formulas.

#### Related Concepts

* [About Controlling Geometry With the Parameters Manager](About-Controlling-Geometry-With-the-Parameters-Manager.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*