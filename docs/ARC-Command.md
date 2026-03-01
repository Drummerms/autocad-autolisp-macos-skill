# ARC (Command)

Creates an arc.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Arc drop-down.
![](../images/GUID-6E1BE1CC-A3C0-4FD0-A44D-8A242CAF780B-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Arc.

To create an arc, you can specify combinations of center, endpoint, start point, radius, angle, chord length, and direction
values. Arcs are drawn in a counterclockwise direction by default. Hold down the Ctrl key as you drag to draw in a clockwise
direction.

The following prompts are displayed.

## Start point

Draws an arc using three specified points on the arc's circumference. The first point is the start point (1).

Second point ![](../images/GUID-6E1BE1CC-A3C0-4FD0-A44D-8A242CAF780B-low.png)
:   Specify the second point (2) is a point on the circumference of the arc.

    End point
    :   Specify the final point (3) on the arc.

        ![](../images/GUID-2A34A0C9-F6C1-4CDC-BDEA-9478814FE594-low.gif)

        You can specify a three-point arc either clockwise or counterclockwise.

Center
:   Specify the second point (2) is the center of the circle of which the arc is a part.

    End point ![](../images/GUID-2151E970-19A0-4BEE-96B2-9106687A191C-low.png)
    :   Using the center point (2), draws an arc counterclockwise from the start point (1) to an endpoint that falls on an imaginary
        ray drawn from the center point through the third point (3).

        ![](../images/GUID-BD4CB9A6-7351-45F0-8FFF-25184E21B135-low.png)

        The arc does not necessarily pass through this third point, as shown in the illustration.

        The distance between the start point and the center determines the radius. The endpoint is determined by a line from the center
        that passes through the third point.

    Angle ![](../images/GUID-184A5A2B-C1A5-42BA-8F32-44479C0CAEC5-low.png)
    :   The distance between the start point and the center determines the radius. The other end of the arc is determined by specifying
        an included angle that uses the center of the arc as the vertex.

        If the angle is negative, a clockwise arc is drawn.

        ![](../images/GUID-BDE30960-CAF7-4185-9B42-19E9E617C505-low.gif)

    Chord length ![](../images/GUID-76E3BE2E-3449-4DEB-B26B-1FFD211AB7CF-low.png)
    :   Draws either a minor or a major arc based on the distance of a straight line between the start point and endpoint.

        If the chord length is positive, the minor arc is drawn counterclockwise from the start point. If the chord length is negative,
        the major arc is drawn counterclockwise.

        ![](../images/GUID-29C010C8-31F1-449A-B6FF-24EC51CB9709-low.png)

End
:   Specify the second point (2) is the endpoint of the arc.

    Center point
    :   Draws an arc counterclockwise from the start point (1) to an endpoint that falls on an imaginary ray drawn from the center
        point (3) through the second point specified (2).

        ![](../images/GUID-01916CF6-B07D-46AB-B34D-C9BF7FC2249B-low.png)

    Angle ![](../images/GUID-52402C2F-AE74-46CC-8055-7CBF4D35AD92-low.png)
    :   Draws an arc counterclockwise from the start point (1) to an endpoint (2), with a specified included angle. Specify the second
        point (2) is the endpoint of the arc. If the angle is negative, a clockwise arc is drawn.

        ![](../images/GUID-DB2A2332-5726-4631-B004-3F6AEE520051-low.png)

    Direction ![](../images/GUID-68BBDD98-B508-453B-AFDB-BE17CE8386D1-low.png)
    :   Begins the arc tangent to a specified direction. It creates any arc, major or minor, clockwise or counterclockwise, beginning
        with the start point (1), and ending at an endpoint (2). The direction is determined from the start point.

        ![](../images/GUID-C0BA5D07-826D-49E3-9A01-B0EF15F95696-low.png)

    Radius ![](../images/GUID-9C1C5369-8399-4925-82AB-4F6D8609AED3-low.png)
    :   Draws the minor arc counterclockwise from the start point (1) to the endpoint (2). If the radius is negative, the major arc
        is drawn.

        ![](../images/GUID-D047C140-11D6-42A0-BE70-285E4E840032-low.png)

## Center

Starts by specifying the center of the circle of which the arc is a part.

Start point
:   Specify start point of arc.

End point ![](../images/GUID-1FDD8A3B-7EFE-49FE-A1E3-A50C89DF27E3-low.png)
:   Draws an arc counterclockwise from the start point (2) to an endpoint that falls on an imaginary ray drawn from the center
    point (1) through a specified point (3).

    ![](../images/GUID-BD4CB9A6-7351-45F0-8FFF-25184E21B135-low.png)

Angle ![](../images/GUID-434190A0-1015-4EB7-BDE5-091C4F43D871-low.png)
:   Draws an arc counterclockwise from the start point (2) using a center point (1) with a specified included angle. If the angle
    is negative, a clockwise arc is drawn.

    ![](../images/GUID-C125C3C5-B716-4904-AAEE-92B19BCCFF2F-low.png)

Chord length ![](../images/GUID-8891AE6A-7AA3-4F91-81A8-68BD9E6C8EEB-low.png)
:   Draws either a minor or a major arc based on the distance of a straight line between the start point and endpoint.

    If the chord length is positive, the minor arc is drawn counterclockwise from the start point. If the chord length is negative,
    the major arc is drawn counterclockwise.

    ![](../images/GUID-29C010C8-31F1-449A-B6FF-24EC51CB9709-low.png)

## Tangent to last line, arc, or polyline ![](../images/GUID-2A5192E6-DF4D-40F2-911A-07CC8F84F904-low.png)

Immediately after you create a line or an arc, you can start an arc that is tangent at an endpoint by starting the ARC command
and pressing ENTER at the Specify Start Point prompt. You need to specify only the endpoint of the arc.

![](../images/GUID-025E08EE-CB38-4515-B06F-DBB7BFF2AB9D-low.gif)

End point of arc
:   Specify a point (1).

#### Related Information

* [About Curved Objects](About-Curved-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*