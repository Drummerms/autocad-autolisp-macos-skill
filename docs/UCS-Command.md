# UCS (Command)

Sets the origin and orientation of the current UCS.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) UCS panel.

*Menu*:
Tools ![](../images/ac.menuaro.gif) New UCS.

*Shortcut Menu*: Right-click the UCS icon and click an option.

## Summary

The UCS is the active coordinate system that establishes the XY plane (work plane) and Z-axis direction for drawing and modeling.
Control the UCS origin and orientation to make drawing more convenient as you specify points, enter coordinates, and work
with drawing aids, such as Ortho mode and the grid.

A UCS can be stored with a viewport if the
[UCSVP](UCSVP-System-Variable.md) system variable is set to 1 for that viewport.

## List of Prompts

The following prompts are displayed.

[Specify Origin of UCS](UCS-Command.md) or [[Face](UCS-Command.md)/[NAmed](UCS-Command.md)/[OBject](UCS-Command.md)/[Previous](UCS-Command.md)/[View](UCS-Command.md)/[World](UCS-Command.md)/[X/Y/Z](UCS-Command.md)/[ZAxis](UCS-Command.md)] <World>:

Specify Origin of UCS

Defines a new UCS using one, two, or three points:

* If you specify a single point, the origin of the current UCS shifts without changing the orientation of the X, Y, and Z axes.
* If you specify a second point, the UCS rotates to pass the positive X axis through this point.
* If you specify a third point, the UCS rotates around the new X axis to define the positive Y axis.

The three points specify an origin point, a point on the positive
*X* axis, and a point on the positive
*XY* plane.

![](../images/GUID-C0FB5ACF-E5C2-4542-A266-3B916CBD6764-low.gif)

NOTE:If you do not specify a
*Z* coordinate value when entering a coordinate, the current
*Z* value is used.

TIP:You can also select and drag the UCS icon origin grip directly to a new location, or choose Move Origin Only from the origin
grip menu.

Face
![](../images/GUID-B0E00611-FC5A-46DD-89F1-4BE96248D8BA-low.png)

TIP:You can also select and drag the UCS icon (or choose Move And Align from the origin grip menu) to dynamically align the UCS
with faces.

Dynamically aligns the UCS to a face on a 3D object.

Move the cursor over a face to see a preview of how the UCS will be aligned.

![](../images/GUID-0A2CA40C-9D45-43CB-B1D0-33DF157ED7D6-low.gif)

Next
:   Locates the UCS on either the adjacent face or the back face of the selected edge.

Xflip
:   Rotates the UCS 180 degrees around the
    *X* axis.

Yflip
:   Rotates the UCS 180 degrees around the
    *Y* axis.

Accept
:   Accepts the changes and places the UCS.

Named

Saves or restores named UCS definitions.

TIP: You can also right-click the UCS icon and click Named UCS to save or restore named UCS definitions.

Restore

Restores a saved UCS definition so that it becomes the current UCS.

Name
:   Specifies the name of the UCS definition to restore.

?—List UCS definitions
:   Lists details about the specified UCS definitions.

Save

Saves the current UCS to a specified name.

Name
:   Specifies the name for the UCS definition.

Delete

Removes the specified UCS definition from the list of saved definitions.

If you delete a UCS definition that is currently active, the UCS stays in place but is listed as NO NAME.

?—List UCS Definitions

Lists saved UCS definitions showing the origin and
*X*,
*Y*, and
*Z* axes for each saved UCS definition relative to the current UCS. Enter an asterisk to list all UCS definitions. If the current
UCS is the same as the WCS (World Coordinate System), it is listed as WORLD. If it is custom, but unnamed, it is listed as
NO NAME.

Object
![](../images/GUID-3C85DB50-1574-4C97-9E66-B4E702439C61-low.png)

Aligns the UCS to a selected 2D or 3D object. The UCS can be aligned with any object type except xlines and 3D polylines.

Move the cursor over an object to see a preview of how the UCS will align, and click to place the UCS. In most cases, the
UCS origin will be located at the endpoint that is nearest to the specified point, the
*X* axis will align to an edge or tangent to a curve, and the
*Z* axis will align perpendicular to the object.

![](../images/GUID-29EF5231-CF08-4556-AC24-A09087288B10-low.gif)

Previous
![](../images/GUID-CDD699CB-A396-407F-9C11-08058FDA3EA5-low.png)

Restores the previous UCS.

You can steps back through the last 10 UCS settings in the current session. UCS settings are stored independently for model
space and paper space.

View
![](../images/GUID-9933AD6A-57C4-439E-95F2-84E1F3E95053-low.png)

Aligns the
*XY* plane of the UCS to a plane perpendicular to your viewing direction. The origin point remains unchanged, but the
*X* and
*Y* axes become horizontal and vertical.

![](../images/GUID-44FA4462-D9C7-457D-921C-F78508CB91C4-low.gif)

World
![](../images/GUID-C5B05715-A78E-4610-82E4-6EAB04EE4FD3-low.png)

Aligns the UCS with the world coordinate system (WCS).

TIP:You can also click the UCS icon and choose World from the origin grip menu.

X
![](../images/GUID-99F58811-FEE5-4AF3-AA4F-996E3AB6F9CD-low.png), Y
![](../images/GUID-963C9043-B97F-40D7-A2AC-D54C8C1C7225-low.png), Z
![](../images/GUID-B02F96CF-D5A9-4972-B321-6E75DD73358C-low.png)

Rotates the current UCS about a specified axis.

Point your right thumb in the positive direction of the
*X* axis and curl your fingers. Your fingers indicate the positive rotation direction about the axis.

![](../images/GUID-77A77A30-839D-4DA5-AA10-AF638A04EBC2-low.gif)

Point your right thumb in the positive direction of the
*Y* axis and curl your fingers. Your fingers indicate the positive rotation direction about the axis.

![](../images/GUID-2B70E075-2CFC-4998-9AC1-E412505B698E-low.gif)

Point your right thumb in the positive direction of the
*Z* axis and curl your fingers. Your fingers indicate the positive rotation direction about the axis.

![](../images/GUID-54AF393B-C8AC-4AA0-92AD-E47256825836-low.gif)

You can define any UCS by specifying an origin and one or more rotations around the
*X*,
*Y*, or
*Z* axis.

![](../images/GUID-682F0BED-D746-4F1A-ACD8-D68616F2B2C2-low.png)

Z Axis

Aligns the UCS to a specified positive
*Z* axis.

The UCS origin is moved to the first point and its positive
*Z* axis passes through the second point.

![](../images/GUID-729CEA52-4B61-4A77-A6B1-F7596BEC8246-low.gif)

Object
:   Aligns the
    *Z* axis tangent to the endpoint that is nearest to the specified point. The positive
    *Z* axis points away from the object.

Apply

Applies the current UCS setting to a specified viewport or all active viewports when other viewports have a different UCS
saved in the viewport. ([UCSVP](UCSVP-System-Variable.md) system variable).

Viewport
:   Applies the current UCS to the specified viewport and ends the UCS command.

All
:   Applies the current UCS to all active viewports.

#### Related Concepts

* [About Controlling the User Coordinate System (UCS)](About-Controlling-the-User-Coordinate-System-UCS.md)
* [About the User Coordinate System (UCS)](About-the-User-Coordinate-System-UCS.md)
* [About Using Named UCS Definitions and Preset Orientations](About-Using-Named-UCS-Definitions-and-Preset-Orientations.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*