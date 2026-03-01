# About Object and Entity Codes (DXF)

In the DXF™ format, the definition of objects differs from entities: objects have no graphical representation and entities
do. For example, dictionaries are objects, and not entities. Entities are also referred to as
*graphical objects* while objects are referred to as
*nongraphical objects*.

Entities appear in both the BLOCK and ENTITIES sections of the DXF file. The use of group codes in the two sections is identical.

Some group codes that define an entity always appear; others are optional and appear only if their values differ from the
defaults.

Do not write programs that rely on the order given here. The end of an entity is indicated by the next 0 group, which begins
the next entity or indicates the end of the section.

NOTE:Accommodating DXF files from future releases of
AutoCAD ®  will be easier if you write your DXF processing program in a table-driven way, ignore undefined group codes, and make no
assumptions about the order of group codes in an entity. With each new
AutoCAD release, new group codes will be added to entities to accommodate additional features.

#### Related Concepts

* [About the DXF Format (DXF)](About-the-DXF-Format-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*