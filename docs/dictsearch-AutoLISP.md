# dictsearch (AutoLISP)

Searches a dictionary for an item

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(dictsearch ename symbol [setnext])
```

*ename*
:   *Type:* Ename (entity name)

    Name of the dictionary being searched.

*symbol*
:   *Type:* String

    A string that specifies the item to be searched for within the dictionary.

*setnext*
:   *Type:* T or nil

    If present and not
    nil, the
    dictnext entry counter is adjusted so the following
    dictnext call returns the entry after the one returned by this
    dictsearch call.

## Return Values

*Type:* List or nil

The entry for the specified item, if successful; otherwise
nil, if no entry is found.

## Examples

The following example illustrates the use of
dictsearch to obtain the dictionary added in the
dictadd example:

```
(setq newdictlist (dictsearch (namedobjdict) "my_way_cool_dictionary"))
((-1 . <Entity name: 1d98950>) (0 . "DICTIONARY") (5 . "52") (102 . "{ACAD_REACTORS")
(330 . <Entity name: 1d98860>) (102 . "}") (330 . <Entity name: 1d98860>)
(100 . "AcDbDictionary") (280 . 0) (281 . 1) (3 . "DATA_RECORD_1") (350 . <Entity name: 1d98958>))
```

#### Related References

* [dictnext (AutoLISP)](dictnext-AutoLISP.md)
* [dictadd (AutoLISP)](dictadd-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*