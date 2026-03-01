# About Using the Working Set to Edit References

To edit a referenced drawing from within the current drawing, you use the *working set* to identify objects that belong to the xref or block definition rather than the current drawing.

While editing a reference in place, you can add or remove objects from the working set. If you create a new object while
editing a reference in place, it is almost always added to the working set automatically. Objects that are not in the working
set are displayed as faded in the drawing.

If a new object is created because of changes made to objects outside the working set, the new object is not added to the
working set. For example, your drawing contains two lines that are not a part of the working set. If you edit the lines by
using FILLET, a new arc is created between the two lines. The arc is not added to the working set.

When a reference object is part of the working set, you can select the object for editing even if it is drawn on a locked
layer in the reference file. You can unlock the object's layer and make changes to the object. Changes made to the object
can be saved, but the layer state remains the same in the reference file, whether it is locked or unlocked.

An object that is removed from the working set is added to the host drawing and removed from the reference when changes are
saved back. An object that is added to the working set is removed from the host drawing, and is restored to the reference
when the changes are saved back.

## Reference Editor Visor

If you select a reference to edit in-place, the Reference Editor visor is displayed. The buttons on the visor (Add to Working
Set, Remove from Working Set, Discard Changes, and Save) are active only during in-place reference editing. The visor is dismissed
automatically after changes made to the reference are saved back or discarded.

#### Related Tasks

* [To Add Objects to the Working set](To-Add-Objects-to-the-Working-set.md)

#### Related Concepts

* [About Saving Back Edited References](About-Saving-Back-Edited-References.md)

#### Related Information

* [Edit a Referenced Drawing in a Separate Window](Edit-a-Referenced-Drawing-in-a-Separate-Window.md)
* [To Remove Objects From the Working set](To-Remove-Objects-From-the-Working-set.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*