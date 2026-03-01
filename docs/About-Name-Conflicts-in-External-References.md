# About Name Conflicts in External References

When you attach an xref, the names of its blocks, dimension styles, layers, linetypes, and text styles are differentiated
from those in the current drawing.

A typical xref definition includes objects, such as lines or arcs. It also includes xref-dependent definitions of blocks,
dimension styles, layers, linetypes, and text styles. When you attach an xref, the program differentiates the names of these
xref-dependent named objects from those in the current drawing by preceding their names with the name of the referenced drawing
and a vertical bar character ( | ). For example, the xref-dependent named object that is a layer named STEEL in a referenced
drawing called *stair.dwg* is listed as STAIR|STEEL.

When you attach an xref, the definitions of its dependent named objects are not added to your drawing permanently. Instead,
these definitions are loaded from the referenced drawing file each time you reload it.

## Bind Xref-Dependent Definitions

An xref-dependent named object's definition can change if the referenced drawing file is modified. For example, a layer name
from a referenced drawing can change if the referenced drawing is modified. The layer name can even disappear if it is purged
from the referenced drawing. This is why the program does not allow you to use an xref-dependent layer or other named object
directly. For example, you cannot insert an xref-dependent block or make an xref-dependent layer the current layer and begin
creating new objects on it.

To avoid the restrictions on xref-dependent named objects, you can bind them to your current drawing. Binding makes the xref-dependent
named objects that you select become a permanent part of your current drawing.

When xref-dependent named objects are merged into a drawing through binding, you can use them the same way you use the drawing's
own named objects. After you bind an xref-dependent named object, the vertical bar character ( | ) is removed from the name
and replaced with two dollar signs ($$) separated by a number (usually zero): for example, the referenced layer, STAIR|STEEL,
becomes STAIR$0$STEEL. You can then use the RENAME command to change STAIR$0$STEEL to STEEL.

If you specify a layer whose associated linetype is not CONTINUOUS, the referenced linetype is also bound. If you apply XBIND
to a block, all named objects that are referenced by the objects in the block are also bound. If the block contains a reference
to an xref, that xref and all of its dependent definitions are bound.

#### Related Concepts

* [About Logging External Reference Operations](About-Logging-External-Reference-Operations.md)

#### Related Information

* [About Missing or Circular External References](About-Missing-or-Circular-External-References.md)
* [To Bind Xref-dependent Named Objects to the Current Drawing](To-Bind-Xref-dependent-Named-Objects-to-the-Current-Drawing.md)
* [To Rename Named Objects](To-Rename-Named-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*