# About DIESEL and Status Bar Customization

DIESEL (Direct Interpretively Evaluated String Expression Language) expressions take strings as input and generate string
results. Use DIESEL in menu macros to make decisions or display text on the status bar.

You can use DIESEL to alter the status bar through the MODEMACRO system variable and in menu items as a macro language instead
of AutoLISP ® .

NOTE:AutoLISP is not available in AutoCAD LT for Mac OS and the MODEMACRO system variable is not available on Mac OS.

Because DIESEL expressions handle strings exclusively, the USERS1-5 system variables are useful for passing information from
an AutoLISP routine to a DIESEL expression. DIESEL expressions are evaluated by AutoLISP routines through the use of the AutoLISP
menucmd function.

NOTE:The USERS1-5 system variables are not available in AutoCAD LT for Mac OS.

#### Topics in this section

* [About Responding to AutoLISP with DIESEL Expressions in Macros](About-Responding-to-AutoLISP-with-DIESEL-Expressions-in-Macros.md)

  You can use DIESEL string expressions as a way to provide responses to a command defined with AutoLISP or ObjectARX.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*