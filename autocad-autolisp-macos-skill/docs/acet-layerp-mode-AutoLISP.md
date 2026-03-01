# acet-layerp-mode (AutoLISP)

Queries and sets the LAYERPMODE setting

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(acet-layerp-mode [status])
```

*status*
:   *Type:* T or nil

    T - Turns LAYERPMODE on, enabling layer-change tracking

    nil - Turns LAYERPMODE off

    If this argument is not present,
    acet-layerp-mode returns the current status of LAYERPMODE.

## Return Values

*Type:* T or nil

T if current status of LAYERPMODE is on;
nil if LAYERPMODE is off.

## Examples

Check the current status of LAYERPMODE:

```
(acet-layerp-mode)
T
```

Turn LAYERPMODE off:

```
(acet-layerp-mode nil)
nil
```

Check the current status of LAYERPMODE:

```
(acet-layerp-mode)
nil
```

#### Related References

* [acet-layerp-mark (AutoLISP)](acet-layerp-mark-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*