# Layers Palette

Displays a list of the layers in the drawing and their properties. You can add, delete, and rename layers, change their properties,
and apply changes in realtime.

LAYER (Command)

*Menu*:
Format
![](../images/ac.menuaro.gif) Layers

![](../images/GUID-18322F09-E3A7-4DE5-AA88-78B138D46FA0-low.png)

## Toolbar

Make Current ![](../images/GUID-F4E69652-F4B8-47E4-ACDC-203F2C9C9910-low.png)
:   Sets the current layer to that of a selected object. (See LAYMCUR command)

Layer Match ![](../images/GUID-BD3247A5-4A0D-4151-B000-B802DC09511D-low.png)
:   Changes the layer of a selected object to match the destination layer. (See LAYMCH command)

Previous Layer ![](../images/GUID-D38211C3-914B-4EAB-A880-AF6BB76C247A-low.png)
:   Undoes the last change or set of changes made to layer settings. (See LAYERP command)

Isolate Layer ![](../images/GUID-77621964-AAA3-4B86-8EAA-DCA17A18C21C-low.png)
:   Hides or locks all layers except those of the selected objects. (See LAYISO command)

Unisolate Layer ![](../images/GUID-BB36F2B2-FE46-40E9-9E5A-D143C822DFFD-low.png)
:   Restores all layers that were hidden or locked with the LAYISO command. (See LAYUNISO command)

Freeze Layer ![](../images/GUID-A85B6AF0-169D-4F7E-B5E9-66D91C34CCF1-low.png)
:   Freezes the layer of selected objects. (See LAYFRZ command)

Layer Off ![](../images/GUID-E9F7CCA6-6783-4D1C-A11B-787098E1D65E-low.png)
:   Turns off the layer of a selected object. (See LAYOFF command)

Lock Layer ![](../images/GUID-BE5FC5DB-6874-4A05-9276-CB3D91E9CFC6-low.png)
:   Locks the layer of a selected object. (See LAYLCK command)

Unlock Layer ![](../images/GUID-7DD8DDF3-44D1-4044-80A4-27F6DAC8534B-low.png)
:   Unlocks the layer of a selected object. (See LAYULK command)

Dock\Float Palette
:   * ![](../images/GUID-E490283A-0592-4286-B5D7-5C473BB4DE5E-low.png) Docks the palette to the right of the drawing area
    * ![](../images/GUID-ED0D56F6-458D-44A3-A482-8B5EF683322E-low.png) Undocks the palette so you can move and resize it

### Layer Drop-down

Displays the current layer and its color, along with some of its common properties. Click the drop-down list to adjust a layer’s
On/Off, Lock/Unlock, or Thaw/Freeze state. You can also select a layer to set it current.

### Layer State Drop-down

Shows the current layer state in the drawing.

Add New Layer State
:   Opens the Add New Layer State dialog to create a new layer state in the drawing.

Manage Layer States
:   Opens the Layer State Manager dialog to manage all the layer states in the drawing.

## Layer List

Modify the layer properties using the layer list. Click the current setting to change the layer property for the selected
layer or group of layers. You can also double-click a layer to set it current.

* *Columns Displayed*. Right-click a column label to select which columns to show.
* *Sort*. Click a column label to sort by that column. Click the arrows at the right end of the Name column label to sort by name
  or color.
* *Column Order*. Drag a column to a new location in the list to change the column order.

Columns

Status (hidden by default)
:   Indicates the status of the layer: layer in use, empty layer, or current layer.

Object Selection (hidden by default) ![](../images/GUID-DF11BFE6-F711-4C57-AD66-A2CBD6264A24-low.png)
:   Indicates if the layer is assigned to an object that is currently selected. Objects must be selected when no command is active.

Visibility ![](../images/GUID-E55CB82A-13D5-461D-8AC0-DB9285D131BD-low.png)
:   Turns the selected layers on and off. When a layer is on, it is visible and available for plotting. When a layer is off, it
    is invisible and not plotted, even if the setting in the Plot column is turned on.

Description (hidden by default) ![](../images/GUID-8297E587-BA68-4507-B728-CD5EB5320599-low.png)
:   (Optional) Describes the layer or the layer filter.

Color ![](../images/GUID-38874068-8B31-4144-9D89-68E1A469B247-low.png)
:   Displays the Select Color dialog box, where you can specify a color for the selected layers.

Name
:   Displays the name of the layer or filter. Press F2 to enter a new name.

