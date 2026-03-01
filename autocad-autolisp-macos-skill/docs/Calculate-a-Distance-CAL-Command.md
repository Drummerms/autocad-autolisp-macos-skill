# Calculate a Distance (CAL Command)

dist(p1,p2)
:   Determines the distance between two points,
    *p1* and
    *p2*. This is the same as the vector expression
    *abs(* **p1** *-* **p2** *)*.

dpl(p,p1,p2)
:   Determines the shortest distance between point
    *p* and the line passing through points
    *p1* and
    *p2*.

    ![](../images/GUID-7733BF4F-BE59-4104-A20A-3DA17DDE6562-low.png)

dpp(p,p1,p2,p3)
:   Determines the distance from a point
    *p* to a plane defined by three points (*p1,p2,p3*).

dist(p1,p2)
:   Determines the distance between two points,
    *p1* and
    *p2*. This is the same as the vector expression
    *abs(* **p1** *-* **p2** *)*.

    ![](../images/GUID-DEEC7B92-D7EC-4356-8F8D-3E3905BC20C8-low.png)

    The following example returns half the distance between the centers of two selected objects:

    *dist(cen,cen)/2*

    The following example finds the distance between the point 3,2,4 and a plane you define by selecting three endpoints:

    *dpp([3,2,4],end, end, end)*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*