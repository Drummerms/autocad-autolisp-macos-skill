# To Rotate a View Within a Viewport

1. Click the layout tab in which you want to rotate a view.
2. Make sure that you are in paper space by double-clicking outside any layout viewports.
3. Make sure that the VPROTATEASSOC system variable is set to 1.
4. Select the viewport that you want to rotate.
5. In the drawing area, right-click and choose Rotate.

   NOTE:You can also click the viewport's center square grip, right-click and choose Rotate.
6. Follow the prompts to enter the base point to rotate the view around and the rotation angle.

The orientation of the viewport and the objects within the viewport appear rotated, but the orientation of the actual objects
remains unchanged in the model.

NOTE:

* When VPROTATEASSOC is set to 0, the view within the viewport is not rotated when the viewport is rotated.
* The ROTATE command rotates graphical objects only and cannot be used to rotate a view; instead, use the MVSETUP command to
  rotate a view within a viewport on a layout. MVSETUP is not available in AutoCAD LT.

#### Related Tasks

* [To Rotate a View by Changing the UCS](To-Rotate-a-View-by-Changing-the-UCS.md)
* [To Rotate a Layout View Using MVSETUP](To-Rotate-a-Layout-View-Using-MVSETUP.md)

#### Related Concepts

* [About Layout Viewports](About-Layout-Viewports.md)

#### Related Information

* [Rotate Views in Layout Viewports](Rotate-Views-in-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*