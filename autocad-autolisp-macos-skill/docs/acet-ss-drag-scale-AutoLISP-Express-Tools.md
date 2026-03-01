# acet-ss-drag-scale (AutoLISP/Express Tools)

Drags a selection set to change scale.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-ss-drag-scale ss pt [prompt] [highlight [cursor]])
```

ss
:   *Type:* Pickset (selection set)

    The selection set to drag.

pt
:   *Type:* List

    The base point.

prompt
:   *Type:* String

    A message to display before dragging is started.

highlight
:   *Type:* T or
    nil

    If given, causes a rubber-band line to be drawn from pt to the current cursor position while dragging; this parameter can
    be
    nil to draw a rubber-band line in the inverse of the screen color, or non-nil to draw a highlighted line.

cursor
:   *Type:* Integer

    The cursor form to display while dragging (0=crosshairs, 1=no cursor, 2=target).

## Return Values

*Type:* Real or
nil

The selected scale factor, or
nil if dragging is aborted.

## Remarks

This function does not scale the selection set, but allows selection of a scaling factor while showing how the result will
appear.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*