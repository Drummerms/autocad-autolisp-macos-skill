# acet-sys-spawn (AutoLISP/Express Tools)

Executes an external program.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-sys-spawn flags command [argument ...])
```

flags
:   *Type:* Integer

    A bitcode of flags indicating how the external program should be executed.

    Supported flags:

    * 1 - wait for the program to complete
    * 2 - run program minimized

command
:   *Type:* String

    Name of the external program.

argument
:   *Type:* String

    A set of arguments to be passed to the external program.

## Return Values

*Type:* Integer

If this function waits for program completion the return value is the exit code from the program, otherwise the return value
is the process ID for the new process. See
acet-sys-term and
acet-sys-wait for more information.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*