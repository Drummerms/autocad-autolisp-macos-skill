# About Arbitrary Handles (DXF)

Arbitrary handles are distinct in that they are not translated to session-persistent identifiers internally, or to entity
names in AutoLISP, and so on. They are stored as handles. When handle values are translated in drawing-merge operations, arbitrary
handles are ignored.

In all environments, arbitrary handles can be exchanged for entity names of the current drawing by means of the  *handent*  functions. A common usage of arbitrary handles is to refer to objects in external DXF and DWG files.

#### Related References

* [Persistent Inter-Object Reference Handles (DXF)](Persistent-Inter-Object-Reference-Handles-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*