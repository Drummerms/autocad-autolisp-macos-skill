# layerstate-removelayers (AutoLISP)

Removes a list of layers from a layer state

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-removelayers layerstatename (list layername layername layername ...))
```

*layerstatename*
:   *Type:* String

    Name of the layer state to be updated.

*layername*
:   *Type:* String

    Name of the layer state to be removed.

## Return Values

*Type:* T or nil

T if the remove is successful; otherwise
nil.

## Examples

```
(layerstate-removelayers "myLayerState" (list "Walls" "Elec1" "Foundation" "Plumbing"))
T
```

#### Related References

* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)
* [layerstate-getlayers (AutoLISP)](layerstate-getlayers-AutoLISP.md)
* [layerstate-addlayers (AutoLISP)](layerstate-addlayers-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*