# handent (AutoLISP)

Returns an object (entity) name based on its handle

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(handent handle)
```

*handle*
:   *Type:* String

    A string identifying an entity handle.

## Return Values

*Type:* Ename (entity name) or nil

If successful,
handent returns the entity name associated with
*handle* in the current editing session. If
handent is passed an invalid handle or a handle not used by any entity in the current drawing, it returns
nil.

The
handent function returns entities that have been deleted during the current editing session. You can undelete them with the
entdel function.

An entity's name can change from one editing session to the next, but an entity's handle remains constant.

## Remarks

The
handent function returns the entity name of both graphic and nongraphical entities.

## Examples

```
(handent "5A2")
<Entity name: 60004722>
```

Used with the same drawing but in another editing session, the same call might return a different entity name. Once the entity
name is obtained, you can use it to manipulate the entity with any of the entity-related functions.

#### Related References

* [entsel (AutoLISP)](entsel-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*