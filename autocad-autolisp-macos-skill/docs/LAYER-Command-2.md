# -LAYER (Command)

Manages layers and layer properties.

## List of Prompts

The following prompts are displayed.

?—List Layers

Displays a list of the currently defined layers, showing their names, states, color numbers, linetypes, lineweights, and whether
they are externally dependent layers.

Make

Creates a layer and makes it current. New objects are drawn on the current layer.

If no layer exists for the name you enter, a new layer with that name is created. The new layer is on and assumes the following
properties by default: color number 7, the CONTINUOUS linetype, and a lineweight of DEFAULT.

If the layer exists but is turned off, it is turned on.

Set

Specifies a new current layer but does not create the layer if it does not already exist. If the layer exists but is turned
off, it is turned on and made current. A frozen layer cannot be made current.

New

Creates layers. You can create two or more layers by entering names separated by commas.

Rename

Renames an existing layer.

On

Makes selected layers visible and available for plotting.

Off

Makes selected layers invisible and excludes them from plotting.

Color

Changes the color associated with a layer. Enter a color name or a number from 1 through 255.

True Color
:   Specifies a true color to be used for the selected object. Enter three integer values from 0 to 255 separated by commas to
    specify a true color.

Color Book
:   Specifies a color from a loaded color book, guide, or set to use for the selected object. Enter the name of a color book that
    has been installed, such as "DIC COLOR GUIDE(R)$DIC 43".

The color is assigned to the layer or layers, and the layers are turned on. To assign a color but turn off the layer, precede
the color with a minus sign (-).

Ltype

Changes the linetype associated with a layer.

Lweight

Changes the lineweight associated with a layer.

If you enter a valid lineweight, the current lineweight is set to the new value. If you enter a lineweight that is not valid,
the current lineweight is set to the nearest fixed lineweight value. If you would like to plot an object with a custom width
not found in the list of fixed lineweight values, you can use the Plot Style Table Editor to customize plotted lineweights.

Transparency

Changes the transparency level associated with a layer. Enter a value from 0 to 90.

After specifying a transparency value, the following prompt is displayed:

Enter name list of layer(s) for transparency
*specified value%* <*0*>:
*Enter the names of the layers to which to apply this transparency level, or press*Enter *to apply it to the current layer only*

Material

Attaches a material to a layer. The material must be available in the drawing before it can be assigned to a layer.

Plot

Controls whether visible layers are plotted. If a layer is set to plot but is currently frozen or turned off, the layer is
not plotted.

Pstyle

Sets the plot style assigned to a layer.

NOTE: The Pstyle option is available only when you are using named plot styles. (The PSTYLEPOLCY system variable is set to 0.)

If you select a plot style other than NORMAL, the following prompt is displayed:

Enter name list of layer(s) for plot style
*current* <*current*>:
*Enter the names of the layers to use this plot style, or press*Enter *to apply the style to the current layer only*

Freeze

Freezes layers, making them invisible and excluding them from regeneration and plotting.

Thaw

Thaws frozen layers, making them visible and available for regeneration and plotting.

Lock

Locks layers, preventing editing of objects on those layers.

Unlock

Unlocks selected locked layers, permitting editing of objects on those layers.

State

Saves and restores the state and property settings of the layers in a drawing.

?—List Named Layer States
:   Lists the named layer state (LAS) files in the support path for the drawing.

Save
:   Saves the state and properties settings of the layers in a drawing under a specified layer state name. When saving a layer
    state, you specify which layer settings are affected when the layer state is later restored.

Restore
:   Restores the state and property settings of all layers to previously saved settings. Restores only those layer state and property
    settings that were selected when the layer state was saved.

Edit
:   Changes the saved layer settings for a specified layer state. When the layer state is restored, the specified settings are
    used.

Name
:   Changes the name of a saved layer state.

Delete
:   Removes a saved layer state.

Import
:   Loads a previously exported layer state (LAS) file, or layers states from a file (DWG, DWT) into the current drawing. Additional
    layers may be created as a result of importing a layer state file.

Export
:   Saves a selected named layer state to a layer state (LAS) file.

Description

Sets the description property value of the existing layer.

A warning prompt is displayed when you enter a description to a layer with an existing description.

Reconcile

Sets the unreconciled property of an unreconciled layer.

? - Name List of Layers
:   Displays a list of all unreconciled layers.

Xref

Resets the xref layer property override in the current drawing to the layer settings in the xref.

Enter an option:
:   Enter the name of the xref layer property that you want to reset. You can select the appropriate xref layer property (or all
    properties) you want to reset from this list:

    * On
    * Color
    * Linetype
    * Lineweight
    * Transparency
    * Plot
    * Freeze
    * Lock
    * New VP Freeze
    * Description
    * All

    After specifying the xref layer property or all properties, the following prompt is displayed:

Enter xref layer name(s) to reset or [?] or <\*>:
:   Enter the names of the xref layer (or multiple layers separated by comma) to reset, or press Enter to reset all xref layers.

? - Name List of Xref Layers
:   Displays a list of all xref layer names.

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)
* [To Work with the Layer List in the Layers Palette](To-Work-with-the-Layer-List-in-the-Layers-Palette.md)

#### Related References

* [LAYER (Command)](LAYER-Command.md)
* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Layers](About-Layers.md)

#### Related Information

* [Layers Palette](Layers-Palette.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*