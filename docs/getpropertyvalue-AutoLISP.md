# getpropertyvalue (AutoLISP)

Returns the current value of an entity’s property

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(getpropertyvalue ename propertyname [or collectionName index name])
```

*ename*
:   *Type:* Ename (entity name)

    Name of the entity being queried. The
    *ename* can refer to either a graphical or a nongraphical entity.

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

*Type:* Integer, Real, String, List, T, or nil

The value of the entity’s property.

## Examples

The following example demonstrates how to get the current radius value of a circle.

```
(command "_circle" "2,2" 2)
nil

(getpropertyvalue (entlast) "radius")
2.0
```

#### Related References

* [dumpallproperties (AutoLISP)](dumpallproperties-AutoLISP.md)
* [ispropertyreadonly (AutoLISP)](ispropertyreadonly-AutoLISP.md)
* [setpropertyvalue (AutoLISP)](setpropertyvalue-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*