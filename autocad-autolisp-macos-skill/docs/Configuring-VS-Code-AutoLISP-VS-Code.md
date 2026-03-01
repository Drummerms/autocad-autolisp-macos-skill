# Configuring VS Code (AutoLISP/VS Code)

Before you start editing and debugging AutoLISP source (LSP) files, you will want to configure the AutoCAD AutoLISP Extension.

NOTE:Debugging is not available in AutoCAD LT.

When configuring the AutoCAD AutoLISP Extension, you can specify values for these settings:

* List format styles
* Code line indent styles
* Maximum characters per line
* Debug attach process and launch program (Not available in AutoCAD LT)

All settings except those related to debugging LSP files have default values.

## Configuring for Debug

The settings related to debugging are used to define debug configurations that allow VS Code and AutoCAD to communicate with
each other. The AutoCAD AutoLISP Extension supports these two debug configurations:

* *AutoLISP Debug Attach (attachlisp)* - A running instance of AutoCAD is identified before VS Code enters Debug mode
* *AutoLISP Debug Launch (launchlisp)* - A new instance of AutoCAD is launched before VS Code enters Debug mode

It is recommended to use the
attachlisp debug configuration when possible, this will save time from having to wait for AutoCAD to launch each time you want to debug
an LSP file. or information on setting up the debug configuration settings for the extension, see
[To Setup the AutoCAD AutoLISP Extension for Debug](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md).

NOTE:Starting with version 1.4.0 of the AutoCAD AutoLISP Extension, the use of a
*launch.json* file to define the extension's debug configurations has been deprecated. Debug configurations are now handled exclusively
as part of the extension's settings. For information on setting up the debug configuration settings for the extension, see
[To Setup the AutoCAD AutoLISP Extension for Debug](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md).

#### Topics in this section

* [To Setup the AutoCAD AutoLISP Extension for Debug (AutoLISP/VS Code)](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*