# entlast (AutoLISP)

Returns the name of the last nondeleted main object (entity) in the drawing

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entlast)
```

No arguments.

## Return Values

*Type:* Ename (entity name)

An entity name; otherwise
nil, if there are no entities in the current drawing.

## Remarks

The
entlast function is frequently used to obtain the name of a new entity that has just been added with the
command function. To be selected, the entity need not be on the screen or on a thawed layer.

## Examples

Set variable
e1 to the name of the last entity added to the drawing:

```
(setq e1 (entlast))
<Entity name: 2c90538>
```

If your application requires the name of the last nondeleted entity (main entity or subentity), define a function such as
the following and call it instead of
entlast.

```
(defun lastent (/ a b)
  (if (setq a (entlast))         Gets last main entity
    (while (setq b (entnext a))  If subentities follow, loopsuntil there are no more
      (setq a b)                 subentities
    )
  )
  a                              Returns last main entity
)                                or subentity
```

#### Related References

* [entget (AutoLISP)](entget-AutoLISP.md)
* [entnext (AutoLISP)](entnext-AutoLISP.md)
* [entsel (AutoLISP)](entsel-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*