# Cursor & Selection Tab (Application Preferences Dialog Box)

Controls the appearance and behavior of the cursor and selection.

OPTIONS (Command)

*Menu*:
AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences

![](../images/GUID-3BA62EB2-A545-4D26-8CEA-F18ED7311082-low.png)

## List of Options

The following options are displayed.

Selection Modes

Controls the selection of objects in the drawing area.

Use Shift Key to Add to Selection
:   Controls whether subsequent selections replace the current selection set or add to it.

    To clear a selection set quickly, draw a selection window in a blank area of the drawing. ([PICKADD](PICKADD-System-Variable.md) system variable)

Allow Press and Drag for Lasso
:   Controls the window selection method. (PICKAUTO system variable)

    If this option is checked, you can draw a selection lasso by clicking and dragging with the pointing device.

Selection Tool

Controls the appearance of the cursor in the drawing area.

Preview
:   Shows a representation of how the crosshair, ObjectSnap aperture, and pickbox will appear in the drawing area.

Crosshair Color
:   Controls the color of the crosshair, ObjectSnap aperture, and pickbox in the drawing area. Automatic is the default color.

    When set to Automatic, the actual color applied changes between white and black based on the background color of the drawing
    area.

Crosshair Lines Length
:   Determines the size of the crosshairs as a percentage of the screen size.

    Valid settings range from 1 to 100 percent. When set to 100, the crosshairs are full-screen and the ends of the crosshairs
    are never visible. When less than 100, the ends of the crosshairs may be visible when the cursor is moved to one edge of the
    screen. ([CURSORSIZE](CURSORSIZE-System-Variable.md) system variable)

ObjectSnap Aperture Size
:   Sets the display size for the object snap target box, in pixels.

    Aperture size determines how close to a snap point you can be before the magnet locks the aperture box to the snap point.
    Values range from 1 to 50 pixels. ([APERTURE](APERTURE-Command.md) system variable)

Pickbox Size
:   Sets the object selection target height, in pixels. ([PICKBOX](PICKBOX-System-Variable.md) system variable)

Autosnap Marker

Controls the appearance of the Autosnap Marker.

Marker Size
:   Sets the display size for the AutoSnap marker.

Preview

Shows you exactly how the objects would look when the command is executed. As you made the changes within the command, you
can instantly preview the final result.

Command Preview
:   Activates the preview option.

Grips

Grips are small squares displayed on an object after it has been selected.

Enable Grips
:   Controls the display of grips on selected objects. You can edit an object with grips by selecting a grip and using the shortcut
    menu. Displaying grips in a drawing significantly affects performance. Clear this option to optimize performance. ([GRIPS](GRIPS-System-Variable.md) system variable)

Enable Grips with Blocks
:   Controls the display of grip tips and Ctrl-cycling tooltips. ([GRIPBLOCK](GRIPBLOCK-System-Variable.md) system variable)

    ![](../images/GUID-FE0B26A9-C5F7-4061-97CB-ED52F90FAFA7-low.png)

Enable Grips Tips
:   Controls the display of grip tips and Ctrl-cycling tooltips. This option has no effect on standard objects. ([GRIPTIPS](GRIPTIPS-System-Variable.md) system variable)

Limit Grip Display To *N* Selected Objects
:   Suppresses the display of grips when the selection set includes more than the specified number of objects. The valid range
    is 1 to 32,767. The default setting is 100. ([GRIPOBJLIMIT](GRIPOBJLIMIT-System-Variable.md) system variable)

Grip Size
:   Sets the size of the grip box in pixels. ([GRIPSIZE](GRIPSIZE-System-Variable.md) system variable)

    ![](../images/GUID-813FB6AD-5688-41D0-B3D6-BCE7B741503A-low.png)

3D Modeling Dynamic Input

Controls dynamic input in 3D.

Show Z Field for Pointer Input
:   Displays a field for the
    *Z* coordinate when using dynamic input.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*