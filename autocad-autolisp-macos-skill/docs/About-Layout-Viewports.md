# About Layout Viewports

Layout viewports are objects that display views of model space. You create, scale, and place them in paper space on a layout.

On each layout, you can create one or more layout viewports. Each layout viewport is like a closed circuit TV monitor of a
view of the model at a scale and orientation that you specify.

![](../images/GUID-0069E800-39F5-4847-BFD8-C55CF9C806C9-low.png)

## Create Layout Viewports

When you use the MVIEW command to create a new layout viewport, you specify the view that you want to display in it with one
of several methods:

* Click the diagonal corners of a rectangular area, and the extents of model space are displayed automatically.
* Specify the Named option to use a previously saved model-space view.
* Specify the New option for temporary access model space to define a rectangular area.
* Choose the Object option and select a closed object such as a circle or closed L-shaped polyline to convert into a layout
  viewport.

NOTE: It is important to create layout viewports on their own layer. When you are ready to output your drawing, you can turn off
that layer to display the layout viewport without its boundary.

## Modify Layout Viewports

After you create a layout viewport, you can change its size and properties, and also scale and move it as needed.

* For control of all the properties of a layout viewport, use the Properties palette.
* For the most common changes, select a layout viewport and use its grips.

![](../images/GUID-915FD1A7-7CF9-44A9-B5D9-308297FF091D-low.png)

NOTE: Because they are objects, you can also use editing commands such as COPY, MOVE, and ERASE on layout viewports.

## Locked Layout Viewports

To prevent accidental panning and zooming, each layout viewport has a Display Locked property that can be turned on or off.
You can access this property from the Properties palette, the right-click menu when a layout viewport is selected, a button
on the Layout Viewports tab on the ribbon, and a button on the status bar when one or more layout viewports are selected.

#### Related Tasks

* [To Deactivate a Layout Viewport](To-Deactivate-a-Layout-Viewport.md)

#### Related Information

* [To Create a New Layout Viewport](To-Create-a-New-Layout-Viewport.md)
* [To Create a Nonrectangular Layout Viewport](To-Create-a-Nonrectangular-Layout-Viewport.md)
* [To Automatically Set Up Multiple Viewports on a Layout](To-Automatically-Set-Up-Multiple-Viewports-on-a-Layout.md)
* [To Place a Named Viewport Configuration Into a Layout](To-Place-a-Named-Viewport-Configuration-Into-a-Layout.md)
* [Reuse Layouts and Layout Settings](Reuse-Layouts-and-Layout-Settings.md)
* [To Modify Layout Viewport Properties Using the Properties Inspector](To-Modify-Layout-Viewport-Properties-Using-the-Properties-Inspector.md)
* [About Freezing Specified Layers in Layout Viewports](About-Freezing-Specified-Layers-in-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*