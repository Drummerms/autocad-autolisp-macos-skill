# dictremove (AutoLISP)

Removes an entry from the specified dictionary

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(dictremove ename symbol)
```

*ename*
:   *Type:* Ename (entity name)

    Name of the dictionary being modified.

*symbol*
:   *Type:* String

    The entry to be removed from
    *ename*.

## Return Values

*Type:* Ename (entity name) or nil

The entity name of the removed entry. If
*ename* is invalid or
*symbol* is not found,
dictremove returns
nil.

## Remarks

By default, removing an entry from a dictionary does not delete it from the database. This must be done with a call to
entdel. Currently, the exceptions to this rule are groups and multiline styles. The code that implements these features requires
that the database and these dictionaries be up to date and, therefore, automatically deletes the entity when it is removed
(with
dictremove) from the dictionary.

The
dictremove function does not allow the removal of an multiline style from the multiline style dictionary if it is actively referenced
by an multiline in the database.

## Examples

The following example removes the dictionary created in the
dictadd example:

```
(dictremove (namedobjdict) "my_way_cool_dictionary")
<Entity name: 1d98950>
```

#### Related References

* [dictadd (AutoLISP)](dictadd-AutoLISP.md)
* [dictsearch (AutoLISP)](dictsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*