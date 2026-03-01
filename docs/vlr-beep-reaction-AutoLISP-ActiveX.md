# vlr-beep-reaction (AutoLISP/ActiveX)

Produces a beep sound

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-beep-reaction [args ...])
```

*args*
:   *Type:* Integer, Real, String, List, File, VLA-object, Safearray, Variant, Ename (entity name), T, or nil

    Any value that can be used a reactor.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

This is a predefined callback function that accepts a variable number of arguments, depending on the reactor type. The function
can be assigned to an event handler for debugging.

## Examples

N/A

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*