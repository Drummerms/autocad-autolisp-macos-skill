# defun-q (AutoLISP)

Defines a function as a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(defun-q sym ([arguments] [/ variables ...]) expr ...)
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

*Type:* List or Symbol

The result of the last expression evaluated.

## Remarks

The
defun-q function is provided strictly for backward-compatibility with previous versions of AutoLISP, and should not be used for other
purposes. You can use
defun-q in situations where you need to access a function definition as a list structure, which is the way
defun was implemented in previous, non-compiled versions of AutoLISP.

If you do not declare any arguments or local symbols, you must supply an empty set of parentheses after the function name.

If duplicate argument or symbol names are specified, AutoLISP uses the first occurrence of each name and ignores the following
occurrences.

## Examples

```
(defun-q my-startup (x) (print (list x)))
MY-STARTUP

(my-startup 5)
(5) (5)
```

Use
defun-q-list-ref to display the list structure of
my-startup:

```
(defun-q-list-ref 'my-startup)
((X) (PRINT (LIST X)))
```

#### Related References

* [defun-q-list-set (AutoLISP)](defun-q-list-set-AutoLISP.md)
* [defun-q-list-ref (AutoLISP)](defun-q-list-ref-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)
* [About Compatibility of Defun with Earlier Releases of AutoCAD (AutoLISP)](About-Compatibility-of-Defun-with-Earlier-Releases-of-AutoCAD-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*