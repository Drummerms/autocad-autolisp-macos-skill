# SNAP (Command)

Restricts cursor movement to specified intervals.

The following prompts are displayed.

### Snap Spacing

Activates Snap mode with the value you specify.

### On

Activates Snap mode using the current settings of the snap grid.

![](../images/GUID-DCE3D1D8-46C9-4491-A101-8ED95EF3C223-low.png)

### Off

Turns off Snap mode but retains the current settings.

### Aspect

Specifies different spacing in the *X* and *Y* directions.

![](../images/GUID-06BA91C1-548C-4792-B07B-578D9A4E7BC5-low.png)

### Legacy

Specifying Yes results in legacy behavior. The cursor snaps to the snap grid at all times.

Specifying No results in modern behavior. The cursor snaps to the snap grid only when an operation is in progress.

### Style

Specifies the format of the snap grid, which is Standard or Isometric.

#### Standard

Sets a rectangular snap grid that is parallel to the *XY* plane of the current UCS. *X* and *Y* spacing may differ.

Spacing
:   Specifies the overall spacing of the snap grid.

Aspect
:   Specifies the horizontal and vertical spacing of the snap grid separately.

#### Isometric

Sets an isometric snap grid, in which the snap locations are initially at 30-degree and 150-degree angles. Isometric snap
cannot have different Aspect values. The lined grid does not follow the isometric snap grid.

![](../images/GUID-9EA114DC-4DA8-408E-B6A6-616CE32FFE60-low.png)

ISOPLANE determines whether the crosshairs lie in the top isometric plane (30- and 150-degree angles), the left isoplane
(90- and 150-degree angles), or the right isoplane (30- and 90-degree angles).

### Type

Specifies the snap type, polar or rectangular. This setting is also controlled by the SNAPTYPE system variable.

Polar
:   Sets the polar angle increment. (POLARANG system variable)

Grid
:   Sets the snap to Grid. When you specify points, the cursor snaps along vertical or horizontal grid points.

#### Related Concepts

* [About Isometric Drawing](About-Isometric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*