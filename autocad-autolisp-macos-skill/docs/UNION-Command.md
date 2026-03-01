# UNION (Command)

Combines selected 3D solids, surfaces, or 2D regions by addition.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Boolean drop-down ![](../images/ac.menuaro.gif) Union.
![](../images/GUID-ADD48D06-59BE-40B3-8AA8-303E5B8BA2F1-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Solid Editing ![](../images/ac.menuaro.gif) Union.

## Summary

You can combine two or more 3D solids, surfaces, or 2D regions into a single, composite 3D solid, surface, or region. You
must select the same type of objects to combine.

![](../images/GUID-375E1498-395C-49B7-B7F8-A0FF01402B95-low.gif)

### Using the Union Command with Surfaces

Although you can use the UNION command with surfaces, it will cause the surface to lose associativity. Instead, it is recommended
that you use the surface editing commands:

* SURFBLEND
* SURFFILLET
* SURFPATCH

### Using the Union Command with Solids and Regions

The selection set can contain objects that lie in any number of arbitrary planes. For mixed object types, selection sets are
divided into subsets that are joined separately. Solids are grouped in the first subset. The first selected region and all
subsequent coplanar regions are grouped in the second set, and so on.

![](../images/GUID-46641F87-BBC4-46C9-B336-865654E8A4F2-low.png)

The resulting composite solid includes the volume enclosed by all of the selected solids. Each of the resulting composite
regions encloses the area of all regions in a subset.

![](../images/GUID-DFD938DF-B754-4902-9BAC-8B310253EBAE-low.png)

You cannot use UNION with mesh objects. However, if you select a mesh object, you will be prompted to convert it to a 3D solid
or surface.

## List of Prompts

The following prompt is displayed.

Select objects
:   Select the 3D solids, surfaces, or regions to be combined.

#### Related Concepts

* [About Creating Composite Objects](About-Creating-Composite-Objects.md)
* [About Regions](About-Regions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*