# BLEND (Command)

Creates a spline in the gap between two selected lines or curves.

## Access Methods

*Menu*:
Modify ![](../images/ac.menuaro.gif) Blend.

## Summary

Select each object near an endpoint. The shape of the resulting spline depends on the specified continuity. The lengths of
the selected objects remain unchanged.

![](../images/GUID-F44EF4E3-2513-4890-A645-BA5846C4AE21-low.gif)

Valid objects include lines, arcs, elliptical arcs, helixes, open polylines, and open splines.

## List of Prompts

The following prompts are displayed.

Select first object or [CONtinuity]:
*Select a line or open curve near the end where the spline should start*

Select second object:
*Select another line or open curve near the end where the spline should end*

Continuity

Specify one of two types of blends.

Tangent
:   Creates a degree 3 spline with tangency (G1) continuity to the selected objects at their endpoints.

Smooth
:   Creates a degree 5 spline with curvature (G2) continuity to the selected objects at their endpoints.

    If you use the Smooth option, do not switch the display from control vertices to fit points. This action changes the spline
    to degree 3, which will change shape of the spline.

#### Related Concepts

* [About Splines](About-Splines.md)

#### Related Information

* [About Curved Objects](About-Curved-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*