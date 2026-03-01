# layerstate-export (AutoLISP)

Exports a layer state to a specified file

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-export layerstatename filename)
```

*layerstatename*
:   *Type:* String

    Name of the layer to export.

*filename*
:   *Type:* String

    Name of the file to which the layer state should be exported.

## Return Values

*Type:* T or nil

T if the export is successful;
nil otherwise.

## Examples

Windows
:   ```
    (layerstate-export "myLayerState" "c:\\mylayerstate.las")
    T
    ```

Mac OS
:   ```
    (layerstate-export "myLayerState" "/mylayerstate.las")
    T
    ```

#### Related References

* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-importfromdb (AutoLISP)](layerstate-importfromdb-AutoLISP.md)
* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*