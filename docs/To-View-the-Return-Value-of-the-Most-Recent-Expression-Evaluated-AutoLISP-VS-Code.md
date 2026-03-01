# To View the Return Value of the Most Recent Expression Evaluated (AutoLISP/VS Code)

NOTE:Debugging is not available in AutoCAD LT.

While debug is active and as you step through AutoLISP expressions, you can watch the return value of the most recently evaluated
expression using the
\*last-value\* variable. The
\*last-value\* variable must be added manually to the Watch section.

1. In Visual Studio Code,
   [start debugging an AutoLISP source (LSP) file](To-Launch-and-Attach-an-Instance-of-AutoCAD-to-VS-Code-for-Debugging-AutoLISP-VS-Code.md).
2. On the Activity Bar, click Debug and Run (or click View menu > Debug).
3. In the Watch section, right-click (or secondary click on Mac OS) and choose Add Expression.
4. In the in-place editor, type
   *\*last-value\** and press Enter.

   ![](../images/GUID-73BE090F-31E3-4FC5-A29F-66F2E63CAB29-low.png)

   Now, when debug is active and execution is interrupted with a breakpoint, the value of the most recently evaluated expression
   will be displayed adjacent to the
   \*last-value\* variable in the Watch section.

#### Related Information

* [Configuring VS Code (AutoLISP/VS Code)](Configuring-VS-Code-AutoLISP-VS-Code.md)
* [To Launch and Attach an Instance of AutoCAD to VS Code for Debugging (AutoLISP/VS Code)](To-Launch-and-Attach-an-Instance-of-AutoCAD-to-VS-Code-for-Debugging-AutoLISP-VS-Code.md)
* [To Add, Remove, or Disable a Breakpoint while Debugging an LSP File (AutoLISP/VS Code)](To-Add,-Remove,-or-Disable-a-Breakpoint-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Watch Variables and Expressions while Debugging an LSP File (AutoLISP/VS Code)](To-Watch-Variables-and-Expressions-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*