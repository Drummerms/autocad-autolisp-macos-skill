# UCSICON (Command)

Controls the visibility, placement, appearance, and selectability of the UCS icon.

## Access Methods

*Menu*:
View ![](../images/ac.menuaro.gif) UCS Icon.

## Summary

The UCS icon indicates the location and orientation of the current UCS. You can manipulate the UCS icon using grips. This
is controlled by the
[UCSSELECTMODE](UCSSELECTMODE-System-Variable.md) system variable.

NOTE: If the location of the UCS origin is not visible in a viewport, the UCS icon is displayed in the lower-left corner of the
viewport instead.

Different coordinate system icons are displayed in paper space and model space. In model space, you can choose between 2D
and 3D icon display styles (see the
[Properties](UCSICON-Command.md) option):

* *2D*. The letter
  *W* appears in the
  *Y* portion of the icon if the UCS is the same as the WCS (world coordinate system). If the UCS is rotated so that the Z axis
  lies in a plane parallel to the viewing plane—that is, if the XY plane is edge-on to the viewer—the 2D UCS icon is replaced
  by a broken pencil icon.
* *3D*. A square is displayed in the
  *XY* plane at the origin if the current UCS is the same as the WCS, and you are viewing the UCS from above (the positive
  *Z* direction). The square is missing if you are viewing the UCS from below. The
  *Z* axis is solid when viewed from above the XY plane and dashed when viewed from below the XY plane.

![](../images/GUID-946104A3-5366-4A25-8666-B3915B25EB91-low.png)

## List of Prompts

The following prompts are displayed.

Enter an option [[ON](UCSICON-Command.md)/[OFF](UCSICON-Command.md)/[All](UCSICON-Command.md)/[Noorigin](UCSICON-Command.md)/[ORigin](UCSICON-Command.md)/[Selectable](UCSICON-Command.md)/[Properties](UCSICON-Command.md)]<*current*>:
*Enter an option or press*Enter

![](../images/GUID-051E890A-E3C5-4812-AB19-81395C665ADB-low.png)

On
:   Displays the UCS icon.

Off
:   Turns off display of the UCS icon.

All
:   Applies changes to the icon in all active viewports. Otherwise, UCSICON affects only the current viewport.

No Origin
:   Displays the icon at the lower-left corner of the viewport regardless of the location of the UCS origin.

Origin
:   Displays the icon at the origin (0,0,0) of the current UCS. If the origin is out of view, it is displayed at the lower-left
    corner of the viewport.

Selectable
:   Controls whether the UCS icon is selectable and can be manipulated with grips.

Properties
:   Displays the
    [UCS Icon dialog box](UCS-Icon-Dialog-Box.md), in which you can control the style, visibility, and location of the UCS icon.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)
* [About the User Coordinate System (UCS) Icon](About-the-User-Coordinate-System-UCSIcon.md)
* [About Controlling the User Coordinate System (UCS)](About-Controlling-the-User-Coordinate-System-UCS.md)

#### Related Information

* [About Controlling the Display of the User Coordinate System Icon](About-Controlling-the-Display-of-the-User-Coordinate-System-Icon.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*