# Rotate Views in Layout Viewports

You can rotate an entire view within a layout viewport with the VPROTATEASSOC system variable.

When VPROTATEASSOC is set to 1, the view within a viewport is rotated with the viewport. When VPROTATEASSOC is set to 0, the
view remains when the viewport is rotated.

You can also rotate an entire view within a layout viewport by changing the UCS and using the PLAN command.

With the UCS command, you can rotate the *XY* plane at any angle around the Z axis. When you enter the PLAN command, the view rotates to match the orientation of the *XY* plane.

![](../images/GUID-A1D0DDA1-CDF2-4A78-85DE-5968B38CD70E-low.png)

NOTE:The ROTATE command rotates individual objects only and should not be used to try to rotate a view.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*