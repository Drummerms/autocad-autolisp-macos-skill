# Convert Points Between UCS and WCS (CAL Command)

Normally, the program assumes all coordinates to be relative to the current UCS. The following functions convert points between
UCS and WCS.

w2u(p1)
:   Converts point
    *p1* expressed in the WCS to the current UCS.

u2w(p1)
:   Converts point
    *p1* expressed in the current UCS to the WCS.

You can use
*w2u* to find the WCS origin in terms of the current UCS:

*w2u([0,0,0])*

## Filtering the X, Y, and Z Components of a Point or Vector

The following functions filter the
*X*,
*Y*, and
*Z* components of a point or vector.

| Point-filter functions | |
| Function | Description |
| xyof(*p1*) | *X* and *Y* components of a point; *Z* component is set to 0.0 |
| xzof(*p1*) | *X* and *Z* components of a point; *Y* component is set to 0.0 |
| yzof(*p1*) | *Y* and *Z* components of a point; *X* component is set to 0.0 |
| xof(*p1*) | *X* component of a point; *Y* and *Z* components are set to 0.0 |
| yof(*p1*) | *Y* component of a point; *X* and *Z* components are set to 0.0 |
| zof(*p1*) | *Z* component of a point; *X* and *Y* components are set to 0.0 |
| rxof(*p1*) | *X* component of a point |
| ryof(*p1*) | *Y* component of a point |
| rzof(*p1*) | *Z* component of a point |

The following example provides the
*Z* component of a point expressed in spherical coordinates:

*zof([2<45<45])*

The following example provides a point whose
*X* and
*Y* coordinate values are taken from point
*a* and the
*Z* coordinate value from point
*b:*

*xyof(a)+zof(b)*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*