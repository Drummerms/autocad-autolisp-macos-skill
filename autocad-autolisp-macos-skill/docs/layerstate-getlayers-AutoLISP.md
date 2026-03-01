# layerstate-getlayers (AutoLISP)

Returns the layers saved in a layer state

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-getlayers layerstatename [invert])
```

*layerstatename*
:   *Type:* String

    Name of the layer state to query for layers.

*invert*
:   *Type:* List or nil

    If invert is omitted or
    nil, returns a list of the layers saved in the layer state. If invert is
    T, it returns a list of the layers in the drawing that are not saved in the layer state.

## Return Values

*Type:* List or nil

A list of layer names. Returns
nil if the layer state does not exist or contains no layers.

## Examples

```
(layerstate-getlayers "myLayerState")
("Layername1" "Layername2")
```

#### Related References

* [layerstate-addlayers (AutoLISP)](layerstate-addlayers-AutoLISP.md)
* [layerstate-removelayers (AutoLISP)](layerstate-removelayers-AutoLISP.md)
* [layerstate-has (AutoLISP)](layerstate-has-AutoLISP.md)
* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*