# dictnext (AutoLISP)

Finds the next item in a dictionary

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(dictnext ename [rewind])
```

Arguments

*ename*
:   *Type:* Ename (entity name)

    Name of the dictionary being viewed.

*rewind*
:   *Type:* T or nil

    If this argument is present and is not
    nil, the dictionary is rewound and the first entry in it is retrieved.

## Return Values

*Type:* Ename (entity name)

The next entry in the specified dictionary; otherwise
nil, when the end of the dictionary is reached. Entries are returned as lists of dotted pairs of DXF-type codes and values. Deleted
dictionary entries are not returned.

The
dictsearch function specifies the initial entry retrieved.

Use
namedobjdict to obtain the master dictionary entity name.

NOTE:Once you begin stepping through the contents of a dictionary, passing a different dictionary name to
dictnext will cause the place to be lost in the original dictionary. In other words, only one global iterator is maintained for use
in this function.

## Examples

Create a dictionary and an entry as shown in the example for
dictadd. Then make another Xrecord object:

```
(setq xname (entmakex datalist))
<Entity name: 1b62d60>
```

Add this Xrecord object to the dictionary, as the second record in the dictionary:

```
(dictadd newdict "DATA_RECORD_2" xname)
<Entity name: 1b62d60>
```

Return the entity name of the next entry in the dictionary:

```
(cdr (car (dictnext newdict)))
<Entity name: 1bac958>
```

dictnext returns the name of the first entity added to the dictionary.

Return the entity name of the next entry in the dictionary:

```
(cdr (car (dictnext newdict)))
<Entity name: 1bac960>
```

dictnext returns the name of the second entity added to the dictionary.

Return the entity name of the next entry in the dictionary:

```
(cdr (car (dictnext newdict)))
nil
```

There are no more entries in the dictionary, so
dictnext returns
nil.

Rewind to the first entry in the dictionary and return the entity name of that entry:

```
(cdr (car (dictnext newdict T)))
<Entity name: 1bac958>
```

Specifying
T for the optional
*rewind* argument causes
dictnext to return the first entry in the dictionary.

#### Related References

* [dictsearch (AutoLISP)](dictsearch-AutoLISP.md)
* [dictadd (AutoLISP)](dictadd-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*