# help (AutoLISP)

Invokes the Help facility

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(help [helpfile [topic [command]]])
```

*helpfile*
:   *Type:* String

    Help file name.

    NOTE:If an empty string is provided, AutoCAD will try to open the topic in the Online help associated with and available for the
    product.

    The file extension is not required with the
    *helpfile* argument. If a file extension is provided, AutoCAD looks only for a file with the exact name specified.

    If no file extension is provided, AutoCAD looks for
    *helpfile* with an extension of
    *.chm*. If no file of that name is found, AutoCAD looks for a file with an extension of
    *.hlp*.

    NOTE:It is recommended to place help files in a folder that doesn't contain Unicode characters. The Microsoft® HTML Help Executable doesn't support paths with Unicode characters, so the help files might not open as expected.

*topic*
:   *Type:* String

    Help topic ID.

    If you are calling a topic within a CHM file, provide the file name without the extension; AutoCAD adds an
    *.htm* extension.

*command* (Windows only)
:   *Type:* String

    Specifies the initial state of the Help window. The
    *command* argument is a string used by the uCommand (in HTML Help) or the fuCommand (in WinHelp) argument of the HtmlHelp() and WinHelp()
    functions as defined in the Microsoft Windows SDK.

    For HTML Help files, the
    *command* parameter can be HH\_ALINK\_LOOKUP or HH\_DISPLAY\_TOPIC. For Windows Help files, the
    *command* parameter can be HELP\_CONTENTS, HELP\_HELPONHELP, or HELP\_PARTIALKEY.

## Return Values

*Type:* String or nil

The
*helpfile* string, if successful; otherwise
nil. If you use
help without any arguments, it returns an empty string ("") if successful, and
nil if it fails.

The only error condition that the
help function returns to the application is the existence of the file specified by
*helpfile*. All other error conditions are reported to the user through a dialog box.

## Remarks

NOTE:This function is supported on Web, but does not affect the program.

## Examples

The following code calls
help to display the information on
MYCOMMAND in the Help file
*achelp.chm*:

```
(help "achelp.chm" "mycommand")
```

#### Related References

* [setfunhelp (AutoLISP)](setfunhelp-AutoLISP.md)
* [acad\_helpdlg (AutoLISP)](acad_helpdlg-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About Accessing and Assigning Help to a Command (AutoLISP)](About-Accessing-and-Assigning-Help-to-a-Command-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*