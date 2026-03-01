# vlax-add-cmd (AutoLISP/ActiveX)

Adds commands to the AutoCAD built-in command set

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vlax-add-cmd global-name func-sym [local-name cmd-flags])
```

*global-name*
:   *Type:* String

    The global name for the command.

*func-sym*
:   *Type:* Subroutine or Symbol

    A symbol naming an AutoLISP function with zero arguments.

*local-name*
:   *Type:* String

    A local name for the command (defaults to
    *global-name*).

*cmd-flags*
:   *Type:* Integer

    A numeric value (defaults to ACRX\_CMD\_MODAL + ACRX\_CMD\_REDRAW)

    The primary flags are

    *ACRX\_CMD\_MODAL* (0) -- Command cannot be invoked while another command is active.

    *ACRX\_CMD\_TRANSPARENT*(1) -- Command can be invoked while another command is active.

    The secondary flags are

    *ACRX\_CMD\_USEPICKSET*(2) -- When the pickfirst set is retrieved it is cleared within AutoCAD. Command will be able to retrieve the pickfirst set.
    Command cannot retrieve or set grips.

    *ACRX\_CMD\_REDRAW*(4) -- When the pickfirst set or grip set is retrieved, neither will be cleared within AutoCAD. Command can retrieve the pickfirst
    set and the grip set.

    If both ACRX\_CMD\_USEPICKSET and ACRX\_CMD\_REDRAW are set, the effect is the same as if just ACRX\_CMD\_REDRAW is set. For more
    information about the flags, see the “Command Stack” in the
    *ObjectARX Reference*.

## Return Values

*Type:* String or nil

The
*global-name* argument, if successful. The function returns
nil if acedRegCmds->addCommand(...) returns an error condition.

## Remarks

With
vlax-add-cmd you can define a function as an AutoCAD command, without using the
*c:*prefix in the function name. You can also define a transparent AutoLISP command, which is not possible with a
*c:*function.

IMPORTANT:You cannot use the command function call in a transparently defined
vlax-add-cmd function. Doing so can cause AutoCAD to close unexpectedly.

The
vlax-add-cmd function makes an AutoLISP function visible as an ObjectARX-style command at the AutoCAD Command prompt during the current
AutoCAD session. The function provides access to the ObjectARX acedRegCmds macro, which provides a pointer to the ObjectARX
system AcEdCommandStack object.

The
vlax-add-cmd function automatically assigns commands to command groups. When issued from a document namespace,
vlax-add-cmd adds the command to a group named
*doc-ID*;
*doc-ID* is a hexadecimal value identifying the document. If issued from a separate-namespace VLX,
vlax-add-cmd adds the command to a group named VLC-D*doc-ID*:*VLX-name*, where
*VLX-name* is the name of the application that issued
vlax-add-cmd.

It is recommended that you use the
vlax-add-cmd function from a separate-namespace VLX. You should then explicitly load the VLX using the AutoCAD APPLOAD command, rather
than by placing it in one of the startup LISP files.

NOTE:

* You cannot use
  vlax-add-cmd to expose functions that create reactor objects or serve as reactor callbacks.
* This function is supported in AutoCAD LT and on Web, but does not affect the program.

## Examples

The
hello-autocad function in the following example has no c: prefix, but
vlax-add-cmd makes it visible as an ObjectARX-style command at the AutoCAD Command prompt:

```
(defun hello-autocad () (princ "hello Visual LISP"))
HELLO-AUTOCAD

(vlax-add-cmd "hello-autocad" 'hello-autocad)
"hello-autocad"
```

#### Related References

* [vlax-remove-cmd (AutoLISP/ActiveX)](vlax-remove-cmd-AutoLISP-ActiveX.md)
* [defun (AutoLISP)](defun-AutoLISP.md)
* [vl-acad-defun (AutoLISP)](vl-acad-defun-AutoLISP.md)
* [vl-acad-undefun (AutoLISP)](vl-acad-undefun-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)
* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*