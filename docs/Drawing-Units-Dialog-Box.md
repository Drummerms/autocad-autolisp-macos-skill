# Drawing Units Dialog Box

Controls the displayed precision and format for coordinates and angles.

UNITS (Command)

*Menu*:
Format ![](../images/ac.menuaro.gif) Units.

![](../images/GUID-DA3989F1-4FBF-4A46-AC26-CFDF8460308F-low.png)

## List of Options

The following options are displayed.

Length

Type
:   Sets the current format for units of measure. The values include Architectural, Decimal, Engineering, Fractional, and Scientific.
    The Engineering and Architectural formats produce feet-and-inches displays and assume that each drawing unit represents one
    inch. The other formats can represent any real-world unit.

Precision
:   Sets the number of decimal places or fractional size displayed for linear measurements.

Angle

Specifies the current angle format and the precision for the current angle display.

Type
:   Sets the current angle format.

Precision
:   Sets the precision for the current angle display.

    The following conventions are used for the various angle measures: decimal degrees appear as decimal numbers, grads appear
    with a lowercase
    *g* suffix, and radians appear with a lowercase
    *r* suffix. The degrees/minutes/seconds format uses
    *d* for degrees, ' for minutes, and " for seconds; for example:

    123d45'56.7"

    Surveyor's units show angles as bearings, using N or S for north or south, degrees/minutes/seconds for how far east or west
    the angle is from direct north or south, and E or W for east or west; for example:

    N 45d0'0" E

    The angle is always less than 90 degrees and is displayed in the degrees/minutes/seconds format. If the angle is precisely
    north, south, east, or west, only the single letter representing the compass point is displayed.

Clockwise
:   Calculates positive angles in the clockwise direction. The default direction for positive angles is counterclockwise.

    When prompted for an angle, you can point in the desired direction or enter an angle regardless of the setting specified for
    Clockwise.

Preview

Displays an example of the current settings for units and angles.

Lighting

Controls the unit of measurement for the intensity of photometric lights in the current drawing. Photometric lights use the
insertion scale to determine the units used in rendering, so Insertion Scale should be set to a unit style other than Unitless.

Insertion Scale

Controls the unit of measurement for blocks and drawings that are inserted into the current drawing.

If you insert a block or a drawing that is created with units that are different from the units used in the current drawing,
the insertion scale value corrects the mismatch. If you do not want the block or drawing to be scaled, specify Unitless.

For information on how the scale of a block or drawing inserted into the current drawing is calculated, see
[About Block Units and Insertion Scale](About-Block-Units-and-Insertion-Scale.md).

NOTE:

If the Insertion Scale is set to Unitless in either the source block or the target drawing, the Source Content Units and Target
Drawing Units settings are referenced to determine the scaling ratio. For information on how to set these settings, see
[To Set Block Insertion Scale for a Drawing](GUID-410E4A05-F789-4416-9D63-3D24A46DD740.htm#GUID-03534430-B211-4AEB-AF6C-8F6A9268D38D).

US Survey Feet is a historical survey unit that's about 2 parts per million larger than the International Feet unit. This
difference is significant only at scales used for mapping in the U.S. The US Survey Feet setting is supported only for inserting
or attaching drawings starting with AutoCAD 2017-based products. Drawings opened in prior versions will treat the US Survey
Feet setting as Unitless.

Base Angle Directions

Sets the direction of the zero angle. The following options affect the entry of angles, the display format, and the entry
of polar, cylindrical, and spherical coordinates.

East
:   Specifies the compass direction east (the default).

North
:   Specifies the compass direction north.

West
:   Specifies the compass direction west.

South
:   Specifies the compass direction south.

Other
:   Specifies a direction different from the points of the compass.

Angle
:   Specifies a value for the zero angle when Other is selected.

Pick an Angle Button
:   Defines the zero angle in the graphics area based on the angle of an imaginary line that connects any two points you specify
    with the pointing device.

#### Related References

* [UNITS (Command)](UNITS-Command-2.md)

#### Related Concepts

* [About Units of Measurement](About-Units-of-Measurement.md)
* [About Unit Format Conventions](About-Unit-Format-Conventions.md)
* [About Block Units and Insertion Scale](About-Block-Units-and-Insertion-Scale.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*