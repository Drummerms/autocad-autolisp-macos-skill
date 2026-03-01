# About Isometric Drawing

Simulate a 3D object from a particular viewpoint by aligning along three major axes

Isometric drawings simulate a 3D object from a particular viewpoint by aligning along three major axes.

By setting the Isometric Snap/Grid, you can easily align objects along one of three isometric planes; however, although the
isometric drawing appears to be 3D, it is actually a 2D representation. Therefore, you cannot expect to extract 3D distances
and areas, display objects from different viewpoints, or remove hidden lines automatically.

If the snap angle is 0, the axes of the isometric planes are 30 degrees, 90 degrees, and 150 degrees. Once you set the snap
style to Isometric, you can work on any of three planes, each with an associated pair of axes:

* *Top* Aligns snap and grid along 30- and 150-degree axes.
* *Right* Aligns snap and grid along 30- and 90-degree axes.
* *Left* Aligns snap and grid along 90- and 150-degree axes.

  ![](../images/GUID-7FE70FDF-D198-4EC0-A9FC-AABD28C2E0D6-low.png)

Choosing one of the three isometric planes causes Ortho and the crosshairs to be aligned along the corresponding isometric
axes. For example, when Ortho is on, the points you specify align along the simulated plane you are drawing on. Therefore,
you can draw the top plane, switch to the left plane to draw another side, and switch to the right plane to complete the drawing.

![](../images/GUID-24378F2A-C1A3-49EE-88ED-B36051439052-low.png)

When drawing on isometric planes, use an ellipse to represent a circle viewed from an oblique angle. The easiest way to draw
an ellipse with the correct shape is to use the Isocircle option of ELLIPSE. The Isocircle option is available only when the
Style option of Snap mode is set to Isometric. See DSETTINGS.

NOTE: To represent concentric circles, draw another ellipse with the same center rather than offsetting the original ellipse. Offsetting
produces an oval-shaped spline that does not represent foreshortened distances as you would expect.

#### Related Tasks

* [To Draw Isometric Circles](To-Draw-Isometric-Circles.md)

#### Related Information

* [Commands for 2D Isometric Drawing](Commands-for-2D-Isometric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*