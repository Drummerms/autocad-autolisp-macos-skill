# About Scaling Views in Layout Viewports

To scale each displayed view in output accurately, set the scale of each view relative to paper space.

You can change the view scale of the viewport using

* The Properties Inspector
* The XP option of the ZOOM command
* The Viewports Scale on the status bar

NOTE:You can modify the list of scales that are displayed in all view and print scale lists with SCALELISTEDIT. After you add a
new scale to the default scale list, you can use the Reset button in the Edit Drawing Scales dialog box to add the new scale
to your drawing.

When you work in a layout, the scale factor of a view in a layout viewport represents a ratio between the actual size of the
model displayed in the viewport and the size of the layout. The ratio is determined by dividing the paper space units by the
model space units. For example, for a quarter-scale drawing, the ratio would be a scale factor of one paper space unit to
four model space units, or 1:4.

Scaling or stretching the layout viewport border does not change the scale of the view within the viewport.

When creating a new drawing based on a template, the scales in the template are used in the new drawing. The scales in the
user profile are not imported.

## *Lock the Scale of Layout Viewports*

Once you set the viewport scale, you cannot zoom within a viewport without changing the viewport scale. By locking the viewport
scale first, you can zoom in to view different levels of detail in your viewport without altering the viewport scale.

Scale locking locks the scale that you set for the selected viewport. Once the scale is locked, you can continue to modify
the geometry in the viewport without affecting the viewport scale. If you turn a viewport's scale locking on, most of the
viewing commands, such as VPOINT, DVIEW, 3DORBIT, PLAN, and VIEW, no longer function in that viewport.

NOTE:Viewport scale locking is also available for nonrectangular viewports. To lock a nonrectangular viewport, you must perform
an extra step in the Properties Inspector to select the viewport object rather than the viewport clipping boundary.

## Annotative Objects and Scaling

Annotative objects are defined at a paper height instead of a model size and assigned one or more scales. These objects are
scaled based on the current annotation scale setting and are automatically displayed at the correct size in the layout or
when plotted. The annotation scale controls the size of the annotative objects relative to the model geometry in the drawing.

You can specify the default list of scales available for layout viewports, page layouts, and plotting in Default Scale List
dialog box.

#### Related Tasks

* [To Lock the Scale of a Layout Viewport](To-Lock-the-Scale-of-a-Layout-Viewport.md)
* [To Scale Linetypes in Layout Viewports](To-Scale-Linetypes-in-Layout-Viewports.md)

#### Related Information

* [To Modify the Scale of a Layout Viewport](To-Modify-the-Scale-of-a-Layout-Viewport.md)
* [To Clip a Layout Viewport Boundary](To-Clip-a-Layout-Viewport-Boundary.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*