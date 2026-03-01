# Pointer Input Settings Dialog Box

Controls the settings of pointer input tooltips.

DSETTINGS (Command)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Drafting Settings:
Dynamic Input tab ![](../images/ac.menuaro.gif) Pointer Input: Settings.

## List of Options

The following options are displayed.

Format

Controls coordinate format in the tooltips that are displayed when pointer input is turned on.

Polar Format
:   Displays the tooltip for the second or next point in polar coordinate format. Enter a comma (,) to change to Cartesian format.
    (DYNPIFORMAT system variable)

Cartesian Format
:   Displays the tooltip for the second or next point in Cartesian coordinate format. Enter an angle symbol (<) to change to polar
    format. (DYNPIFORMAT system variable)

Relative Coordinates
:   Displays the tooltip for the second or next point in relative coordinate format. Enter a pound sign (#) to change to absolute
    format. (DYNPICOORDS system variable)

Absolute Coordinates
:   Displays the tooltip for the second or next point in absolute coordinate format. Enter an at sign ( ) to change to relative
    format. Note that you cannot use the direct distance method when this option is selected. (DYNPICOORDS system variable)

Visibility

Controls when pointer input is displayed. (DYNPIVIS system variable)

As Soon As I Type Coordinate Data
:   When pointer input is turned on, displays tooltips only when you start to enter coordinate data. (DYNPIVIS system variable)

When a Command Asks for a Point
:   When pointer input is turned on, displays tooltips whenever a command prompts you for a point. (DYNPIVIS system variable)

Always—Even When Not in a Command
:   Always displays tooltips when pointer input is turned on. (DYNPIVIS system variable)

#### Related References

* [DSETTINGS (Command)](DSETTINGS-Command.md)

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*