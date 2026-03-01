# layerstate-importfromdb (AutoLISP)

Imports a layer state from a specified drawing file

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-importfromdb layerstatename filename)
```

*layerstatename*
:   *Type:* String

    Name of the layer state to be imported.

*filename*
:   *Type:* String

    Name of the file from which to import a layer state.

## Return Values

*Type:* T or nil

T if the import is successful;
nil otherwise.

## Examples

Windows
:   ```
    (layerstate-importfromdb "mylayerstate" "c:\\mydrawing.dwg")
    T
    ```

Mac OS
:   ```
    (layerstate-importfromdb "mylayerstate" "/mydrawing.dwg")
    T
    ```

#### Related References

* [layerstate-import (AutoLISP)](layerstate-import-AutoLISP.md)
* [layerstate-getnames (AutoLISP)](layerstate-getnames-AutoLISP.md)
* [layerstate-export (AutoLISP)](layerstate-export-AutoLISP.md)
* [layerstate-save (AutoLISP)](layerstate-save-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*