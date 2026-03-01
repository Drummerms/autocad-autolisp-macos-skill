# layerstate-delete (AutoLISP)

Deletes a layer state

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-delete layerstatename)
```

*layerstatename*
:   *Type:* String

    Name of the layer state to be deleted.

## Return Values

*Type:* T or nil

T if the delete succeeds; otherwise
nil.

## Examples

```
(layerstate-delete "myLayerState")
T
```

#### Related References

* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-importfromdb (AutoLISP)](layerstate-importfromdb-AutoLISP.md)
* [layerstate-export (AutoLISP)](layerstate-export-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*