# UCS Dialog Box

Controls the UCS and UCS icon settings for viewports.

UCSMAN (Command)

## Summary

Lists, renames, and restores user coordinate system (UCS) definitions, and controls UCS and UCS icon settings for viewports.

## List of Tabs

The UCS dialog box includes the following tabs:

* Named
* Orthographic
* Settings

Named Tab (UCS Dialog Box)

Lists UCS definitions and sets the current UCS.

![](../images/GUID-D8A12FED-2040-41D0-AA26-287DC3A83A41-low.png)

Current UCS
:   Displays the name of the current UCS. If the UCS has not been saved and named, it is listed as UNNAMED.

UCS Names List
:   Lists the coordinate systems defined in the current drawing. If there are multiple viewports and multiple unnamed UCS settings,
    the list includes only the unnamed UCS of the current viewport. Unnamed UCS definitions that are locked to other viewports
    ([UCSVP](UCSVP-System-Variable.md) system variable = 1) are not listed in the current viewport. A pointer indicates the current UCS.

    UNNAMED is always the first entry if the current UCS is unnamed. World is always listed and cannot be renamed or deleted.
    If you define other coordinate systems for the active viewport during the current editing session, a Previous entry is next.
    You can step back through these coordinate systems by selecting Previous and Set Current repeatedly.

    To add a UCS name to this list, use the Save option of the
    [UCS](UCS-Command.md) command.

Delete (-)
:   Deletes a named UCS. You cannot delete the World or Previous UCS.

Options

Manages the selected UCS in the dialog box.

Set Current
:   Restores the selected coordinate system.

Rename
:   Renames a customized UCS. You cannot rename the World UCS.

Details
:   Displays the
    [UCS Details dialog box](UCS-Details-Dialog-Box.md), which displays UCS coordinate data.

Orthographic Tab (UCS Dialog Box)

Changes the UCS to one of the orthographic UCS settings.

![](../images/GUID-793E480F-1FD6-4B2A-A1FB-DFF96DB2F82B-low.png)

Current UCS
:   Displays the name of the current UCS. If the UCS has not been saved and named, it is listed as UNNAMED.

Orthographic UCS Names
:   Lists the six orthographic coordinate systems defined in the current drawing. The orthographic coordinate systems are defined
    relative to the UCS specified in the Relative To list.

    * *Name.* Specifies the name of the orthographic coordinate system.
    * *Depth.* Specifies the distance between the
      *XY* plane of the orthographic UCS and a parallel plane that passes through the origin of the coordinate system specified by the
      [UCSBASE](UCSBASE-System-Variable.md) system variable. The parallel plane of the UCSBASE coordinate system can be an
      *XY*,
      *YZ*, or
      *XZ* plane.

      NOTE:You can specify the depth or a new origin for the selected orthographic UCS. See Depth option.

Relative To
:   Specifies the base coordinate system for defining the orthographic UCSs. By default, WCS is the base coordinate system.

    Whenever you change the Relative To setting, the origin of the selected orthographic UCS is restored to its default position.

    If you save an orthographic coordinate system in a drawing as part of a viewport configuration, or if you select a setting
    in Relative To other than World, the orthographic coordinate system name changes to UNNAMED to distinguish it from the predefined
    orthographic coordinate system.

Options

Manages the selected UCS in the dialog box.

Set Current
:   Restores the selected coordinate system.

Reset
:   Restores the origin of the selected orthographic coordinate system. The origin is restored to its default location (0,0,0)
    relative to the specified base coordinate system.

Depth
:   Specifies the distance between the
    *XY* plane of the orthographic UCS and a parallel plane that passes through the origin of the coordinate system. In the Orthographic
    UCS Depth dialog box, enter a value or choose the Select New Origin button to use the pointing device to specify a new depth
    or a new origin.

Details
:   Displays the
    [UCS Details dialog box](UCS-Details-Dialog-Box.md), which displays UCS coordinate data.

Settings Tab (UCS Dialog Box)

Displays and modifies UCS icon settings and UCS settings saved with a viewport.

![](../images/GUID-5D930083-74CC-4088-9492-786101CA66BF-low.png)

Icon

Specifies the UCS icon display settings for the current viewport.

On
:   Displays the UCS icon in the current viewport.

Display at UCS Origin Point
:   Displays the UCS icon at the origin of the current coordinate system in the current viewport. If this option is cleared, or
    if the origin of the coordinate system is not visible in the viewport, the UCS icon is displayed at the lower-left corner
    of the viewport.

Apply to All Active Viewports
:   Applies the UCS icon settings to all active viewports in the current drawing.

Allow Selecting UCS Icon
:   Controls whether the UCS icon is highlighted when the cursor moves over it and whether you can click to select it and access
    the UCS icon grips.

UCS

Specifies UCS behavior when the UCS setting is updated.

Save UCS with Viewport
:   Saves the coordinate system setting with the viewport ([UCSVP](UCSVP-System-Variable.md) system variable). If this option is cleared, the viewport reflects the UCS of the viewport that is current.

Update View to Plan When UCS Is Changed
:   Restores Plan view when the coordinate system in the viewport is changed. ([UCSFOLLOW](UCSFOLLOW-System-Variable.md) system variable)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*