# About Flattened Views

Create a flattened view of the 3D solids and regions in the current view.

## Create a 2D Presentation of a 3D Model

With the FLATSHOT command, you can create a flattened, 2D representation of the 3D model projected onto the *XY* plane. The resulting objects can be inserted as a block or saved as a separate drawing. This feature is useful for creating
technical illustrations.

![](../images/GUID-BE0DBA74-BE48-4B74-8E42-390992D16885-low.png)

The flatshot process works only in model space. Start by setting up the view you want, including orthographic or parallel
views. All 3D objects in the model space viewport are captured. Therefore, be sure to place the objects you do not want captured
on layers that are turned off or frozen.

As you create the block, you can control how hidden lines are displayed by adjusting the Foreground and Obscured Lines settings
in the Flatshot dialog box. For best results with mesh objects, clear the Show box under Obscured Lines so that hidden lines
are not represented.

3D objects that have been sectioned are captured in their entirety, as if they had not been sectioned.

NOTE:To create profile images of 3D solids for a paper space layout, use the SOLPROF command.

## Modify a Block Created with Flatshot

You can modify a flattened view that has been inserted as a block in the same way that you modify any other 2D block geometry.

#### Related Information

* [To Create a Flattened View of a 3D Model](To-Create-a-Flattened-View-of-a-3D-Model.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*