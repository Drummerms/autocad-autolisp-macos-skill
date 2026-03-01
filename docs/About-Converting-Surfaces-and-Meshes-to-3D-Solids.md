# About Converting Surfaces and Meshes to 3D Solids

You can convert eligible surface and mesh objects to 3D solids.

When you create 3D models, you can use 3D surfaces for precise surface control and analysis, and 3D meshes for freeform sculpting.
You can convert these objects into 3D solids for applying Boolean operations, generating sections, and extracting physical
properties.

NOTE:The DELOBJ system variable controls whether the objects you select are automatically deleted when the 3D object is created.

## Convert 3D Surfaces to 3D Solids

You can convert surfaces to 3D solids by extruding the surface with THICKEN. To thicken the surface inward in this example,
a negative value was entered.

![](../images/GUID-D8E83C21-0BE7-419A-ACB3-1ECF85F328D6-low.png)

Use the SURFSCULPT command to convert a set of surfaces that completely enclose a volume to a 3D solid. In the illustration
below, an extruded arc is intersected by two planar surfaces to enclose a "watertight" volume.

![](../images/GUID-314306BB-D991-40D8-B96B-B9308581ED5D-low.png)

NOTE: A good practice is to make sure that the enclosing surfaces overlap or intersect to help you avoid tiny gaps.

## Convert 3D Meshes to 3D Solids

When you convert mesh objects to 3D solids, the shape of the new solid object approximates, but does not exactly duplicate,
the original mesh object. You can control the differentiation somewhat by specifying whether the result is smooth or faceted
with the SMOOTHMESHCONVERT system variable. You can also specify whether coplanar faces are merged, which optimizes them.

For example, the illustrated 3D mesh was first modified by increasing its smoothness level, and then it was converted into
a smooth 3D solid.

![](../images/GUID-927FC38E-FB49-434D-BFB6-DF1718F3320A-low.png)

NOTE: You can also convert meshes to 3D solids by first converting them to surfaces and then thickening them.

#### Related Tasks

* [To Convert One or More Surfaces to Solids](To-Convert-One-or-More-Surfaces-to-Solids.md)
* [To Convert Contiguous Surfaces That Enclose a Volume to a 3D Solid Object](To-Convert-Contiguous-Surfaces-That-Enclose-a-Volume-to-a-3D-Solid-Object.md)
* [To Convert a Mesh Object to a 3D Solid](To-Convert-a-Mesh-Object-to-a-3D-Solid.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*