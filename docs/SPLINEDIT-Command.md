# SPLINEDIT (Command)

Modifies the parameters of a spline or converts a spline-fit polyline to a spline.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Spline Edit.
![](../images/GUID-AFBF4398-17D8-4574-9CDF-2E45BD29DD9C-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

Modifies the data that defines a spline, such as the number and weight of control vertices, the fit tolerance, and the starting
and ending tangents.

NOTE: SPLINEDIT automatically converts spline-fit polylines to splines even if you immediately exit SPLINEDIT after selecting the
spline-fit polyline.

The data that defines a spline is represented in one of two formats: as a control frame or as fit points. The format can change
depending on how the spline was orginally created, the options selected from the grip menus, or the options used in SPLINEDIT.

You can change any of following data:

* Control frame data consists of control vertices, the polynomial degree of the spline, and the weights assigned to each control
  vertex.
* Fit data consists of fit points, knot parameterization, the fit tolerance, and the tangents at the endpoints of the spline.

NOTE: Switching from displaying control vertices to fit points automatically changes the selected spline to degree 3. Splines originally
created using higher-degree equations will likely change shape as a result. In addition, if the spline was created using a
positive tolerance value, the fit points will be relocated to the knots on the spline, and the tolerance value is reset to
0.

The following prompts are displayed.

### Select spline

Specifies which spine you want to modify.

### Close/Open

One of the following options displays, depending on whether the selected spline is open or closed. An open spline has two
endpoints, while a closed spline forms a loop.

Close
:   Closes an open spline by defining the last point to be coincident with the first. By default, closed splines are periodic,
    maintaining curvature continuity (C2) along the entire curve.

Open
:   Opens a closed spline by removing the final curve segment between the first and last points specified when the spline was
    originally created.

### Join

Combines a selected spline with other splines, lines, polylines, and arcs at coincident endpoints to form a larger spline.
Objects are joined with kinks at the points where they are joined (C0 continuity).

### Fit Data

Edits fit point data using the following options:

Add
:   Adds fit points to the spline.

    After selecting a fit point, specify a new fit point to be added to the spline in the direction of the next fit point, which
    is automatically highlighted.

    If you select the last fit point on an open spline, the new fit point is added to the end of the spline.

    If you select the first fit point on an open spline, you have the option of specifying whether the new fit point is added
    before or after the first point.

    ![](../images/GUID-EFC5A1EF-3517-4A4B-A179-F3FF44DC8547-low.png)

Close/Open
:   One of the following options displays, depending on whether the selected spline is open or closed. An open spline has two
    endpoints, while a closed spline forms a loop.

    * *Close.* Closes an open spline by defining the last point to be coincident with the first. By default, closed splines are periodic,
      maintaining curvature continuity (C2) along the entire curve.
    * *Open.* Opens a closed spline by removing the final curve segment between the first and last points specified when the spline was
      originally created.

Delete
:   Removes selected fit points from a spline.

Kink
:   Adds a knot and fit point at the specified location on the spline, which does not maintain tangent or curvature continuity
    at that point.

Move
:   Moves fit points to new locations.

    * *New Location.* Moves the selected fit point to the specified location.

      ![](../images/GUID-5160A89D-3C13-4110-8043-92FBAC5EB4AC-low.png)
    * *Next.*Specifies the next fit point.
    * *Previous.*Specifies the previous fit point.
    * *Select point.* Specifies any fit point on the spline.

Purge
:   Replaces the fit data from the spline with control vertices.

Tangents
:   Changes the starting and ending tangents of a spline. Specify a point to establish a tangent direction. You can use object
    snaps such as Perpendicular or Parallel.

    * *Specify tangent*. (Available for closed splines) Specifies a new tangent direction at the point of closure.
    * *System default.* Calculates the default end tangents.

Tolerance
:   Refits the spline to the existing fit points using the new tolerance value.

    ![](../images/GUID-8618EA29-41E6-41EA-9800-5A32C5680FCB-low.png)

Exit
:   Returns to the previous prompt.

### Edit Vertex

Edits control frame data using the following options:

Add
:   Adds a new control vertex at the point you specify that is located between two existing control vertices.

Delete
:   Removes a selected control vertex.

Elevate Order
:   Increases the polynomial order (degree plus one) of the spline. This results in increasing the number of control vertices
    across the spline.

    The maximum value is 26.

Move
:   Relocates a selected control vertex.

    * New Location
    * Next
    * Previous
    * Select Point

Weight
:   Changes the weight of a specified control vertex.

    * *New weight.* Recalculates the spline based on the new weight value for the specified control vertex. A larger value pulls the spline closer
      to the control vertex.

Exit
:   Returns to the previous prompt.

### Convert to Polyline

Converts the spline to a polyline.

The precision value determines how closely the resulting polyline matches the spline. Valid values are any integer between
0 and 99.

NOTE: A high precision value will decrease performance.

The PLINECONVERTMODE system variable determines whether the polylines are created with linear or arc segments.

The DELOBJ system variable determines whether the original spline is retained.

### Reverse

Reverses the direction of the spline. This option is intended primarily for third-party applications.

### Undo

Cancels the last action.

### Exit

Ends the command.

#### Related Concepts

* [About Modifying Splines](About-Modifying-Splines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*