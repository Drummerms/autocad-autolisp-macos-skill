# About Adding an Entity without Using the Command Function (AutoLISP)

An application can add an entity to the drawing database by calling the
entmake function.

Like that of
entmod, the argument to
entmake is a list whose format is similar to that returned by
entget. The new entity that the list describes is appended to the drawing database (it becomes the last entity in the drawing).
If the entity is a complex entity (a block, polyface mesh, or "legacy" polyline), it is not appended to the database until
it is complete.

The following example code creates a circle on the MYLAYER layer:

```
(entmake '((0 . "CIRCLE") ; Object type
  (8 . "MYLAYER")         ; Layer
  (10 5.0 7.0 0.0)        ; Center point
  (40 . 1.0)              ; Radius
))
```

The following
entmake restrictions apply to all entities:

* The first or second member in the list must specify the entity type. The type must be a valid DXF group code. If the first
  member does not specify the type, it can specify only the name of the entity: group -1 (the name is not saved in the database).
* AutoCAD must recognize all objects that the entity list refers to. There is one exception:
  entmake accepts new layer names.
* Any internal fields passed to
  entmake are ignored.
* entmake cannot create viewport entities.

For entity types introduced in AutoCAD Release 13 and later releases, you must also specify subclass markers (DXF group code
100) when creating the entity. All AutoCAD entities have the AcDbEntity subclass marker, and this must be explicitly included
in the
entmake list. In addition, one or more subclass marker entries are required to identify the specific sub-entity type. These entries
must follow group code 0 and must precede group codes that are specifically used to define entity properties in the
entmake list. For example, the following is the minimum code required to create a MTEXT entity with
entmake:

```
(entmake '(
  (0 . "MTEXT")
  (100 . "AcDbEntity") ; Required for all post-R12 entities.
  (8 . "ALAYER")
  (100 . "AcDbMText")  ; Identifies the entity as MTEXT.
  (10 4.0 4.0 0.0)
  (1 . "Some\\Ptext")
))
```

The following table identifies the entities that do not require subentity marker entries in the list passed to
entmake:

| DXF names of entities introduced prior to AutoCAD Release 13 | |
| 3DFACE | ARC |
| ATTDEF | ATTRIB |
| CIRCLE | DIMENSION |
| INSERT | LINE |
| POINT | POLYLINE ("legacy" 2D and 3D) |
| SEQEND | SHAPE |
| SOLID | TEXT |
| VERTEX | VIEWPORT |

The
entmake function verifies that a valid layer name, linetype name, and color are supplied. If a new layer name is introduced,
entmake automatically creates the new layer. Objects created on a frozen layer are not regenerated until the layer is thawed. The
entmake function also checks for block names, dimension style names, text style names, and shape names, if the entity type requires
them. The function fails if it cannot create valid entities.

#### Related Concepts

* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Deleting an Entity (AutoLISP)](About-Deleting-an-Entity-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*