# ELEV (Command)

Sets elevation and extrusion thickness of new objects.

## Access Methods

![](../images/ac.keyboard.gif) Command entry:  *'elev* for transparent use

## Summary

The ELEV command sets the default *Z* value for new objects above or below the *XY* plane of the current UCS. This value is stored in the ELEVATION system variable.

NOTE:Generally, it is recommended that you leave the elevation set to zero and control the *XY* plane of the current UCS with the [UCS](UCS-Command.md) command.

ELEV controls only new objects; it does not affect existing objects. The elevation is reset to 0.0 whenever you change the
coordinate system to the world coordinate system (WCS).

## List of Prompts

The following prompts are displayed.

Specify New Default Elevation
:   The current elevation is the default *Z* value for new objects when you specify only *X* and *Y* values for a 3D point.

    The elevation setting is the same for all viewports regardless of their user coordinate systems (UCS definitions). New objects
    are created at the specified *Z* value relative to the current UCS in the viewport.

Specify New Default Thickness
:   The thickness sets the distance to which a 2D object is extruded above or below its elevation. A positive value is extruded
    along the positive *Z* axis; a negative value is extruded along the negative *Z* axis.

    ![](../images/GUID-C87DC515-7B60-4138-AEA3-5F1BA5190920-low.png)

#### Related Concepts

* [About Adding 3D Thickness to 2D Objects](About-Adding-3D-Thickness-to-2D-Objects.md)
* [About Controlling the User Coordinate System (UCS)](About-Controlling-the-User-Coordinate-System-UCS.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*