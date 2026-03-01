# STATUS (Command)

Displays drawing statistics, modes, and extents.

## Access Methods

*Menu*:
Tools
![](../images/ac.menuaro.gif) Inquiry
![](../images/ac.menuaro.gif) Status.

![](../images/ac.keyboard.gif) Command entry:  *'status* for transparent use

## Summary

All coordinates and distances are displayed by STATUS in the format specified by
[UNITS](UNITS-Command-2.md).

STATUS reports the number of objects in the current drawing. This includes graphical objects such as arcs and polylines, and
nongraphical objects such as layers and linetypes, and block definitions.

In addition to overall drawing statistics and settings, the amount of installed memory free on your system, the amount of
disk space available, and the amount of free space in the swap file are also listed.

When used at the DIM prompt, STATUS reports the values and descriptions of all dimensioning system variables.

In addition, STATUS displays the following information.

## List of Options

The following options are displayed.

Model or Paper Space Limits Are
:   Displays the grid limits defined by
    [LIMITS](LIMITS-Command.md). The first line shows the
    *XY* coordinate of the limit's lower-left corner, stored in the
    [LIMMIN](LIMMIN-System-Variable.md) system variable. The second line shows the
    *XY* coordinate of the limit's upper-right corner, stored in the
    [LIMMAX](LIMMAX-System-Variable.md) system variable. The notation Off to the right of the
    *Y* coordinate value indicates that limits checking is set to 0.

Model or Paper Space Uses
:   Displays the drawing extents, which includes all objects in the database and can exceed the grid limits. The first line shows
    the
    *XY* coordinate of the lower-left corner of the extents. The second line shows the
    *XY* coordinate of the upper-right corner. The notation Over to the right of the
    *Y* coordinate value indicates that the drawing extends outside the grid limits.

Display Shows
:   Lists the portion of the drawing extents visible in the current viewport. The first line shows the
    *XY* coordinate of the display's lower-left corner. The second line shows the
    *XY* coordinate of the upper-right corner.

Insertion Base Is
:   Specifies the point used when the drawing is inserted into another drawing as a block. ([INSBASE](INSBASE-System-Variable.md) system variable)

Snap Resolution Is
:   Sets the snap spacing for the current viewport. ([SNAPUNIT](SNAPUNIT-System-Variable.md) system variable)

Grid Spacing Is
:   Specifies the grid spacing (X and Y) for the current viewport. ([GRIDUNIT](GRIDUNIT-System-Variable.md) system variable)

Current Space
:   Shows whether model space or paper space is active.

Current Layout
:   Displays “Model” or the name of the current layout.

Current Layer
:   Sets the current layer. ([CLAYER](CLAYER-System-Variable.md) system variable)

Current Color
:   Sets the color of new objects. ([CECOLOR](CECOLOR-System-Variable.md) system variable)

Current Linetype
:   Sets the linetype of new objects. ([CELTYPE](CELTYPE-System-Variable.md) system variable)

Current Material
:   Sets the material of new objects. ([CMATERIAL](CMATERIAL-System-Variable.md) system variable)

Current Lineweight
:   Sets the lineweight of new objects. ([CELWEIGHT](CELWEIGHT-System-Variable.md) system variable)

Current Plot Style
:   Sets the current plot style of new objects. ([CPLOTSTYLE](CPLOTSTYLE-System-Variable.md) system variable)

Current Elevation
:   Stores the current elevation of new objects relative to the current UCS. ([ELEVATION](ELEVATION-System-Variable.md) system variable)

Thickness
:   Sets the current 3D thickness. ([THICKNESS](THICKNESS-System-Variable.md) system variable)

Fill, Grid, Ortho, Qtext, Snap, Tablet
:   Shows whether these modes are on or off.

Object Snap Modes
:   Lists the running object snap modes. ([OSNAP](OSNAP-Command.md) command)

#### Related Concepts

* [Get Information from Drawings](Get-Information-from-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*