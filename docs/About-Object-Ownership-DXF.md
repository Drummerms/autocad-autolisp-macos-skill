# About Object Ownership (DXF)

The root owner of most objects appearing in the OBJECTS section is the named object dictionary, which is, therefore, always
the first object that appears in this section. Objects that are not owned by the named object dictionary are owned by other
entities, objects, or symbol table entries. Objects in this section may be defined by
AutoCAD ®  or by applications with access to ObjectARX ®  API. The DXF names of application-defined object types should always be associated with a class name in the CLASS section
of the DXF file, or else the object record cannot be bound to the application that will interpret it.

As with other dictionaries, the named-object dictionary record consists solely of associated pairs of entry names and hard
ownership pointer references to the associated object.

To avoid name collision between objects, developers should always use their registered developer prefix for their entries.

#### Related References

* [About OBJECT Section Group Codes (DXF)](About-OBJECT-Section-Group-Codes-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*