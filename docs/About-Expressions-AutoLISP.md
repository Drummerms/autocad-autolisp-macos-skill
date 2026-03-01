# About Expressions (AutoLISP)

An expression is the basic structure that is used when working with AutoLISP.

AutoLISP expressions have the following form:

```
(function arguments)
```

Each expression:

* Begins with an open (left) parenthesis.
* Consists of a function name and optional arguments for that function. Each argument can also be an expression.
* Ends with a close (right) parenthesis.
* Returns a value that can be used by a surrounding expression. The value of the last interpreted expression is returned to
  the calling expression.

For example, the following code example involves three functions:

```
(fun1 (fun2 arguments)(fun3 arguments))
```

The first function,
fun1, has two arguments, which in this example are expressions. The values returned by the expressions are used by
fun1. The other functions,
fun2 and
fun3, each have one argument. AutoLISP evaluates the innermost expression first, working its way outward. For this example, expressions
containing
fun2 and
fun3 are evaluated before
fun1.

The following example shows the use of the
 *\**  (multiplication) function, which accepts one or more numbers as arguments:

```
(* 2 27)
54
```

Because this code example has no surrounding expression, AutoLISP returns the result to the window from which you entered
the code.

Expressions nested within other expressions return their result to the surrounding expression.

The following example uses the result from the
 *+*  (addition) function as one of the arguments for the
 *\**  (multiplication) function.

```
(* 2 (+ 5 10))
30
```

In the previous example,
(+ 5 10) returns a value of 5. After the innermost expression is evaluated, the AutoLISP interpreter sees the following:

```
(* 2 15)
30
```

## Entering AutoLISP Expressions

AutoLISP expressions can be entered directly at the AutoCAD Command prompt, loaded with an AutoLISP source (LSP) file, or
evaluated with the Visual LISP Editor (AutoCAD for Windows only). When you type an open (left) parenthesis, you indicate to
AutoCAD that the following text should be passed to the AutoLISP interpreter for evaluation.

NOTE:The Visual LISP Editor is not available for AutoCAD LT for Windows or on Mac OS.

If you enter the incorrect number of close (right) parentheses, AutoLISP displays the following prompt:

```
(_>
```

The number of open parentheses in this prompt indicates how many levels of open parentheses remain unclosed. If this prompt
appears, you must enter the required number of close parentheses for the expression to be evaluated.

```
(* 2 (+ 5 10
((_> ) )
30
```

A common mistake is to omit the closing quotation mark (") in a text string, in which case the close parentheses are interpreted
as part of the string and have no effect in resolving the open parentheses. To correct this condition, press Shift+Esc to
cancel the function, then re-enter it correctly.

#### Topics in this section

* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)

  Reference topics in the documentation use a consistent convention to describe the proper syntax for an AutoLISP function.

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Formatting and Spaces in Code (AutoLISP)](About-Formatting-and-Spaces-in-Code-AutoLISP.md)
* [About Symbols and Variables (AutoLISP)](About-Symbols-and-Variables-AutoLISP.md)
* [About Functions with Arguments (AutoLISP)](About-Functions-with-Arguments-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*