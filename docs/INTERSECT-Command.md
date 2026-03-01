# INTERSECT (Command)

Creates a 3D solid, surface, or 2D region from overlapping solids, surfaces, or regions.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Boolean drop-down ![](../images/ac.menuaro.gif) Intersect.
![](../images/GUID-11186647-B2A6-43AE-A1E6-2DE3092E7AA9-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) Solid Editing
![](../images/ac.menuaro.gif) Intersect.

## Summary

With INTERSECT, you can create a 3D solid from the common volume of two or more existing 3D solids, surfaces, or regions.
If you select a mesh, you can convert it to a solid or surface before completing the operation.

You can extrude 2D profiles and then intersect them to create a complex model efficiently.

![](../images/GUID-1C31FCED-9999-4012-B6F9-518D00711466-low.gif)

The selection set can contain regions, solids, and surfaces that lie in any number of arbitrary planes. INTERSECT divides
the selection set into subsets and tests for intersections within each subset. The first subset contains all the solids and
surfaces in the selection set. The second subset contains the first selected region and all subsequent coplanar regions. The
third subset contains the next region that is not coplanar with the first region and all subsequent coplanar regions, and
so on until all regions belong to a subset.

![](../images/GUID-054B9F79-58B7-489C-A15B-36510B345FE2-low.png)

#### Related Concepts

* [About Creating Composite Objects](About-Creating-Composite-Objects.md)
* [About Regions](About-Regions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*