# About Compatibility of Defun with Earlier Releases of AutoCAD (AutoLISP)

The internal implementation of defun changed in AutoCAD 2000.

This change is transparent to the great majority of AutoLISP users upgrading from earlier AutoCAD releases. The change only
affects AutoLISP code that manipulated defun definitions as a list structure, such as by appending one function to another, as in the following code:

```
(append s::startup (cdr mystartup))
```

For situations like this, you can use defun-q to define your functions. An attempt to use a defun function as a list results in an error. The following example illustrates the error:

```
(defun foo (x) 4)
foo

(append foo '(3 4))
; error: Invalid attempt to access a compiled function definition.
You may want to define it using defun-q: #<SUBR @024bda3c FOO>
```

The error message alerts you to the possibility of using defun-q instead of defun. The defun-q function is provided strictly for backward compatibility with earlier releases and should not be used for other purposes.

#### Related Concepts

* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [About Functions with Arguments (AutoLISP)](About-Functions-with-Arguments-AutoLISP.md)
* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*