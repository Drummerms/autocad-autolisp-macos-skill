# Units & Guides Tab (Application Preferences Dialog Box)

Controls the units used when inserting blocks or referencing objects, and which drafting guides are enabled.

OPTIONS (Command)

*Menu*:
AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences

![](../images/GUID-C73160C4-05B6-42B0-9D62-1A749BC7AFD6-low.png)

## List of Options

The following options are displayed.

Insertion Scale

Controls the default scale for inserting blocks and drawings into a drawing.

For information on how the default scale is calculated, see
[About Block Units and Insertion Scale](About-Block-Units-and-Insertion-Scale.md).

Source Content Units
:   Sets source content units value when INSUNITS is set to 0.

    If Unspecified-Unitless is selected, the object is not scaled when inserted. ([INSUNITSDEFSOURCE](INSUNITSDEFSOURCE-System-Variable.md) system variable)

Target Drawing Units
:   Sets target drawing units value when INSUNITS is set to 0. ([INSUNITSDEFTARGET](INSUNITSDEFTARGET-System-Variable.md) system variable)

3D Objects

Controls the number of isolines to display for surfaces and meshes.

U Size
:   Sets the surface density for PEDIT Smooth in the
    *M* direction and the U isolines density on surface objects. ([SURFU](SURFU-System-Variable.md) system variable)

V Size
:   Sets the surface density for PEDIT Smooth in the
    *N* direction and the V isolines density on surface objects. ([SURFV](SURFV-System-Variable.md) system variable)

AutoTrack Settings

Controls the settings that relate to AutoTrack™ behavior, which is available when polar tracking or object snap tracking is turned on (see
[DSETTINGS](DSETTINGS-Command.md)).

Display Polar Tracking Vector
:   Displays a vector along specified angles when polar tracking is on. With polar tracking, you can draw lines along angles.
    Polar angles are 90-degree divisors, such as 45, 30, and 15 degrees. ([TRACKPATH](TRACKPATH-System-Variable.md) system variable = 2)

    In a 3D view, a polar tracking vector parallel to the
    *Z* axis of the UCS is also displayed, and the tooltip displays +Z or -Z for the angle depending on the direction along the Z
    axis.

Display Full-screen Tracking Vector
:   Tracking vectors are construction lines from which you can draw objects at specific angles or in specific relationships to
    other objects. If this option is selected, alignment vectors are displayed as infinite lines. (TRACKPATH system variable =
    1)

Display AutoTrack Tooltip
:   Controls the display of the AutoSnap marker, tooltip, and magnet. ([AUTOSNAP](AUTOSNAP-System-Variable.md) system variable)

Drawing Scale

Defines the default scales used by the program.

Default Scales List
:   Displays the
    [Default Scale List dialog box](Default-Scale-List-Dialog-Box.md). Use this dialog box to manage the default list of scales displayed in several dialog boxes associated with layout viewports
    and printing. You can delete all custom scales and restore the default list of scales.

Fields

Sets preferences related to fields.

Display Background of Fields
:   Controls whether fields are displayed with a gray background.

    When this option is cleared, fields are displayed with the same background as any text. ([FIELDDISPLAY](FIELDDISPLAY-System-Variable.md) system variable)

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)
* [About Block Units and Insertion Scale](About-Block-Units-and-Insertion-Scale.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*