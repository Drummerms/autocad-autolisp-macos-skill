# Match Properties Settings Dialog Box

Specifies the properties that are copied from the select source object to the destination objects.

MATCHPROP (Command) :

*Toolbar*:
![](../images/GUID-F83BA1A0-36C4-43E4-B80B-8EF3E0976E54-low.png) :
Select source object ![](../images/ac.menuaro.gif) Specify the settings option at the prompt

![](../images/GUID-4AF817E0-7208-43DB-90B5-C26A7DFD2C00-low.png)

## Summary

Specifies which basic properties and special properties to copy from the source object to the destination objects.

## List of Options

The following options are displayed.

Basic Properties

Color
:   Changes the color of the destination object to that of the source object. Available for all objects.

Layer
:   Changes the layer of the destination object to that of the source object. Available for all objects.

Linetype
:   Changes the linetype of the destination object to that of the source object. Available for all objects except attributes,
    hatches, multiline text, points, and viewports.

Linetype Scale
:   Changes the linetype scale factor of the destination object to that of the source object. Available for all objects except
    attributes, hatches, multiline text, points, and viewports.

Lineweight
:   Changes the lineweight of the destination object to that of the source object. Available for all objects.

Transparency
:   Changes the transparency of the of the destination object to that of the source object. Available for all objects.

Thickness
:   Changes the thickness of the destination object to that of the source object. Available only for arcs, attributes, circles,
    lines, points, 2D polylines, regions, and text.

Plot Style
:   Changes the plot style of the destination object to that of the source object. If you are working in color-dependent plot
    style mode ([PSTYLEPOLICY](PSTYLEPOLICY-System-Variable.md) is set to 1), this option is unavailable. Available for all objects, except those with the Jitter edge modifier applied.

Special Properties

Dimension
:   In addition to basic object properties, changes the dimension style and annotative properties of the destination object to
    that of the source object. Available only for dimension, leader, and tolerance objects.

Polyline
:   In addition to basic object properties, changes the width and linetype generation properties of the destination polyline to
    those of the source polyline. The fit/smooth property and the elevation of the source polyline are not transferred to the
    destination polyline. If the source polyline has variable width, the width property is not transferred to the destination
    polyline.

Material
:   In addition to basic object properties, changes the material applied to the object. If the source object does not have a material
    assigned and the destination object does, the material is removed from the destination object.

Text
:   In addition to basic object properties, changes the text style and annotative properties of the destination object to that
    of the source object. Available only for single-line and multiline text objects.

Viewport
:   In addition to basic object properties, changes the following properties of the destination paper space viewport to match
    those of the source viewport: on/off, display locking, standard or custom scale, shade plot, snap, grid, and UCS icon visibility
    and location.

    The settings for clipping and for UCS per viewport and the freeze/thaw state of the layers are not transferred to the destination
    object.

Shadow Display
:   In addition to basic object properties, changes the shadow display. The object can cast shadows, receive shadows, or both,
    or it can ignore shadows.

Hatch
:   In addition to basic object properties, changes the hatch properties (including its annotative properties) of the destination
    object to that of the source object. To match the hatch origin, use Inherit Properties in HATCH or HATCHEDIT. Available only
    for hatch objects.

Table
:   In addition to basic object properties, changes the table style of the destination object to that of the source object. Available
    only for table objects.

Multileader
:   In addition to basic object properties, changes the multileader style and annotative properties of the destination object
    to that of the source object. Available only for multileader objects.

#### Related References

* [MATCHPROP (Command)](MATCHPROP-Command.md)

#### Related Concepts

* [About Transferring Information Between Open Drawings](About-Transferring-Information-Between-Open-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*