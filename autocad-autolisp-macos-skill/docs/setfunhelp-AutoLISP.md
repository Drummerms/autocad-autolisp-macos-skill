# setfunhelp (AutoLISP)

Registers a user-defined command with the Help facility so the appropriate Help file and topic are called when the user requests
help on that command

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(setfunhelp c:fname [helpfile [topic [command]]])
```

*c:fname*
:   *Type:* String

    User-defined command (the
    C:XXXfunction). You must include the
    c: prefix.

*helpfile*
:   *Type:* String

    Help file name. The file extension is not required with the
    *helpfile* argument. If a file extension is provided, AutoCAD looks only for a file with the exact name specified.

    If no file extension is provided, AutoCAD looks for
    *helpfile* with an extension of .*chm*. If no file of that name is found, AutoCAD looks for a file with an extension of .*hlp*.

*topic*
:   *Type:* String

    Help topic ID. If you are calling a topic within a CHM file, provide the file name without the extension; AutoCAD adds an
    *.htm* extension.

*command*
:   *Type:* String

    Initial state of the Help window. The
    *command*argument is a string used by the uCommand (in HTML Help) or the fuCommand (in WinHelp) argument of the HtmlHelp() and WinHelp()
    functions as defined in the Microsoft Windows SDK.

    For HTML Help files, the
    *command*parameter can be HH\_ALINK\_LOOKUP or HH\_DISPLAY\_TOPIC. For Windows Help files, the
    *command* parameter can be HELP\_CONTENTS, HELP\_HELPONHELP, or HELP\_PARTIALKEY.

## Return Values

*Type:* String or nil

*c:fname*, if successful; otherwise,
nil.

This function verifies only that the
*c:fname* argument has the
c: prefix. It does
*not* verify that the
c:fname function exists, nor does it verify the correctness of the other arguments supplied.

## Remarks

NOTE:This function is supported on Web, but does not affect the program since it doesn't support contextual help.

## Examples

The following example illustrates the use of
setfunhelp by defining a simple function and issuing
setfunhelp to associate the function with the Entget topic in the AutoCAD Help file (*acad.chm*):

```
(defun c:foo ()
  (getstring "Press F1 for help on the foo command:")
)
(setfunhelp "c:test" "acad.chm" "entget")
```

After this code is loaded, issuing the
foo command and then pressing F1 displays the circle topic.

This example works, but serves no real purpose. In the real world, you would create your own Help file and associate that
Help file and topic with your function.

Define a function named
test:

```
(defun c:test()(getstring "\
TEST: " )(princ))
C:TEST
```

Associate the function with a call to Help with the string “line”:

```
(setfunhelp "c:test" "acad_acr.chm" "line")
"c:test"
```

Run the
test command and at the prompt, press F1; you should see the Help topic for the AutoCAD LINE command.

NOTE:When you use the
defun function to define a
C:XXX function, it removes that function's name from those registered by
setfunhelp (if one exists). Therefore,
setfunhelp should be called only after the
defun call, which defines the user-defined command.

#### Related References

* [help (AutoLISP)](help-AutoLISP.md)
* [acad\_helpdlg (AutoLISP)](acad_helpdlg-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About Accessing and Assigning Help to a Command (AutoLISP)](About-Accessing-and-Assigning-Help-to-a-Command-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*