# About Protected Symbols (Visual LISP IDE)

When Visual LISP is loaded, you may be warned if you attempt to change the value of some symbols used by the AutoLISP language.

NOTE:The Visual LISP IDE is not available in AutoCAD LT for Windows and on Mac OS.

These symbols are known as protected symbols, and include items such as arithmetic operators (for example,
 *+* ,
 *-* ) and the values
T and
nil.

You can use the Visual LISP Symbol Service feature to determine if a symbol is protected. When you first start AutoCAD, protected
symbols receive no special protection. If you change a protected symbol at the AutoCAD Command prompt, no indication is made
that a symbol has any special status. However, once you start Visual LISP, this changes. From the moment you start Visual
LISP until the end of your AutoCAD session, Visual LISP intercepts any attempt to modify a protected symbol. Processing of
protected symbols depends on the status of a Visual LISP environment option.

You can specify one of the following options:

* *Transparent* - Protected symbols are treated like any other symbol.
* *Print message* - AutoLISP issues a warning message when you modify a protected symbol, but the modification is still carried out. For example,
  the following demonstrates what happens when you modify the predefined
  T variable:

  Command:
  *(setq t "look out")*

  ; \*U\* WARNING: assignment to protected symbol: T <- "look out"

  "look out"
* *Prompt to enter break loop* - Results in Visual LISP displaying the following message box when you attempt to modify a protected symbol:

  ![](../images/GUID-9FFC40A0-6215-4A32-AE47-743F03593827-low.png)

  Click Yes to interrupt processing and enter a Visual LISP break loop. Control switches to the Visual LISP Console window.
  To set the symbol and continue processing, click the Continue button on the Visual LISP toolbar; to abort modification, click
  Reset. If you click No, the symbol's value is modified, and processing continues normally.
* *Error* - This option prohibits modification of protected symbols. Any attempt to modify a protected symbol results in an error message.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*