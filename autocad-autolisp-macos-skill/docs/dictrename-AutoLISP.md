# dictrename (AutoLISP)

Renames a dictionary entry

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(dictrename ename oldsym newsym)
```

*ename*
:   *Type:* Ename (entity name)

    Name of the dictionary being modified.

*oldsym*
:   *Type:* String

    Original key name of the entry.

*newsym*
:   *Type:* String

    New key name of the entry.

## Return Values

*Type:* String or nil

The
*newsym* value, if the rename is successful. If the
*oldname* is not present in the dictionary, or if
*ename* or
*newname* is invalid, or if
*newname* is already present in the dictionary, then
dictrename returns
nil.

## Examples

The following example renames the dictionary created in the
dictadd sample:

```
(dictrename (namedobjdict) "my_way_cool_dictionary" "An even cooler dictionary")
"An even cooler dictionary"
```

#### Related References

* [dictadd (AutoLISP)](dictadd-AutoLISP.md)
* [dictsearch (AutoLISP)](dictsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*