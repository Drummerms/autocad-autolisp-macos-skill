# layerstate-save (AutoLISP)

Saves a layer state in the current drawing

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-save layerstatename mask viewport)
```

*layerstatename*
:   *Type:* String

    Name of the layer state to save.

*mask*
:   *Type:* Integer

    Numeric sum designating which properties in the layer state are to be restored.

    *1* -- Restore the saved On or Off value

    *2* -- Restore the saved Frozen or Thawed value

    *4* -- Restore the saved Lock value

    *8* -- Restore the saved Plot or No Plot value

    *16* -- Restore the saved VPVSDFLT value

    *32* -- Restore the saved Color

    *64* -- Restore the saved LineType

    *128* -- Restore the saved LineWeight

*viewport*
:   *Type:* Ename (entity name)

    An ename of the viewport whose VPLAYER setting is to be captured. If nil, the layer state will be saved without VPLAYER settings.

## Return Values

*Type:* T or nil

T if the save is successful; otherwise
nil.

## Examples

```
(layerstate-save "myLayerState" 21 viewportId)
T

(layerstate-save "myLayerState" nil nil)
nil
```

#### Related References

* [layerstate-has (AutoLISP)](layerstate-has-AutoLISP.md)
* [layerstate-getnames (AutoLISP)](layerstate-getnames-AutoLISP.md)
* [layerstate-rename (AutoLISP)](layerstate-rename-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*