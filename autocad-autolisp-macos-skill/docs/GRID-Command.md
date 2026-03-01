# GRID (Command)

Displays a grid pattern in the current viewport.

## Access Methods

*Menu*:
Tools
![](../images/ac.menuaro.gif) Drafting Settings
.

*Status bar*: Grid
![](../images/GUID-DC41259C-A2FF-497F-899C-627668F1CD1D-low.png)

## List of Prompts

The following prompts are displayed.

Specify
[grid spacing(X)](GRID-Command.md) or [[ON](GRID-Command.md)/[OFF](GRID-Command.md)/[Snap](GRID-Command.md)/[Major](GRID-Command.md)/[aDaptive](GRID-Command.md)/[Limits](GRID-Command.md)/[Follow](GRID-Command.md)/[Aspect](GRID-Command.md)] <*current*>:
*Specify a value or enter an option*

Grid Spacing (X)
:   Sets the grid to the specified value. Entering
    *x* after the value sets the grid spacing to the specified value multiplied by the snap interval.

On
:   Turns on the grid using the current spacing.

Off
:   Turns off the grid.

Snap
:   Sets the grid spacing to the snap interval specified by the
    [SNAP](SNAP-Command.md) command.

Major
:   Specifies the frequency of major grid lines compared to minor grid lines. Grid lines rather than grid dots are displayed in
    any visual style except 2D Wireframe. ([GRIDMAJOR](GRIDMAJOR-System-Variable.md) system variable)

Adaptive
:   Controls the density of grid lines when zoomed in or out.

    * *Adaptive Behavior.* Limits the density of grid lines or dots when zoomed out. This setting is also controlled by the [GRIDDISPLAY](GRIDDISPLAY-System-Variable.md) system variable.
    * *Allow Subdivision Below Grid Spacing.* If turned on, generates additional, more closely spaced grid lines or dots when zoomed in. The frequency of these grid lines
      is determined by the frequency of the major grid lines.

Limits
:   Displays the grid beyond the area specified by the
    [LIMITS](LIMITS-Command.md) command.

Follow
:   Changes the grid plane to follow the XY plane of the dynamic UCS. This setting is also controlled by the [GRIDDISPLAY](GRIDDISPLAY-System-Variable.md) system variable.

Aspect
:   Changes the grid spacing in the
    *X* and
    *Y* directions, which can have different values.

    Entering
    *x* following either value defines it as a multiple of the snap interval rather than the drawing units.

    The Aspect option is not available when the current snap style is Isometric.

#### Related Concepts

* [About Adjusting the Grid and Grid Snap](About-Adjusting-the-Grid-and-Grid-Snap.md)
* [About Isometric Drawing](About-Isometric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*