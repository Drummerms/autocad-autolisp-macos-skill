# To Work with Layers

Create, rename, and remove layers. Set the current layer. Change layer properties such as color, linetype, lineweight, and
transparency.

Use the Layers palette to work with layers.

* Click
  Format menu ![](../images/ac.menuaro.gif) Layers.

NOTE:You can also work with individual layers and their properties using the Properties Inspector.

## Create a Layer

1. In the Layers palette, click New Layer.
   ![](../images/GUID-CEBE5841-1D07-48FA-8123-EDA50623F353-low.png)

   A layer name is added to the layer list.
2. Enter a new layer name by typing over the highlighted layer name.
   * Layer names can be up to 255 characters long (double-byte or alphanumeric), and include letters, numbers, spaces, and several
     special characters.
   * Layer names cannot include the following characters: < > / \ “ : ; ? \* | = ‘
3. For complex drawings with many layers, enter descriptive text in the Description field on the Properties Inspector.
4. Specify the settings and default properties of the new layer on the Properties Inspector.

## Rename a Layer

1. In the Layers palette, click to select a layer.
2. Right-click and select Rename.
3. Enter a new name.

## Remove a Layer

1. In the Layers palette, click to select a layer.
2. Right-click and select Delete.

The following layers cannot be deleted:

* Layers 0 and Defpoints
* Layers containing objects, including objects in block definitions
* The current layer
* Layers used in an external reference

NOTE:To remove all unused layers, use PURGE.

## Set the Current Layer

1. In the Layers palette, click to select a layer.
2. Right-click and select Make Active.

## Change the Properties Assigned to Layers

1. If you want to change multiple layers, use one of the following methods in the Layers palette:
   * Press and hold Command, and choose several layer names.
   * Press and hold Shift, and choose the first and last layers in a range.
2. Click the current setting on the layer list that you want to change.
3. Choose the setting that you want to use.

When changing layer properties:

* If the linetype you want is not displayed, click Manage, click Load and use one of the following methods:
  + In the Load or Reload Linetypes dialog box, choose the linetypes to load.
  + In the Load or Reload Linetypes dialog box, click
    ![](../images/GUID-FA2468C9-2B7D-4763-9BF7-DBD1A219BC27-low.png) to open an additional linetype definition (LIN) file. Choose the linetypes to load and click OK.
* Lineweights are not displayed automatically. If you want to display or hide lineweights, click Show/Hide Lineweight on the
  status bar.
  ![](../images/GUID-26EA4A54-9253-40F4-A7F4-77AB88591803-low.png)

  If no change is visible, it's probably due to a combination of the thickness of the line compared to the display resolution
  of your monitor.
* Transparency is not displayed automatically. If you want to display or hide the transparency of objects, click Show/Hide Transparency
  on the status bar.
  ![](../images/GUID-A526A335-632F-4F88-8883-3C658B28A0F2-low.png)

NOTE:The properties that you choose are used for all objects on the layer that have a
*ByLayer* setting for that property.

#### Related Tasks

* [To Work with the Layer List in the Layers Palette](To-Work-with-the-Layer-List-in-the-Layers-Palette.md)
* [To Change the Visibility of Layers](To-Change-the-Visibility-of-Layers.md)
* [To Lock or Unlock a Layer](To-Lock-or-Unlock-a-Layer.md)
* [To Purge All Unused Layers](To-Purge-All-Unused-Layers.md)

#### Related References

* [Layers Palette](Layers-Palette.md)
* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Layers](About-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*