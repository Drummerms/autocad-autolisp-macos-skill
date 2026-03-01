# Assign UCS Definitions to Viewports

To facilitate editing objects in different views, you can define a different UCS (User Coordinate System) for each view.

Multiple viewports provide different views of your model. For example, you might set up viewports that display top, front,
right side, and isometric views. To facilitate editing objects in different views, you can create a different UCS definition
for each view. Each time you make a viewport current, you can begin drawing using the same UCS you used the last time that
viewport was current.

The UCS in each viewport is controlled by the UCSVP system variable. When UCSVP is set to 1 in a viewport, the UCS last used
in that viewport is saved with the viewport and is restored when the viewport is made current again. When UCSVP is set to
0 in a viewport, its UCS is always the same as the UCS in the current viewport.

For example, you might set up three viewports: a top view, front view, and isometric view. If you set the UCSVP system variable
to 0 in the isometric viewport, you can use the Top UCS in both the top viewport and the isometric viewport. When you make
the top viewport current, the isometric viewport's UCS reflects the UCS top viewport. Likewise, making the front viewport
current switches the isometric viewport's UCS to match that of the front viewport.

The example is illustrated in the following figures. The first figure shows the isometric viewport reflecting the UCS of the
upper-left, or top, viewport, which is current.

![](../images/GUID-5D3139B4-81E6-4091-9439-79342ED4633E-low.png)

The second figure shows the change that occurs when the lower-left, or front, viewport is made current. The UCS in the isometric
viewport is updated to reflect the UCS of the front viewport.

![](../images/GUID-8785FBCB-DDD1-44AA-A30D-87735E17258C-low.png)

In previous releases, the UCS was a global setting for all viewports in either model or paper space. If you want to restore
the behavior of earlier releases, you can set the value of the UCSVP system variable to 0 in all active viewports.

#### Related Tasks

* [To Work With Model Space Viewports](To-Work-With-Model-Space-Viewports.md)
* [To Make a Viewport Current](To-Make-a-Viewport-Current.md)

#### Related Concepts

* [Set Model Space Viewports](Set-Model-Space-Viewports.md)
* [About Saving and Restoring Model Space Viewport Arrangements](About-Saving-and-Restoring-Model-Space-Viewport-Arrangements.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*