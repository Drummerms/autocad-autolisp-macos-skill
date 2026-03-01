# tblnext (AutoLISP)

Finds the next item in a symbol table

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(tblnext table-name [rewind])
```

*table-name*
:   *Type:* String

    Symbol table name.

    Valid
    *table-name* values are:

    * "APPID"
    * "BLOCK"
    * "DIMSTYLE"
    * "LAYER"
    * "LTYPE"
    * "STYLE"
    * "UCS"
    * "VIEW"
    * "VPORT"

    The argument is not case sensitive.

*rewind*
:   *Type:* T or nil

    If this argument is present and is not
    nil, the symbol table is rewound and the first entry in it is retrieved.

## Return Values

*Type:* List or nil

If a symbol table entry is found, the entry is returned as a list of dotted pairs of DXF-type codes and values. If there are
no more entries in the table,
nil is returned. Deleted table entries are never returned.

## Remarks

When
tblnext is used repeatedly, it normally returns the next entry in the specified table each time. The
tblsearch function can set the
*next* entry to be retrieved. If the
*rewind* argument is present and is not
nil, the symbol table is rewound and the first entry in it is retrieved.

## Examples

Retrieve the first layer in the symbol table:

```
(tblnext "layer" T)
((0 . "LAYER") (2 . "0") (70 . 0) (62 . 7) (6 . "CONTINUOUS"))
```

The return values represent the following:

```
(0 . "LAYER")               Symbol type
(2 . "0")                   Symbol name
(70 . 0)                    Flags
(62 . 7)                    Color number, negative if off
(6 . "CONTINUOUS")          Linetype name
```

Note that there is no -1 group. The last entry returned from each table is stored, and the next one is returned each time
tblnext is called for that table. When you begin scanning a table, be sure to supply a non-nil second argument to rewind the table and to return the first entry.

Entries retrieved from the block table include a -2 group with the entity name of the first entity in the block definition
(if any). For example, the following command obtains information about a block called BOX:

```
(tblnext "block")
((0 . "BLOCK") (2 . "BOX") (70 . 0) (10 9.0 2.0 0.0) (-2 . <Entity name: 1dca370>))
```

The return values represent the following:

```
(0 . "BLOCK")                    Symbol type
(2 . "BOX")                      Symbol name
(70 . 0)                         Flags
(10 9.0 2.0 0.0)                 Origin X,Y,Z
(-2 . <Entity name: 1dca370>)    First entity
```

The entity name in the -2 group is accepted by
entget and
entnext, but not by other entity access functions. For example, you cannot use
ssadd to put it in a selection set. By providing the -2 group entity name to
entnext, you can scan the entities comprising a block definition;
entnext returns
nil after the last entity in the block definition.

If a block contains no entities, the -2 group returned by
tblnext is the entity name of its endblk entity.

NOTE:The
vports function returns current
VPORT table information; therefore, it may be easier to use
vports as opposed to
tblnext to retrieve this information.

#### Related References

* [tblobjname (AutoLISP)](tblobjname-AutoLISP.md)
* [tblsearch (AutoLISP)](tblsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*