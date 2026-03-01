# VIEWRES (Command)

Sets the resolution for objects in the current viewport.

## Summary

The model is regenerated.

VIEWRES controls the appearance of circles, arcs, splines, and arced polylines using short vectors. The greater the number
of vectors, the smoother the appearance of the circle or arc. For example, if you create a very small circle and then zoom
in, it might appear to be a polygon. Using VIEWRES to increase the zoom percentage and regenerate the drawing updates and
smooths the circle's appearance.

![](../images/GUID-0F1F21C3-CA62-41F9-BCFD-E35EC4C360AD-low.png)

NOTE:Increasing the zoom percentage in VIEWRES may increase the time it takes to regenerate the drawing.

When a named (paper space) layout is made current for the first time and a default viewport is created in the layout, the
viewing resolution for this initial viewport is the same as the viewing resolution for the Model layout viewport.

The VIEWRES setting is saved in the drawing. To change the default for new drawings, consider specifying the VIEWRES setting
in the template files on which you base your new drawings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*