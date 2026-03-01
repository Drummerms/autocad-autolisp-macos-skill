# About Creating Meshes

Mesh tessellation provides enhanced capabilities for modeling object shapes in a more detailed way.

Starting with AutoCAD-based products 2010 and later, the default mesh object type can be smoothed, creased, split, and refined.
Although you can continue to create the legacy polyface and polygon mesh types, you can obtain more predictable results by
converting to the newer mesh object type.

![](../images/GUID-73A45881-E2ED-47D3-A613-8FDAE3F805D6-low.png)

## Methods for Creating Mesh

You can create mesh objects using the following methods:

* *Create mesh primitives.* Create standard shapes, such as boxes, cones, cylinders, pyramids, spheres, wedges, and tori (MESH).
* *Create mesh from other objects.* Create ruled, tabulated, revolved, or edge-defined mesh objects, whose boundaries are interpolated from other objects or
  points (RULESURF, TABSURF, REVSURF, EDGESURF).
* *Convert from other object types.* Convert existing solid or surface models, including composite models, to mesh objects (MESHSMOOTH).
* *Create custom meshes (legacy).* Use 3DMESH to create polygon meshes, usually scripted with AutoLISP routines, to create open-ended mesh. Use PFACE to create
  mesh with multiple vertices defined by coordinates that you specify. Although you can continue to create legacy polygonal
  and polyface meshes, it is recommended that you convert to the enhanced mesh object type to obtain enhanced editing capabilities.

## About Tessellation

Tessellation is a collection of planar shapes that tile a mesh object. The tessellation divisions, visible in unselected
mesh objects, mark the edges of the editable mesh faces. (To see these divisions in the Hidden or Conceptual visual styles,
VSEDGES must be set to 1.)

When you smooth and refine mesh objects, you increase the density of the tessellation (the number of subdivisions).

* *Smoothing.* Increases how closely the mesh surface adheres to a rounded form. You can increase mesh smoothness levels for selected objects
  in increments or by changing the smoothness level in the Properties window. Smoothness level 0 (zero) applies the lowest level
  of smoothing to a mesh object. Smoothness level 4 applies a high degree of smoothness.

  ![](../images/GUID-BEE8FC2C-B974-4115-ADDB-16C1CE51714C-low.png)
* *Refinement.* Quadruples the number of subdivisions in a selected mesh object or in a selected subobject, such as a face. Refinement also
  resets the current smoothness level to 0, so that the object can no longer be sharpened beyond that level. Because refinement
  greatly increases the density of a mesh, you might want to restrict this option to areas that require finely detailed modification.
  Refinement also helps you mold smaller sections with less effect on the overall shape of the model.

  ![](../images/GUID-B0213499-8FBA-4603-89EA-AC21CF5FD548-low.png)

While highly refined mesh gives you the ability to make detailed modifications, it can decrease program performance. By maintaining
maximum smoothness, face, and grid levels, you can help ensure that you do not create meshes that are too dense to modify
effectively (use SMOOTHMESHMAXLEV and SMOOTHMESHGRID).

## Setting Mesh Properties

You can set defaults for mesh primitives and modify some properties after creating mesh objects.

* *Mesh Primitive options.*Use the system variables, for example DIVMESHBOXHEIGHT or DIVMESHWEDGESLOPE, to set default tessellation for new mesh objects
  of a given type.
* *Properties window.* Modifies properties for both the mesh object and its subobjects after they are created. For a selected mesh object, you can
  modify the level of smoothness. For faces and edges, you can apply or remove creasing and modify crease retention levels.
* *Level of smoothness.* By default, the mesh primitive objects that you create have no smoothness. You can change this default with the Settings
  option of the MESH command. The modified smoothness value is maintained only during the current drawing session.

#### Related Tasks

* [To Change the Default Level of Smoothness of New Mesh Primitive Objects](To-Change-the-Default-Level-of-Smoothness-of-New-Mesh-Primitive-Objects.md)

#### Related Concepts

* [About Creating Mesh Boxes](About-Creating-Mesh-Boxes.md)
* [About Creating Mesh Cones](About-Creating-Mesh-Cones.md)
* [About Creating Mesh Cylinders](About-Creating-Mesh-Cylinders.md)
* [About Creating Mesh Pyramids](About-Creating-Mesh-Pyramids.md)
* [About Creating Mesh Spheres](About-Creating-Mesh-Spheres.md)
* [About Creating Mesh Wedges](About-Creating-Mesh-Wedges.md)
* [About Creating Mesh Tori](About-Creating-Mesh-Tori.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*