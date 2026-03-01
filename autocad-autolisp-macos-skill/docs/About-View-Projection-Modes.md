# About View Projection Modes

View projection produces realistic visual effects of a model.

The ViewCube tool supports two view projection modes (Perspective and Orthographic) and a combination of both these modes
(Perspective with Ortho faces). Orthographic projection is also referred to as parallel projection. Perspective projected
views are calculated based on the distance from a theoretical camera and target point. The shorter the distance between the
camera and the target point, the more distorted the perspective effect appears; greater distances produce less distorted affects
on the model. Orthographic projected views display all the points of a model being projected parallel to the screen.

Orthographic projection mode makes it easier to work with a model due to all the edges of the model appearing as the same
size, regardless of the distance from the camera. Orthographic projection mode though, is not how you commonly see objects
in the real world. Objects in the real world are seen in perspective projection. So when you want to generate a rendering
or hidden line view of a model, using perspective projection will give the model a more realistic look.

The following illustration shows the same model viewed from the same viewing direction, but with different view projections.

| ![](../images/GUID-A100D207-9119-43DC-98BE-3698E9B99B94-low.png) Parallel | ![](../images/GUID-5F049568-5E9F-4D2B-88EB-0A063C73FE45-low.png) Perspective |

When you change the view for a model, the view is updated using the previous projection mode unless the current projection
mode for the ViewCube tool is Perspective with Ortho Faces. The Perspective with Ortho Faces mode forces all views to be displayed
in perspective projection unless the model is being viewed from one of the face views: top, bottom, front, back, left, or
right.

#### Related Tasks

* [To Display the ViewCube Menu](To-Display-the-ViewCube-Menu.md)

#### Related Information

* [Reorient the Current View](Reorient-the-Current-View.md)
* [About the ViewCube Menu](About-the-ViewCube-Menu.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*