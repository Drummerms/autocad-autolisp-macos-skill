# About Predefined Variables (AutoLISP)

AutoLISP has several predefined variables that can be used with your custom functions and commands.

You can change the value of these variables with the
setq function. However, other applications might rely on their values being consistent; therefore, it is recommended that you
do not modify these variables.

The following variables are predefined for use with AutoLISP applications:

* PAUSE - Defined as a constant string of a double backslash (\\) character. This variable is used with the command function to pause
  for user input.
* PI - Defined as the constant p (pi). It evaluates to approximately 3.14159.
* T - Defined as the constant
  T. This is used as a non-nil value.

NOTE:Visual LISP, by default, protects these variables from redefinition. You can override this protection through the Visual LISP
Symbol Service feature or by setting a Visual LISP environment option. The Visual LISP IDE is not available in AutoCAD LT
for Windows and on Mac OS.

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)
* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [About Nil Variables (AutoLISP)](About-Nil-Variables-AutoLISP.md)
* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*