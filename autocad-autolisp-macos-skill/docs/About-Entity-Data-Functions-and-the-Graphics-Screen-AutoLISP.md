# About Entity Data Functions and the Graphics Screen (AutoLISP)

Changes to the drawing made by the entity data functions are reflected on the graphics screen, provided the entity being deleted,
undeleted, modified, or created is in an area and on a layer that is currently visible.

There is one exception; when
entmod modifies a subentity, it does not update the image of the entire (complex) entity. If, for example, an application modifies
100 vertices of a "legacy" 2D polyline with 100 calls to
entmod, the time required to recalculate and redisplay the entire polyline is unacceptably slow. Instead, an application can perform
a series of subentity modifications, and then redisplay the entire entity with a single call to the
entupd function.

Consider the following; if the first entity in the current drawing is lightweight polyline with several vertices, the following
code modifies the second vertex of the polyline and regenerates its display.

```
(setq e1 (entnext))    ; Sets e1 to the polyline's entity name.
(setq v1 (entnext e1)) ; Sets v1 to its first vertex.
(setq v2 (entnext v1)) ; Sets v2 to its second vertex.
(setq v2d (entget v2)) ; Sets v2d to the vertex data.
(setq v2d
  (subst
    '(10 1.0 2.0 0.0)
    (assoc 10 v2d)     ; Changes the vertex's location in v2d
    v2d                ; to point (1,2,0).
  )
)
(entmod v2d)           ; Moves the vertex in the drawing.
(entupd e1)            ; Regenerates the polyline entity e1.
```

The argument to
entupd can specify either a main entity or a subentity. In either case,
entupd regenerates the entire entity. Although its primary use is for complex entities,
entupd can regenerate any entity in the current drawing.

NOTE:To ensure that all instances of the block references are updated, you must regenerate the drawing by invoking the AutoCAD
REGEN command (with
command). The
entupd function is not sufficient if the modified entity is in a block definition.

#### Related Concepts

* [About Entity Context and Coordinate Transform Data (AutoLISP)](About-Entity-Context-and-Coordinate-Transform-Data-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)
* [About Entity Data Functions and the Graphics Screen (AutoLISP)](About-Entity-Data-Functions-and-the-Graphics-Screen-AutoLISP.md)
* [About Entity Handles and Their Uses (AutoLISP)](About-Entity-Handles-and-Their-Uses-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*