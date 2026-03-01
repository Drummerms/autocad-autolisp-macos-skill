# acdimenableupdate (AutoLISP)

Controls the automatic updating of associative dimensions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(acdimenableupdate flag)
```

*flag*
:   *Type:* T or nil

    Controls the automatic updating of associative dimensions when geometry is modified.

    *T*  -- Enable automatic updating of associative dimensions when the geometry is modified.

    *nil*  -- Associative dimensions are not updated (even if the geometry is modified) until the DIMREGEN command is used.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

The
acdimenableupdate function is intended for developers who are editing geometry and don't want the dimension to be updated until after the edits
are complete.

## Examples

Disable the automatic update of associative dimensions in the drawing:

```
(acdimenableupdate nil)
```

Enable the automatic update of associative dimensions in the drawing:

```
(acdimenableupdate T)
```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*