# autoload (AutoLISP)

Predefines command names to load an associated AutoLISP file

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(autoload filename cmdlist)
```

*filename*
:   *Type:* String

    AutoLISP file to be loaded when one of the commands defined by the
    *cmdlist* argument is entered at the Command prompt. You can omit the path from the
    *filename*, AutoCAD looks for the file in the support file search path. The extension from the filename can also be omitted;
    *.lsp* or
    *.fas*, or
    *.vlx* (Windows only).

*cmdlist*
:   *Type:* List

    A list of strings.

## Return Values

*Type:* nil

Always returns
nil.

If you associate a command with
*filename* and that command is not defined in the specified file, AutoCAD alerts you with an error message when you enter the command.

## Remarks

The first time a user enters a command specified in
*cmdlist*, AutoCAD loads the application specified in
*filename*, then continues the command.

IMPORTANT:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

## Examples

The following causes AutoCAD to load the
*bonusapp.lsp* file the first time the APP1, APP2, or APP3 commands are entered at the Command prompt:

```
(autoload "BONUSAPP" '("APP1" "APP2" "APP3"))
```

#### Related References

* [load (AutoLISP)](load-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*