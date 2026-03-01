# Load/Unload Applications Dialog Box

Loads and unloads applications and defines which applications to load at startup.

APPLOAD (Command)

*Menu*:
Tools
![](../images/ac.menuaro.gif) Load Application.

![](../images/GUID-21D90E04-5962-4C24-A8DA-74462705FA6E-low.png)

## Summary

Loads and unloads applications and specifies applications to be loaded at startup.

## List of Options

The following options are displayed.

The options at the top of this dialog box are derived from the
[standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md). Following are descriptions of the additional options provided by the Load/Unload Applications dialog box:

Load
:   Loads or reloads the applications that are currently selected either in the files list or on the History List tab. Load is
    unavailable until you select a file that you can load. ObjectARX and DBX applications are loaded immediately, but LSP and
    FAS applications are queued and then loaded when you close the Load/Unload Applications dialog box.

    If you select a file that is already loaded, Load reloads the application when applicable. You cannot reload ObjectARX applications.
    In this case, you must first unload the ObjectARX application and then load it again. The Load option is also available from
    a shortcut menu by right-clicking a file on the History List tab.

Loaded Applications
:   Displays an alphabetical list (by file name) of currently loaded applications. LISP routines are displayed in this list only
    if you loaded them in the Load/Unload Applications dialog box.

    You can drag files into this list from the files list or from any application with dragging capabilities, such as Finder.

    You can also unload certain applications from this list. See the Unload option for details. Files that you cannot unload are
    not available for selection.

History List
:   Displays an alphabetical list (by file name) of applications that you previously loaded with Add To History selected. If Add
    To History is not selected when you drag files into this list, the dragged files are loaded but not added to the history list.

    You can drag files into this list from the files list, or from any application with dragging capabilities, such as Finder.

    You can load and remove applications from this list, but to unload applications, you must use the Loaded Applications tab.
    See the Load, Unload, and Remove options.

Add to History
:   Adds any applications that you load to the history list.

Unload/Remove
:   Unloads the selected applications or removes them from the History List. Unload is available only when a file is selected
    on the Loaded Applications tab. Remove is available only when you select a file on the History List tab.

    LISP applications cannot be unloaded, nor can ObjectARX applications that are not registered for unloading.

    NOTE:Remove does not unload the selected application. The Remove option is also available from a shortcut menu by right-clicking
    an application on the History List tab.

Startup Suite
:   Contains a list of applications that are loaded each time you start
    AutoCAD 2026.

    You can drag application files from the files list, or from any application with dragging capabilities such as Finder, into
    the Startup Suite area to add them to the Startup Suite.

    You cannot add applications that you load with the
    AutoCAD 2026 web browser to the Startup Suite.

Contents
:   Displays the
    [Startup Suite dialog box](GUID-B38F610B-51FB-4938-BDEC-A0A737F5DB6C.htm#WSC30CD3D5FAA8F6D86B7920FFC2D5EE17-7FEC). You can also add files to the Startup Suite by clicking the Startup Suite icon or by right-clicking an application on the
    History List tab and clicking Add to Startup Suite on the shortcut menu.

Status Line
:   Displays messages that indicate the status of loading and unloading operations.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*