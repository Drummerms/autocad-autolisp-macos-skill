# Plot Stamp Settings Dialog Box

Specifies the information for the plot stamp.

PLOTSTAMP (Command)

![](../images/GUID-875F9F14-C98C-414F-BB82-167578B0C090-low.png)

## List of Options

The following options are displayed.

AutoCAD Fields

Specifies the drawing information you want applied to the plot stamp. The selected fields are separated by commas and a space.

Drawing Name
:   Includes the drawing name and path in the plot stamp information.

Layout Name
:   Includes the name of the layout in the plot stamp information.

Date and Time
:   Includes the date and time in the plot stamp information.

    NOTE:A plot stamp uses the current date and time format setting of the operating system. Plot stamp specifically uses the short
    date style for dates.

Login Name
:   Includes the user login name in the plot stamp information.

    The user login name is contained in the LOGINNAME system variable.

Device Name
:   Includes the current plotting device name in the plot stamp information.

Paper Size
:   Includes the paper size for the currently configured plotting device in the plot stamp information.

Plot Scale
:   Includes the plot scale in the plot stamp information.

User Defined Fields

Provides text that can optionally be plotted, logged, or both plotted and logged at plot time. The selected value in each
user-defined list will be plotted.

For example, you might populate one list with media types or prices and the other with job names. If the user-defined value
is set to <none>, then no user-defined information is plotted

Add/Edit
:   Displays the
    [Add User Defined Fields dialog box](Add-User-Defined-Fields-Dialog-Box.md), where you can add, edit, or delete user-defined fields.

Parameter File

Stores plot stamp information in a file with a
*.pss* extension. Multiple users can access the same file and stamp their plots based on company standard settings.

Two PSS files are provided,
*Mm.pss* and
*Inches.pss*, which are located in the
*Support* folder. The initial default plot stamp parameter file name is determined by the regional settings of the operating system
when the program is installed.

Path
:   Specifies the location of the plot stamp parameter file.

Load
:   Displays the Plotstamp Parameter File Name dialog box (a standard file selection dialog box) in which you can specify the
    location of the parameter file you want to use.

Save As
:   Saves the current plot stamp settings in a new parameter file.

Show/Hide Advanced Settings

Expands or collapses the Advanced Settings section towhich contains placement and text options for the plot stamp.

Location and Offset

Determines the plot stamp location, the orientation of the plot stamp, and the offset you want to apply relative to either
the printable area or the paper border.

Location
:   Indicates the area where you want to place the plot stamp. Selections include Top Left, Bottom Left (default), Bottom Right,
    and Top Right. The location is relative to the image orientation of the drawing on the page.

Orientation
:   Indicates the rotation of the plot stamp in relation to the specified page. The options are Horizontal and Vertical for each
    of the locations (for example, Top Left Horizontal and Top Left Vertical).

Stamp Upside-Down
:   Rotates the plot stamp upside down.

X Offset
:   Determines the
    *X* offset value that is calculated from either the corner of the paper or the corner of the printable area, depending on which
    setting you specify. If you specify Offset Relative to Paper Border, the offset value is calculated so that the plot stamp
    information fits within the paper size.

Y Offset
:   Determines the
    *Y* offset value that is calculated from either the corner of the paper or the corner of the printable area, depending on which
    setting you specify. If you specify Offset Relative to Paper Border, the offset value is calculated so that the plot stamp
    information fits within the paper size.

Offset Relative to Printable Area
:   Calculates the offset values that you specify from the corner of the printable area of the paper (not the corner of the paper).

Offset Relative to Paper Border
:   Calculates the offset values that you specify from the corner of the paper (not the corner of the printable area of the paper).

Text and Units

Determines the font, height, and number of lines you want to apply to the plot stamp text.

Font
:   Specifies the TrueType font you want to apply to the text used for the plot stamp information.

Height
:   Specifies the text height you want to apply to the plot stamp information.

Single Line Plot Stamp
:   Places the plot stamp information in a single line of text. The plot stamp information can consist of up to two lines of text,
    but the placement and offset values you specify must accommodate text wrapping and text height. If this option is cleared,
    plot stamp text is wrapped after the third field.

Units
:   Specifies the units to use to calculate the height of the text: inches, millimeters, and pixels.

Log File

Writes the plot stamp information to a log file instead of, or in addition to, stamping the current plot. If plot stamping
is turned off, the log file can still be created.

Create a Log File
:   Writes the plot stamp information to a log file. The default log file is
    *plot.log*, and it is located in the main application folder.

    You can specify a different file name and path. After the initial
    *plot.log* file is created, the plot stamp information in each succeeding plotted drawing is added to this file. Each drawing's plot
    stamp information is a single line of text. The plot stamp log file can be placed on a network drive and shared by multiple
    users. Plot stamp information from each user is appended to the
    *plot.log* file.

Log File Name
:   Specifies the file name for the log file you are creating. Enter a new file name if you do not want to use the default file
    name,
    *plot.log*.

Browse
:   Lists the currently saved plot stamp log files. You can choose to overwrite an existing plot stamp log file with the currently
    specified plot stamp information, and then to save this file.

#### Related References

* [PLOTSTAMP (Command)](PLOTSTAMP-Command.md)

#### Related Concepts

* [About Setting Options for Plotted Objects](About-Setting-Options-for-Plotted-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*