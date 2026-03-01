# Function-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP function-handling functions.

| Function-handling functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(apply function lst)](apply-AutoLISP.md) | Passes a list of arguments to a specified function | ✓ | ✓ | ✓ | -- | ✓ |
| [(defun sym ([arguments] [/variables ...]) expr ... )](defun-AutoLISP.md) | Defines a function | ✓ | ✓ | ✓ | -- | ✓ |
| [(defun-q sym ([arguments] [/ variables ...]) expr ...)](defun-q-AutoLISP.md) | Defines a function as a list (intended for backward-compatibility only) | ✓ | ✓ | ✓ | -- | ✓ |
| [(defun-q-list-ref 'function)](defun-q-list-ref-AutoLISP.md) | Displays the list structure of a function defined with defun-q | ✓ | ✓ | ✓ | -- | ✓ |
| [(defun-q-list-set 'sym list)](defun-q-list-set-AutoLISP.md) | Defines a function as a list (intended for backward-compatibility only) | ✓ | ✓ | ✓ | -- | ✓ |
| [(eval expr)](eval-AutoLISP.md) | Returns the result of evaluating an AutoLISP expression | ✓ | ✓ | ✓ | -- | ✓ |
| [(lambda arguments expr ...)](lambda-AutoLISP.md) | Defines an anonymous function | ✓ | ✓ | ✓ | -- | ✓ |
| [(progn [expr ...])](progn-AutoLISP.md) | Evaluates each expression sequentially, and returns the value of the last expression | ✓ | ✓ | ✓ | -- | ✓ |
| [(trace function ...)](trace-AutoLISP.md) | Aids in AutoLISP debugging | ✓ | ✓ | ✓ | -- | ✓ |
| [(untrace function ...)](untrace-AutoLISP.md) | Clears the trace flag for the specified functions | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*