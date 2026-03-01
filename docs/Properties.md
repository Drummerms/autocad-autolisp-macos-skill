# Properties

Assign properties such as color and linetype to individual objects, or as default properties assigned to layers.

In the following drawing, the walls, exterior stone facing, doors, fixtures, cabinetry, HVAC, electrical, and text were created
using different colors to help differentiate between them.

![](../images/GUID-D034346F-5F9F-41BE-88DC-BD02B8C2F9EC-low.png)

## The Properties Inspector Palette

The Properties Inspector palette is an essential tool. By default, the Properties Inspector palette is docked on the right
side below the Layers palette.

![](../images/GUID-E9861549-48D2-407F-9E86-3081A546DE5E-low.png)

NOTE:If you close the Properties Inspector palette, you can reopen it by selecting Properties Inspector from the Window menu, by
pressing Command+5, or by typing PROPERTIES.

The Properties Inspector displays a list of all the important property settings. You can click any of the available fields
to change the current settings. In the following example, if no objects are selected, the current color will be changed from
ByLayer to Red. All subsequently created objects will then be assigned the color property Red.

![](../images/GUID-40DD889C-D657-4624-AA0D-068F92A3E70B-low.png)

## All or My Properties

You can switch the Properties Inspector to display all properties for the selected objects, or to display a personalized list
of properties. Set up your personalized list of properties using the Customize My Properties button.

![](../images/GUID-E13569F0-3E10-41E0-9D66-06ED7D3795B8-low.png)

## Verify and Change Object Properties

You can use the Properties Inspector palette to verify and change property settings for selected objects. If you click an
object in your drawing to select it, here is what you might see in the Properties Inspector palette.

![](../images/GUID-E11BF7AD-2A3E-4E80-8C3F-364A5D8E15FF-low.png)

Notice that the current properties for the selected object are displayed in the palette. You can change any of these properties
by clicking and changing the setting. A property that is set to "ByLayer" inherits its setting from the layer. In the previous
example, the objects that were created on the 20 ELECTRICAL layer are purple because that is the default color of the objects
on that layer.

If you select several objects, only their common properties are listed in the palette. If you change one of these properties,
all the selected objects will change in one operation. Selecting objects is covered in more detail in the Modify topic.

NOTE:To clear the current selection, press Esc.

## Match the Properties of Objects

For a fast way to copy the properties of a selected object to other objects, use the Match Properties tool on the toolbar,
or enter MATCHPROP or MA in the Command window.
![](../images/GUID-F83BA1A0-36C4-43E4-B80B-8EF3E0976E54-low.png)

After you click the Match Propetries tool, select the source object, and then select all of the objects that you want to
modify.

## Linetypes

Dashed and other non-continuous linetypes are assigned from the Properties Inspector palette. You must first load a linetype
before you can assign it.

From the Format menu, click Linetype. This action displays the Linetype Manager dialog box.

Perform the following steps:

1. Click +. Choose one or more linetypes that you want to use. Notice that dashed (non-continuous) linetypes come in several
   preset sizes.
2. Specify a different "global scale factor" for all linetypes—the larger the value, the longer the dashes and spaces. Click
   Save.

   ![](../images/GUID-A3F4B33A-E0E7-46E3-AEE7-C28374C5ECD2-low.png)

Once you've loaded the linetypes that you plan to use, you can select any object and specify a linetype from the Properties
palette. Alternatively, you can specify a default linetype for any layer in the Layer Properties Manager.

## Lineweights

The Lineweight property provides a way to display different thicknesses for selected objects. The thickness of the lines remain
constant regardless of the scale of the view. In a layout, lineweights display and print in real-world units.

![](../images/GUID-11A514D0-421E-44B5-972B-538BF07ABB34-low.png)

You can leave the lineweight set to ByLayer, or you can specify a value that overrides the layer's lineweight. In some cases,
the lineweight previews look the same because they are displayed in approximated pixel widths on a monitor.

TIP:It's usually best to leave lineweights turned off while you work. Heavy lineweights can obscure nearby objects when you use
object snaps. You might want to turn them on for checking purposes just before you print.

To control the display of lineweights, use the LWDISPLAY system variable or toggle the Show/Hide Lineweights button on the
status bar.
![](../images/GUID-1181E2DA-4C54-47A5-B32E-D79762F0CE7C-low.png)

Regardless of how the lightweights appear on your monitor, objects always print at the lineweight you specify.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Layers](GUID-3C0294C1-4659-42FF-96E7-A5501CCE7046.htm " Organize your drawing by assigning objects to layers.
")

**Next topic:** [Modify](GUID-C4C6369F-879D-4AF4-93E2-17F2E0DBB171.htm " Perform operations such as erase, move, and trim on the objects in a drawing.
")

#### Related References

* [LINETYPE (Command)](LINETYPE-Command.md)
* [MATCHPROP (Command)](MATCHPROP-Command.md)
* [PROPERTIES (Command)](PROPERTIES-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*