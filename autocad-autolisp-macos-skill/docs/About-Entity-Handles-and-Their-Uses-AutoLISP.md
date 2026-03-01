# About Entity Handles and Their Uses (AutoLISP)

The handent function retrieves the name of an entity with a specific handle.

As with entity names, handles are unique within a drawing. However, an entity's handle is constant throughout its life. AutoLISP
applications that manipulate a specific database can use handent to obtain the current name of an entity they must use. You can use the AutoCAD LIST command to get the handle of a selected
object.

The following example code uses handent to obtain and display the entity name that is associated with the handle “5a2”.

```
(if (not (setq e1 (handent "5a2")))
  (princ "\
No entity with that handle exists. ")
  (princ e1)
)
```

In one particular editing session, this code might display the following:

```
<Entity name: 60004722>
```

In another editing session with the same drawing, the fragment might display an entirely different number. But in both cases
the code would be accessing the same entity.

The handent function has an additional use. Entities can be deleted from the database with entdel. The entities are not purged until the current drawing ends. This means that handent can recover the names of deleted entities, which can then be restored to the drawing by a second call to entdel.

NOTE:Handles are provided for block definitions, including subentities.

Entities in drawings that are cross-referenced by way of XREF Attach are not actually part of the current drawing; their
handles are unchanged but cannot be accessed by handent. However, when drawings are combined by means of INSERT, INSERT \*, XREF Bind (XBIND), or partial DXFIN, the handles of entities
in the incoming drawing are lost, and incoming entities are assigned new handle values to ensure each handle in the current
drawing remains unique.

#### Related Concepts

* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Entity Context and Coordinate Transform Data (AutoLISP)](About-Entity-Context-and-Coordinate-Transform-Data-AutoLISP.md)
* [About Entity Data Functions and the Graphics Screen (AutoLISP)](About-Entity-Data-Functions-and-the-Graphics-Screen-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*