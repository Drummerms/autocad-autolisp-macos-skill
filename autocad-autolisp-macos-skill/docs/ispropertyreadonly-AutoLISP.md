# ispropertyreadonly (AutoLISP)

Returns the read-only state of an entity’s property

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(ispropertyreadonly ename propertyname [or collectionName index name])
```

*ename*
:   *Type:* Ename (entity name)

    Name of the entity being queried. The
    *ename* can refer to either a graphical or a non-graphical entity.

*propertyname*
:   *Type:* String

    Name of the property being queried. For a list of all the valid property names of a given object, use
    dumpallproperties.

*collectionName*
:   *Type:* String

    If the object is a collection object, the Collection name is passed here.

*index*
:   *Type:* Integer

    The collection index being queried.

*name*
:   *Type:* String

    The name of the property within the collection being queried.

## Return Values

*Type:* Integer

1 is returned when the property is read-only; otherwise, 0 is returned when the property is writable.

## Examples

The following example demonstrates how to check the read-only state of the Radius and Area properties of a circle.

```
(setq e1 (car (entsel "\
Select an arc or circle: ")))
<Entity name: 10e2e4ba0>

(ispropertyreadonly e1 "Radius")
0

(ispropertyreadonly e1 "Area")
1
```

#### Related References

* [dumpallproperties (AutoLISP)](dumpallproperties-AutoLISP.md)
* [getpropertyvalue (AutoLISP)](getpropertyvalue-AutoLISP.md)
* [setpropertyvalue (AutoLISP)](setpropertyvalue-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*