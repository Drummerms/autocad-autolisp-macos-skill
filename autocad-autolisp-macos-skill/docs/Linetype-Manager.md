# Linetype Manager

Loads linetypes and sets the current linetype.

LINETYPE (Command)

*Menu*:
Format
![](../images/ac.menuaro.gif) Linetype.

![](../images/GUID-1F5602A8-0383-4BBF-B227-C4BC0FA148D3-low.png)

## List of Options

The following options are displayed.

Linetype Filters

Determines which linetypes to display in the linetype list. You can filter linetypes based on whether they are xref-dependent,
or whether they are referenced by objects.

List of Linetypes

Displays the loaded linetypes according to the option specified in Linetype Filters. To quickly select all or clear all linetypes,
right-click in the linetype list to display the shortcut menu.

Current
:   Indicates which linetype is current.

    Double-click a linetype to set it as the current linetype. Setting the current linetype to BYLAYER means that an object assumes
    the linetype that is assigned to a particular layer. Setting the linetype to BYBLOCK means that an object assumes the CONTINUOUS
    linetype until it is grouped into a block. Whenever the block is inserted, all objects inherit the block's linetype. The
    [CELTYPE](CELTYPE-System-Variable.md) system variable stores the linetype name.

Linetype
:   Displays names of loaded linetypes. To rename a linetype, select it and then click it again and enter a new name. BYLAYER,
    BYBLOCK, CONTINUOUS, and xref-dependent linetypes cannot be renamed.

Appearance
:   Displays a sample of selected linetypes.

Description
:   Displays descriptions of the linetypes, which can be edited in the Details area.

Load (+)

Displays the
[Load or Reload Linetypes dialog box](GUID-8B84AA03-B157-4C5D-8B30-AB94C8890B2B.htm#WSC30CD3D5FAA8F6D813D93F4FFC2D60BB4-7FA3), in which you can load into the drawing selected linetypes from the
 *acad.lin*  file and add them to the linetype list.

Delete (-)

Deletes selected linetypes from the drawing. You can delete only unused linetypes. The BYLAYER, BYBLOCK, and CONTINUOUS linetypes
cannot be deleted.

NOTE:Be careful about deleting linetypes if you are working on a drawing in a shared project or one based on a set of layering
standards. The deleted linetype definition remains stored in the
 *acad.lin*  or
 *acadiso.lin*  file and can be reloaded.

Details

Provides alternative access to properties and additional settings.

Name
:   Displays the selected linetype name, which can be edited.

Description
:   Displays the description of the selected linetype, which can be edited.

Global Scale Factor
:   Displays the global scale factor for all linetypes. (LTSCALE system variable)

Current Object Scale
:   Sets linetype scale for newly created objects. The resulting scale is the global scale factor multiplied by the object's scale
    factor. (CELTSCALE system variable)

ISO Pen Width
:   Sets the linetype scale to one of a list of standard ISO values. The resulting scale is the global scale factor multiplied
    by the object's scale factor.

Use Paper Space Units for Scaling
:   Scales linetypes in paper space and model space identically. Useful when working with multiple viewports. (PSLTSCALE system
    variable)

#### Related Tasks

* [To Load a Linetype](To-Load-a-Linetype.md)

#### Related Concepts

* [About Linetypes](About-Linetypes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*