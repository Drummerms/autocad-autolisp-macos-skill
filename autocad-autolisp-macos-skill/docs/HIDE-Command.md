# HIDE (Command)

Regenerates a 3D wireframe model with hidden lines suppressed.

## Access Methods

*Menu*:
View
![](../images/ac.menuaro.gif) Hide.

## Summary

When you use
[VPOINT](VPOINT-Command.md),
[DVIEW](DVIEW-Command.md), or
[VIEW](VIEW-Command-2.md) to create a 3D view of your 2D drawing, a wireframe is displayed in the current viewport. All lines are present, including
those hidden by other objects. HIDE eliminates the hidden lines from the screen.

HIDE considers the following to be opaque surfaces that hide objects: circles, solids, traces, text, regions, wide polyline
segments, 3D faces, polygon meshes, and the extruded edges of objects with nonzero thickness.

If they are extruded, circles, solids, traces, and wide polyline segments are treated as solid objects with top and bottom
faces. You cannot use HIDE on objects whose layers have been frozen; however, you can use HIDE on objects whose layers have
been turned off.

To hide text created with MTEXT or TEXT, the
[HIDETEXT](HIDETEXT-System-Variable.md) system variable must be set to 1 or the text must be assigned a thickness value.

![](../images/GUID-3690F67D-3A35-42B7-A985-95E30B759854-low.png)

When using the HIDE command, if the
[INTERSECTIONDISPLAY](INTERSECTIONDISPLAY-System-Variable.md) system variable is on, face-to-face intersections of 3D surfaces are displayed as polylines.

The 3D Hidden visual style does not honor the setting of INTERSECTIONDISPLAY.

![](../images/GUID-363C3BD1-B228-4993-AE58-07515DA526FF-low.png)

If the
[DISPSILH](DISPSILH-System-Variable-DELETE.md) system variable is on, HIDE displays 3D solid objects with silhouette edges only. It won't show the internal edges produced
by objects that have facets.

If the HIDETEXT system variable is off, HIDE ignores text objects when producing the hidden view. Text objects are always
displayed regardless of whether they are obscured by other objects, and objects obscured by text objects are unaffected.

#### Related Concepts

* [About Hiding Lines in 3D Objects](About-Hiding-Lines-in-3D-Objects.md)
* [About Using Visual Styles](About-Using-Visual-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*