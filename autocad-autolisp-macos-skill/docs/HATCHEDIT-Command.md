# -HATCHEDIT (Command)

Uses command prompts to modify hatch-specific properties, such as pattern, scale, and angle for existing hatches or fills.

## List of Prompts

The following prompts are displayed.

Select hatch objects:

Enter hatch option [[DIsassociate](HATCHEDIT-Command.md)/[Style](HATCHEDIT-Command.md)/[Properties](HATCHEDIT-Command.md)/[DRaw order](HATCHEDIT-Command.md)/[ADd boundaries](HATCHEDIT-Command.md)/[Remove boundaries](HATCHEDIT-Command.md)/[recreate Boundary](HATCHEDIT-Command.md)/[ASsociate](HATCHEDIT-Command.md)/[separate Hatches](HATCHEDIT-Command.md)/[Origin](HATCHEDIT-Command.md)/[ANnotative](HATCHEDIT-Command.md)/[hatch COlor](HATCH-Command-2.md)/[LAyer](HATCH-Command-2.md)/[Transparency](HATCH-Command-2.md)] <Properties>: *Enter an option or press* Enter

Disassociate

Removes the associative quality from an associative hatch or fill.

Style

Specifies the method used to hatch or fill boundaries within the outermost boundary.

Ignore
:   Ignores all internal objects and hatches or fills through them.

Outer (Recommended)
:   Hatches or fills inward from the outer boundary. HATCH turns hatching or filling off if it encounters an internal island.
    This option hatches or fills only the outermost level of the structure and leaves the internal structure blank.

Normal
:   Hatches or fills inward from the outer boundary. If HATCH encounters an internal island, it turns off hatching or filling
    until it encounters another island within the island.

Properties

Specifies new hatch properties for the selected hatch or hatches. You can specify a new pattern or pattern type and then enter
the pertinent properties. For an explanation of setting pattern and fill properties at the Command prompt, see [-HATCH](HATCH-Command-2.md).

Draw Order

Assigns a draw order to selected hatches or fills. You can place a hatch or fill behind all other objects, in front of all
other objects, behind the hatch boundary, or in front of the hatch boundary. ([HPDRAWORDER](HPDRAWORDER-System-Variable.md) system variable)

Add Boundaries

Modifies the area of a single hatch or fill by adding boundaries.

Available when editing a single hatch or fill.

For more information, see [Add: Pick Points](Hatch-and-Gradient-Dialog-Box.md) or [Add: Select Objects](Hatch-and-Gradient-Dialog-Box.md).

Remove Boundaries

Modifies the area of a single hatch or fill by removing boundaries.

Available when editing a single hatch or fill.

For more information, see [Remove Boundaries](Hatch-and-Gradient-Dialog-Box.md).

Recreate Boundary

Creates a polyline or region around the selected hatch or fill, and optionally associates the hatch object with it.

Available when editing a single hatch or fill.

For more information, see [Recreate Boundary](Hatch-and-Gradient-Dialog-Box.md).

Associate

Specifies that the hatch or fill is associative. A hatch or fill that is associative is updated when you modify its boundary
objects.

Specify Internal Point
:   Determines a boundary from existing objects that form an enclosed area around the specified point, and associates the selected
    hatch with the boundary objects.

Select Objects
:   Determines a boundary from selected objects that form an enclosed area, and associates the selected hatch with the boundary
    objects.

Separate Hatches

Separates multiple hatch objects that were created as a single object into individual hatch objects.

Origin

Controls the starting location of hatch pattern generation. Some hatches, such as brick patterns, are meant to be aligned
with a point on the hatch boundary. By default, all hatch origins correspond to the current UCS origin.

Use Current Origin
:   Sets the hatch origin to use the value set in the [HPORIGINMODE](HPORIGINMODE-System-Variable.md) system variable.

Set New Origin
:   Specifies the new hatch origin point directly.

Default to Boundary Extents
:   Calculates a new origin based on the rectangular extents of the hatch. Choices include each of the four corners of the extents
    and its center. You can also store the value of the new hatch origin in the [HPORIGIN](HPORIGIN-System-Variable.md) system variable.

Annotative

Specifies that hatches in the selection set are annotative. This property automates the process of scaling annotations so
that they plot or display at the correct size on the paper.

Hatch Color

Overrides the current color with a specified color for hatch patterns and solid fills. The color value is stored in the [HPCOLOR](HPCOLOR-System-Variable.md) system variable. When Hatch Type is set to Pattern, you can also specify a new background color. The background color value
is stored in the [HPBACKGROUNDCOLOR](HPBACKGROUNDCOLOR-System-Variable.md) system variable.

To set the hatch color back to the current color for objects, enter “*.*” or *Use Current*. To turn off the background color, enter “*.*” or *none*.

Default object color
:   Enter the color number (1 through 255) or the color name (the names for the first seven colors). For example, you can specify
    the color red by entering the ACI (AutoCAD Color Index) number *1* or the ACI name *red*. You can also set the hatch color to ByLayer or ByBlock.

Truecolor
:   Specify an RGB color expressed as values from 0 to 255, such as *210,155,95*.

Colorbook
:   Specify a custom color from a color book installed on your system.

Layer

Assigns new hatch objects to the specified layer, overriding the current layer. Enter *Use Current* or “*.*” to use the current layer.

Transparency

Sets the transparency level for new hatches or fills, overriding the current object transparency. Enter *Use Current* or “*.*” to use the current object transparency setting.

#### Related References

* [HATCHEDIT (Command)](HATCHEDIT-Command-2.md)
* [Hatch Visor](Hatch-Visor.md)

#### Related Concepts

* [Hatch Edit Dialog Box](Hatch-Edit-Dialog-Box.md)
* [About Hatch Pattern Scaling](About-Hatch-Pattern-Scaling.md)
* [About Hatch Islands](About-Hatch-Islands.md)
* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*