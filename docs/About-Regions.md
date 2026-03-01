# About Regions

Regions are 2D enclosed areas that have physical properties such as centroids or centers of mass. You can combine existing
regions into a single, complex region.

Regions can be used for

* Extracting design information
* Applying hatching and shading
* Combining simple objects into more complex ones with Boolean operations.

  ![](../images/GUID-DD05F392-7BF7-4211-9445-5C3324CB55F8-low.png)

You can create regions from objects that form closed *loops*. Loops can be combinations of lines, polylines, circles, arcs, ellipses, elliptical arcs, and splines that enclose an area.

You can create regions by unifying, subtracting, or intersecting them:

Objects combined using UNION:

![](../images/GUID-152BEA2D-5925-41D6-B154-D158E38CD4E2-low.png)

Objects combined using SUBTRACT:

![](../images/GUID-44D87CDB-6BC9-4189-A5A0-DA6DF644CFC8-low.png)

Objects combined using INTERSECT:

![](../images/GUID-53589FF5-A0B7-443A-800F-77A456A11AA3-low.png)

## Invalid Boundaries

When a boundary cannot be determined, it might be because the specified internal point is not within a fully enclosed area.
In the example below, red circles are displayed around unconnected endpoints to identify gaps in the boundary.

![](../images/GUID-1BF19E0E-4040-43FA-861E-6D5CC6BE2AC2-low.png)

#### Related References

* [Commands for Regions and Areas](Commands-for-Regions-and-Areas.md)

#### Related Information

* [To Work With Regions](To-Work-With-Regions.md)
* [To Work With Complex Regions](To-Work-With-Complex-Regions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*