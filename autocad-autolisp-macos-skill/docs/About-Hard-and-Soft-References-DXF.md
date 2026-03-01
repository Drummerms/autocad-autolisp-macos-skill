# About Hard and Soft References (DXF)

Hard references, whether they are pointer or owner, protect an object from being purged. Soft references do not.

In the
AutoCAD program, block definitions and complex entities are hard owners of their elements. A symbol table and dictionaries are soft
owners of their elements. Polyline entities are hard owners of their vertex and seqend entities. Insert entities are hard
owners of their attrib and seqend entities.

When establishing a reference to another object, it is recommended that you think about whether the reference should protect
an object from the PURGE command.

#### Related References

* [Persistent Inter-Object Reference Handles (DXF)](Persistent-Inter-Object-Reference-Handles-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*