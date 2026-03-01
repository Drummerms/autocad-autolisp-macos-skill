# To Load an LSP File into AutoCAD while Debugging (AutoLISP/VS Code)

NOTE:Debugging is not available in AutoCAD LT.

When you start debugging, the AutoLISP source (LSP) file in the active editor window is automatically loaded into AutoCAD.
However, if you want to load other LSP files open in VS Code, you can load those files by doing the following:

1. In Visual Studio Code,
   [start debugging an AutoLISP source (LSP) file](To-Launch-and-Attach-an-Instance-of-AutoCAD-to-VS-Code-for-Debugging-AutoLISP-VS-Code.md).
2. While debugging, activate the editor window containing the LSP file you want to load into AutoCAD.
3. On the Status Bar, click Load Lisp.

   ![](../images/GUID-BE8E1CC8-705A-4456-B417-D059A2FA868E-low.png)

   NOTE:An LSP file can’t be reloaded after it has already been loaded during a debug session. If you need to make changes to a LSP
   file that you are currently debugging, stop debugging and make changes to the LSP file before you start a new debug session.

   TIP:If you need to debug multiple LSP files, it is recommended to load those files with the AutoLISP
   LOAD function in the LSP file that is in the active editor window before starting a new debug session.

#### Related Information

* [Configuring VS Code (AutoLISP/VS Code)](Configuring-VS-Code-AutoLISP-VS-Code.md)
* [To Launch and Attach an Instance of AutoCAD to VS Code for Debugging (AutoLISP/VS Code)](To-Launch-and-Attach-an-Instance-of-AutoCAD-to-VS-Code-for-Debugging-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*