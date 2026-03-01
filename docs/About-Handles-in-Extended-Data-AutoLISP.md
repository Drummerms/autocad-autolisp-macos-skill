# About Handles in Extended Data (AutoLISP)

Extended data can contain handles (dxf group code 1005) to save relational structures within a drawing.

This allows you to build relationships between two or more entities by saving the handle of one object to another objects’s
xdata. The handle can be retrieved later from the xdata and passed to handent to obtain the other entity. Because more than one entity can reference another, handles in xdata might not necessarily be
unique. The AutoCAD AUDIT command does require that handles in extended data either be NULL or valid entity handles (within the current drawing). The best way to ensure that xdata entity handles are valid is to obtain
a referenced entity's handle directly from its definition data by means of entget. The handle value is in dxf group code 5.

When you reference entities in other drawings (for example, entities that are attached with AutoCAD XREF command), you can
avoid protests from the AutoCAD AUDIT command by using extended entity strings (dxf group code 1000) rather than handles (dxf
group code 1005). The handles of cross-referenced entities are either not valid in the current drawing, or they conflict with
valid handles. However, if an xref attachment changes to a bound xref or is combined with the current drawing in some other
way, it is up to the application to revise the entity references accordingly.

When drawings are combined by means of INSERT, INSERT\*, or XREF Bind (XBIND), or partial DXFIN, handles are translated so
they become valid in the current drawing. (If the incoming drawing did not employ handles, new ones are assigned.) Extended
entity handles that refer to incoming entities are also translated when these commands are invoked.

When an entity is placed in a block definition (with the AutoCAD BLOCK command), the entity within the block is assigned new
handles. (If the original entity is restored by means of the AutoCAD OOPS command, it retains its original handles.) The value
of any xdata handles remains unchanged. When a block is exploded (with the AutoCAD EXPLODE command), xdata handles are translated
in a manner similar to the way they are translated when drawings are combined. If the xdata handle refers to an entity that
is not within the block, it is unchanged. However, if the xdata handle refers to an entity that is within the block, the data
handle is assigned the value of the new (exploded) entity's handle.

#### Related Concepts

* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)
* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [About Management of Extended Data Memory Use (AutoLISP)](About-Management-of-Extended-Data-Memory-Use-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*