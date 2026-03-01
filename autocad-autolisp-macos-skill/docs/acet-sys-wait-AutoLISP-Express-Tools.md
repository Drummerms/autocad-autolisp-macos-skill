# acet-sys-wait (AutoLISP/Express Tools)

Waits for a process to complete.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-sys-wait processID [time])
```

processID
:   *Type:* Integer

    ID for the sub-process.

time
:   *Type:* Integer

    If given, the number of milliseconds to wait.

## Return Values

*Type:* Integer

Exit code from the given process, or -1 if an error occurred or
*time* expired.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*