# acet-sys-beep (AutoLISP/Express Tools)

Makes a noise.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-sys-beep sound)
```

sound
:   *Type:* Integer

    A sound selector value. Can be one of:

    * -1: Standard beep using computer speaker
    * 0:
      SystemDefault
    * 16:
      SystemHand
    * 32:
      SystemQuestion
    * 48:
      SystemExclamation
    * 64:
      SystemAsterisk

## Return Values

*Type:* nil

Returns
nil.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*