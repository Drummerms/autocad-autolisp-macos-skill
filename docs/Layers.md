# Layers

Organize your drawing by assigning objects to layers.

When a drawing becomes visually complex, you can hide the objects that you currently do not need to see.

![](../images/GUID-D034346F-5F9F-41BE-88DC-BD02B8C2F9EC-low.png)

In the drawing below, the doors and electrical wiring were temporarily hidden by turning off their layers.

![](../images/GUID-492ED00B-E785-44CA-B51B-C6C909D2BB77-low.png)

You gain this level of control by organizing the objects in your drawing on layers that are associated with a specific function
or a purpose. It might be helpful to think of layers as clear plastic sheets:

![](../images/GUID-E573A9A8-FC63-4527-98AB-D15815B1D115-low.png)

With layers, you can

* Associate objects by their function or location
* Display or hide all related objects in a single operation
* Enforce linetype, color, and other property standards for each layer

IMPORTANT:Resist the temptation to create everything on one layer. Layers are the most important organizing feature available in AutoCAD
drawings.

## Layer Controls

To see how a drawing is organized, use the Layers palette. By default, the Layers palette is docked on the right side above
the Properties Inspector. Undock the palette to resize the palette and individual columns within the palette.

![](../images/GUID-4109AC54-AF2E-4678-BD82-BDB3DA0A2F74-low.png)

NOTE:If you close the Layers palette, you can reopen it by selecting Layers from the Window menu, by pressing Command+4, or by
typing LAYER.

Here's what the Layers palette displays in this drawing.

![](../images/GUID-3F21E31D-A97E-4EEC-A25A-E7A0FE5B9CD6-low.png)

As indicated, layer 10 WALLS is the
*current layer*. All new objects are automatically placed on that layer.

In the visibility column, notice that the circle icons for two layers are not filled in. These layers were turned off to hide
the doors and electrical wiring in the floor plan.

NOTE:You might need to right-click the column headers to display the columns you want to see.

Notice that each layer name starts with a two-digit number. This convention makes it easy to control the order of the layers
because their order does not depend on the alphabet.

TIP:For complex drawings, you might want to consider a more elaborate layer naming standard. For example, layer names could begin
with 3 digits followed by a naming code that accommodates multiple floors in a building, project numbers, sets of survey and
property data, and so on.

## Practical Recommendations

* Layer 0 is the default layer that exists in all drawings and has some esoteric properties. Instead of using this layer, it's
  best to create your own layers with meaningful names.
* Any drawing that contains at least one dimension object automatically includes a reserved layer named Defpoints.
* Create a layer for behind-the-scenes construction geometry, reference geometry, and notes that you usually do not need to
  see or print.
* Create a layer for layout viewports. Information about layout viewports is covered in the Layouts topic.
* Create a layer for all hatches and fills. This lets you to turn them all on or off in one action.

## Layer Settings

The following are the most commonly used layer settings in the Layer Properties Manager. You click the icon to turn the setting
on and off.

* Turn off layers. You turn off layers to reduce the visual complexity of your drawing while you work.

  ![](../images/GUID-3007DE3C-5F3E-43F5-B4F0-A3813ACA0A2A-low.png)
* Freeze layers. You freeze layers that you do not need to access for a while. Freezing layers is similar to turning them off,
  but improves performance in very large drawings.

  ![](../images/GUID-20E42312-CE05-440E-AC07-365E4F47395F-low.png)
* Lock layers. You lock layers when you want to prevent accidental changes to the objects on those layers. Also, the objects
  on locked layers appear faded, which helps reduce the visual complexity of your drawing, but still lets you see the objects
  faintly.

  ![](../images/GUID-B24A6B16-F29B-48B2-88A9-1497DC1A173E-low.png)
* Set default properties. You set the default properties for each layer, including color, linetype, lineweight, and transparency.
  New objects that you create will use these properties unless you override them. Overriding layer properties is explained later
  in this topic.

## Controls in the Layer Properties Manager

To create a layer, click the button shown and enter the name of the new layer. To change the current layer, double-click the
layer name or right-click the layer name and select Make Active.

![](../images/GUID-48E211F8-D9CC-4692-9967-CB470A832063-low.png)

## Quick Access to Layer Settings

The Layers palette takes up a lot of space, and you don't always need to access all the options. For quick access to the most
common layer controls, dock the Layers palette. When no objects are selected, the palette displays the name of the current
layer as shown here.

![](../images/GUID-B57A5696-BDF7-4AA8-B662-B590BE884F0F-low.png)

Occasionally, check to make sure that the objects you create will be on the correct layer. It's easy to forget to do this,
but it's also easy to set. Click the drop-down arrow to display a list of layers, and then click a layer on the list to make
it the current layer. You can also click on any icon in the list to change its setting.

![](../images/GUID-EA596AED-9D21-4529-A4E9-D612FBECF7EC-low.png)

## Maintain Your Standards

It's critically important either to establish or to conform to a company-wide layer standard. With a layer standard, drawing
organization will be more logical, consistent, compatible, and maintainable over time and across departments. Layer standards
are essential for team projects.

If you create a standard set of layers and save them in a drawing template file, those layers will be available when you start
a new drawing, and you can start working immediately. Additional information about drawing template files is presented in
the Basics topic.

## Summary

Layers organize your drawing, enabling you to temporarily suppress the display of unneeded graphical data. You can also assign
default properties such as color and linetype to each layer.

NOTE:Some experienced AutoCAD users set properties only by changing layers, while others set properties independently of layers
or in combination with layers. Assigning properties to objects is covered in the Properties topic.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Precision](GUID-85D8C41C-9C3E-440F-BD60-61848DD27219.htm " Ensure the precision required for your models.
")

**Next topic:** [Properties](GUID-72AC2E5A-4E0E-45B0-B36C-CE8B6C23B2C8.htm "Assign properties such as color and linetype to individual objects, or as default properties assigned to layers.
")

#### Related References

* [LAYER (Command)](LAYER-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*