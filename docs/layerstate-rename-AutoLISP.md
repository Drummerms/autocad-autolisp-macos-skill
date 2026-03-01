# layerstate-rename (AutoLISP)

Renames a layer state

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-rename oldlayerstatename newlayerstatename)
```

*oldlayerstatename*
:   *Type:* String

    Name of the layer state to be renamed.

*newlayerstatename*
:   *Type:* String

    Name of the layer state to be updated.

## Return Values

*Type:* T or nil

T if the rename is successful; otherwise
nil.

## Examples

```
(layerstate-rename "myLayerState" "myNewLayerState")
T
```

#### Related References

* [layerstate-has (AutoLISP)](layerstate-has-AutoLISP.md)
* [layerstate-getnames (AutoLISP)](layerstate-getnames-AutoLISP.md)
* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*