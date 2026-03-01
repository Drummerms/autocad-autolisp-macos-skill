# Reference Edit Dialog Box

Specifies the reference to edit.

REFEDIT (Command)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Edit Xref In-place.

## Summary

To select a reference to edit, select an object in the reference. If you select an object that is part of one or more nested
references, the nested references are displayed in the dialog box.

![](../images/GUID-7310CBF1-1096-4F2F-AC9B-0A0E5BC2E694-low.png)

## List of Options

The following options are displayed.

Select a Reference to Edit

Displays the reference selected for in-place editing and any references nested within the selected reference.

Nested references are displayed only if the selected object is part of a nested reference. If multiple references are displayed,
choose a specific xref or block to modify. Only one reference can be edited in place at a time.

Preview

Displays a preview image of the currently selected reference.

The preview image displays the reference as it was last saved in the drawing. The reference preview image is not updated when
changes are saved back to the reference.

Path

Displays the file location of the selected reference. If the selected reference is a block, no path is displayed.

Nested Objects

Specifies how the selection of nested objects should be handled.

Automatically Select All Nested Objects
:   Controls whether nested objects are included automatically in the reference editing session.

    If this option is checked, all the objects in the selected reference will be automatically included in the reference editing
    session.

Prompt to Select Nested Objects
:   Controls whether nested objects must be selected individually in the reference editing session.

    If this option is checked, after you close the Reference Edit dialog box and enter the reference edit state, you are prompted
    to select the specific objects in the reference that you want to edit.

    Select nested objects:
    *Select objects within the reference that you want to edit*

Settings

Provides options for editing references.

Create Unique Layer, Style, and Block Names
:   Controls whether layers and other named objects extracted from the reference are uniquely altered.

    If selected, named objects in xrefs are altered (names are prefixed with $#$), similar to the way they are altered when you
    bind xrefs. If cleared, the names of layers and other named objects remain the same as in the reference drawing. Named objects
    that are not altered to make them unique assume the properties of those in the current host drawing that share the same name.

Display Attribute Definitions for Editing
:   Controls whether all variable attribute definitions in block references are extracted and displayed during reference editing.

    If Display Attribute Definitions for Editing is selected, the attributes (except constant attributes) are made invisible,
    and the attribute definitions are available for editing along with the selected reference geometry. When changes are saved
    back to the block reference, the attributes of the original reference remain unchanged. The new or altered attribute definitions
    affect only subsequent insertions of the block; the attributes in existing block instances are not affected. Xrefs and block
    references without definitions are not affected by this option.

Lock Objects Not in Working Set
:   Locks all objects not in the working set. This prevents you from accidentally selecting and editing objects in the host drawing
    while in a reference editing state.

    The behavior of locked objects is similar to objects on a locked layer. If you try to edit locked objects, they are filtered
    from the selection set.

#### Related References

* [REFEDIT (Command)](REFEDIT-Command.md)

#### Related Concepts

* [About Editing Selected Objects in Referenced Drawings and Blocks](About-Editing-Selected-Objects-in-Referenced-Drawings-and-Blocks.md)
* [Reference Editor Visor](Reference-Editor-Visor.md)
* [-REFEDIT (Command)](REFEDIT-Command-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*