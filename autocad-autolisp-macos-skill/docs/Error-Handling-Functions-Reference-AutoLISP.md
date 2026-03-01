# Error-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP error-handling functions.

| Error-handling functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(\*error\* string)](error-AutoLISP.md) | A user-definable error-handling function | ✓ | ✓ | ✓ | -- | ✓ |
| [(\*pop-error-mode\*)](pop-error-mode-AutoLISP.md) | Error-handling function that ends the previous call to \*push-error-using-command\* or \*push-error-using-stack\* | ✓ | ✓ | ✓ | -- | ✓ |
| [(\*push-error-using-command\*)](push-error-using-command-AutoLISP.md) | Error-handling function that indicates the use of the command function within a custom \*error\* handler | ✓ | ✓ | ✓ | -- | ✓ |
| [(\*push-error-using-stack\*)](push-error-using-stack-AutoLISP.md) | Error-handling function that indicates the use of variables from the AutoLISP stack within a custom \*error\* handler | ✓ | ✓ | ✓ | -- | ✓ |
| [(alert string)](alert-AutoLISP.md) | Displays an alert dialog box with the error or warning message passed as a string | ✓ | ✓ | ✓ | -- | / - supported, but doesn't display the alert box |
| [(exit)](exit-AutoLISP.md) | Forces the current application to quit | ✓ | ✓ | ✓ | -- | ✓ |
| [(quit)](quit-AutoLISP.md) | Forces the current application to quit | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-catch-all-apply 'function list)](vl-catch-all-apply-AutoLISP.md) | Passes a list of arguments to a specified function and traps any exceptions | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-catch-all-error-message error-obj)](vl-catch-all-error-message-AutoLISP.md) | Returns a string from an error object | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-catch-all-error-p arg)](vl-catch-all-error-p-AutoLISP.md) | Determines whether an argument is an error object returned from vl-catch-all-apply | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*