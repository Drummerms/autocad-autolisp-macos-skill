# -REFEDIT (Command)

Edits an xref or a block definition directly within the current drawing.

## List of Prompts

The following prompts are displayed.

Select reference: *Select an xref or block in the current drawing*

Select nesting level [OK/Next] <Next>: *Enter an option or press* Enter

OK

Accepts the currently highlighted reference for in-place reference editing.

If you are editing a block reference with attributes, you can enter *y* to display the attribute definitions and make them available for editing. The attributes are made invisible, and the attribute
definitions are available for editing along with the selected reference geometry. When changes are saved back to the block
reference, the attributes of the original reference remain unchanged. The new or altered attribute definitions affect only
subsequent insertions of the block; the attributes in existing block instances are not affected.

All
:   Objects in the selected reference will be automatically included in the reference editing session.

Nested
:   After you close the Reference Edit dialog box and enter the reference edit state, you are prompted to select the specific
    objects in the reference that you want to edit.

Next

Advances through the reference and nested references available for selection. The currently selected reference is highlighted.

A working set is formed with the objects you have selected for editing. The working set includes objects that can be saved
back to update the xref or block definition. When you save back changes, changes made to the objects in the reference file
are saved without actually opening the reference drawing or recreating the block. The working set is visually distinct from
the rest of the current drawing: all objects in the current drawing, except objects in the working set, appear faded. The
[XFADECTL](XFADECTL-System-Variable.md) system variable controls the fading of objects while you edit a reference in place.

You can select objects in xrefs for editing even if they are on a locked layer in the reference file. When a reference object
is part of the working set, you can unlock the object's layer and make changes to the object. Only the changes made to the
object are saved back to the reference file; the xref layer remains locked in the reference file.

NOTE:

Objects outside of the working set are not faded unless the visual style is set to 2D Wireframe during in-place reference
editing.

#### Related References

* [REFEDIT (Command)](REFEDIT-Command.md)

#### Related Concepts

* [About Editing Selected Objects in Referenced Drawings and Blocks](About-Editing-Selected-Objects-in-Referenced-Drawings-and-Blocks.md)
* [Reference Edit Dialog Box](Reference-Edit-Dialog-Box.md)
* [Reference Editor Visor](Reference-Editor-Visor.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*