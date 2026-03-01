# VPLAYER (Command)

Sets layer visibility within viewports.

## List of Prompts

The following prompts are displayed.

In the Model layout, only two options are available: Newfrz and Vpvisdflt.

### ?—List Frozen Layers

Displays the names of frozen layers in a selected viewport.

### Color

Changes the color associated with a layer.

True Color
:   Specifies a true color to use for the selected object.

Color Book
:   Specifies a color from a loaded color book to use for the selected object.

All
:   Applies the changes in all viewports.

Select
:   Applies the changes in selected viewports.

Current
:   Applies the changes in the current viewport only.

Except Current
:   Applies the changes to all viewports across all layouts except the current viewport.

### Ltype

Changes the linetype associated with a layer.

* All
* Select
* Current
* Except Current

### Lweight

Changes the lineweight associated with a layer.

If you enter a lineweight that is not valid, the current lineweight is set to the nearest fixed lineweight value.

If you want to plot an object with a custom width not found in the list of fixed lineweight values, you can use the Plot Style
Table Editor to customize plotted lineweights.

* All
* Select
* Current
* Except Current

### Pstyle

Sets the plot style assigned to a layer. This option is not available if you are using color-dependent plot styles in the
current drawing (the PSTYLEPOLICY system variable is set to 1).

* All
* Select
* Current
* Except Current

### Transparency

Changes the transparency level associated with a layer.

* All
* Select
* Current
* Except Current

### Freeze

Freezes a layer or set of layers in one or more viewports. Objects on frozen layers are not displayed, regenerated, or plotted.

* All
* Select
* Current
* Except Current

### Thaw

Thaws layers in specific viewports.

* All
* Select
* Current
* Except Current

### Reset

Sets the visibility of layers in specified viewports to their current default setting.

* All
* Select
* Current
* Except Current

### Removeoverrides

Removes specific viewport layer property overrides for selected layers, or all overrides.

* All
* Select
* Current
* Except Current

### Newfrz (New Freeze)

Creates new layers that are frozen in all viewports.

### Vpvisdflt (Viewport Visibility Default)

Thaws or freezes the specified layers in subsequently created viewports.

#### Related Concepts

* [About Overriding Layer Properties in a Layout Viewport](About-Overriding-Layer-Properties-in-a-Layout-Viewport.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*