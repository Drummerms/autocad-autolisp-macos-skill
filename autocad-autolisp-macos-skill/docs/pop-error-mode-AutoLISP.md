# \*pop-error-mode\* (AutoLISP)

Error-handling function that ends the previous call to
\*push-error-using-command\* or
\*push-error-using-stack\*

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(*pop-error-mode*)
```

No arguments.

## Return Values

*Type:* T

A value of
T is returned.

## Remarks

A call to
\*pop-error-mode\* should be made after replacing a custom
\*error\* handler function with the previously defined
\*error\* handler.

NOTE:This function is not required when using the
command-s function in an
\*error\* handler.

## Examples

The following example demonstrates the use of the
\*pop-error-mode\* function.

```
(defun my_err (err_msg)
    (if (/= err_msg "Function cancelled")
      (prompt (strcat "\
Error: " err_msg))
    )
    (command "._undo" "_e")
    (command "._U")
    (setq *error* olderr)
  (princ)
)

(defun myUtil (key / )
    (setq olderr *error*
          *error* my_err)
    (*push-error-using-command*)         ; Indicate use of the command function instead of command-s
                                         ; in a custom error handler

    (command "._undo" "_group")          ; The following will not be executed in this sample, but is good
                                         ; framework for setting up your own error handlers

    (/ 1 0)                              ; Call a function with incorrect values to trigger the custom error handler
                                         ; Remove when setting up your code

    ;; Perform your tasks here

    (command "._undo" "_e")
    (setq *error* olderr)                ; Restore old *error* handler
    (*pop-error-mode*)                   ; End the use of *push-error-using-command*
)
```

After loading the sample code, enter
*(myutil “String”)* at the Command prompt to enter the error handler.

#### Related References

* [\*push-error-using-command\* (AutoLISP)](push-error-using-command-AutoLISP.md)
* [\*push-error-using-stack\* (AutoLISP)](push-error-using-stack-AutoLISP.md)

#### Related Concepts

* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*