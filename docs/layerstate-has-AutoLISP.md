# layerstate-has (AutoLISP)

Checks if a layer state is present

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-has layerstatename)
```

*layerstatename*
:   *Type:* String

    Name of the layer state to be queried.

## Return Values

*Type:* T or nil

T if the name exists; otherwise
nil.

## Examples

```
(layerstate-has "myLayerState")
T
```

#### Related References

* [layerstate-getnames (AutoLISP)](layerstate-getnames-AutoLISP.md)
* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-importfromdb (AutoLISP)](layerstate-importfromdb-AutoLISP.md)
* [layerstate-rename (AutoLISP)](layerstate-rename-AutoLISP.md)
* [layerstate-restore (AutoLISP)](layerstate-restore-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*