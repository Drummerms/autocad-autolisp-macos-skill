# redraw (AutoLISP)

Redraws the current viewport or a specified object (entity) in the current viewport

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(redraw [ename [mode]])
```

*ename*
:   *Type:* ads\_name

    The name of the entity name to be redrawn.

*mode*
:   *Type:* Integer

    Value that controls the visibility and highlighting of the entity. The
    *mode* can be one of the following values:

    *1* -- Show entity

    *2* -- Hide entity (blank it out)

    *3* -- Highlight entity

    *4* -- Unhighlight entity

    The use of entity highlighting (mode 3) must be balanced with entity unhighlighting (mode 4).

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

If
redraw is called with no arguments, the function redraws the current viewport. If called with an entity name argument,
redraw redraws the specified entity.

The
redraw function has no effect on highlighted or hidden entities; however, a AutoCAD REGEN command forces the entities to redisplay
in their normal manner.

If
*ename* is the header of a complex entity (a polyline or a block reference with attributes),
redraw processes the main entity and all its subentities if the
*mode* argument is positive. If the
*mode* argument is negative,
redraw operates on only the header entity.

## Examples

None

#### Related References

* [grclear (AutoLISP)](grclear-AutoLISP.md)
* [grdraw (AutoLISP)](grdraw-AutoLISP.md)
* [grvecs (AutoLISP)](grvecs-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*