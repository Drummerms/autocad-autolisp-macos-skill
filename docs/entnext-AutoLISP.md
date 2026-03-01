# entnext (AutoLISP)

Returns the name of the next object (entity) in the drawing

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entnext [ename])
```

*ename*
:   *Type:* Ename (entity name)

    The name of an existing entity.

## Return Values

*Type:* Ename (entity name) or nil

If
entnext is called with no arguments, it returns the entity name of the first nondeleted entity in the database. If an
*ename* argument is supplied to
entnext, the function returns the entity name of the first nondeleted entity following
*ename* in the database. If there is no next entity in the database, it returns
nil. The
entnext function returns both main entities and subentities.

## Examples

```
(setq e1 (entnext))    ; Sets e1 to the name of the first entity in  the  drawing

(setq e2 (entnext e1)) ; Sets e2 to the name of the entity following e1
```

NOTE:The entities selected by
ssget are main entities, not attributes of blocks or vertices of polylines. You can access the internal structure of these complex
entities by walking through the subentities with
entnext. Once you obtain a subentity's name, you can operate on it like any other entity. If you obtain the name of a subentity with
entnext, you can find the parent entity by stepping forward with
entnext until a seqend entity is found, then extracting the -2 group from that entity, which is the main entity's name.

#### Related References

* [entget (AutoLISP)](entget-AutoLISP.md)
* [entlast (AutoLISP)](entlast-AutoLISP.md)
* [entsel (AutoLISP)](entsel-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*