# Use Snap Modes in Arithmetic Expressions (CAL Command)

You can use Snap modes as parts of arithmetic expressions. The program prompts you to select an object and returns the coordinate
of the appropriate snap point. Using arithmetic expressions with Snap modes greatly simplifies entering coordinates relative
to other objects.

When you use these Snap modes, enter only the three-character name. For example, when you use the Center Snap mode, enter
*cen*. CAL Snap modes set the value of the
[LASTPOINT](LASTPOINT-System-Variable.md) system variable.

| CAL Snap modes | |
| Abbreviation | Snap mode |
| END | ENDPOINT |
| INS | INSERT |
| INT | INTERSECTION |
| MID | MIDPOINT |
| CEN | CENTER |
| NEA | NEAREST |
| NOD | NODE |
| QUA | QUADRANT |
| PER | PERPENDICULAR |
| TAN | TANGENT |

The following example uses the Center and Endpoint Snap modes in a CAL expression:

*(cen+end)/2*

CAL prompts for a circle or arc and an object. It then determines the midpoint between the center of the circle or arc and
the end of the selected object.

Using the Midpoint Snap mode, in the following example CAL prompts for an object and returns a point 1 unit in the
*Y* direction from the midpoint of the selected object:

*mid+[,1]*

The following example uses the Endpoint Snap mode to calculate the centroid of a triangle defined by three endpoints:

*(end+end+end)/3*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*