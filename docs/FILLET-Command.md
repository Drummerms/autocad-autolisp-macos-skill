# FILLET (Command)

Rounds and fillets the edges of objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Fillet drop-down ![](../images/ac.menuaro.gif) Fillet.
![](../images/GUID-96B6BF37-E721-4F8B-BDC9-22D1F1036AC4-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Fillet.

A round or fillet is

* an arc that is created tangent between two 2D objects.
* a curved transition between two surfaces or adjacent faces on a 3D solid.

In this example, an arc is created tangent to the selected lines, which are trimmed to meet the endpoints of the arc.

![](../images/GUID-91DC1D1C-8B9A-48A4-9377-FBDC62CCC8CB-low.gif)

## Create 2D Fillets

A round or fillet can be created between two objects of the same or different object types: 2D polylines, arcs, circles, ellipses,
elliptical arcs, lines, rays, splines, and xlines.

If the two selected objects are on the same layer, the arc defined is created on that layer. Otherwise, the arc is created
on the current layer. The layer affects object properties including color and linetype.

The following prompts are displayed when creating a 2D fillet.

### First Object

Select the first of two objects or the first line segment of a 2D polyline to define the fillet.

![](../images/GUID-2016A0A5-070D-4C13-BD5F-43EB08190F6F-low.png)

Second object or shift-select to apply corner
:   Select the second object or line segment of a 2D polyline to define the fillet.

    You can also hold down the Shift key before selecting the second object or line segment of a 2D polyline to extend or trim
    the selected objects to form a sharp corner. While Shift is held down, a temporary value of zero is assigned to the current
    fillet radius value.

    If the selected objects are straight line segments of a 2D polyline, the line segments can be adjacent to each other or separated
    by one other segment. When the selected segments are separated by a segment, the segment that separates them is removed and
    replaced with the fillet.

    The direction and length of the arc created is determined by the points picked to select the objects. Always select an object
    closest to where you want the endpoints of the fillet to be drawn.

    ![](../images/GUID-912EFADC-CD36-4011-8913-90602C2A9027-low.png)

    When a circle is selected, the circle is not trimmed; the fillet drawn meets the circle smoothly.

    ![](../images/GUID-DCDBDB86-88A9-45E8-97A4-D89C288C8636-low.png)

    NOTE:Adding a fillet or round to a hatch boundary that was defined with individual objects results in the removal of hatch associativity.
    If the hatch boundary was defined from a polyline, associativity is maintained.

### Undo

Reverses the previous action in the command.

### Polyline

Inserts a fillet at each vertex of a 2D polyline where two straight line segments meet. The fillets become new segments of
the polyline, unless the Trim option is set to No Trim.

![](../images/GUID-831A8073-FFAF-4441-AE83-EF5E2C88B930-low.png)

Select 2D polyline
:   Select the 2D polyline to insert fillets at each vertex.

    If an arc segment separates two straight line segments, the arc segment is removed and replaced with the fillet.

    NOTE:Line segments that are too short to accommodate the fillet radius are not modified.

### Radius

Sets the radius for subsequent fillets; changing this value does not affect existing fillets.

NOTE:A radius value of zero can be used to create a sharp corner. Filleting two lines, rays, xlines, or line segments of a 2D polyline
with a radius of zero extends or trims the objects so they intersect.

### Trim

Controls whether the selected objects are trimmed to meet the endpoints of the fillet.

* *Trim.* Selected objects or line segments are trimmed to meet the endpoints of the fillet.
* *No Trim.* Selected objects or line segments are not trimmed before the fillet is added.

The current value is stored in the TRIMMODE system variable.

### Multiple

Allows for the rounding of more than one set of objects.

## Create 3D Fillets (Not available in AutoCAD LT)

A fillet can be added along the edge of a 3D solid or surface. When prompted to select the first object to define a fillet,
select the edge of a 3D solid or surface.

NOTE:If you select a mesh object, you can choose to convert the mesh to a 3D solid or surface and continue the operation.

The following prompts are displayed after selecting the edge of a 3D solid or surface.

### Edge

When the edge of a 3D solid is selected, you can select multiple edges to fillet. Press Enter to end selection.

![](../images/GUID-9BEB89F8-34B4-4193-9E3C-B97E39D8A132-low.png)

If you select three or more edges that converge at a vertex to form the corner of a box, the vertices are blended to form
part of a sphere if the three incident fillets have the same radii.

Chain
:   Changes selection mode between single-edge and sequential tangent edges, called a
    *chain* selection.

    For example, if you select an edge along the side of a 3D solid, the tangential edges that touch the selected edge are selected.

    ![](../images/GUID-985D377D-086B-4330-84AD-FE1F07EAD201-low.png)

    * *Edge Chain.* Enables sequential tangent edge selection mode.
    * *Edge.* Enables single-edge selection mode.

Loop
:   Specifies a loop of edges on the face of a 3D solid or surface.

    For example, if you select an edge on the top of a 3D solid box, all other tangential edges along the top of the box are selected.

    ![](../images/GUID-BCE65052-8373-4371-BBF4-E947CA609F9F-low.png)

    For any edge, there are two possible loops. After selecting a loop edge, you are prompted to accept the current selection
    or select the adjacent loop.

    * *Accept.* Selects the edges of the current loop.
    * *Next.* Selects the edges of the adjacent loop.

### Radius

Sets the radius of the fillet.

### Expression

Controls the fillet radius with a mathematical expression.

See About Controlling Geometry With the Parameters Manager for a list of operators and functions allowed.

#### Related Tasks

* [To Work With 2D Fillets and Rounds](To-Work-With-2D-Fillets-and-Rounds.md)
* [To Fillet a 3D Solid Edge](To-Fillet-a-3D-Solid-Edge.md)

#### Related Concepts

* [About Fillets and Rounds](About-Fillets-and-Rounds.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*