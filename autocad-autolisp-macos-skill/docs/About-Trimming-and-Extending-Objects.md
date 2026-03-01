# About Trimming and Extending Objects

You can shorten or lengthen objects to meet the edges of other objects.

In practice, this means you can first create, copy, or offset an object such as a line or an arc, and then later adjust it
to fit exactly between other objects.

## Quick Mode Operation - Default

After you start the TRIM or EXTEND commands, simply select the objects near the ends to be trimmed or extended. There are
three default options for selecting the objects:

* Two-point fence selection. Click two points that define a segment crossing through the objects near the ends to be trimmed
  or extended. In this case, the lines are being extended:

  ![](../images/GUID-9B8A6029-7E7F-4D49-AE5B-22C3333CB65A-low.png)
* Individual selection. Simply click one or more objects near the ends to be trimmed or extended. In this case, the selected
  line is being trimmed:

  ![](../images/GUID-1BF0FFF9-2758-4023-93CD-221010AF19D3-low.png)
* Freehand selection. Click and hold down the left mouse button in an empty area and drag the cursor through one or more objects
  near the ends to be trimmed or extended. In this case, the lines are being trimmed:

  ![](../images/GUID-84360D09-76D4-4FB3-8B48-53F3C6552AEB-low.png)

NOTE:Hold down Shift to switch temporarily between the TRIM and EXTEND commands.

## Standard Mode Operation

When you use Standard mode, objects you select as cutting edges or boundary edges are not required to intersect the object
being trimmed. You can trim or extend an object to a projected edge or to an extrapolated intersection; that is, where the
objects would intersect if they were extended.

If you do not specify a boundary and press Enter at the Select Objects prompt, all displayed objects become potential boundaries.

NOTE: To select cutting edges or boundary edges that include blocks, you can use only the single selection, Crossing, Fence, and
Select All options.

## Trim Objects

You can trim objects so that they end precisely at the edges of selected objects. An object can also be one of the cutting
edges and one of the objects being trimmed. For example, in the illustrated light fixture, the circle is a cutting edge for
the construction lines and is also being trimmed.

![](../images/GUID-7B90379A-7E4F-49C0-B813-64A64480F68C-low.png)

When you trim several objects, the different selection methods can help you choose the current cutting edges and objects to
trim. In the following example, the cutting edges are selected using crossing selection.

![](../images/GUID-CE55EAAD-6E66-44DE-BBDD-09C8760B4554-low.png)

The following example uses the fence selection method to select a series of objects for trimming.

![](../images/GUID-C01D11D6-F334-4FAB-9B8B-A9B4C938348E-low.png)

You can trim objects to their nearest intersection with other objects. Instead of selecting cutting edges, you press Enter.
Then, when you select the objects to trim, the nearest displayed objects act as cutting edges. In this example, the walls
are trimmed so that they intersect smoothly.

![](../images/GUID-D42C09AD-99CF-4352-A0EC-66D6857FDAF8-low.png)

NOTE:You can extend objects without exiting the TRIM command. Press and hold Shift while selecting the objects to be extended.
When COMMANDPREVIEW system variable is on, an interactive preview of the command outcome is shown.

## Extend Objects

You can extend objects so that they end precisely at boundary edges defined by other objects. In this example, you extend
the lines precisely to a circle, which is the boundary edge.

![](../images/GUID-7E3B21FE-C2F2-4D8C-A3C0-8CD3AF9BF929-low.png)

NOTE:You can trim objects without exiting the EXTEND command. Press and hold Shift while selecting the objects to be trimmed. When
COMMANDPREVIEW system variable is on, an interactive preview of the command outcome is shown.

## Trim and Extend Wide Polylines

2D wide polylines trim and extend at their centerlines. The ends of wide polylines are always squared off to the end of the
polyline, not rounded or at a diagonal.

If you trim or extend a tapered 2D polyline segment, the width of the extended end is corrected to continue the original taper
to the new endpoint, if possible. Otherwise, the ending width is forced to 0, a sharp point.

![](../images/GUID-AF9AA68D-9FDF-4DB5-8E14-FF9BA6A6F5B4-low.png)

## Trim and Extend Spline-Fit Polylines

Trimming a spline-fit polyline removes the curve-fit information and changes the spline-fit segments into ordinary polyline
segments.

Extending a spline-fit polyline adds a new vertex to the control frame for the polyline.

## Extend a Spline

Extending a spline preserves the shape of the original portion of the spline, but the extended portion is linear and tangent
to the end of the original spline.
![](../images/GUID-AD8AC4AB-272A-4B3B-9CD7-B3ECCD8AC903-low.png)

## Trim or Extend in 3D

You can trim or extend an object to any other object in 3D space, regardless of whether the objects are on the same plane
or parallel to the cutting or boundary edges. In the TRIM and EXTEND commands, use the Project and Edge options to select
one of three projections for trimming or extending:

* The
  *XY* plane of the current UCS
* The plane of the current view
* True 3D, which is not a projection

#### Related Concepts

* [About Resizing or Reshaping Objects](About-Resizing-or-Reshaping-Objects.md)

#### Related Information

* [To Extend an Object](To-Extend-an-Object.md)
* [To Trim an Object](To-Trim-an-Object.md)
* [To Trim in 3D Using the Current View Plane](To-Trim-in-3D-Using-the-Current-View-Plane.md)
* [To Trim Objects in 3D Wireframe Models](To-Trim-Objects-in-3D-Wireframe-Models.md)
* [To Stretch an Object](To-Stretch-an-Object.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*