# About Modifying an Entity without the Command Function (AutoLISP)

An entity can be modified directly by changing its entity list and posting the changes back to the database.

The entmod function modifies an entity by passing it a list in the same format as a list returned by entget but with some of the entity group code values (presumably) modified by the application. This function complements entget. The primary mechanism by which an AutoLISP application updates the database is by retrieving an entity with entget, modifying its entity list, and then passing the list back to the database with entmod.

The following example code retrieves the definition data of the first entity in the drawing and changes its layer property
to MYLAYER.

```
(setq en (entnext))         ; Sets en to first entity name in the drawing.
(setq ed (entget en))       ; Sets ed to the entity data for entity name en.
(setq ed
  (subst (cons 8 "MYLAYER")
    (assoc 8 ed)            ; Changes the layer group in ed.
    ed                      ; to layer MYLAYER.
  )
)
(entmod ed)                 ; Modifies entity en's layer in the drawing.
```

There are restrictions on the changes to the database that entmod can make; entmod cannot change the following:

* The entity's type or handle.
* Internal fields. (Internal fields are the values that AutoCAD assigns to certain group codes: -2, entity name reference; -1,
  entity name; 5, entity handle.) Any attempt to change an internal field—for example, the main entity name in a Seqend subentity
  (group code -2)—is ignored.
* Viewport entities. An attempt to change a viewport entity causes an error.

Other restrictions apply when modifying dimensions and hatch patterns.

AutoCAD must recognize all objects (except layers) that the entity list refers to. The name of any text style, linetype,
shape, or block that appears in an entity list must be defined in the current drawing before the entity list is passed to
entmod. The one exception is that entmod accepts new layer names. If the entity list refers to a layer name that has not been defined in the current drawing, entmod creates a new layer. The attributes of the new layer are the standard default values used by the New option of the AutoCAD
LAYER command.

The entmod function can modify subentities such as polyline vertices and block attributes. If you use entmod to modify an entity in a block definition, this affects all references to that block which exist in model space and paper
space. Attributes, unless defined as constant, are not updated for each block reference that exists in a drawing. Also, entities
in block definitions cannot be deleted by entdel.

#### Related Concepts

* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)
* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Deleting an Entity (AutoLISP)](About-Deleting-an-Entity-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*