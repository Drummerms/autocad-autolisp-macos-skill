# SURFBLEND (Command)

Creates a continuous blend surface between two existing surfaces.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Surface Creation drop-down ![](../images/ac.menuaro.gif) Surface Blend.
![](../images/GUID-F583F639-0757-4578-B365-1EB760924257-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Surfaces ![](../images/ac.menuaro.gif) Blend.

## Summary

When you blend two surfaces together, you specify surface continuity and bulge magnitude.

Set
[SURFACEASSOCIATIVITY](SURFACEASSOCIATIVITY-System-Variable.md) to 1 to create a relationship between the blend surface and the originating curves.

![](../images/GUID-DEA5A6B2-7E64-45AD-AF8F-3E0A6AB30084-low.gif)

## List of Prompts

The following prompts are displayed.

Select Surface Edge

Selects an edge subobject or a surface or region (not the surface itself) as the first and second edges.

Chain

Selects contiguous, connected, edges.

Continuity

Measures how smoothly surfaces flow into each other. The default is G0. Select a value or use the grip to change the continuity.

![](../images/GUID-D5D61B66-0E25-4943-899B-B59B853B799F-low.png)

Bulge Magnitude

Sets the roundness of the blend surface edge where it meets the originating surface. The default is 0.5. Valid values are
between 0 and 1.

#### Related Concepts

* [About Blending Surfaces](About-Blending-Surfaces.md)
* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*