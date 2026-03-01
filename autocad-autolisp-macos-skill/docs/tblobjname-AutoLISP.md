# tblobjname (AutoLISP)

Returns the entity name of a specified symbol table entry

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(tblobjname table-name symbol)
```

*table-name*
:   *Type:* String

    Symbol table to be searched. The argument is not case-sensitive.

*symbol*
:   *Type:* String

    Symbol to be searched for.

## Return Values

*Type:* Ename (entity name) or nil

The entity name of the symbol table entry, if found.

The entity name returned by
tblobjname can be used in
entget and
entmod operations.

## Examples

The following command searches for the entity name of the block entry “ESC-01”:

```
(tblobjname "block" "ESC-01")
<Entity name: 1dca368>
```

#### Related References

* [tblnext (AutoLISP)](tblnext-AutoLISP.md)
* [tblsearch (AutoLISP)](tblsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*