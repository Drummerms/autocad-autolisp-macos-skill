# acet-sys-command (AutoLISP/Express Tools)

Runs a command in a shell and waits for the shell to complete execution before returning.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-sys-command shell-command)
```

shell-command
:   *Type:* String

    Command to execute.

## Return Values

*Type:* Integer

Exit code from the shell command, or -1 on error.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*