Freeze ![](../images/GUID-A9B1C80D-B41F-4B38-84FD-57B512AEF472-low.png)
:   Freezes the selected layers. You can freeze layers to improve performance and reduce regeneration time in complex drawings.
    Objects on frozen layers are not displayed, plotted, or regenerated.

    In drawings that support 3D modeling, frozen layers are not rendered. (Not applicable to AutoCAD LT.)

    TIP:Freeze the layers that you want to remain invisible for long periods. If you plan to switch visibility settings frequently,
    use the On/Off setting to avoid regenerating the drawing.

Lock ![](../images/GUID-CB96AA0D-D441-4970-AC05-80BE10CC05CB-low.png)
:   Locks and unlocks the selected layers. Objects on a locked layer cannot be modified. Objects on locked layers appear faded
    and a small lock icon is displayed when you hover over the object.

    NOTE:Use LAYLOCKFADECTL to set the fade level for locked layers to see which objects are on locked layers.

Lineweight (hidden by default) ![](../images/GUID-CA49D514-D534-4B0D-B576-ACF9C6A2144D-low.png)
:   Displays the lineweight associated with the layer. Clicking the lineweight name displays a drop-down list with the available
    lineweights.

Linetype (hidden by default) ![](../images/GUID-140AB2D4-3F4F-4349-8A0B-5A8C540959D5-low.png)
:   Displays the linetype associated with the layer. Clicking the linetype name displays a drop-down list with the loaded linetypes.
    Choose Manage at the bottom of the drop-down list to display the Select Linetype dialog box.

Transparency (hidden by default) ![](../images/GUID-D4012877-AFCF-4F0D-BDEE-0956A738AD37-low.png)
:   Controls the visibility of all objects on the selected layer. When transparency is applied to individual objects, the objects’
    transparency property overrides the transparency setting of the layer. Drag the slider to adjust the transparency of objects
    on the layer. The higher the value, the more transparent the objects appear.

Plot ![](../images/GUID-DB3872A7-A78B-4B89-8593-8DF03F48FD73-low.png)
:   Controls whether the selected layers are plotted. If you turn off plotting for a layer, the objects on that layer are still
    displayed. Layers that are off or frozen are not plotted, regardless of the Plot setting.

Plot Style (hidden by default) ![](../images/GUID-A2DC0EFA-E3F9-4C05-A0C0-5E08E3D9CF86-low.png)
:   Displays the plot style associated with the layer. If you are working with color-dependent plot styles (the PSTYLEPOLICY system
    variable is set to 1), you cannot change the plot style associated with a layer. Clicking the plot style name displays a drop-down
    list with the available plot styles.

New VP Freeze (hidden by default) ![](../images/GUID-57B18A04-4F9A-4821-AFED-2EDFA3F35368-low.png)
:   Freezes selected layers in new layout viewports. For example, freezing the DIMENSIONS layer in all new viewports restricts
    the display of dimensions in any newly created layout viewports but does not affect the DIMENSIONS layer in existing viewports.
    If you later create a viewport that requires dimensions, you can override the default setting by changing the current viewport
    setting.

VP Freeze (available only from a layout tab) ![](../images/GUID-2DD982BC-8D0E-47F8-87A0-45861FC443C6-low.png)
:   Freezes selected layers only in the current layout viewport. If a layer is already frozen or turned off in the drawing, you
    can't thaw the layer in the current layout viewport.

VP Color (available only from a layout tab) ![](../images/GUID-7E968556-4D48-47BD-886E-F774FC634D65-low.png)
:   Sets an override for the color associated with the selected layer for the current layout viewport.

VP Lineweight (available only from a layout tab) ![](../images/GUID-F3E40D9F-8A03-4CEF-B870-78005D8C1561-low.png)
:   Sets an override for the lineweight associated with the selected layer for the current layout viewport.

VP Linetype (available only from a layout tab) ![](../images/GUID-FD989AB9-43AE-4BC9-9D55-3BC816719151-low.png)
:   Sets an override for the linetype associated with the selected layer for the current layout viewport.

VP Transparency (available only from a layout tab) ![](../images/GUID-4E77E08D-B321-4337-8DE8-D78AEF735C82-low.png)
:   Sets an override for transparency associated with the selected layer for the current layout viewport.

VP Plot Style (available only from a layout tab) ![](../images/GUID-7D86DF0A-5795-4FB6-9A83-C51F09B80E55-low.png)
:   Sets an override for the plot style associated with the selected layer for the current layout viewport. Override settings
    are not visible in the viewport or plotted when the visual style in the drawing is set to Conceptual or Realistic. For color-dependent
    plot styles (the PSTYLEPOLICY system variable is set to 1), you cannot set a plot style override.

