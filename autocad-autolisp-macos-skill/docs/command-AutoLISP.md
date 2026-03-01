# command (AutoLISP)

Executes an AutoCAD command

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(command [arguments ...])
```

*arguments*
:   *Type:* Integer, Real, String, or List

    AutoCAD commands and their options.

    The
    *arguments* to the
    command function can be strings, reals, integers, or points, as expected by the prompt sequence of the executed command. A null string
    ("") is equivalent to pressing Enter on the keyboard. Invoking
    command with no argument is equivalent to pressing Esc and cancels most AutoCAD commands.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

The
command function evaluates each argument and sends it to AutoCAD in response to successive prompts. It submits command names and
options as strings, 2D points as lists of two reals, and 3D points as lists of three reals. AutoCAD recognizes command names
only when it issues a Command prompt.

Note that if you issue
command from Visual LISP on Windows, focus does not change to the AutoCAD window. If the command requires user input, you'll see
the return value (nil) in the Console window, but AutoCAD will be waiting for input. You must manually activate the AutoCAD window and respond
to the prompts. Until you do so, any subsequent commands will fail.

The AutoCAD SKETCH command reads the digitizer directly and therefore cannot be used with the AutoLISP
command function. If the AutoCAD SCRIPT command is used with the
command function, it should be the last function call in the AutoLISP routine.

Also, if you use the
command function in an
*.lsp* or
*.mnl* file, it should be called only from within a
defun statement. Use the
S::STARTUP function to define commands that need to be issued immediately when you begin a drawing session.

For commands that require the selection of an object (like the AutoCAD BREAK and TRIM commands), you can supply a list obtained
with
entsel instead of a point to select the object.

Commands executed from the
command function are not echoed to the command line if the AutoCAD CMDECHO system variable (accessible from
setvar and
getvar) is set to 0.

NOTE:When command input comes from the AutoLISP
command function, the settings of the AutoCAD PICKADD and PICKAUTO system variables are assumed to be 1 and 0, respectively. This
preserves compatibility with previous releases of AutoCAD and makes customization easier (because you don't have to check
the settings of these variables).

With the introduction of the Action Recorder in AutoCAD 2009-based products, commands were assigned versions. Commands used
at the Command prompt always use the latest version of the specific command. However, commands used in AutoLISP and command
macros might work differently. The
initcommandversion function is used to determine the version of the next command to be executed.

## Examples

The following example sets two variables
*pt1* and
*pt2* equal to two point values 1,1 and 1,5. It then uses the
command function to issue the AutoCAD LINE command and pass the two point values.

```
(setq pt1 '(1 1) pt2 '(1 5))
(1 5)

(command "._line" pt1 pt2 "")
nil
```

#### Related References

* [command-s (AutoLISP)](command-s-AutoLISP.md)
* [initcommandversion (AutoLISP)](initcommandversion-AutoLISP.md)
* [initdia (AutoLISP)](initdia-AutoLISP.md)
* [vl-cmdf (AutoLISP)](vl-cmdf-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*