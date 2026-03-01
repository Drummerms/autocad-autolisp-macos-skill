# About Displaying Messages (AutoLISP)

AutoLISP programs often need to inform the user of an error or request for input.

Messages that are displayed should try and not interrupt the flow of a command, and when they do the text displayed should
be short and precise as to what the problem is or the input that is being requested. AutoLISP offers the following functions
to display messages to the user:

* prompt - Displays string at the AutoCAD Command prompt.
* princ - Displays a value at the AutoCAD Command prompt or to an open file. Strings are displayed without the enclosing quotation
  marks.
* prin1 - Displays a value at the AutoCAD Command prompt or to an open file. Strings are enclosed in quotation marks.
* print - Displays a value at the AutoCAD Command prompt or to an open file, but a blank line is placed before the value and a space
  is placed after the value. Strings are enclosed in quotation marks.
* alert - Displays a dialog box containing an error or warning message.
* terpri - Prints a newline to the AutoCAD Command prompt.

The
write-char,
write-line,
get*XXX*, and
entsel functions can also display messages at the AutoCAD Command prompt.

When entered from the Visual LISP Console window prompt, the prompt function displays a message (a string) in the AutoCAD
Command window and returns nil to the Visual LISP Console window. The
princ,
prin1, and
print functions all display a value (not necessarily a string) in the AutoCAD Command prompt and returns the value to the Visual
LISP Console window.

NOTE:The Visual LISP IDE is not available in AutoCAD LT for Windows and on Mac OS.

The following examples demonstrate the differences between the basic output functions and how they handle the same string
of text.

```
(setq str "The \"allowable\" tolerance is \261 \274\"")
(prompt str) outputs The "allowable" tolerance is 1/4"
returns nil

(princ str) outputs The "allowable" tolerance is 1/4"
returns "The \"allowable\" tolerance is 1/4\""

(prin1 str) outputs "The \"allowable\" tolerance is 1/4""
returns "The \"allowable\" tolerance is 1/4\""

(print str) outputs<blank line> "The \"allowable\" tolerance is 1/4""<space>
returns "The \"allowable\" tolerance is 1/4\""
```

#### Topics in this section

* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)

  If you invoke the princ function without passing an expression to it, it displays nothing and has no value to return.

#### Related Concepts

* [About Control Characters in Strings (AutoLISP)](About-Control-Characters-in-Strings-AutoLISP.md)
* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)
* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)
* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*