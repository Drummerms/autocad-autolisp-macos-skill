# entdel (AutoLISP)

Deletes objects (entities) or restores previously deleted objects

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entdel ename)
```

*ename*
:   *Type:* Ename (entity name)

    Name of the entity to be deleted or restored.

## Return Values

*Type:* Ename (entity name)

The entity name.

## Remarks

The entity specified by
*ename* is deleted if it is currently in the drawing. The
entdel function restores the entity to the drawing if it has been deleted previously in this editing session. Deleted entities are
purged from the drawing when the drawing is exited. The
entdel function can delete both graphical and nongraphical entities.

The
entdel function operates only on main entities. Attributes and polyline vertices cannot be deleted independently of their parent
entities. You can use the
command function to operate the AutoCAD ATTEDIT or PEDIT commands to modify subentities.

You cannot delete entities within a block definition. However, you can completely redefine a block definition, minus the entity
you want deleted, with
entmake.

## Examples

Get the name of the first entity in the drawing and assign it to variable
e1:

```
(setq e1 (entnext))
<Entity name: 2c90520>
```

Delete the entity named by e1:

```
(entdel e1)
<Entity name: 2c90520>
```

Restore the entity named by e1:

```
(entdel e1) <Entity name: 2c90520>
```

#### Related References

* [entget (AutoLISP)](entget-AutoLISP.md)
* [entlast (AutoLISP)](entlast-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*