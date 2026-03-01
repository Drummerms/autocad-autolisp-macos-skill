# About Formatting and Spaces in Code (AutoLISP)

AutoLISP code can span multiple lines, and contain empty lines and extra spaces. Empty lines and extra spaces do not have
any significant meaning, but can make your code easier to read.

Multiple spaces between function and variable names, and constants are equivalent to a single space. The end of a line and
tab is also treated as a single space. The following two expressions produce the same result:

```
(setq test1 123 test2 456)

(setq
  test1 123
  test2 456
)
```

The extensive use of parentheses in AutoLISP code can make it difficult to read. The traditional techniques for combatting
this confusion is indentation, and to align the open and close parentheses of a function. The more deeply nested a line of
code is, the farther to the right the line is positioned.

The following two functions are the same code, but the second one is much easier to read and determine visually if the parentheses
of the AutoLISP expressions are balanced.

```
(defun c:mycmd ()
(setq old_clayer (getvar "clayer"))
(setq insPt (getpoint "\
Specify text insertion: "))
(if (/= insPt nil)
(progn
(command "_.UNDO" "_BE")
(command "._-LAYER" "_M" "Text" "_C" "3" "" "")
(command "_.-TEXT" insPt "" "0" "Sample Text")
(command "_.UNDO" "_E")))
(setvar "clayer" old_clayer)
(princ)
)

(defun c:mycmd ()
  (setq old_clayer (getvar "clayer"))

  (setq insPt (getpoint "\
Specify text insertion: "))

  (if (/= insPt nil)
    (progn
      (command "_.UNDO" "_BE")
      (command "._-LAYER" "_M" "Text" "_C" "3" "" "")
      (command "_.-TEXT" insPt "" "0" "Sample Text")
      (command "_.UNDO" "_E")
    )
  )

  (setvar "clayer" old_clayer)
 (princ)
)
```

#### Related Tasks

* [To Create and Open AutoLISP Source Code Files (AutoLISP)](To-Create-and-Open-AutoLISP-Source-Code-Files-AutoLISP.md)

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [About Source Code Files (AutoLISP)](About-Source-Code-Files-AutoLISP.md)
* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Comments in AutoLISP Program Files (AutoLISP)](About-Comments-in-AutoLISP-Program-Files-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*