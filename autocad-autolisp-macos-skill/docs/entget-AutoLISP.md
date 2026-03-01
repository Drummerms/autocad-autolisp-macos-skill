# entget (AutoLISP)

Retrieves an object's (entity's) definition data

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entget ename [applist])
```

*ename*
:   *Type:* Ename (entity name)

    Name of the entity being queried. The
    *ename* can refer to either a graphical or a nongraphical entity.

*applist*
:   *Type:* List

    A list of registered application names.

## Return Values

*Type:* Ename (entity name)

An association list containing the entity definition of
*ename*. If you specify the optional
*applist* argument,
entget also returns the extended data associated with the specified applications. Objects in the list are assigned AutoCAD DXF™
group codes for each part of the entity data.

Note that the DXF group codes used by AutoLISP differ slightly from the group codes in a DXF file.

## Examples

Assume that the last object created in the drawing is a line drawn from point (1,2) to point (6,5). The following example
shows code that retrieves the entity name of the last object with the
entlast function, and passes that name to
entget:

```
(entget (entlast))
((-1 . <Entity name: 1bbd1d0>) (0 . "LINE") (330 . <Entity name: 1bbd0c8>)
(5 . "6A") (100 . "AcDbEntity") (67 . 0) (410 . "Model") (8 . "0") (100 . "AcDbLine")
(10 1.0 2.0 0.0) (11 6.0 5.0 0.0) (210 0.0 0.0 1.0))
```

#### Related References

* [entmod (AutoLISP)](entmod-AutoLISP.md)
* [entlast (AutoLISP)](entlast-AutoLISP.md)
* [entnext (AutoLISP)](entnext-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*