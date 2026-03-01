# layerstate-restore (AutoLISP)

Restores a layer state into the current drawing

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-restore layerstatename viewport [restoreflags])
```

*layerstatename*
:   *Type:* String

    Name of the layer to restore.

viewport
:   *Type:* Ename (entity name)

    An ename of the viewport to which
    *layerstatename* should be restored. If viewport is
    nil, the layer state is restored to model space.

restoreflags
:   *Type:* Integer

    Optional numeric sum affecting how the layer state is restored.

    *1* -- Turn off all layers not in the restored layer state

    *2* -- Freeze all layers not in the restored layer state

    *4* -- Restore the layer state properties as viewport overrides (requires viewport to be not a
    nil value).

## Return Values

*Type:* List or nil

nil if the layer state does not exist or contains no layers; otherwise, returns a list of layer names.

## Examples

```
(layerstate-restore "myLayerState" viewportId 5)
("Layername1" "Layername2")
```

#### Related References

* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)
* [layerstate-has (AutoLISP)](layerstate-has-AutoLISP.md)
* [layerstate-getnames (AutoLISP)](layerstate-getnames-AutoLISP.md)
* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-importfromdb (AutoLISP)](layerstate-importfromdb-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*