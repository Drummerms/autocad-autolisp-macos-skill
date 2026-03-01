# New Layer Name Dialog Box

Adds a custom prefix or suffix to layer names to help organize components of a section block

SECTIONPLANESETTINGS (Command)

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Section Plane drop-down ![](../images/ac.menuaro.gif) Section Plane Settings
![](../images/GUID-96950BDA-DB2D-46FC-B877-42437F9D31E9-low.png): In the
[Section Settings dialog box](GUID-C7D36F43-E683-4C6D-AA87-1F099E37EEC5.htm#WSFACF1429558A55DEF27E5F106B5723EEC-7D6B), Layer list, click New Layer Name Settings.

![](../images/GUID-3837FEE4-E597-4507-AF0C-D9FEE5BE03C0-low.png)

## Summary

By default, all section block geometry is placed on Layer 0 (zero). However, you can specify suffix or prefix labels to help
organize section block components, such as intersection boundaries and fill. When the section block is inserted, the section
block components are placed on new layers whose name combines the name of the layer that contains the sectioned object and
the prefix or suffix you specify. If the section plane includes objects on two or more layers, two or more new object layers
are created.

For example, suppose you create a suffix called “\_kitchen” and then select \*ObjectByLayer\*\_kitchen in the Section Settings
dialog box, under Intersection Boundary. If you create a section block that bisects objects on the Walls and Cabinetry layers,
two new layers are created to contain the block geometry for intersection boundaries: Walls\_kitchen and Cabinetry\_kitchen.

You can then easily modify the appearance of a set of block components by changing their properties. If a property such as
Color is set as an object override in the Section Settings dialog box, you can change the property in that location. If the
property is set to ByLayer, you can change it in the
[Layers palette](Layers-Palette.md).

## List of Options

The following options are displayed.

Added Text Type
:   Specifies whether or how identifying text is added to the layer name for the section block component.

    * *None.*No additional text is added to the layer name. The section block geometry is placed on the same layer as the original geometry.
    * *Prefix.* If the Layer property is specified as \*ObjectByLayer\* in the Section Settings dialog box, the label is added in front of
      the layer name.
    * *Suffix.*If the Layer property is specified as \*ObjectByLayer\* in the Section Settings dialog box, the label is added to the end of
      the layer name.

Added Text
:   Specifies identifying text to be added to the name of the layer that contains the component geometry when the section block
    is inserted.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*