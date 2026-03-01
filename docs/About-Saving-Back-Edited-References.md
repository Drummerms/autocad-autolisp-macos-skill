# About Saving Back Edited References

While editing a referenced drawing or a block definition in place, you can save back or discard changes.

While editing a block reference in place, you either can *save back* or discard changes made to the reference. If you save back changes to a reference, the drawing is regenerated.

When the changes are saved back, the block definition is redefined and all instances of the block are regenerated to reflect
the changes. If you choose to discard the changes, the working set is deleted and the block reference returns to its original
state.

Similarly, while editing an xref in place, you can save back or discard changes. Objects in the working set that inherit properties
not originally defined in the xref retain those new properties. For example, an xref contains layers A, B, and C, and the
drawing that references it contains layer D. If new objects are drawn on layer D during in-place reference editing and changes
are saved back to the reference, layer D is copied to the xref drawing.

If you remove objects from the working set and save changes, the objects are removed from the reference and added to the
current drawing. Any changes you make to objects in the current drawing (not in the xref or block) are not discarded. If you
delete any object that is not in the working set, the object is not restored even if you choose to discard changes. You can
return the drawing to its original state by using UNDO. If you make unwanted changes to an xref and use REFCLOSE to save back
the changes, you must use UNDO to undo any changes made during the reference editing session. After you have undone any unwanted
changes, use REFCLOSE to save changes to restore the xref file to its original state.

IMPORTANT: While editing a reference in place, if you delete an object that is not in the working set, the object is not restored if
you discard changes at the closing of the reference editing session.

Objects in the current drawing that inherit properties defined by the xref retain those new properties. Properties taken
from the xref drawing are bound to the current drawing. The xref layer named SITE, for example, appears in the current drawing
as $#$SITE when assigned to an object not in the working set.

If BINDTYPE is set to 0, a prefix of $#$ is added to the reference name in the current drawing. If BINDTYPE is set to 1, reference
names remain unchanged in the current drawing, similar to names of inserted objects. (Not available in AutoCAD LT)

NOTE: When you edit and save an xref in place, the original drawing preview is no longer available unless you open and save the
referenced drawing.

#### Related Information

* [Edit a Referenced Drawing in a Separate Window](Edit-a-Referenced-Drawing-in-a-Separate-Window.md)
* [About Editing Selected Objects in Referenced Drawings and Blocks](About-Editing-Selected-Objects-in-Referenced-Drawings-and-Blocks.md)
* [To Save Back Changes](To-Save-Back-Changes.md)
* [To Discard all Changes](To-Discard-all-Changes.md)
* [About Editing Referenced Drawings and Blocks With Nesting or Attributes](About-Editing-Referenced-Drawings-and-Blocks-With-Nesting-or-Attributes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*