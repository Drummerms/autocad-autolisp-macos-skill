# DVIEW (Command)

Defines parallel projection or perspective views by using a camera and target.

## Summary

NOTE:Transparent [ZOOM](ZOOM-Command.md) and [PAN](PAN-Command.md) are not available in DVIEW. When you define a perspective view, ZOOM, PAN, transparent ZOOM and PAN are not available while
that view is current.

## List of Prompts

The following prompts are displayed.

[Select objects](DVIEW-Command.md) or <use >.[DVIEWBLOCK](DVIEW-Command.md)

Enter option

[[CAmera](DVIEW-Command.md)/[TArget](DVIEW-Command.md)/[Distance](DVIEW-Command.md)/[POints](DVIEW-Command.md)/[PAn](DVIEW-Command.md)/[Zoom](DVIEW-Command.md)/[TWist](DVIEW-Command.md)/[CLip](DVIEW-Command.md)/[Hide](DVIEW-Command.md)/[Off](DVIEW-Command.md)/[Undo](DVIEW-Command.md)]: [Specify a point](DVIEW-Command.md) *with your pointing device, or enter an option*

![](../images/GUID-6B683D13-B530-4F2D-9803-2BAB06D2F967-low.png)

Object Selection

Specifies objects to use in the preview image as you change views. Selecting too many objects slows image dragging and updating.

DVIEWBLOCK

If you press Enter at the Select Objects prompt, DVIEWBLOCK displays a preview image. You can create your own DVIEWBLOCK block
in a 1 unit by 1 unit by 1 unit area, with its origin at the lower-left corner. The following illustration shows an example
of using the default DVIEWBLOCK to set the view (moving the graphics cursor adjusts the view).

![](../images/GUID-BA223A37-DB9D-4D83-8D9E-94F167A9BC80-low.png)

Point Specification

Rolls the view under the camera. The point you select with your pointing device is a start point for the dragging operation.
Your viewing direction changes about the target point as you move the pointing device.

The angles must be positive. The direction angle indicates the front of the view, and the magnitude angle determines how far
the view rolls.

Camera

Specifies a new camera position by rotating the camera about the target point. Two angles determine the amount of rotation.

Camera Location
:   Sets the camera's position based on the specified point.

Enter Angle from the XY Plane
:   Sets the camera's position at an angle above or below the *XY* plane. An angle of 90 degrees looks down from above, and an angle of -90 looks up from below. A camera angle of 0 degrees
    places the camera parallel to the *XY* plane of the user coordinate system (UCS).

Toggle (Angle In)
:   Switches between two angle input modes. Entering an angle at the Command prompt locks the cursor movement so you see only
    the positions available for that angle. Toggle unlocks the cursor movement for the angle, and you can use the cursor to rotate
    the camera.

Enter Angle in XY Plane from X Axis
:   Sets the position at an angle in the *XY* plane relative to the *X* axis of the current UCS. This angle measures from -180 to 180 degrees. A rotation angle of 0 degrees looks down the *X* axis of the UCS toward the origin.

    ![](../images/GUID-90A38412-5DE6-49B2-9DD0-1A9902F12E1C-low.png)

    The illustration shows the camera rotating to the left from its initial position, leaving its angle from the *XY* plane unchanged.

Toggle (Angle From)
:   Switches between two angle input modes. Entering an angle at the Command prompt locks the cursor movement so you see only
    the positions available for that angle. Toggle unlocks the cursor movement for the angle, and you can use the cursor to rotate
    the camera.

Target

Specifies a new position for the target by rotating it around the camera. The effect is like turning your head to see different
parts of the drawing from one vantage point. Two angles determine the amount of rotation.

Enter Angle from the XY Plane
:   [Enter Angle from the XY Plane](DVIEW-Command.md)

Toggle (Angle In)
:   [Toggle (Angle In)](DVIEW-Command.md)

Enter Angle in XY Plane from X Axis
:   [Enter Angle in XY Plane from X Axis](DVIEW-Command.md)

    The illustration shows the effect of moving the target point from left to right, leaving its angle from the *XY* plane unchanged.

    ![](../images/GUID-41F89695-8336-4914-910F-F43042CD04A8-low.png)

Toggle (Angle From)
:   [Toggle (Angle From)](DVIEW-Command.md)

Distance

Moves the camera in or out along the line of sight relative to the target. This option turns on perspective viewing, which
causes objects farther from the camera to appear smaller than those closer to the camera. A special perspective icon replaces
the coordinate system icon. You are prompted for the new camera-to-target distance.

