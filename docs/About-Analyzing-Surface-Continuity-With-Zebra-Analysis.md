# About Analyzing Surface Continuity With Zebra Analysis

The zebra analysis tool projects stripes onto a surface so that you can inspect the continuity between surfaces.

Surface continuity is a measure of how smoothly two surfaces flow into each other. A car hood, for example, can be composed
of multiple small surfaces that appear to be one because of the smoothness of the surface continuity. Zebra analysis can also
identify flaws in what should be a fair surface in a ship hull, an issue that can increase drag and have structural consequences
in some cases.

NOTE: Analysis tools only work in the 3D visual styles; they will not work in 2D.

## How to Interpret the Zebra Stripes

In the seam where two surfaces meet, the way that the zebra stripes align and curve tells you a lot about the smoothness of
the join.

* *G0 Position.* The position of the surface edges is collocated; they touch. But the tangency and curvature do not match. The zebra stripes
  do not line up.

  ![](../images/GUID-289419A8-BA07-4916-83B4-9C2EAE6AED71-low.png)
* *G1 Tangency.* The position and tangency of surfaces is the same. This indicates G1 (G0 + G1 or position + tangency). The zebra stripes
  line up, but they veer away from one another at sharp curves.

  ![](../images/GUID-F94ED88D-3F06-4A23-9DEE-7C44D94F6BC6-low.png)
* *G2 Curvature.* The position, tangency, and curvature of the surface edges is the same. This indicates G2 (G0 + G1 + G2 or position + tangency
  + curvature).

  The stripes line up, but they do not veer away from each other at sharp curves (because they share the same curvature). This
  distinction is subtle and a little harder to discern from G1 continuity.

  ![](../images/GUID-174F15A9-56D7-4DC3-8B97-5C6014ED1F6D-low.png)

#### Related Tasks

* [To Work With Surface Continuity Analysis](To-Work-With-Surface-Continuity-Analysis.md)

#### Related Concepts

* [About Analyzing Surfaces](About-Analyzing-Surfaces.md)
* [About Analyzing the Curvature of NURBS Surfaces](About-Analyzing-the-Curvature-of-NURBS-Surfaces.md)
* [About Analyzing Draft Angle](About-Analyzing-Draft-Angle.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*