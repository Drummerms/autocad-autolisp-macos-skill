# Calculate a Point on a Line (CAL Command)

The
*plt* and
*pld* functions return a point on a given line. You can specify the location of the point on the line either by its distance from
the first point or parametrically by a
*t* parameter.

pld(p1,p2,dist)
:   Calculates a point on the line passing through points
    *p1* and
    *p2*. The parameter
    *dist* defines the distance of the point from the point
    *p1*.

plt(p1,p2,t)
:   Calculates a point on the line passing through points
    *p1* and
    *p2*. The parameter *t* defines the parametric location of the point on the line.

The following are examples of the parameter *t:*

*If t=0 the point is p1*

*If t=0.5 the point is the midpoint between p1 and p2*

*If t=1 the point is p2*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*