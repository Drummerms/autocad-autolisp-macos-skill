# General Tab (Application Preferences Dialog Box)

Controls the behavior of program features.

OPTIONS (Command)

*Menu*:
AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences

![](../images/GUID-3473B135-6BBB-4F90-8856-08A80E5C7495-low.png)

## List of Options

The following options are displayed.

Mouse & Trackpad Customization

Controls the behavior of the mouse or trackpad.

Enable Quick Secondary Click as Return Key
:   Controls right-click behavior. A quick click is the same as pressing Enter. A longer click displays a shortcut menu.

Reverse Zoom Direction
:   Toggles the direction of transparent zoom operations when you scroll the middle mouse wheel. ([ZOOMWHEEL](ZOOMWHEEL-System-Variable.md) system variable)

Follow the System Scrolling Direction
:   Controls whether the AutoCAD trackpad follows the system scrolling direction during panning or orbiting in 3D. ([FOLLOWSYSTEMSCROLL](FOLLOWSYSTEMSCROLL-System-Variable.md) system variable)

Spacebar Customization

Controls the behavior of the spacebar when pressed or held.

Enable Spacebar Hold to Pan
:   Toggles if you can hold down the Spacebar to enable panning. ([SPACEPAN](SPACEPAN-System-Variable.md) system variable)

Window Elements

Show Rollover Tooltips
:   Controls the display of rollover tooltips when the cursor hovers over an object.

Viewport Controls

Controls the display of the menus in the upper-left corner of all viewports.

Display the Viewport Controls
:   Controls whether the menus for viewport tools, views, and visual styles that are located in the upper-left corner of every
    viewport are displayed. ([VPCONTROL](VPCONTROL-System-Variable.md) system variable)

Graphics

Change Graphic Engine
:   If you're running Mac OS 10.14 or 10.15, the Metal graphics engine is the default. You can switch back to the previous graphics
    engine, OpenGL. Metal is not supported on Mac OS 10.13 or earlier.

    NOTE:Restart AutoCAD for Mac to see the language change.

Notification

Enables product messages from Autodesk in Notification Center.

File Save Precautions

Assists in avoiding data loss.

Automatic Save
:   Saves your drawing automatically at the intervals you specify. You can specify the location of all Autosave files by using
    the
    [SAVEFILEPATH](SAVEFILEPATH-System-Variable.md) system variable.
    [SAVEFILE](SAVEFILE-System-Variable.md) (read-only) stores the name of the Autosave file.

    NOTE:Automatic save is disabled when the
    [Block Editor](Block-Editor.md) is open.

    *Minutes Between Saves:*When Automatic Save is on, specifies how often the drawing is saved. ([SAVETIME](SAVETIME-System-Variable.md) system variable)

File Save

Saves your drawing in a DWG and DXF format of your choice.

Save As
:   Provides you a list of standard drawing formats to save your drawing as.

Zoom Adjustment

Controls the zoom behavior of the input device.

Zoom Speed
:   Controls how much the magnification changes when the mouse wheel is rolled forward or backward, or you single swipe on Magic
    Mouse or a trackpad. ([ZOOMFACTOR](ZOOMFACTOR-System-Variable.md) system variable)

Layout Elements

Controls the tasks that the program performs when a new layout is created.

Create Viewports in New Layouts
:   Creates a single viewport automatically when you create a new layout. ([LAYOUTCREATEVIEWPORT](LAYOUTCREATEVIEWPORT-System-Variable.md) system variable)

Show Page Setup Manager
:   Displays the
    [Page Setup Manager](Page-Setup-Manager.md) the first time you click a named (paper space) layout. Use this dialog box to set options related to paper and print settings.
    ([SHOWPAGESETUPFORNEWLAYOUTS](SHOWPAGESETUPFORNEWLAYOUTS-System-Variable.md) system variable)

Language

Allows you to change the language shown in user interface and command input. English, French, Spanish, Korean, Chinese (Simplified),
Japanese, Italian, and German are available.

NOTE:Restart AutoCAD for Mac to see the language change.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)
* [About Rollover Tooltips](About-Rollover-Tooltips.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*