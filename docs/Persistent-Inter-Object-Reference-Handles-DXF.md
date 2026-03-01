# Persistent Inter-Object Reference Handles (DXF)

A set of group code ranges permits objects to directly specify references to other objects within the same drawing/DXF file.
Four ranges are provided for the four types of reference handles that you can specify:

* Soft-pointer handle
* Hard-pointer handle
* Soft-owner handle
* Hard-owner handle

These handle types are manifested as entity names in AutoLISP ® , as ads\_name values in ObjectARX ®  and as like-named classes derived from ObjectARX. These values are always maintained in insert, xref, and wblock operations
such that references between objects in a set being copied are updated to point to the copied objects, while references to
other objects remain unchanged.

Also, a group code range for “arbitrary” handles is defined to allow convenient storage of handle values that are not converted
to entity names and then translated in insert, xref, or wblock.

NOTE: If you use 1005 xdata group codes to store handles, they are treated as soft-pointer handles, which means that when groups
of objects are copied or inserted into another drawing, references between the involved objects are translated. Although 1005
xdata items are always returned as handles in AutoLISP and ObjectARX, all of the reference handle group code ranges are represented
as “entity names” in AutoLISP and as ads\_name structures in ObjectARX.

#### Topics in this section

* [Pointer and Ownership References (DXF)](Pointer-and-Ownership-References-DXF.md)
* [About Hard and Soft References (DXF)](About-Hard-and-Soft-References-DXF.md)
* [About Arbitrary Handles (DXF)](About-Arbitrary-Handles-DXF.md)
* [About 1005 Group Codes (DXF)](About-1005-Group-Codes-DXF.md)

#### Related References

* [About Advanced DXF Issues (DXF)](About-Advanced-DXF-Issues-DXF.md)
* [Pointer and Ownership References (DXF)](Pointer-and-Ownership-References-DXF.md)
* [About Hard and Soft References (DXF)](About-Hard-and-Soft-References-DXF.md)
* [About Arbitrary Handles (DXF)](About-Arbitrary-Handles-DXF.md)
* [About 1005 Group Codes (DXF)](About-1005-Group-Codes-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*