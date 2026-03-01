# About Editing Selected Objects in Referenced Drawings and Blocks

You can modify external references and redefine block definitions from within the current drawing by using in-place reference
editing. Both blocks and xrefs are considered references.

By editing the reference in place, you can modify the reference within the visual context of your current drawing.

Often, a drawing contains one or more xrefs as well as multiple block references. When working with block references, you
can select a block, modify it, view and edit its properties, and update the block definition.

When working with xrefs, you can select the reference you want to work with, modify its objects, and save back the changes
to the reference drawing. You can make minor changes without having to go back and forth between drawings.

TIP:You can quickly copy one or more selected objects nested within a referenced drawing or a block into the current drawing with
the NCOPY command.

## Understand the Working Set

The objects that you select from the selected xref or block are temporarily extracted and made available for editing in the
current drawing. The set of extracted objects is called the *working set*, which can be modified and then saved back to update the xref or block definition.

Objects that make up the working set are visually distinct from other objects in the drawing. All objects in the current drawing,
except objects in the working set, are faded.

## Control the Fading of Objects

The XFADECTL system variable controls how objects are displayed while a reference is edited in place. The set of objects
extracted from the reference are displayed normally. All other objects in the drawing, including objects in the current drawing
and in any references not belonging to the working set, are faded. The value indicates the intensity of display for objects
not in the working set. The larger the value is for XFADECTL, the more the objects are faded.

![](../images/GUID-4F884DCC-EE1F-442C-9C2D-21F34FD02FFB-low.png)

NOTE:Objects outside the working set are not faded during in-place reference editing unless VSCURRENT is set to a value of 2D wireframe.

## Reference Editor Visor

The Reference Editor visor is displayed and activated after you select which nested objects to edit. Using the buttons on
the Reference Editor visor, you can add objects to or remove objects from the working set, and you can discard or save back
changes to the reference. The Reference Editor visor is automatically dismissed after you save back or discard changes made
to the working set.

NOTE:If you plan to make major changes to a reference, open the reference drawing and edit directly within the file. Using in-place
reference editing to make major changes can increase the size of your current drawing file significantly during the in-place
reference editing session.

#### Related Concepts

* [About Saving Back Edited References](About-Saving-Back-Edited-References.md)

#### Related Information

* [Edit a Referenced Drawing in a Separate Window](Edit-a-Referenced-Drawing-in-a-Separate-Window.md)
* [To Edit Xref or Block References in Place](To-Edit-Xref-or-Block-References-in-Place.md)
* [About Using the Working Set to Edit References](About-Using-the-Working-Set-to-Edit-References.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*