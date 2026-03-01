# command-s (AutoLISP)

Executes an AutoCAD command and the supplied input

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(command-s [cmdname [arguments ...]])
```

*cmdname*
:   *Type:* String

    Name of the command to execute.

*arguments*
:   *Type:* Integer, Real, String, or List

    The command input to supply to the command being executed.

    The arguments to the command function can be strings, reals, integers, or points, as expected by the prompt sequence of the
    executed command. A null string ("") is equivalent to pressing Enter on the keyboard.

## Return Values

*Type:* nil

nil is returned by the function when the command is done executing on the provided arguments. An
\*error\* is returned when the function fails to complete successfully.

## Remarks

See the sections later in this topic for more information.

## Examples

The following example demonstrates how to execute the AutoCAD CIRCLE command and create a circle with a diameter of 2.75.

```
Command: (command-s "._circle" "5,4" "_d" 2.75)
nil
```

The following example demonstrates how to prompt the user for the center point of the circle.

```
Command: (setq cPt (getpoint "\
Specify center point: "))
(5.0 4.0 0.0)

Command: (command-s "._circle" cPt "_d" 2.75)
nil
```

The following is an invalid use of prompting for user input with the command-s function.

```
Command: (command-s "._circle" (getpoint "\
Specify center point: ") "_d" 2.75)
```

## Differences from the Command Function

The
command-s function is a variation of the
command function which has some restrictions on command token content, but is both faster than command and can be used in
\*error\* handlers due to internal logic differences.

A command token is a single argument provided to the
command-s function. This could be a string, real, integer, point, entity name, list, and so on. The following example shows the AutoCAD
LINE command and three command tokens:

```
(command-s "._line" "0,0" "5,7" "")
```

The "-s" suffix stands for "subroutine" execution of the supplied command tokens. In this form, AutoCAD is directly called
from AutoLISP, processes the supplied command tokens in a temporary command processor distinct from the main document command
processor, and then returns, thus terminating the temporary command processor. The command that is being executed must be
started and completed in the same
command-s function.

In contrast, the
command function remains a "co-routine" execution of the supplied command tokens, where AutoLISP evaluates the tokens one at a time,
sending the result to AutoCAD, and then returning to allow AutoCAD to process that token. AutoCAD then calls AutoLISP back,
and AutoLISP resumes evaluation of the expression in progress. In this logic flow, subsequent token expressions can query
AutoCAD for the results of previous token processing and use it.

In summary, the "co-routine" style of command token processing is more functionally powerful, but is limited in when it can
be used when running. The "subroutine" style of command token processing can be used in a much wider range of contexts, but
processes all command tokens in advance, and actual execution is non-interactive. For the same set of command tokens,
command-s function is significantly faster.

## Known Considerations

When using the
command-s function, you must take the following into consideration:

* Token streams fed in a single command-s expression must represent a full command and its input. Any commands in progress when
  command tokens are all processed will be cancelled. The following is not valid with the
  command-s function:

  ```
  (command-s "._line")
  (command-s "2,2" "12.25,9" "")
  ```
* All command tokens will be evaluated before they are handed over to AutoCAD for execution. In contrast, the
  command function actually performs each command token evaluation and then feeds the result to AutoCAD, which processes it before
  the next command token is processed.
* No "Pause" command tokens may be used. Expressions that interact with the drawing area or Command Window may be used, but
  will all be processed before AutoCAD receives and processes any of them.

  The following is not valid with the
  command-s function:

  ```
  (command-s "._line" "0,0" PAUSE "")
  ```

IMPORTANT:Although the
command-s function is similar to the
command function, caution should be taken when using U or UNDO to roll back the system state if there is an AutoCAD command already
in progress when the AutoLISP expression is entered. In that case, the results of running UNDO may cause the command in progress
to fail or even crash AutoCAD.

## \*error\* Handler

If your \*error\* handler uses the
command function, consider updating the way you define your custom
\*error\* handlers using the following methods:

* *Substitute
  command-s for
  command in
  \*error\* handler*

  For typical
  \*error\* handler cases where the previous state of the program needs to be restored and a few batch commands are executed, you can
  substitute (command-s <...>) for
  (command <...>). The
  \*error\* handler is called from the same context as it always has been.

  The following demonstrates a based
  \*error\* handler using the
  command-s function:

  ```
  (defun my_err(s)
    (prompt "\
  ERROR: mycmd failed or was cancelled")
    (setvar "clayer" old_clayer)
    (command-s "._undo" "_e")
    (setq *error* mv_oer)
  )

  (defun c:mycmd ()
    (setq old_err *error*
          *error* my_err
          old_clayer (getvar "clayer")
    )

    (setq insPt (getpoint "\
  Specify text insertion: "))

    (if (/= insPt nil)
      (progn
        (command-s "._undo" "_be")
        (command-s "._-layer" "_m" "Text" "_C" "3" "" "")
        (command-s "._-text" insPt "" "0" "Sample Text")
        (command-s "._undo" "_e")
      )
    )

    (setvar "clayer" old_clayer)
    (setq *error* mv_oer)
   (princ)
  )
  ```
* *Retaining the use of the
  command function in
  \*error\* handler*

  If using the
  command-s function is not viable option, then the
  command function can still be used, but only at the expense of losing access to any local symbols that would normally be on the AutoLISP
  call stack at the time of the
  \*error\* processing.

  The following is an overview of what is required to continue to use the
  command function in the
  \*error\* handler.

  + When overriding the
    \*error\* symbol with a custom
    \*error\* handler, invoke the
    \*push-error-using-command\* function to inform AutoLISP that error handling will be used with the proceeding
    command functions.

    NOTE:Whenever an AutoLISP expression evaluation begins, the AutoLISP engine assumes that the
    command function will not be allowed within an
    \*error\* handler.
  + If the
    \*error\* handler refers to local symbols that are on the AutoLISP stack at the point where AutoLISP program failed or was cancelled,
    you must remove those references, or make the referenced symbols global symbols.

    All local symbols on the AutoLISP call stack are pushed out of scope because the AutoLISP evaluator is reset before entering
    the
    \*error\* handler.

  Now the
  command function can be used within the
  \*error\* handler.

  However, if your program actually pushes and pops error handlers as part of its operations, or your AutoLISP logic can be
  invoked while other unknown AutoLISP logic is invoked, there are a couple more steps you may have to make.

  + When restoring an old error handler, also invoke the
    \*pop-error-mode\* function to reverse the effects of any call to the
    \*push-error-using-command\* or
    \*push-error-using-stack\* functions.
  + If your logic has nested pushes and pops of the
    \*error\* handler, and an
    \*error\* handler has been set up to use the command function by invoking
    \*push-error-using-command\*, while the nested handler will not use it, you can provide access to the locally defined symbols on the AutoLISP stack by
    invoking
    \*push-error-using-stack\* at the same point where you set
    \*error\* to the current handler. If this is done, you must also invoke
    \*pop-error-mode\* after the old
    \*error\* handler is restored.

#### Related References

* [command (AutoLISP)](command-AutoLISP.md)
* [initcommandversion (AutoLISP)](initcommandversion-AutoLISP.md)
* [initdia (AutoLISP)](initdia-AutoLISP.md)
* [vl-cmdf (AutoLISP)](vl-cmdf-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*