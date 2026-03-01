# DELOBJ (System Variable)

Controls whether geometry used to create other objects is retained or deleted.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 3 |

If the [SURFACEASSOCIATIVITY](SURFACEASSOCIATIVITY-System-Variable.md) system variable is set to 1, the DELOBJ setting is ignored.

| 0 | All defining geometry is retained. |
| 1 | Deletes profile curves, including those used with the [EXTRUDE](EXTRUDE-Command.md), [SWEEP](SWEEP-Command.md), [REVOLVE](REVOLVE-Command.md), and [LOFT](LOFT-Command.md) commands. Removes all defining geometry for [CONVTOSOLID](CONVTOSOLID-Command.md), [CONVTOSURFACE](CONVTOSURFACE-Command.md), [CONVTONURBS](CONVTONURBS-Command.md), and [CONVTOMESH](CONVTOMESH-Command.md) commands. Cross sections used with the LOFT command are also deleted. |
| 2 | Deletes all defining geometry, including paths and guide curves used with the SWEEP and LOFT commands. |
| 3 | Deletes all defining geometry, including paths and guide curves used with the SWEEP and LOFT commands if the action results in a solid object. Removes all defining geometry for CONVTOSOLID, CONVTOSURFACE, CONVTONURBS, and CONVTOMESH commands. |
| -1 | Displays prompts to delete profile curves, including those used with the EXTRUDE, SWEEP, REVOLVE, and LOFT commands. Prompts to remove cross sections used with the LOFT command.  The original geometry for CONVTOSOLID, CONVTOSURFACE, and CONVTOMESH commands is removed without prompting. |
| -2 | Displays prompts to delete all defining geometry, including paths and guide curves used with the SWEEP and LOFT commands.  The original geometry for CONVTOSOLID, CONVTOSURFACE, and CONTOMESH commands is removed without prompting. |
| -3 | Displays prompts to delete all defining geometry if the resulting entities are a surface of any type. Deletes all original geometry resulting in a solid entity, original geometry for CONVTOSOLID, CONVTOSURFACE, CONVTONURBS, and CONVTOMESH commands is removed without prompting |

#### Related Concepts

* [About Constructing Solids and Surfaces From 2D Geometry](About-Constructing-Solids-and-Surfaces-From-2D-Geometry.md)
* [About Converting Surfaces and Meshes to 3D Solids](About-Converting-Surfaces-and-Meshes-to-3D-Solids.md)
* [About Creating Associative Surfaces](About-Creating-Associative-Surfaces.md)
* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*