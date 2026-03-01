# Use AutoLISP Variables (CAL Command)

You can use AutoLISP variables within arithmetic expressions. The variables must be one of the following types: real, integer,
or 2D or 3D point (vector).

This example defines a point located 5 units in the
*X* direction and 1 unit in the
*Y* direction from the point stored in AutoLISP variable  *A* .

*A+[5,1]*

If you enter an AutoLISP variable with a name containing a character with special meaning in CAL, such as +, -, \*, or /, enclose
the variable name in apostrophes ('), for example:

*'number-of-holes'*

## Assigning Values to AutoLISP Variables

To assign a value to an AutoLISP variable, precede the arithmetic expression with the variable name and the equal sign (=).
Later, you can use the value of this variable for other calculations.

This example saves the values of two expressions in AutoLISP variables
 *P1*  and
 *R1* .

Command:
*cal*

>> Expression:
*P1=cen+[1,0]*

>> Select entity for CEN snap:
*Select a circle or an arc*

Command:
*cal*

>> Expression:
*R1=dist(end,end)/3*

>> Select entity for END snap:
*Select an object with an endpoint*

This example uses the values of variables
 *P1*  and
 *R1* :

Command:
*circle*

Specify center point for circle or [3P/2P/Ttr (tangent tangent radius)]:
*'cal*

>> Expression:
*P1+[0,1]*

Specify radius of circle or [Diameter] <*last*>:
*'cal*

>> Expression:
*R1+0.5*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*