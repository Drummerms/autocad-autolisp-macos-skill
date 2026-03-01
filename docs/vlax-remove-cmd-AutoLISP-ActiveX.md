# vlax-remove-cmd (AutoLISP/ActiveX)

Removes a single command or a command group

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vlax-remove-cmd global-name)
```

*global-name*
:   *Type:* String or T

    Name of the command, or
    T. If
    *global-name* is
    T, the whole command group VLC-*AppName* (for example,
    VLC-VLIDE) is deleted.

## Return Values

*Type:* T or nil

T, if successful; otherwise
nil (for example, the command is not defined).

## Remarks

Removes a single command or the whole command group for the current AutoCAD session.

## Examples

Remove a command defined with
vlax-add-cmd:

```
(vlax-remove-cmd "hello-autocad")
T
```

Repeat the
vlax-remove-cmd:

```
(vlax-remove-cmd "hello-autocad")
nil
```

This time
vlax-remove-cmd returns
nil, because the specified command does not exist anymore.

#### Related References

* [vlax-add-cmd (AutoLISP/ActiveX)](vlax-add-cmd-AutoLISP-ActiveX.md)
* [defun (AutoLISP)](defun-AutoLISP.md)
* [vl-acad-defun (AutoLISP)](vl-acad-defun-AutoLISP.md)
* [vl-acad-undefun (AutoLISP)](vl-acad-undefun-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)
* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*