# acad-push-dbmod (AutoLISP)

Stores the current value of the
DBMOD system variable

*Supported Platforms:* Windows, Mac OS, and Web

*Prerequisites:* The AcApp ObjectARX application must be loaded before the function can be called, which is loaded by default.

## Signature

```
(acad-push-dbmod)
```

No arguments.

## Return Values

*Type:* T

Always returns
T.

## Remarks

This function is used with
acad-pop-dbmod to control the
DBMOD system variable. You can use this function to change a drawing without changing the
DBMOD system variable. The
DBMOD system variable tracks changes to a drawing and triggers save-drawing queries.

This function pushes the current value of the
DBMOD system variable onto an internal stack. To use
acad-push-dbmod and
acad-pop-dbmod, precede operations with
acad-push-dbmod and then use
acad-pop-dbmod to restore the original value of the
DBMOD system variable.

## Examples

The following example shows how to store the modification status of a drawing, change the status, and then restore the original
status.

```
(acad-push-dbmod)
(setq new_line '((0 . "LINE") (100 . "AcDbEntity") (8 . "0")
             (100 . "AcDbLine") (10 1.0 2.0 0.0) (11 2.0 1.0 0.0)
             (210 0.0 0.0 1.0)))
(entmake new_line)            ; Set DBMOD to flag 1
(command "._color" "2")        ; Set DBMOD to flag 4
(command "._-vports" "_SI")    ; Set DBMOD to flag 8
(command "._vpoint" "0,0,1")   ; Set DBMOD to flag 16
(acad-pop-dbmod)              ; Set DBMOD to original value
```

#### Related References

* [acad-pop-dbmod (AutoLISP)](acad-pop-dbmod-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*