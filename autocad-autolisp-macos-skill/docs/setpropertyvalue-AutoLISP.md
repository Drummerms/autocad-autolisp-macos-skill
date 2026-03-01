# setpropertyvalue (AutoLISP)

Sets the property value for an entity

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(setpropertyvalue ename propertyname value [or collectionName index name val])
```

*ename*
:   *Type:* Ename (entity name)

    Name of the entity being modified. The
    *ename* can refer to either a graphical or a non-graphical entity.

*propertyname*
:   *Type:* String

    Name of the property to be modified. For a list of all the valid property names of a given object, use
    dumpallproperties.

*value*
:   *Type:* Integer, Real, String, List, T, or nil

    Value to set the property to when the object is not a collection.

*collectionName*
:   *Type:* String

    If the object is a collection object, the Collection name is passed here.

*index*
:   *Type:* Integer

    The collection index to be modified.

*name*
:   *Type:* String

    Name of the property in the collection to be modified.

*val*
:   *Type:* Integer, Real, String, List, T, or nil

    Value to set the property to.

## Return Values

*Type:* nil

nil is returned unless an error occurs when the property value is being updated.

## Examples

The following example demonstrates how to change the radius of a circle.

```
(command "._circle" "2,2" 2)
nil

(setpropertyvalue (entlast) "radius" 3)
nil
```

The following example demonstrates how to apply overrides to a linear dimension.

```
(command "._dimlinear" "2,2" "5,4" "3,3")
nil

(setq e2 (entlast))
<Entity name: 10e2e4bd0>

(setpropertyvalue e2 "Dimtfill" 2)
nil

(setpropertyvalue e2 "Dimtfillclr" "2")
nil

(setpropertyvalue e2 "Dimclrt" "255,0,0")
nil
```

The following example demonstrates how to change the first vertex of the Vertices collection.

```
(command "._pline" "0,0" "3,3" "5,2" "")
nil

(setq e3 (entlast))
<Entity name: 10e2e4da0>

(setpropertyvalue e3 "Vertices" 0 "EndWidth" 1.0)
nil
```

#### Related References

* [dumpallproperties (AutoLISP)](dumpallproperties-AutoLISP.md)
* [getpropertyvalue (AutoLISP)](getpropertyvalue-AutoLISP.md)
* [ispropertyreadonly (AutoLISP)](ispropertyreadonly-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*