A slider bar along the top of the drawing area is labeled from 0x to 16x, with 1x representing the current distance. Moving
the slider bar to the right increases the distance between camera and target. Moving it to the left decreases that distance.
To turn off perspective viewing, click the Off option from the main DVIEW prompt.

If the target and camera points are close together, or if you specify a long-focal-length lens, you might see very little
of your drawing when you specify a new distance. If you see little or none of your drawing, try the maximum scale value (16x)
or enter a large distance. To magnify the drawing without turning perspective viewing on, use the Zoom option of DVIEW.

![](../images/GUID-E88A7045-2917-4A95-8DCE-FE06B1BD9D10-low.png)

The illustration shows the effect of moving the camera along the line of sight relative to the target, where the field of
view remains constant.

Points

Locates the camera and target points using *X*,*Y*,*Z* coordinates. You can use *XYZ* point filters.

To help you define a new line of sight, a rubber-band line is drawn from the current camera position to the crosshairs. You
are prompted for a new camera location.

A rubber-band line connects the target point to the crosshairs to help you place the camera relative to the target. The illustration
shows the change in view as you swap the camera and target points. Lens and distance settings are the same in each case.

![](../images/GUID-92297320-84FB-4FD5-A2F5-0A0FB98B5E4F-low.png)

For information about entering direction and magnitude angles, see Point Specification.

Pan

Shifts the image without changing the level of magnification.

Zoom

If perspective viewing is off, dynamically increases or decreases the apparent size of objects in the current viewport.

A slider bar along the top of the drawing area is labeled from 0x to 16x, with 1x representing the current scale. Moving the
slider bar to the right increases the scale. Moving it to the left decreases the scale.

If perspective viewing is on, Zoom adjusts the camera lens length, which changes the field of view and causes more or less
of the drawing to be visible at a given camera and target distance. The default lens length is 50mm, simulating what you'd
see with a 35mm camera and a 50mm lens. Increasing the lens length is similar to switching to a telephoto lens. Decreasing
the lens length widens the field of view, as with a wide-angle lens.

A slider bar along the top of the drawing area is labeled from 0x to 16x, with 1x representing the current lens length. Moving
the slider bar to the right increases the lens length. Moving it to the left decreases the lens length.

![](../images/GUID-061E3AD8-F044-4017-A6EB-38B162B15B4D-low.png)

Twist

Twists or tilts the view around the line of sight. The twist angle is measured counterclockwise, with 0 degrees to the right.

Clip

Clips the view, obscuring portions of the drawing that are behind or in front of the front clipping plane. The front and back
clipping planes are invisible walls that you can position perpendicular to the line of sight between the camera and target.

Back
:   Obscures objects located behind the back clipping plane.

    * *Distance from Target.* Positions the back clipping plane and turns on back clipping. A positive distance places the clipping plane between the target
      and the camera. A negative distance places it beyond the target. You can use the slider bar to drag the clipping plane.
    * *On.* Turns on back clipping at the current clipping distance.
    * *Off.* Turns off back clipping.

Front
:   Obscures objects located between the camera and the front clipping plane.

    * *Distance from Target.*Positions the front clipping plane and turns on front clipping. A positive distance places the clipping plane between the
      target and the camera. A negative distance places it beyond the target. You can use the slider bar to drag the clipping plane.
    * *Eye.* Positions the front clipping plane at the camera.
    * *On.* Turns on front clipping. This option is available only when perspective viewing is off.
    * *Off.* Turns off front clipping. This option is available only when perspective viewing is off.

    ![](../images/GUID-5AB11E66-24FD-4A67-910A-42F5B3E6CCC5-low.png)

Off
:   Turns off front and back clipping. If perspective viewing is on, front clipping remains on at the camera position.

Hide

Suppresses hidden lines on the selected objects to aid in visualization. Circles, solids, traces, regions, wide polyline segments,
3D faces, polygon meshes, and the extruded edges of objects with nonzero thickness are considered to be opaque surfaces that
hide objects.This hidden line suppression is quicker than that performed by [HIDE](HIDE-Command.md), but it cannot be plotted.

Off

Turns off perspective viewing. The Distance option turns on perspective viewing.

Undo

Reverses the effects of the last DVIEW action. You can undo multiple DVIEW operations.

#### Related Concepts

* [About Creating a 3D Dynamic View](About-Creating-a-3D-Dynamic-View.md)

#### Related Information

* [About Parallel and Perspective Views](About-Parallel-and-Perspective-Views.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*