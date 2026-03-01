# layerstate-compare (AutoLISP)

Compares a layer state to the layers in the current drawing

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-compare layerstatename viewport)
```

*layerstatename*
:   *Type:* String

    Name of the layer state compare.

*viewport*
:   *Type:* Ename (entity name)

    An ename of the viewport to be used in the compare. If viewport is
    nil, the current viewport is used

## Return Values

*Type:* T or nil

T if successful; otherwise
nil.

## Examples

```
(layerstate-compare "myLayerState")
nil
```

#### Related References

* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-importfromdb (AutoLISP)](layerstate-importfromdb-AutoLISP.md)
* [layerstate-restore (AutoLISP)](layerstate-restore-AutoLISP.md)
* [layerstate-getnames (AutoLISP)](layerstate-getnames-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*