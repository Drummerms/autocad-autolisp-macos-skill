# vlr-trace-reaction (AutoLISP/ActiveX)

A predefined callback function that prints one or more callback arguments in the Trace window

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-trace-reaction)
```

No arguments.

## Return Values

*Type:* nil

Always returns
nil. A message displays the type of trigger event, the reactor type, and the command that triggered the reactor.

## Remarks

This function can be used as a debugging tool to verify that a reactor has fired.

## Examples

Define a command reactor and assign
vlr-trace-reaction as the callback function:

```
(VLR-Reaction-Set (VLR-Command-Reactor) :VLR-commandWillStart 'VLR-trace-reaction)
VLR-trace-reaction
```

At the AutoCAD Command prompt, enter the following:

```
_.LINE
```

Respond to the command prompts, then activate the Visual LISP window and open the Trace window. You should see the following
in the Trace window:

```
; "Reaction": :VLR-commandWillStart; "argument list": (#<VLR-COMMAND-REACTOR> ("LINE"))
```

The output from
vlr-trace-reaction identifies the type of trigger event, the reactor type, and the command that triggered the reactor.

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*