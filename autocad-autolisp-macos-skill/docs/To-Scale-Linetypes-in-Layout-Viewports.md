# To Scale Linetypes in Layout Viewports

You can scale linetypes in paper space either based on the drawing units of the space in which the object was created or based
on the paper space units.

* You can set the PSLTSCALE system variable to maintain the same linetype scaling for objects displayed at different zoom factors
  in the layout (paper space) and in the layout viewport (model space). For example:

1. With PSLTSCALE set to 1 (default), set the current linetype to dashed, and then draw a line in a paper space layout.
2. In the layout, create a viewport with a zoom factor of 1x, make that layout viewport current, and then draw a line using the
   same dashed linetype. The dashed lines should appear to be the same.
3. If you change the viewport zoom factor to 2x, the linetype scaling for the dashed line in the layout and the dashed line in
   the layout viewport will be the same, regardless of the difference in the zoom factor.

* With PSLTSCALE turned on, you can still control the dash lengths with LTSCALE and CELTSCALE. In the following illustration,
  the pattern of the linetypes in the drawing on the left has been scaled to be the same regardless of the scale of the view.
  In the drawing on the right, the scale of the linetypes matches the scale of each view.

![](../images/GUID-658BEB3D-3F1E-4B8C-B272-4F5CBBE5B8EA-low.png)

#### Related Tasks

* [To Lock the Scale of a Layout Viewport](To-Lock-the-Scale-of-a-Layout-Viewport.md)

#### Related Information

* [About Scaling Views in Layout Viewports](About-Scaling-Views-in-Layout-Viewports.md)
* [To Modify the Scale of a Layout Viewport](To-Modify-the-Scale-of-a-Layout-Viewport.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*