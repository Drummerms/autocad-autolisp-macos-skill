# trace (AutoLISP)

Aids in AutoLISP debugging

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(trace [function ...])
```

*function*
:   *Type:* Symbol

    A symbol that names a function. If no argument is supplied,
    trace has no effect.

## Return Values

*Type:* Symbol or nil

The last function name passed to
trace. If no argument is supplied,
trace returns
nil.

## Remarks

The
trace function sets the trace flag for the specified functions. Each time a specified function is evaluated, a trace display appears
showing the entry of the function (indented to the level of calling depth) and prints the result of the function.

Trace output is sent one of the following locations

* AutoCAD Command Line window; when Visual LISP is not active in AutoCAD on Windows
* Visual LISP Trace window (Not available in AutoCAD LT for Windows, or on Mac OS and Web)

NOTE:Once you start Visual LISP during an AutoCAD session, it remains active until you exit AutoCAD. Therefore, all
trace output prints in the Visual LISP Trace window for the remainder of that AutoCAD session. Exiting or closing Visual LISP while
AutoCAD is running only closes the IDE windows and places Visual LISP in a quiescent state; it does not result in a true shutdown.
You must reopen Visual LISP to view the output in the Trace window.

Use
untrace to turn off the trace flag.

## Examples

Define a function named
foo and set the trace flag for the function:

```
(defun foo (x) (if (> x 0) (foo (1- x))))
FOO

(trace foo)
FOO
```

Invoke
foo and observe the results:

```
(foo 3)
Entering (FOO 3)
Entering (FOO 2)
Entering (FOO 1)
Entering (FOO 0)
Result: nil
Result: nil
Result: nil
Result: nil
```

Clear the trace flag by invoking
untrace:

```
(untrace foo)
FOO
```

#### Related References

* [untrace (AutoLISP)](untrace-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*