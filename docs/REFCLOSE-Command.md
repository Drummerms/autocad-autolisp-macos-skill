# REFCLOSE (Command)

Saves back or discards changes made during in-place editing of a reference, either an xref or a block definition.

## Access Methods

![](../images/ac.mouse.gif) Toolbar: Reference Editor visor ![](../images/ac.menuaro.gif) Save

![](../images/ac.mouse.gif) Toolbar: Reference Editor visor ![](../images/ac.menuaro.gif) Discard Changes

## Summary

If you save or discard changes with REFCLOSE, you can still use the
[UNDO](UNDO-Command.md) command to return to the reference editing session. If you have made unwanted changes to an xref and already saved back the
changes, use UNDO to undo the unwanted changes; then use REFCLOSE to save back changes and restore the xref to its original
state.

NOTE:When you edit and save xrefs in place in a drawing, the preview image for the original reference drawing is no longer available
unless you open and save the drawing again.

## List of Prompts

The following prompts are displayed.

Enter option [Save/Discard reference changes] <Save>:

Save
:   Saves back to the xref source drawing or to the block definition in the current drawing all changes made to objects in the
    working set. If you remove an object from the working set and save changes, the object is deleted from the reference and added
    to the current drawing.

    NOTE:If the file format of the xref source drawing is AutoCAD Release 14 or earlier, the file is saved in AutoCAD 2010 file format.
    The file format is not changed for xref source drawings in AutoCAD 2000 or later formats.

Discard Reference Changes
:   Discards the working set; the source drawing or block definition is returned to its original state. Any changes you make to
    objects in the current drawing (not in the xref or block) are not discarded. If you delete any object that is not in the working
    set, the object is not restored even if you choose to discard changes.

#### Related Concepts

* [About Saving Back Edited References](About-Saving-Back-Edited-References.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*