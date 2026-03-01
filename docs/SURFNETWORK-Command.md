# SURFNETWORK (Command)

Creates a surface in the space between several curves in the U and V directions (including surface and solid edge subobjects).

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Surface drop-down ![](../images/ac.menuaro.gif) Surface Network.
![](../images/GUID-F700457A-FF55-43F7-A84D-DCA8F93D52CA-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Surfaces ![](../images/ac.menuaro.gif) Network.

## Summary

A network surface can be created between a network of curves or between the edges of other 3D surfaces or solids.

![](../images/GUID-0DD01C8F-FF9D-4F3B-82AF-CD04A00CB57E-low.gif)

The surface will be dependent on the curves or edges from which it was created if the
[SURFACEASSOCIATIVITY](SURFACEASSOCIATIVITY-System-Variable.md) system variable is set to 1.

## List of Prompts

The following prompts display:

Select Curves or Surface Edges in the First Direction
:   Select a network of open curves, open surface edges, or region edges (not the surfaces or regions) for the
    *U* or
    *V* direction.

Select Curves or Surface Edges in the Second Direction
:   Select a network of open curves, open surface edges, or region edges (not the surfaces or regions) for the
    *U* or
    *V* direction.

Bulge Magnitude
:   Sets the roundness of the network surface edge where it meets the originating surface. Valid values are between 0 and 1. The
    default is 0.5. This option displays only if a lofting edge belongs to a 3D solid or surface (not a curve).

#### Related Concepts

* [About Creating Network Surfaces](About-Creating-Network-Surfaces.md)
* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*