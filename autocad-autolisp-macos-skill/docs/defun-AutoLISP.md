# defun (AutoLISP)

Defines a function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(defun sym ([arguments] [/ variables ...]) expr ...)
```

*sym*
:   *Type:* Symbol

    A symbol naming the function.

*arguments*
:   *Type:* Integer, Real, String, List, T, or nil

    The names of arguments expected by the function.

*/ variables*
:   *Type:* Symbol

    The names of one or more local variables for the function.

    The slash preceding the variable names must be separated from the first local name and from the last argument, if any, by
    at least one space.

*expr*
:   *Type:* List

    Any number of AutoLISP expressions to be evaluated when the function executes.

## Return Values

The result of the last expression evaluated.

IMPORTANT:Never use the name of a built-in function or symbol for the
*sym* argument to
defun. This overwrites the original definition and makes the built-in function or symbol inaccessible. To get a list of built-in
and previously defined functions, use the
atoms-family function.

## Remarks

If you do not declare any arguments or local symbols, you must supply an empty set of parentheses after the function name.

If duplicate argument or symbol names are specified, AutoLISP uses the first occurrence of each name and ignores the following
occurrences.

## Examples

```
(defun myfunc (x y) ...)         Function takes two arguments
(defun myfunc (/ a b) ...)       Function has two local variables
(defun myfunc (x / temp) ...)    One argument, one local variable
(defun myfunc () ...)            No arguments or local variables
```

#### Related References

* [defun-q (AutoLISP)](defun-q-AutoLISP.md)
* [vl-acad-defun (AutoLISP)](vl-acad-defun-AutoLISP.md)
* [vl-acad-undefun (AutoLISP)](vl-acad-undefun-AutoLISP.md)
* [vlax-add-cmd (AutoLISP/ActiveX)](vlax-add-cmd-AutoLISP-ActiveX.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)
* [About Compatibility of Defun with Earlier Releases of AutoCAD (AutoLISP)](About-Compatibility-of-Defun-with-Earlier-Releases-of-AutoCAD-AutoLISP.md)
* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*