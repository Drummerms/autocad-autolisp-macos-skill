# acad-pop-dbmod (AutoLISP)

Restores the value of the
DBMOD system variable to the value that was most recently stored with
acad-push-dbmod

*Supported Platforms:* Windows, Mac OS, and Web

*Prerequisites:* The AcApp ObjectARX application must be loaded before the function can be called, which is loaded by default.

## Signature

```
(acad-pop-dbmod)
```

No arguments.

## Return Values

*Type:* T or nil

Returns
T if successful; otherwise, if the stack is empty, returns
nil.

## Remarks

This function pops the current value of the
DBMOD system variable off an internal stack.

This function is used with
acad-push-dbmod to control the
DBMOD system variable. The
DBMOD system variable tracks changes to a drawing and triggers save-drawing queries.

#### Related References

* [acad-push-dbmod (AutoLISP)](acad-push-dbmod-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*