# About Layers

Layers are the primary method for organizing the objects in a drawing by function or purpose. Layers can reduce the visual
complexity of a drawing and improve display performance by hiding information that you don’t need to see at the moment.

Before you start drawing, create a set of layers that are useful to your work. In a house plan, you might create layers for
the foundation, floor plan, doors, fixtures, electrical, and so on.

In this example, the display is limited to the objects on the Floor Plan layer by turning off the other layers.

![](../images/GUID-8F2ECFEC-E493-4974-A522-07FE81054A0D-low.png)

For other disciplines, the names and number of layers that you create will be different. Once you create a standard set of
layers, you can save the drawing as a template file (*.dwt*) that you can use when you start a new drawing.

For complex drawings, you might want to consider a more elaborate layer naming standard. For example, layer names could begin
with 3 digits followed by a naming code that accommodates multiple floors in a building, project numbers, sets of survey and
property data, and so on. This type of naming convention also makes it easy to control the order of the layers and limit the
layers displayed in the layer list.

## Layer Tools

Use the Layers palette to manage your layers.

* Create, rename, and remove layers
* Set the current layer on which new objects are automatically created
* Specify the default properties for objects on the layer

  You can override any layer property of an object. For example, if an object’s color property is set to BYLAYER, the object
  displays the color of that layer. If the object’s color is set to Red, the object displays as red, regardless of the color
  assigned to that layer.
* Set whether the objects on a layer are displayed or turned off
* Control whether objects on a layer are plotted
* Set whether a layer is locked against editing
* Control the layer display properties for layout viewports
* Sort and group layer names
* Manage layer states

## Current Layer

All new objects are drawn on the current layer. The current layer is indicated in the Layers palette.

![](../images/GUID-18322F09-E3A7-4DE5-AA88-78B138D46FA0-low.png)

A layer cannot be the current layer if:

* The layer is frozen
* The layer is part of an external reference

You can also use the layer controls at the top of the Properties Inspector to:

* Change basic layer properties
* Change the current layer based on a selected object
* Change a layer's properties based on a selected object
* Change the layer of selected objects based on the layer of a selected object
* Undo the last changes made to layer settings
* Manage layer states

![](../images/GUID-F2D77408-AC94-4EB6-AF75-E028845296E9-low.png)

## Layer Visibility

You can control the visibility of objects on a layer by toggling the layer on/off or by using freeze/thaw.

![](../images/GUID-2EE47669-B7B9-405D-92A0-548EF2F8D8CF-low.png) You can turn layers off and on as needed. Objects on layers turned off are invisible in the drawing.

![](../images/GUID-20E42312-CE05-440E-AC07-365E4F47395F-low.png) Freezing and thawing layers is similar to turning them off and on. However, when working with drawings with lots of layers,
freezing unneeded layers can speed up display and regeneration. For example, objects on a frozen layer are not considered
during a ZOOM EXTENTS.

## Locking Layers

You can prevent objects on selected layers from being inadvertently modified by locking those layers. Objects on locked layers
appear faded and a small lock icon is displayed when you hover over the object.

![](../images/GUID-15D066FD-68C1-4C9B-9106-8F1A7F656759-low.png)

The fading feature for locked layers lets you reduce the visual complexity of a drawing, but still maintain visual reference
and object snapping capabilities.

You can set the fade level for locked layers with the LAYLOCKFADECTL system variable.

In this example, the fading level is set at 25%, 50%, and the maximum fading level, 90%.

![](../images/GUID-9C50C1AF-A1E6-4239-AEE5-3289823D5381-low.png)

There are a few things to keep in mind when working with locked layers:

* The locked layer fading value further reduces the visibility of transparent objects.
* The locked layer fading value does not affect how objects appear when plotted.
* Grips are not displayed on objects that are on locked layers.

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)
* [To Change the Layer of Selected Objects](To-Change-the-Layer-of-Selected-Objects.md)
* [To Match the Layer Setting Between Selected Objects](To-Match-the-Layer-Setting-Between-Selected-Objects.md)
* [To Change the Visibility of Layers](To-Change-the-Visibility-of-Layers.md)
* [To Purge All Unused Layers](To-Purge-All-Unused-Layers.md)

#### Related References

* [Layers Palette](Layers-Palette.md)
* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Overriding Layer Properties in a Layout Viewport](About-Overriding-Layer-Properties-in-a-Layout-Viewport.md)
* [About Xref Layer Properties and Overrides](About-Xref-Layer-Properties-and-Overrides.md)

#### Related Information

* [About Saving and Restoring Layer States and Settings](About-Saving-and-Restoring-Layer-States-and-Settings.md)
* [Overview of Object Properties](Overview-of-Object-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*