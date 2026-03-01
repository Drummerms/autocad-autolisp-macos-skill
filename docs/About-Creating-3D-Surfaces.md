# About Creating 3D Surfaces

Surface modeling provides the ability to create and edit associative and NURBS surfaces.

A surface is a 3D object that is an infinitely thin shell. There are 2 types of surfaces: procedural and NURBS.

* *Procedural surfaces* can be associative, maintaining relationships with other objects so that they can be manipulated as a group.
* *NURBS surfaces* are not associative. Instead, they have control vertices that allow you to sculpt shapes in a more natural way.

Use procedural surfaces to take advantage of associative modeling, and use NURBS surfaces to take advantage of sculpting with
control vertices. The illustration below shows a procedural surface on the left, and a NURBS surface on the right.

![](../images/GUID-1BC962DD-4424-4B4E-A0D8-F1BEFC83FB68-low.gif)

## 3D Surface Modeling

A surface model is a thin shell that does not have mass or volume. AutoCAD provides two types of surfaces: procedural surfaces
and NURBS surfaces.

* Use procedural surfaces to take advantage of associating surfaces with their defining curves.
* Use NURBS surfaces to take advantage of sculpting with control vertices.

One typical modeling workflow is to create basic models using meshes, solids, and procedural surfaces, and then convert them
to NURBS surfaces for additional shaping.

![](../images/GUID-588C01FE-A111-4F12-8EBC-50E42B66A59C-low.png)

You create surface models using many of the same tools that you use for solid models: sweeping, lofting, extruding, and revolving.
You can also create surfaces by blending, patching, offsetting, filleting, and extending other surfaces.

## Choose a Surface Creation Method

Create procedural and NURBS surfaces using the following methods:

* *Create surfaces from profiles.* Create surfaces from profile shapes composed of lines and curves with EXTRUDE, LOFT, PLANESURF, REVOLVE, SURFNETWORK, and
  SWEEP.
* *Create surfaces from other surfaces.* Blend, patch, extend, fillet, and offset surfaces to create new surfaces (SURFBLEND, SURFPATCH, SURFEXTEND, SURFFILLET, and
  SURFOFFSET.
* *Convert objects into procedural surfaces.* Convert existing solids (including composite objects), surfaces, and meshes into procedural surfaces (CONVTOSURFACE).
* *Convert procedural surfaces into NURBS surfaces.* Some objects cannot be converted directly to NURBS (for example, mesh objects). In that case, convert the object to a procedural
  surface and then convert it to a NURBS surface (CONVTONURBS).

![](../images/GUID-F513ADF3-E0D2-410E-BC48-B2CAC9C560B2-low.png)

## Understand Surface Continuity and Bulge Magnitude

Surface continuity and bulge magnitude are properties that are frequently used when creating surfaces. When you create a
new surface, you can specify the continuity and bulge magnitude with special grips.

Continuity is a measure of how smoothly two curves or surfaces flow into each other. The type of continuity can be important
if you need to export your surfaces to other applications.

Continuity types include the following:

* *G0 (Position).* Measures location only. If the edge of each surface is collinear, the positions of the surfaces are continuous (G0) at the
  edge curves. Note that two surfaces can meet at any angle and still have positional continuity.

  ![](../images/GUID-A351CCF8-F8F2-4DA3-8EEA-D8C754F0AC7F-low.png)
* *G1 (Tangency).* Includes both positional and tangential continuity (G0 + G1). With tangentially continuous surfaces, the end tangents match
  at the common edges. The two surfaces appear to be traveling in the same direction at the join, but they may have very different
  apparent “speeds” (also called rates of change in direction, or curvature).

  ![](../images/GUID-31EDEF8C-9EDD-49ED-AB75-5442D5FE095D-low.png)
* *G2 (Curvature).* Includes positional, tangential, and curvature continuity (G0 + G1+G2). The two surfaces share the same curvature.

  ![](../images/GUID-95D1188C-4B2A-4464-BEB6-DEA36E0A09E8-low.png)

Bulge magnitude is a measure of how much surface curves or “bulges” as it flows into another surface. Magnitude can be between
0 and 1 where 0 is flat and 1 curves the most.

## Set Surface Properties Before and After Creation

Set defaults that control a variety of surface properties before and after you create the surface objects.

* *Surface modeling system variables.* There are a number of system variables that are frequently used and changed during surface creation: SURFACEMODELINGMODE,
  SURFACEASSOCIATIVTIY, SURFACEASSOCIATIVITYDRAG, SURFACEAUTOTRIM, and SUBOBJSELECTIONMODE.
* *Properties palette.*  Modifies properties for both the surface objects and their subobjects after they are created. For example, you can change
  the number of isolines in the U and V directions.

#### Related Tasks

* [To Create a Blend Surface Between a Surface and a Solid](To-Create-a-Blend-Surface-Between-a-Surface-and-a-Solid.md)
* [To Patch a Closed Surface](To-Patch-a-Closed-Surface.md)
* [To Create a Solid by Offsetting a Surface](To-Create-a-Solid-by-Offsetting-a-Surface.md)
* [To Create a Planar Surface](To-Create-a-Planar-Surface.md)
* [To Create a Network Surface](To-Create-a-Network-Surface.md)
* [To Convert Objects to Procedural Surfaces](To-Convert-Objects-to-Procedural-Surfaces.md)

#### Related Concepts

* [About Constructing Solids and Surfaces From 2D Geometry](About-Constructing-Solids-and-Surfaces-From-2D-Geometry.md)
* [About Surface Modeling Workflow](About-Surface-Modeling-Workflow.md)
* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)
* [About Blending Surfaces](About-Blending-Surfaces.md)
* [About Patching Surfaces](About-Patching-Surfaces.md)
* [About Offsetting Surfaces](About-Offsetting-Surfaces.md)
* [About Creating Planar Surfaces](About-Creating-Planar-Surfaces.md)
* [About Creating Network Surfaces](About-Creating-Network-Surfaces.md)
* [About Converting Objects to Procedural Surfaces](About-Converting-Objects-to-Procedural-Surfaces.md)
* [About Analyzing Surfaces](About-Analyzing-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*