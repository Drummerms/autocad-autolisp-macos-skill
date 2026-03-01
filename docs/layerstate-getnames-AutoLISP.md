# layerstate-getnames (AutoLISP)

Returns a list of the layer state names

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-getnames [includehidden] [includexref])
```

*includehidden*
:   *Type:* T or nil

    If
    *includehidden* is
    T, the list will include the names of hidden layer states. If omitted or
    nil, hidden layer states will be excluded.

*includexref*
:   *Type:* T or nil

    If
    *includexref* is
    nil, the list will exclude the names of xref layer states. If omitted or
    T, xref layer states will be included

## Return Values

*Type:* List or nil

Returns a list of the layer state names.

## Examples

```
(layerstate-getnames)
("First Floor" "Second Floor" "Foundation")
```

#### Related References

* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)
* [layerstate-rename (AutoLISP)](layerstate-rename-AutoLISP.md)
* [layerstate-restore (AutoLISP)](layerstate-restore-AutoLISP.md)
* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-importfromdb (AutoLISP)](layerstate-importfromdb-AutoLISP.md)
* [layerstate-has (AutoLISP)](layerstate-has-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*