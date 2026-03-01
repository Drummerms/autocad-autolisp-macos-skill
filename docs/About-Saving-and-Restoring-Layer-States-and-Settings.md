# About Saving and Restoring Layer States and Settings

You can save your current layer settings as a *layer state* that you can quickly restore later.

## Save Layer Settings

The layer settings that you can save and restore include the settings assigned to each layer such as color and linetype,
as well as whether the layer is turned off, frozen, or locked.

Using the Edit Layer State dialog box, you can modify the settings of each layer saved in a layer state. You can also add
and remove layers to a layer state. For example, if new layers were added since the layer state was saved, you can add them,
specify their settings, and then close the layer state dialog box.

IMPORTANT:The Save button in the Layer States Manager is used only when you want to save the *current* layer settings to the *current* layer state. Normally, when you create a layer state, it is automatically saved and you need only to close the dialog box.

## Restore Layer Settings

When you restore a layer state, the layer settings that were current when the layer state was saved are used. However, the
Layer States Manager also lets you specify which layer settings to restore. For example, you can choose to restore only the
Frozen/Thawed setting of the layers in a drawing, ignoring all other settings saved in the layer state.

Special cases when restoring layer states are handled as follows:

* When restoring a layer state, the layer that was current when the layer state was saved is made current. If that layer no
  longer exists, the current layer does not change.
* By default, if the drawing contains layers that were added after a layer state was saved, the new layers are turned off when
  the layer state is restored. The intent of this setting is to preserve the visual appearance of the drawing at the time that
  the layer state was saved.
* The following rules apply if you restore a layer state when the current viewport is a *layout* viewport and the Layer State Manager option, Visibility in Current VP, is turned on:
  + Layers that should be turned off or frozen in the layout viewport are set to VP Freeze
  + Layers that should be visible in the layout viewport are also turned on and thawed in model space

## Restore Property Override Settings in Layout Viewports

When the Apply Properties as Viewport Overrides option is selected in the Layer States Manager, property overrides are restored
to the layout viewport that is current at the time the layer state is restored. Property overrides in layout viewports are
saved only for the *current* layout viewport, and are restored only to the *current* layout viewport.

When a layer state is saved in model space and is restored in paper space, the following rules apply:

* You can choose whether color, linetype, lineweight, transparency, or plot style settings are restored as viewport overrides.
* Viewport overrides are applied to the current layout viewport.
* Layers that were turned off or frozen in model space are set to VP Freeze in the Layer Properties Manager for the current
  layout viewport.

When a layer state is saved in paper space and is restored in model space, the following rules apply:

* Layer property overrides for the *current* layout viewport are restored globally as layer properties in model space.
* Layers that were frozen in the *current* layout viewport are also frozen globally in model space.

## Apply Layer States in Xrefs

When a drawing that contains saved layer states is referenced in another drawing, the list of xref layer states are displayed
in the Layer States Manager.

The names of xref layer states include the referenced drawing’s name separated by two underscore characters using the format,
*Xref Name\_\_Layer State Name*. When the xref is bound to the referencing drawing, the two underscore characters are replaced by $0$ using the format, *Xref Name$0$Layer State Name*.

The following rules apply to layer states in xref drawings:

* The layer states from xrefs cannot be edited in the Layer States Manager.
* Xref layers can be included in new layer states defined in the referencing drawing.
* Layer states from nested xrefs are also displayed in the Layer States Manager.
* Layer states from xrefs are removed from the referencing drawing when the xref is detached or unloaded.

#### Related Tasks

* [To Work With Layer States](To-Work-With-Layer-States.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*