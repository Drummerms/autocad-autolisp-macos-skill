# ssname (AutoLISP)

Returns the object (entity) name of the indexed element of a selection set

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssname ss index)
```

*ss*
:   *Type:* Pickset (selection set)

    A selection set.

*index*
:   *Type:* Integer or Real

    Element in a selection set. The first element in the set has an index of zero. To access entities beyond number 32,767 in
    a selection set, you must supply the
    *index* argument as a real.

## Return Values

*Type:* Ename (entity name) or nil

An entity name, if successful. If
*index* is negative or greater than the highest-numbered entity in the selection set,
ssname returns
nil.

## Remarks

Entity names in selection sets obtained with
ssget are always names of main entities. Subentities (attributes and polyline vertices) are not returned. (The
entnext function allows access to them.)

## Examples

Get the name of the first entity in a selection set:

```
(setq ent1 (ssname ss 0))
<Entity name: 1d62d68>
```

Get the name of the fourth entity in a selection set:

```
(setq ent4 (ssname ss 3))
<Entity name: 1d62d90>
```

To access entities beyond the number 32,767 in a selection set, you must supply the
*index* argument as a real, as in the following example:

```
(setq entx (ssname sset 50843.0))
```

#### Related References

* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [sslength (AutoLISP)](sslength-AutoLISP.md)
* [ssmemb (AutoLISP)](ssmemb-AutoLISP.md)
* [ssnamex (AutoLISP)](ssnamex-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*