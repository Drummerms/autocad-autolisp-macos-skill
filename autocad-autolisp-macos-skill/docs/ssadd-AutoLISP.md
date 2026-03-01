# ssadd (AutoLISP)

Adds an object (entity) to a selection set, or creates a new selection set

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssadd [ename [ss]])
```

*ename*
:   *Type:* Ename (entity name)

    An entity name.

*ss*
:   *Type:* Pickset (selection set)

    A selection set.

## Return Values

*Type:* Pickset (selection set) or nil

The modified selection set passed as the second argument, if successful; otherwise
nil.

## Remarks

If called with no arguments,
ssadd constructs a new selection set with no members. If called with the single entity name argument
*ename*,
ssadd constructs a new selection set containing that single entity. If called with an entity name and the selection set
*ss*,
ssadd adds the named entity to the selection set.

## Examples

When adding an entity to a set, the new entity is added to the existing set, and the set passed as
*ss* is returned as the result. Thus, if the set is assigned to other variables, they also reflect the addition. If the named
entity is already in the set, the
ssadd operation is ignored and no error is reported.

Set
e1 to the name of the first entity in drawing:

```
(setq e1 (entnext))
<Entity name: 1d62d60>
```

Set
ss to a null selection set:

```
(setq ss (ssadd))
<Selection set: 2>
```

The following command adds the
e1 entity to the selection set referenced by
ss:

```
(ssadd e1 ss)
<Selection set: 2>
```

Get the entity following
e1:

```
(setq e2 (entnext e1))
<Entity name: 1d62d68>
```

Add
e2 to the
ss entity:

```
(ssadd e2 ss)
<Selection set: 2>
```

#### Related References

* [ssdel (AutoLISP)](ssdel-AutoLISP.md)
* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssmemb (AutoLISP)](ssmemb-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*