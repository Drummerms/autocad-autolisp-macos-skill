# layerstate-addlayers (AutoLISP)

Adds or updates a series of layers to a layer state

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(layerstate-addlayers layerstatename (list layername state color linetype lineweight plotstyle) [(list ...)])
```

*layerstatename*
:   *Type:* String

    Name of the layer state to be updated.

*layername*
:   *Type:* String

    Name of the layer to be added or updated.

*state*
:   *Type:* Integer or nil

    Numeric sum designating properties in the layer to be set.

    *1* -- Turns the layer off

    *2* -- Freeze the layer

    *4* -- Lock the layer

    *8* -- Flag the layer as No Plot

    *16* -- Set the layer as being frozen in new viewports

    A
    nil value uses defaults of on, thawed, unlocked, plottable, and thawed in new viewports.

*color*
:   *Type:* List

    A dotted pair specifying the layers color type and value,
    *e.g.* (62 . ColorIndex),
    (420 . TrueColor), or
    (430 . "colorbook$colorname").

*linetype*
:   *Type:* String

    Name of the layer linetype. The linetype must already be loaded in the drawing or the default of "Continuous" will be used.
    A
    nil value sets the layer linetype to "Continuous."

*lineweight*
:   *Type:* Integer

    Number corresponding to a valid lineweight, i.e., 35 = .35, 211 = 2.11. A
    nil value sets the layer lineweight to "Default."

*plotstyle*
:   *Type:* String

    Name of the layers plot style. The plotstyle name must already be loaded in the drawing or the default of "Normal" will be
    used. A
    nil value sets the layer plotstyle to "Normal." If the drawing is in color dependent mode, this setting is ignored.

## Return Values

*Type:* T or nil

T if successful; otherwise
nil.

## Examples

```
(layerstate-addlayers
  "myLayerState"
  (list "Walls" 4 '(62 . 45) "Divide" 35 "10% Screen")
  (list "Floors" 6 '(420 . 16235019) "Continuous" 40 "60% Screen")
  (list "Ceiling" 0 '(430 . "RAL CLASSIC$RAL 1003") "DOT" nil nil)
)
T
```

#### Related References

* [layerstate-getlayers (AutoLISP)](layerstate-getlayers-AutoLISP.md)
* [layerstate-has (AutoLISP)](layerstate-has-AutoLISP.md)
* [layerstate-removelayers (AutoLISP)](layerstate-removelayers-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*