# Calculate a Vector from Two Points (CAL Command)

The functions
*vec* and
*vec1* calculate a vector from two points.

vec(p1,p2)
:   Provides the vector from point
    *p1* to point
    *p2.*

vec1(p1,p2)
:   Provides the unit vector from point
    *p1* to point
    *p2.*

The following example uses CAL to move selected objects 3 units in the direction from the center of one selected circle to
the center of another selected circle:

Command:
*move*

Select objects

Specify base point or displacement:
*'cal*

>> Expression:
*3\*vec1(cen,cen)*

Select entity for CEN snap:
*Specify a circle or an arc*

Specify second point of displacement or <use first point as displacement>:
*Specify a point or press*Enter

The following examples illustrate the meaning of vector and point calculations.

| Examples of vector and point calculations | |
| Expression | Meaning |
| vec(*a,b*) | Determines vector translation from point *a* to point *b*. |
| vec1(*a,b*) | Determines unit vector direction from point *a* to point *b*. |
| L\*vec1(*a,b*) | Determines vector of length *L* in the direction from point *a* to point *b*. |
| *a*+*v* | Determines point *b*, which is a translation of the point *a* through vector *v*. |
| *a*+[5<20] | Determines point *b* located 5 units away from point *a* at an angle of 20 degrees. Note that [5<20] is a vector in polar coordinates. |

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*