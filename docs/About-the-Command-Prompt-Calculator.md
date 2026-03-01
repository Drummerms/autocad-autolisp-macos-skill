# About the Command Prompt Calculator

By entering an expression in the Command prompt calculator, you can quickly solve a mathematical problem or locate points
in your drawing.

The CAL command runs the 3D calculator utility to evaluate vector expressions (combining points, vectors, and numbers) and
real and integer expressions. The calculator performs standard mathematical functions. It also contains a set of specialized
functions for calculations involving points, vectors, and geometry. With the CAL command, you can

* Calculate a vector from two points, the length of a vector, a normal vector (perpendicular to the *XY* plane), or a point on a line
* Calculate a distance, radius, or angle
* Specify a point with the pointing device
* Specify the last-specified point or intersection
* Use object snaps as variables in an expression
* Convert points between a UCS and the WCS
* Filter the *X*, *Y*, and *Z* components of a vector
* Rotate a point around an axis

## Evaluating Expressions

CAL evaluates expressions according to standard mathematical rules of precedence.

| Mathematical operators in order of precedence | |
| Operator | Operation |
| ( ) | Groups expressions |
| ^ | Indicates numeric exponent |
| \*, / | Multiplies and divides numbers |
| +, - | Adds and subtracts numbers |

## Calculating Points

You can use CAL whenever you need to calculate a point or a number within a command.

For example, you enter *(mid+cen)/2* to specify a point halfway between the midpoint of a line and the center of a circle.

The following example uses CAL as a construction tool. It locates a center point for a new circle, and then calculates one
fifth of the radius of an existing circle.

![](../images/GUID-C19DF9C7-E3B9-4B53-AD57-21BA6474EEA8-low.png)

Here is the command prompt sequence:

Command: *circle*

Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: *'cal*

>> Expression: *(mid+cen)/2*

>> Select entity for MID snap: *Select the notch line (1)*

>> Select entity for CEN snap: *Select the large circle (2)*

Diameter/<Radius>: *'cal*

>> Expression: *1/5\*rad*

>> Select circle, arc or polyline segment for RAD function: *Select the large circle (3)*

#### Related Tasks

* [To Use the Command Prompt Calculator](To-Use-the-Command-Prompt-Calculator.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*