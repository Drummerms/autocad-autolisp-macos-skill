# tblsearch (AutoLISP)

Searches a symbol table for a symbol name

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(tblsearch table-name symbol [setnext])
```

*table-name*
:   *Type:* String

    Symbol table to be searched. This argument is not case-sensitive.

*symbol*
:   *Type:* String

    Symbol name to be searched for. This argument is not case-sensitive.

*setnext*
:   *Type:* T or nil

    If this argument is supplied and is not
    nil, the
    tblnext entry counter is adjusted so the following
    tblnext call returns the entry after the one returned by this
    tblsearch call. Otherwise,
    tblsearch has no effect on the order of entries retrieved by
    tblnext.

## Return Values

*Type:* List (dotted pairs) or nil

If
tblsearch finds an entry for the given symbol name, it returns that entry. If no entry is found,
tblsearch returns
nil.

## Examples

The following command searches for a text style named “standard”:

```
(tblsearch "style" "standard")
((0 . "STYLE") (2 . "STANDARD") (70 . 0) (40 . 0.0) (41 . 1.0) (50 . 0.0) (71 . 0) (42 . 0.3) (3 . "txt") (4 . ""))
```

#### Related References

* [tblnext (AutoLISP)](tblnext-AutoLISP.md)
* [tblobjname (AutoLISP)](tblobjname-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*