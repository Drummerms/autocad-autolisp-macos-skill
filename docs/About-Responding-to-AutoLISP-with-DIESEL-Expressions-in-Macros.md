# About Responding to AutoLISP with DIESEL Expressions in Macros

You can use DIESEL string expressions as a way to provide responses to a command defined with AutoLISP or ObjectARX.

DIESEL expressions return string values (text strings) that can be used as a response to standard commands, AutoLISP, and
ObjectARX ®  routines, and other macros.

NOTE:AutoLISP is not available in AutoCAD LT for Mac OS and ObjectARX is not available in AutoCAD LT.

The value returned by a DIESEL expression is a text string, it can be used in response to an AutoLISP
get*XXX* or ObjectARX
acetGet*XXX* function call. This functionality enables menu items to evaluate current drawing conditions and to return a value to an AutoLISP
or ObjectARX routine.

If you load and execute the following sample AutoLISP routine, the program prompts for a symbol name and size, and a location
in the drawing.

```
(defun C:SYMIN()
  (setq sym
    (getstring
      "\
Enter symbol name: ")      ; Prompts for a symbol name
  )

  (setq
    siz (getreal
          "\
Select symbol size: ") ; Prompts for a symbol size

    p1 (getpoint
          "\
Insertion point: ")    ; Prompts for insertion point
  )

  (command "._insert"               ; Issues the INSERT command
           sym                      ; using the desired symbol
           p1 siz siz 0)            ; insertion point, and size

 (princ)                            ; Exits quietly
)
```

NOTE:An AutoLISP routine that you use regularly should include error checking to verify the validity of user input.

While the previous example is being executed, you can click user interface elements that execute a DIESEL expression in response
to one of the prompts. For example, you might use the expression
$M=$(\*,$(getvar,dimscale),0.375) to use a scale factor that is 3/8 that of the current DIMSCALE.

This cannot be done with similar AutoLISP code; a value returned by an AutoLISP expression cannot typically be used as a response
to a
get*XXX* function call (such as, the
getreal function in the preceding sample).

#### Related References

* [DIESEL Functions Reference](DIESEL-Functions-Reference.md)
* [DIESEL Error Message Reference](DIESEL-Error-Message-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About DIESEL Expressions in Macros](About-DIESEL-Expressions-in-Macros.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*