Automatic Groups
:   There are layer groups that are created and populated dynamically by the product:

    * *All non-Xref Layers.* Lists all the layers that are not referenced from an xref drawing.
    * *All Used Layers.* Toggles the display of the All Used Layers layer group. This layer group dynamically updates to list all the layers that
      do not currently have any objects on them. (See SHOWALLUSEDLAYERSGROUP system variable)
    * *Xref (External References).* Toggles the display of the Xref layer group. This layer group dynamically updates to list all attached external references
      (xrefs) as nested layer groups and their layers. Show Xref Layers must be enabled before this layer group can be displayed.
      (See SHOWXREFGROUPS system variable)
    * *Layers with Overrides.* Toggles the display of the Viewport Overrides layer group. This layer group dynamically updates to list all the layers in
      the active layout viewport that contain property overrides. (See SHOWVPOVERRIDESGROUP system variable)
    * *Unreconciled Layers.* Toggles the display of the Unreconciled Layers layer group. This layer group dynamically updates to list all the layers that
      have not been reconciled. (See SHOWUNRECONCILEDLAYERSGROUP system variable)
    * *Xref Overrides* Lists all the layers being referenced from an xref drawing that have an xref layer property override.

## Column Label Shortcut Menu

![](../images/GUID-2CBFF7C3-B841-4DE1-81B1-732DEA140167-low.png)

Column Names
:   Lists all columns by name. A check mark indicates that the column is included in the display. Click a column name to display
    or hide the column. VP Freeze, VP Color, VP Linetype, VP Lineweight, and VP Plot Style are available only when a layout viewport
    is active.

Optimize all columns
:   Changes the width of all columns to fit the content in each column.

Optimize column
:   Changes the width of the selected column to fit the content in that column.

Restore All Columns to Defaults
:   Sets all columns to their default display and width settings.

## Layer List Shortcut Menu

![](../images/GUID-CFC5BC03-49CF-4D44-811F-A2714092E13B-low.png)

Make Active
:   Sets the selected layer as the current layer. (See CLAYER system variable)

Layer Status
:   Toggles the Freeze, Lock, Freeze in New Viewports, or Prints layer status of the selected layers. The Isolate option isolates
    the selected layers in the drawing. All layers except those selected, are turned off and locked. (See LAYISO command)

Rename
:   Renames the selected layer.

Delete
:   Deletes the selected layer from the drawing. You can delete only unreferenced layers. Referenced layers include layers 0 and
    DEFPOINTS, layers containing objects (including objects in block definitions), the current layer, and xref-dependent layers.

    NOTE:Be careful about deleting layers if you are working on a drawing in a shared project or one based on a set of layering standards.

Duplicate Layer
:   Creates a new layer based on the selected layer. The new layer inherits all properties and statuses of the selected layer.

Combine with Layer
:   Displays the Choose a Layer dialog box which allows you to merge the selected layers to a specified layer. After the layers
    are merged, the selected layers are removed from the drawing. (See -LAYMRG)

Create Group from Layers
:   Creates a new layer group and adds the selected layers as references of the layer group.

Move to Group
:   Displays the Choose a Group dialog box which allows you to add the selected layers as references to a specified layer group.

Remove from Group
:   Removes the selected layers from the layer group.

Create Group from Similar Layers
:   Displays the New Dynamic Group dialog box and defines a rule for each of the layer's properties. Name the new dynamic group
    or modify the rules for the new dynamic group before creating the dynamic group.

New Layer
:   Creates a new layer. The layer list displays a layer named Layer1. You can edit the name immediately. The new layer inherits
    the properties of the currently selected layer in the layer list (color, on or off state, and so on).

New Group
:   Creates a new layer group. The layer list displays a layer group named Group1. You can edit the name immediately.

New Dynamic Group
:   Displays the New Dynamic Group dialog box and allows you to create a layer group that contains all the layers based on the
    layer properties specified.

Select All Layers
:   Selects all layers displayed in the list view.

Select All Others
:   Selects all other layers in the list view except the currently selected layers.

## Group Item Shortcut Menu

![](../images/GUID-FB707CF9-FF14-4DFB-BEA7-BF08C8B7A360-low.png)

Edit Group (Applies to dynamic layer groups only)
:   Displays the New Dynamic Group dialog box and allows you to modify the groups rules.

Group Layer Status
:   Toggles the Visibility, Freeze, or Lock, Freeze in New Viewports, or Prints layer status of the selected layers. The Isolate
    option isolates the selected layers in the drawing. All layers except those selected, are turned off and locked. (See LAYISO
    command)

