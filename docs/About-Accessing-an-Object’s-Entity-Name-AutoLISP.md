# About Accessing an Object’s Entity Name (AutoLISP)

An AutoLISP routine must obtain an object’s entity name to make subsequent calls to the entity data or selection set functions.

The entsel and nentsel functions prompt the user to interactively select an object in the drawing area and return not only the selected object’s
entity name but additional information for the routine's use. The entsel function returns both the entity name of the object selected and the center of the pick box when the pointer button on the
input device was clicked.

Some entity operations require knowledge of the point by which the object was selected. Examples from the set of existing
AutoCAD commands include: BREAK, TRIM, and EXTEND. The nentsel function returns the same information as the entsel function, except when a complex is selected such as a polyline or block. Both these functions accept keywords if they are
preceded by a call to initget.

The entnext function retrieves entity names sequentially. If entnext is called with no arguments, it returns the name of the first entity in the drawing database. If its argument is the name
of an entity in the current drawing, entnext returns the name of the succeeding entity.

The entlast function retrieves the name of the last entity in the database. The last entity is the most recently created main entity,
so entlast can be called to obtain the name of an entity that has just been created with a call to command.

You can set the entity name returned by entnext to the same variable name passed to this function. This “walks” a single entity name variable through the database, as shown
in the following example code:

```
(setq one_ent (entnext))         ; Gets name of first entity.
(while one_ent
..
                                 ; Processes new entity.
.
(setq one_ent (entnext one_ent))
)                                ; Value of one_ent is now nil.
```

The following example code illustrates how ssadd can be used in conjunction with entnext to create selection sets and add members to an existing set.

```
(setq e1 (entnext))
(if (not e1)                           ; Sets e1 to name of first entity.
  (princ "\
No entities in drawing. ")
  (progn
    (setq ss (ssadd))                  ; Sets ss to a null selection set.
    (ssadd e1 ss)                      ; Returns selection set ss with e1 added.
    (setq e2 (entnext e1))             ; Gets entity following e1.
    (ssadd e2 ss)                      ; Adds e2 to selection set ss.
  )
)
```

#### Topics in this section

* [About Entity Context and Coordinate Transform Data (AutoLISP)](About-Entity-Context-and-Coordinate-Transform-Data-AutoLISP.md)

  The nentsel and nentselp functions are similar to entsel, except they return two additional values to handle entities nested
  within block references.

#### Related Concepts

* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)
* [About Entity Context and Coordinate Transform Data (AutoLISP)](About-Entity-Context-and-Coordinate-Transform-Data-AutoLISP.md)
* [About Entity Data Functions and the Graphics Screen (AutoLISP)](About-Entity-Data-Functions-and-the-Graphics-Screen-AutoLISP.md)
* [About Entity Handles and Their Uses (AutoLISP)](About-Entity-Handles-and-Their-Uses-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*