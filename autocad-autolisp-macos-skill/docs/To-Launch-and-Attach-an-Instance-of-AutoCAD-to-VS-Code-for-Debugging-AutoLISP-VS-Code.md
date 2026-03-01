# To Launch and Attach an Instance of AutoCAD to VS Code for Debugging (AutoLISP/VS Code)

NOTE:Debugging is not available in AutoCAD LT.

1. In Visual Studio Code, open and activate an editor window that contains the AutoLISP source code to debug.
2. On the Activity Bar, click Debug and Run (or click View menu > Debug).

   ![](../images/GUID-E1D15D6B-BD14-406F-9527-CEC7F47A3C67-low.png)
3. Click the Configurations drop-down list and choose one of the following configurations:
   * *AutoLISP Debug: Launch* – Launches a new instance of AutoCAD and attaches VS Code to that instance
   * *AutoLISP Debug: Attach* – Allows you to attach VS Code to an instance of AutoCAD that is already running

   ![](../images/GUID-C4ED461F-B7BC-46D9-B665-FB061B5F8B86-low.png)
4. Click Start Debugging or press F5.

   ![](../images/GUID-379948F1-FB7F-4249-8D9C-B6FF6A4B3340-low.png)

   A new instance of AutoCAD is started if you choose AutoLISP Debug: Launch from the Configurations list.
5. If you choose AutoLISP Debug: Attach from the Configurations list, choose acad (or AutoCAD on Mac OS) from the list of running
   processes.

   ![](../images/GUID-14BF4585-75A1-4312-B3D4-682FD0CBD71C-low.png)

Whether you start debugging with the AutoLISP Debug: Launch or AutoLISP Debug: Attach configuration, VS Code should now be
attached to an instance of the AutoCAD application. Once attached to AutoCAD, you should see the Debug toolbar displayed above
the active editor window.

![](../images/GUID-7EADC022-177F-4989-BE69-25C32FF98BD9-low.png)

The Debug toolbar contains these tools:

* *Continue* – Continues the execution of the AutoLISP program to the next breakpoint
* *Step Over* – An entire expression (and all nested expressions) are evaluated, then execution stops at the end of the overall expression
* *Step In* – Execution begins and halts before evaluation of the inner parenthetical expression
* *Step Out* – Execution resumes executing the rest of the expressions within a function and then execution halts on the outermost parenthetical
  expression
* *Restart* – Terminates and restarts the debugging operation; the AutoLISP source (LSP) file in the active window is automatically reloaded
  into the AutoCAD application
* *Disconnect/Stop* – Terminates the debugging operation and disconnects VS Code from the AutoCAD application

#### Related Information

* [Configuring VS Code (AutoLISP/VS Code)](Configuring-VS-Code-AutoLISP-VS-Code.md)
* [To Setup the AutoCAD AutoLISP Extension for Debug (AutoLISP/VS Code)](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md)
* [To Add, Remove, or Disable a Breakpoint while Debugging an LSP File (AutoLISP/VS Code)](To-Add,-Remove,-or-Disable-a-Breakpoint-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Watch Variables and Expressions while Debugging an LSP File (AutoLISP/VS Code)](To-Watch-Variables-and-Expressions-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Access the Call Stack while Debugging an LSP File (AutoLISP/VS Code)](To-Access-the-Call-Stack-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Evaluate Selected Expressions while Debugging an LSP File (AutoLISP/VS Code)](To-Evaluate-Selected-Expressions-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Evaluate AutoLISP Expressions in the Debug Console (AutoLISP/VS Code)](To-Evaluate-AutoLISP-Expressions-in-the-Debug-Console-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*