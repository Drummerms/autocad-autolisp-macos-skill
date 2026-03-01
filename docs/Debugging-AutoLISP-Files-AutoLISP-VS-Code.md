# Debugging AutoLISP Files (AutoLISP/VS Code)

The AutoCAD program ships with a utility called the
*AutoLISP Debug Adapter* which allows VS Code and AutoCAD to communicate with each other.

NOTE:Debugging is not available in AutoCAD LT.

Communication between VS Code and AutoCAD is established when either of the AutoLISP debug configurations are used. These
debug configurations can be defined by following the steps in
[To Setup the AutoCAD AutoLISP Extension for Debug](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md).

When an instance of AutoCAD is launched or attached to using one of the debug configurations you can:

* Add breakpoints and interrupt the execution of an AutoLISP program to evaluate its current state
* Evaluate selected expressions
* Load an AutoLISP source (LSP) file into AutoCAD
* Watch local and global variables during the execution of an AutoLISP program
* Inspect the call stack of an AutoLISP program
* Execute AutoLISP functions and AutoCAD commands in the Debug Console

## Supported VS Code Debug Features

The following is a list of debug features that are supported by the AutoCAD AutoLISP Extension:

* View the call stack, including switching the stack frame
* Evaluate variables in the Watch window
* Inspect the current value of a variable when the mouse cursor is positioned it in the editor window
* See function parameters in the Variable window
* Add, remove, and disable breakpoints
* Step into, step out, and step over expressions
* Run to cursor
* Run-time error and syntax checking
* View the value of the last executed expression via the
  \*LAST-VALUE\* variable

## VS Code Debug Features Not Supported

The following is a list of debug features that are not supported by the AutoCAD AutoLISP Extension:

* Pause
* Conditional and data breakpoints
* Set variables
* Log points
* Memory and assemble codes

#### Topics in this section

* [To Launch and Attach an Instance of AutoCAD to VS Code for Debugging (AutoLISP/VS Code)](To-Launch-and-Attach-an-Instance-of-AutoCAD-to-VS-Code-for-Debugging-AutoLISP-VS-Code.md)
* [To Add, Remove, or Disable a Breakpoint while Debugging an LSP File (AutoLISP/VS Code)](To-Add,-Remove,-or-Disable-a-Breakpoint-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Load an LSP File into AutoCAD while Debugging (AutoLISP/VS Code)](To-Load-an-LSP-File-into-AutoCAD-while-Debugging-AutoLISP-VS-Code.md)
* [To Watch Variables and Expressions while Debugging an LSP File (AutoLISP/VS Code)](To-Watch-Variables-and-Expressions-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To View the Return Value of the Most Recent Expression Evaluated (AutoLISP/VS Code)](To-View-the-Return-Value-of-the-Most-Recent-Expression-Evaluated-AutoLISP-VS-Code.md)
* [To Access the Call Stack while Debugging an LSP File (AutoLISP/VS Code)](To-Access-the-Call-Stack-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Evaluate Selected Expressions while Debugging an LSP File (AutoLISP/VS Code)](To-Evaluate-Selected-Expressions-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Evaluate AutoLISP Expressions in the Debug Console (AutoLISP/VS Code)](To-Evaluate-AutoLISP-Expressions-in-the-Debug-Console-AutoLISP-VS-Code.md)

#### Related Information

* [Getting Started with Visual Studio Code (AutoLISP/VS Code)](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)
* [Configuring VS Code (AutoLISP/VS Code)](Configuring-VS-Code-AutoLISP-VS-Code.md)
* [FAQ: When I Click Debug, Why Doesn’t the Debug Operation Start or it Starts but Fails? (AutoLISP/VS Code)](FAQ-When-I-Click-Debug,-Why-Doesn’t-the-Debug-Operation-Start-or-it-Starts-but-Fails-AutoLISP-VS-Cod.md)
* [Tutorial: Debugging LSP Files with the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Debugging-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*