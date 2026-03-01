# Tutorial: Getting Started (AutoLISP)

Creating custom routines with the AutoLISP programming language is an excellent way for you to automate and extend the program
to the way that you want to work.

AutoLISP is based on the LISP (LISt Processing) programming language. A list is a structure enclosed by parentheses. The elements
in a list can be one or more of the following:

* A function such as a programming operation, mathematical function, or a list manipulation operation
* Values such as an AutoCAD command or system variable name, text string, integer or real number, or coordinate
* Another list

Usually, the first element in the list is the name of a function, and the following elements are called
*arguments*, which provide the values that the function will process.

The following shows the syntax that is used for an AutoLISP expression:

```
(function_name [argument1 argumentX …])
```

The program's help system contains a list of the available functions that can be used in an AutoLISP program. Each function
topic, includes information about

* How to use a function,
* The type of data and number of arguments a function expects,
* Which arguments are optional
* The type of data that a function returns.

Most function topics also include example code to help you get started with that function.

At first glance, the syntax used by AutoLISP expressions in a program can be intimidating but with a little bit of practice
and time you will get used to it. In addition to an AutoLISP expression starting with a
( (open parenthesis), an expression can also start with the
! character. The
! (exclamation point) character can only be used at the AutoCAD Command prompt and is used to return the current value of an
AutoLISP variable.

The following are some examples of AutoLISP expressions:

* (setq dRadius 1.25)
* !dRadius
* (command "circle" "0,0" dRadius)

## Nested Expressions

As an AutoLISP program grows in complexity, so will the expressions that you create. AutoLISP expressions can be nested inside
of each other. When expressions are nested, they are always evaluated from the innermost expression to the outermost. The
evaluation process of AutoLISP expressions is similar to the order of operations in mathematics.

The following is an example of a nested mathematical expression in AutoLISP:

```
(+ 0.01 (* 2 0.875))
```

In this example, the innermost expression (\* 2 0.875) is evaluated first. The two numbers are multiplied together, and the
\* (product or multiplication) function returns a value of 1.75. AutoLISP then evaluates the outer expression as (+ 0.01 1.75).
After the two numbers are added together, AutoLISP returns a final value of 1.76.

The following are other examples of nested expressions:

```
(setq nDist (getreal "\
Enter a distance: "))
```

The
getreal function prompts the user for a real numeric value. The value provided is then passed to the
setq function and assigned to the
nDist user-defined variable.

```
(alert (strcat "Welcome " "to " "AutoLISP!"))
```

The
strcat function combines all the strings into a single string value. The value returned by the
strcat function is then passed to the
alert function and displayed in a message box.

## Working with AutoLISP Expressions at the Command Prompt

1. At the Command prompt, enter
   *!dRadius*.

   AutoLISP returns the value stored in the
   dRadius user-defined variable. If the variable has not been defined yet or has no value, then a value of
   nil is returned.
2. At the Command prompt, enter
   *(setq dRadius 1.25)*.

   AutoLISP creates a user-defined variable named
   dRadius and assigns it the value of 1.25. The
   setq function returns a value of 1.25, which is the value assigned to the variable.
3. At the Command prompt, enter
   *!dRadius*.

   AutoLISP returns the value stored in the user-defined variable, which is a value of 1.25.
4. At the Command prompt, enter
   *(command ".\_circle" "0,0" dRadius)*.

   AutoLISP starts the AutoCAD CIRCLE command, and passes the command two values. The value of “0,0” is used to define the location
   of the circle's center point and
   dRadius is used to specify the radius of the circle. Since
   dRadius has a value of 1.25, the radius of the circle is set to 1.25.
5. At the Command prompt, enter
   *(setq pt (getpoint "\
   Specify the circle's center point: "))*.

   AutoLISP prompts you for a coordinate value. You can enter a coordinate value using the keyboard or click in the drawing area.
   The coordinate value provided is assigned to the
   pt variable.
6. At the Command prompt, enter
   *(command ".\_circle" pt dRadius)*.

   AutoLISP starts the AutoCAD CIRCLE command, and the command uses the values assigned to both the
   pt and
   dRadius variables.

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [AutoLISP and Visual LISP (AutoLISP)](AutoLISP-and-Visual-LISP-AutoLISP.md)
* [Related Developer References (AutoLISP)](Related-Developer-References-AutoLISP.md)
* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*