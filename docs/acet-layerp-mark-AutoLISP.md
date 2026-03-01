# acet-layerp-mark (AutoLISP)

Places beginning and ending marks for Layer Previous recording

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(acet-layerp-mark [status])
```

*status*
:   *Type:* T or nil

    *T*  -- sets a begin mark

    *nil*  -- sets an end mark, clearing the begin mark

## Return Values

*Type:* T or nil

T if a begin mark is in effect; otherwise
nil.

If
*status* is omitted,
acet-layerp-mark returns the current mark status for layer settings.

## Remarks

The
acet-layerp-mark function allows you to group multiple layer commands into a single transaction so that they can be undone by issuing the
AutoCAD LAYERP command a single time. The LAYERPMODE setting must be On in order to set marks.

## Examples

The following code changes layer 0 to blue, and then makes several additional layer changes between a set of begin and end
marks. If you issue the AutoCAD LAYERP command after running this code, layer 0 reverts to blue.

```
(defun TestLayerP ()
  ;; Turn LAYERPMODE on, if it is not already
  (if (not (acet-layerp-mode))
    (acet-layerp-mode T)
  )

  ;; Set layer 0 to the color blue
  (command "._layer" "_color" "blue" "0" "")

  ;; Set a begin mark
  (acet-layerp-mark T)

  ;; Issue a series of layer commands, and then set an end mark
  (command "._layer" "_color" "green" "0" "")
  (command "._layer" "_thaw" "*" "")
  (command "._layer" "_unlock" "*" "")
  (command "._layer" "_ltype" "hidden" "0" "")
  (command "._layer" "_color" "red" "0" "")

  ;; Set an end mark
  (acet-layerp-mark nil)
 (princ)
)
```

#### Related References

* [acet-layerp-mode (AutoLISP)](acet-layerp-mode-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*