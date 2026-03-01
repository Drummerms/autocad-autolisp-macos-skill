# entupd (AutoLISP)

Updates the screen image of an object (entity)

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entupd ename)
```

*ename*
:   *Type:* Ename (entity name)

    The name of the entity to be updated on the screen.

## Return Values

*Type:* Ename (entity name) or nil

The updated entity; otherwise
nil, if nothing was updated.

## Remarks

When a "legacy" polyline vertex or block attribute is modified with
entmod, the entire complex entity is not updated on the screen. The
entupd function can be used to cause a modified polyline or block to be updated on the screen. This function can be called with
the entity name of any part of the polyline or block; it need not be the head entity. While
entupd is intended for polylines and blocks with attributes, it can be called for any entity. It always regenerates the entity on
the screen, including all subentities.

NOTE:If
entupd is used on a nested entity (an entity within a block) or on a block that contains nested entities, some of the entities might
not be regenerated. To ensure complete regeneration, you must invoke the AutoCAD REGEN command.

## Examples

Assuming that the first entity in the drawing is a 3D polyline with several vertices, the following code modifies and redisplays
the polyline:

```
(setq e1 (entnext))       ; Sets e1 to the polyline's entity name
(setq e2 (entnext e1))    ; Sets e2 to its first vertex
(setq ed (entget e2))     ; Sets ed to the vertex data
(setq ed
  (subst '(10 1.0 2.0)
    (assoc 10 ed)         ; Changes the vertex's location in ed
    ed                    ; to point (1,2)
  )
)
(entmod ed)               ; Moves the vertex in the drawing
(entupd e1)               ; Regenerates the polyline entity e1
```

#### Related References

* [entmod (AutoLISP)](entmod-AutoLISP.md)
* [entget (AutoLISP)](entget-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*