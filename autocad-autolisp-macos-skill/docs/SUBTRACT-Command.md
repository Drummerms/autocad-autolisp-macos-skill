# SUBTRACT (Command)

Combines selected 3D solids or 2D regions by subtraction.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Boolean drop-down ![](../images/ac.menuaro.gif) Subtract.
![](../images/GUID-B8FD9C75-EAF3-42AC-B3BB-AF8633948F70-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Region ![](../images/ac.menuaro.gif) Subtract.

## Summary

With SUBTRACT, you can create a 3D solid by subtracting one set of existing 3D solids from another, overlapping set. You can
create a 2D region object by subtracting one set of existing region objects from another, overlapping set. You can select
only regions for use with this command.

NOTE:Using SUBTRACT with 3D surfaces is not recommended. Use the
[SURFTRIM](SURFTRIM-Command.md) command instead.

Select the objects that you want to keep, press Enter, then select the objects that you want to subtract.

![](../images/GUID-FA196C9E-A681-4B67-88A6-DF402C6F3E5E-low.gif)

Objects in the second selection set are subtracted from objects in the first selection set. A single new 3D solid, surface,
or region is created.

![](../images/GUID-B263D983-0344-4610-BA6A-3B68BBA56E3D-low.png)

Objects in the second selection set are subtracted from objects in the first selection set. A single new region is created.

![](../images/GUID-7F42CA3C-9CDF-4BAE-9634-CC62F11027F0-low.png)

You can only subtract regions from other regions that are on the same plane. However, you can perform simultaneous SUBTRACT
actions by selecting sets of regions on different planes. The program then produces separate subtracted regions on each plane.
Regions for which there are no other selected coplanar regions are rejected.

You cannot use SUBTRACT with mesh objects. However, if you select a mesh object, you will be prompted to convert it to a 3D
solid or surface.

## List of Prompts

The following prompts are displayed.

Select objects (to subtract from)
:   Specifies the 3D solids, surfaces, or regions to be modified by subtraction.

Select objects (to subtract)
:   Specifies the 3D solids, surfaces, or regions to subtract.

#### Related Concepts

* [About Regions](About-Regions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*