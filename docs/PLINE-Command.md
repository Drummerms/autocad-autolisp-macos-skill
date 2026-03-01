# PLINE (Command)

Creates a 2D polyline, a single object that is composed of line and arc segments.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Polyline.
![](../images/GUID-30386B3B-BD89-447D-A95A-EFCE56889866-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Polyline.

![](../images/GUID-09D550C2-1DF8-47D5-A66E-8119CFF6D4A4-low.gif)

The following prompts are displayed.

Specify start point
:   Sets the starting point for the polyline.

    * A temporary plus-shaped marker displays at the first point.
    * Pressing Enter starts a new polyline from the last endpoint specified in creating a polyline, line, or arc.

Specify next point
:   * If you specify a second point, you create straight segments.
    * If you enter
      *a* (for Arc), you create arc segments.

## Prompts Common to Line and Arc Segments

Close
:   Connects the first and last segments to create a closed polyline.

Halfwidth
:   Specifies the width from the center of a wide segment to an edge.

    ![](../images/GUID-79424AA9-1596-4360-B969-7211826090CA-low.png)

Width
:   Specifies the width of the next segment.

    ![](../images/GUID-05976B64-17F4-4679-B249-2231506B6200-low.png)

    Some things to keep in mind when defining the half-width or width of a polyline.

    * The starting width becomes the default ending width.
    * The ending width becomes the uniform width for all subsequent segments until you change the width again.
    * The starting and ending points of wide line segments are at the centerline of the segment.

      ![](../images/GUID-FCF42104-1E00-4185-B48D-423F947F573F-low.png)
    * Typically, the intersections of adjacent wide polyline segments are beveled.

      ![](../images/GUID-EAA852C0-D1B0-4252-8763-0AA160C85835-low.png)
    * No beveling is performed for nontangent arc segments, very acute angles, or when a dot-dash linetype is used.

Undo
:   Removes the most recently added segment.

## Line-Only Prompts

Arc
:   Begins creating arc segments tangent to the previous segment.

Length
:   Creates a segment of a specified length at the same angle as the previous segment. If the previous segment is an arc, the
    new line segment is tangent to that arc segment.

    ![](../images/GUID-545EFDBC-DE76-4EA3-B2C6-61B194CA2906-low.png)

## Arc-Only Prompts

Endpoint of arc
:   Completes an arc segment. The arc segment is tangent to the previous segment of the polyline.

Angle
:   Specifies the included angle of the arc segment from the start point.

    ![](../images/GUID-AA3D3084-9DE8-4F89-8052-F006D8EF8A50-low.png)

    Entering a positive number creates counterclockwise arc segments. Entering a negative number creates clockwise arc segments.

Center
:   Specifies an arc segment based on its center point.

    NOTE:For the Center option of the PLINE command, enter
    *ce*; for the Center object snap, enter
    *cen* or
    *center*.

    ![](../images/GUID-3E63E085-C0ED-45BB-8ECD-CFEA47D8DA72-low.png)

Direction
:   Specifies the tangent for the arc segment.

    ![](../images/GUID-F6173CC0-631C-42D4-BC39-9C1650C31450-low.png)

    * *(2) Tangent direction from the start point of the arc.* Specifies a point that establishes a tangency of the curve to the start point. The arc curves away from the vector between
      the start point and the tangent point.
    * *(3) Endpoint of the arc.*Specifies the endpoint of the arc segment.

    TIP:Press Ctrl to draw in a clockwise direction.

Line
:   Switches from drawing arc segments to drawing straight segments.

Radius
:   Specifies the radius of the arc segment.

Second pt
:   Specifies the second point and endpoint of a three-point arc.

## Linetype Pattern

The PLINEGEN system variable controls how linetype patterns generate around the vertices of a 2D polyline.

* *0.* Generates linetypes that start and end with a dash at each vertex of the polyline
* *1.* Generates linetypes in an uninterrupted pattern through the vertices of the polyline

![](../images/GUID-68E7FD4C-850A-460C-854D-BBAF85E4BEA4-low.png)

NOTE: Changing this value does not affect existing polylines. Change the Linetype Generation setting on the Properties palette
to update existing polylines.

#### Related Tasks

* [To Draw a Polyline with Straight Segments](To-Draw-a-Polyline-with-Straight-Segments.md)
* [To Draw a Line and Arc Polyline](To-Draw-a-Line-and-Arc-Polyline.md)
* [To Modify Polylines With PEDIT](To-Modify-Polylines-With-PEDIT.md)

#### Related Concepts

* [About Polylines](About-Polylines.md)
* [About Lines](About-Lines.md)

#### Related Information

* [About Curved Objects](About-Curved-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*