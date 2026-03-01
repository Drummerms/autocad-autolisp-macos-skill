# About Controlling the Display of Edges

Different edge types can be displayed using different colors and linetypes. You can also add special effects, such as jitter
and line extensions.

In 3D solid or surface models, the current visual style sets the visibility and appearance of isolines, facet edges, silhouette
edges, occluded edges, and intersection edges. Facet edges (the edges between planar faces representing a surface) are displayed
only when the angle between the facets is smaller than the crease angle value you specify.

For example, edge modifiers such as line extension and jitter, produce the appearance of a model that is still in the conceptual
phase. Jitter makes lines appear as though they were sketched with a pencil. Line extension produces another kind of hand-drawn
effect.

NOTE: Plot styles are not available for objects with the Jitter edge modifier applied.

![](../images/GUID-DCD32104-BFE2-4AE1-83B1-78C9AF2C9A9F-low.png)

## Edges in the 2D Wireframe Visual Style

The 2D Wireframe visual style is optimized for 2D drawings, but it can also be used for 3D views. Several system variables
control the display of 3D solid and surface models with this visual style. For example, the DISPSILH system variable controls
the display of silhouette edges such as the apparent edges on a cylinder. Occluded lines are hidden lines that can be displayed
with a distinctive linetype and color. Occluded lines can be assigned a distinctive linetype with the OBSCUREDLTYPE system
variable and an occluded color with the OBSCUREDCOLOR system variable.

![](../images/GUID-1E2134A2-F42B-4129-96F7-06F05D795619-low.png)

NOTE:After changing settings for occluded lines or edges, use the REGEN command or change the view to regenerate the drawing and
display the changes.

#### Related Information

* [About Using Visual Styles](About-Using-Visual-Styles.md)
* [Shade and Color Faces](Shade-and-Color-Faces.md)
* [About Backgrounds and Shadows](About-Backgrounds-and-Shadows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*