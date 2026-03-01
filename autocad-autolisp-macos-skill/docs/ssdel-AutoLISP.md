# ssdel (AutoLISP)

Deletes an object (entity) from a selection set

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssdel ename ss)
```

*ename*
:   *Type:* Ename (entity name)

    An entity name.

*ss*
:   *Type:* Pickset (selection set)

    A selection set.

## Return Values

*Type:* Pickset (selection set) or nil

The name of the selection set; otherwise
nil, if the specified entity is not in the set.

Note that the entity is actually deleted from the existing selection set, as opposed to a new set being returned with the
element deleted.

## Examples

In the following examples, entity name
e1 is a member of selection set
ss, while entity name
e3 is not a member of
ss:

```
(ssdel e1 ss)
<Selection set: 2>
```

Selection set
ss is returned with entity
e1 removed.

```
(ssdel e3 ss)
nil
```

The function returns
nil because
e3 is not a member of selection set
ss.

#### Related References

* [ssadd (AutoLISP)](ssadd-AutoLISP.md)
* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssmemb (AutoLISP)](ssmemb-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*