# ssmemb (AutoLISP)

Tests whether an object (entity) is a member of a selection set

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssmemb ename ss)
```

*ename*
:   *Type:* Ename (entity name)

    An entity name.

*ss*
:   *Type:* Pickset (selection set)

    A selection set.

## Return Values

*Type:* Ename (entity name) or nil

If
*ename* is a member of
*ss*,
ssmemb returns the entity name. If
*ename* is not a member,
ssmemb returns
nil.

## Examples

In the following examples, entity name
e2 is a member of selection set
ss, while entity name
e1 is not a member of
ss:

```
(ssmemb e2 ss)
<Entity name: 1d62d68>

(ssmemb e1 ss)
nil
```

#### Related References

* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssadd (AutoLISP)](ssadd-AutoLISP.md)
* [ssdel (AutoLISP)](ssdel-AutoLISP.md)
* [sslength (AutoLISP)](sslength-AutoLISP.md)
* [ssname (AutoLISP)](ssname-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*