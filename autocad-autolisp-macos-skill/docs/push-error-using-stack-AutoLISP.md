# \*push-error-using-stack\* (AutoLISP)

Error-handling function that indicates the use of variables from the AutoLISP stack within a custom
\*error\* handler

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(*push-error-using-stack*)
```

No arguments.

## Return Values

*Type:* T

A value of
T is returned.

## Remarks

Allows access to the local AutoLISP variables on the stack defined within the function where the error occurred from your
custom
\*error\* handler. A call to the
\*push-error-using-stack\* function overrides a previous call to
\*push-error-using-command\*.

If
\*push-error-using-command\* or
\*push-error-using-stack\* are not called, by default AutoLISP works as if
\*push-error-using-stack\* was called.

NOTE:This function cannot be used when the
command function is used within the local custom
\*error\* handler.

## Examples

The following example demonstrates the use of the
\*push-error-using-stack\* function.

```
(setq var1 "Global1"      ; Set some global variables
      var2 "Global2")

(defun mySub_err (err_msg)
    (if (/= err_msg "Function cancelled")
      (progn
        (prompt (strcat "\
Error: " err_msg))
        (prompt (strcat "\
LocalSub1: " var1))
        (prompt (strcat "\
LocalSub2: " var2))
        (terpri)
      )
    )

    (command-s "._undo" "_e")
    (command-s "._U")
    (setq *error* olderr)
  (princ)
)

(defun subUtil (val / olderr var1 var2)
    (*push-error-using-stack*)         ; Indicates if the custom error handler has access to local
                                       ; variables defined in his function

    (setq olderr *error*
          *error* mySub_err)

    (command "._undo" "_group")        ; The following will not be executed in this sample, but is good
                                       ; framework for setting up your own error handlers

    (setq var1 "Sub1"                  ; Set some local variables
          var2 "Sub2")

    ;; Perform your tasks here
    (strcat "Foo" val)

    (command "._undo" "_e")
    (setq *error* olderr)              ; Restore old *error* handler
    (*pop-error-mode*)                 ; End the use of *push-error-using-command*
)

(defun my_err (err_msg)
    (if (/= err_msg "Function cancelled")
      (progn
        (prompt (strcat "\
Error: " err_msg))
        (prompt (strcat "\
Local1: " var1))
        (prompt (strcat "\
Local2: " var2))
        (terpri)
      )
    )

    (command "._undo" "_e")
    (command "._U")
    (setq *error* olderr)
  (princ)
)

(defun myUtil (val / var1 var2)
    (setq olderr *error*
          *error* my_err)

    (*push-error-using-command*)       ; Indicate use of Command function instead of Command-s
                                       ; in the custom error handler

    (setq var1 "Local1"                ; Set some local variables
          var2 "Local2")

    (command "._undo" "_group")        ; The following will not be executed in this sample, but is good
                                       ; framework for setting up your own error handlers

    (subUtil val)                      ; Call to a custom function that uses *push-error-using-stack*

    (/ 1 0)                            ; Call a function with incorrect values to trigger the custom error handler
                                       ; Remove when setting up your code

    ;; Perform your tasks here

    (command "._undo" "_e")
    (setq *error* olderr)              ; Restore old *error* handler
    (*pop-error-mode*)                 ; End the use of *push-error-using-command*
)
```

After loading the sample code, enter
*(myutil 1)* at the Command prompt to enter the error handler for the nested function and
*(myutil “String”)* to test the error handler of the main function.

#### Related References

* [\*pop-error-mode\* (AutoLISP)](pop-error-mode-AutoLISP.md)
* [\*push-error-using-command\* (AutoLISP)](push-error-using-command-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*