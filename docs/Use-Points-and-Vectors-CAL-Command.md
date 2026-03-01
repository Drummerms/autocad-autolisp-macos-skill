# Use Points and Vectors (CAL Command)

Both points and vectors are pairs or triples of real numbers. A point defines a location in space, but a vector defines a
direction (or translation) in space.

Some CAL functions, such as
*pld* and
*plt*, return a point. Other functions, such as
*nor* and
*vec*, return a vector.

## Formatting Points and Vectors

A point or vector is a set of three real expressions enclosed in brackets ([ ]):
*[r1,r2,r3]*

The notation *p1*, *p2*, and so forth designates points. The notation
*v1*, *v2*, and so forth designates vectors. In drawings, points are displayed as dots, and vectors are displayed as lines with arrows.

CAL supports points expressed in all formats.

| Point formats | |
| Coordinate system | Point format |
| Polar | [dist<angle] |
| Cylindrical | [dist<angle,z] |
| Spherical | [dist<angle1<angle2] |
| Relative | Uses the @ prefix [@x,y,z] |
| WCS (instead of UCS) | Uses the \* prefix [\*x,y,z] |

You can omit the following components of a point or vector: coordinate values of zero and a comma immediately preceding the
right bracket (]).

The following are valid points:

*[1,2]* is the same as
*[1,2,0]*

*[,,3]* is the same as
*[0,0,3]*

*[ ]* is the same as
*[0,0,0]*

In the following example, the point is entered in the relative spherical coordinate system with respect to the (WCS). The
distance is 1+2=3; the angles are 10+20=30 degrees and 45 degrees, 20 minutes.

*[ \*1+2<10+20<45d20"]*

The following is a valid point that contains arithmetic expressions as its components:

*[2\*(1.0+3.3),0.4-1.1,2\*1.4]*

The following example uses the Endpoint object snap and the vector [2,0,3] to calculate a point that is offset from a selected
endpoint:

*end + [2,,3]*

The calculated point is offset 2 units in the
*X* direction and 3 units in the
*Z* direction relative to the selected endpoint.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*