Rename Group
:   Renames the selected layer group.

Delete Group
:   Deletes the selected layer group. You have the option to delete just the layer group, or the layer group and the layers that
    the group references.

    The GROUPLAYERDELETABLE system variable controls the removal behavior of layers referenced by a layer group when it is being
    deleted.

Hide Group (Automatic Groups Only)
:   Hides the selected layer group. You can show the group by selecting it from the Show Automatic Groups menu.

Duplicate Group
:   Creates a new layer group based on the selected layer group. The new layer group inherits the references to all the layers
    of the selected layer group.

Merge Group Layers
:   Displays the Choose a Layer dialog box which allows you to merge the layers in the selected layer group to a specified layer.
    After the layers are merged, the selected layers are removed from the drawing. (See -LAYMRG command)

Convert to Group
:   Creates a layer group from the selected dynamic layer group. When new layers are added or changed, they are no longer automatically
    added to or removed from the group based on their properties.

New Layer
:   Creates a new layer. The layer list displays a layer named Layer1. You can edit the name immediately. The new layer inherits
    the properties of the currently selected layer in the layer list (color, on or off state, and so on).

New Group
:   Creates a new layer group. The layer list displays a layer group named Group1. You can edit the name immediately.

New Dynamic Group
:   Displays the New Dynamic Group dialog box and allows you to create a layer group that contains all the layers based on the
    layer properties specified.

Select Layers in Group
:   Selects all the layers in the selected layer group.

## Lower Toolbar

New Layer ![](../images/GUID-2CC1DBEF-E888-44B1-BBD5-07888B19861F-low.png)
:   Creates a new layer. The layer list displays a layer named Layer1. You can edit the name immediately. The new layer inherits
    the properties of the currently selected layer in the layer list (color, on or off state, and so on).

Layer State Manager ![](../images/GUID-1D9D9AEF-5A48-4737-90D7-C893D5D6E5C8-low.png)
:   Opens the Layer State Manager dialog to manage all the layer states in the drawing.

New Layer Group ![](../images/GUID-5963E3EF-3620-44E6-9AA4-275E4AA64C46-low.png)
:   Creates a new layer group. The layer list displays a layer group named Group1. You can edit the name immediately.

New Dynamic Layer Group ![](../images/GUID-D9114AF8-1E29-4EB2-A792-3CBA6B97BB97-low.png)
:   Displays the New Dynamic Group dialog box and allows you to create a layer group that contains all the layers based on the
    layer properties specified.

Delete Selected ![](../images/GUID-17FEE52D-E18F-406E-8BCC-677EA9E10A25-low.png)
:   Deletes the selected layers or layer groups.

    You can delete only unreferenced layers. Referenced layers include layers 0 and DEFPOINTS, layers containing objects (including
    objects in block definitions), the current layer, and xref-dependent layers.

    NOTE:Be careful about deleting layers or layer groups if you are working on a drawing in a shared project or one based on a set
    of layering standards.

### Display Settings ![](../images/GUID-D0F44214-20A7-43A5-8272-D84C13778068-low.png)

Displays a menu of options that controls the display of layer groups, layers, and column headers in the Layer list.

Show Layer Groups
:   Toggles the display of all layer groups. (See SHOWGROUPS system variable)

    * *Show Groups on Top.* Displays all layer groups sorted at the top of the Layer list. (See GROUPSONTOP system variable)
    * *Show Groups on Bottom.* Displays all layer groups sorted at the bottom of the Layer list. (See GROUPSONTOP system variable)

Show Empty Groups
:   Toggles the display of empty layer groups. (See SHOWEMPTYGROUPS system variable)

Show Xref Layers
:   Toggles the display of all layers in attached external references (xrefs). (See SHOWXREFLAYERS system variable)

Show Automatic Groups
:   Toggles the display of layer groups that are created and populated dynamically by the product.

View Options
:   Toggles the display of the column headings, and provides options to automatically adjust the size of all or the selected column
    to its maximum width in the Layer list.

### Search for Layer

Filters the Layer list by name quickly as you enter characters. This filter is not saved when you close the Layers palette.

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)

#### Related References

* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Layers](About-Layers.md)

#### Related Information

* [Select Linetype Dialog Box](Select-Linetype-Dialog-Box.md)
* [Color Palette Dialog Box](Color-Palette-Dialog-Box.md)
* [Choose a Layer Dialog Box](Choose-a-Layer-Dialog-Box.md)
* [Choose a Group Dialog Box](Choose-a-Group-Dialog-Box.md)
* [New Dynamic Group Dialog Box](New-Dynamic-Group-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*