# initcommandversion (AutoLISP)

Forces the next command to run with the specified version

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(initcommandversion [version])
```

*version*
:   *Type:* Integer

    This argument specifies the version of the command to be used. If this argument is not present, the next use (and next use
    only) of a supported command will initialize to the latest version.

## Return Values

*Type:* T

Always returns
T.

## Remarks

This function makes it possible to force a specific behavior for a supported command regardless of how it is being run. This
only affects commands that have been updated to support a command version. In such commands, a test for an initialized command
version replaces the legacy test for whether the command is being run from AutoLISP or a script. When a supported command
is being run manually, the default version is 2 (or the latest version). When a command is being run from automation, the
default version is 1.

## Examples

Initializing a specific command version may affect each supported command differently. For example, here is the AutoCAD FILLET
command with and without an initialized version:

Command:
*FILLET*

Current settings: Mode = TRIM, Radius = 0.0000

Select first object or [Undo/Polyline/Radius/Trim/Multiple]: \*Cancel\*

Command:
*(initcommandversion 1)*

Command:
*FILLET*

Current settings: Mode = TRIM, Radius = 0.0000

Select first object or [uNdo/Polyline/Radius/Trim/mUltiple]: \*Cancel\*

Another typical example is the AutoCAD COLOR command. Run normally, COLOR displays the Select Color dialog; but by running
(initcommandversion 1) before the COLOR command, it is forced to prompt from color from the Command prompt.

#### Related References

* [command (AutoLISP)](command-AutoLISP.md)
* [command-s (AutoLISP)](command-s-AutoLISP.md)
* [initdia (AutoLISP)](initdia-AutoLISP.md)
* [vl-cmdf (AutoLISP)](vl-cmdf-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*