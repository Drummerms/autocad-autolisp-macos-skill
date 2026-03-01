# About Trimming Surfaces

Trim surfaces to meet the edges of other objects.

An important step in the surface modeling workflow is trimming surfaces. You can trim a surface where it meets an intersecting
object or you can project geometry onto a surface as a trimming edge.

When a surface is trimmed, the removed surface areas can be replaced with SURFUNTRIM.

NOTE: SURFUNTRIM does not restore areas removed by the SURFACEAUTOTRIM system variable and PROJECTGEOMETRY. It only restores areas
trimmed with SURFTRIM.

The Properties palette indicates if the surface contains any trimmed edges.

## Projecting Geometry onto Surfaces, Solids, and Regions

Similar to projecting a movie onto a screen, you can project geometry onto 3D solids, surfaces, and regions from different
directions to create trimming edges. The PROJECTGEOMETRY command creates a duplicate curve on the object that you can move
and edit. You can also trim against 2D curves that do not actually touch the surface, but that appear to intersect the object
in the current view.

Use the SURFACEAUTOTRIM system variable to automatically trim a surface when you project geometry onto it.

### Options for Projecting Geometry

Project geometry from 3 different angles: the Z axis of the current UCS, the current view, or a path between two points.

* *Project to UCS* - Projects the geometry along the positive or negative Z axis of the current UCS.
* *Project to View* - Projects the geometry based on the current view.
* *Project to Two Points* - Projects the geometry along a path between two points.

#### Related Tasks

* [To Work With Trimming Surfaces](To-Work-With-Trimming-Surfaces.md)

#### Related Concepts

* [About Modifying Surfaces](About-Modifying-Surfaces.md)
* [About Extending Surfaces](About-Extending-Surfaces.md)
* [About Rebuilding NURBS Surfaces and Curves](About-Rebuilding-NURBS-Surfaces-and-Curves.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*