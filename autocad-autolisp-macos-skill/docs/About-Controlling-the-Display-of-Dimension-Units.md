# About Controlling the Display of Dimension Units

The numeric values of dimensions can be displayed as a single measurement or in two measurement systems. In either case, you
can control details of how the numeric values are presented.

The settings for primary units control the display of the dimension values, including the unit format, the numeric precision,
and the decimal separator style. For example, you can enter the diameter symbol as a prefix, as shown in the illustration.
Any prefix you specify replaces the prefixes normally used for diameter and radius dimensions (unicode 2205 and R, respectively).

![](../images/GUID-40C49D00-F967-43E5-A17F-6DC69FACB6B4-low.png)

These settings are available on the Modify/New Dimension Style dialog box, Primary Units tab.

## Control the Display of Alternate Units

You can create dimensions in two systems of measurement simultaneously. A common use of this feature is to add feet and inches
dimensions to drawings created using metric units. The alternate units appear in square brackets ([ ]) in the dimension text.
Alternate units cannot be applied to angular dimensions.

If alternate-units dimensioning is on when you edit a linear dimension, the measurement is multiplied by an alternate scale
value that you specify. This value represents the number of alternate units per current unit of measurement. The default value
for imperial units is 25.4, which is the number of millimeters per inch. The default value for metric units is about 0.0394,
which is the number of inches per millimeter. The number of decimal places is specified by the precision value for alternate
units.

For example, for imperial units, if the alternate scale setting is the default value, 25.4, and the alternate precision is
0.00, the dimension might look like the following figure.

![](../images/GUID-13CF33FF-2D3A-4061-85D2-955E61A7F7FB-low.png)

#### Related Tasks

* [To Add and Format Primary Units](To-Add-and-Format-Primary-Units.md)
* [To Add and Format Alternate Units](To-Add-and-Format-Alternate-Units.md)
* [To Display Dimension Values in Sub-units](To-Display-Dimension-Values-in-Sub-units.md)

#### Related Concepts

* [About Controlling the Appearance of Dimension Text](About-Controlling-the-Appearance-of-Dimension-Text.md)
* [About Displaying Lateral Tolerances](About-Displaying-Lateral-Tolerances.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*