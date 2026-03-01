# Hatch Visor

Defines the boundaries, pattern or fill properties, and other parameters for hatch and fills.

![](../images/GUID-B5758D9D-1673-4213-A39A-D26377BB92BE-low.png)

Hatch pattern controls

![](../images/GUID-8825D433-2B2A-4E6D-A074-27826CF2880C-low.png)

Solid fill controls

![](../images/GUID-14902C30-E5ED-418A-AD61-3E55B0BD3FE7-low.png)

Gradient fill controls

## Summary

The Hatch visor is displayed when you start the HATCH or GRADIENT command, or select an existing hatch or fill in a drawing.

When multiple hatches or fills of different types are selected in a drawing, some of the controls on the Hatch visor are disabled.

## List of Options

The following options are displayed.

Pattern

Displays a preview image of the current hatch pattern or fill.

Click the preview image to display the Hatch Library palette and select a new pattern to use, or click the button to the right
of the preview image to switch the type of hatch pattern or fill being created.

Properties

Color (Hatch Patterns and Solid Fills)
:   Overrides the current color for hatch patterns and solid fills. ([HPCOLOR](HPCOLOR-System-Variable.md) system variable)

Background Color (Hatch Patterns)
:   Specifies the color for hatch pattern backgrounds. Not available when using the Solid pattern. ([HPBACKGROUNDCOLOR](HPBACKGROUNDCOLOR-System-Variable.md) system variable)

Gradient Color 1 (Gradient Fills)
:   Specifies the first of two gradient colors. ([GFCLR1](GFCLR1-System-Variable.md) system variable)

Gradient Color 2 (Gradient Fills)
:   Specifies the second gradient color. ([GFCLR2](GFCLR2-System-Variable.md) system variable)

Angle (Hatch Patterns and Gradient Fills)
:   Specifies an angle for the hatch or fill relative to the
    *X* axis of the current UCS. Valid values are from 0 to 359. ([HPANG](HPANG-System-Variable.md) system variable)

Scale (Hatch Patterns)
:   Expands or contracts a predefined or custom hatch pattern. This option is available only when Hatch Type is set to Pattern.
    ([HPSCALE](HPSCALE-System-Variable.md) system variable)

Pick Points

Determines the boundary to hatch or fill from existing objects that form an enclosed area around a specified point.

![](../images/GUID-BDD473C0-2427-4810-9E79-30702A267D5E-low.png)

Select Boundary

Determines the boundary to hatch or fill from selected objects that form an enclosed area.

![](../images/GUID-B6761C2D-D44B-47A0-9903-436718221D11-low.png)

When you use the Select Boundary option, HATCH does not automatically detect interior objects. You must select the objects
within the selected boundary to hatch or fill those objects according to the current island detection style. Right-click and
choose Settings to change the current island detection style.

Remove Boundary

Removes from the boundary definition any of the objects that were previously added. Option is only available after a boundary
has been defined.

Create Boundary

Creates a polyline or region around the selected hatch or fill, and optionally associates the hatch or fill object with it.
Option is only available when modifying an existing hatch or fill object.

Create Separated Hatches

Controls whether a single hatch or fill object or multiple hatch or fill objects are created when several separate closed
boundaries are specified. ([HPSEPARATE](HPSEPARATE-System-Variable.md) system variable)

Match Hatch Properties

Sets the properties of a hatch or fill with a selected hatch or fill object.

Exit the Hatch Editor and Close the Visor

Quits the current command and closes the visor.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*