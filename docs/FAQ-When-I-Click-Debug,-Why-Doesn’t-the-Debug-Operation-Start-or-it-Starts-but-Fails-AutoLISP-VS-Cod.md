# FAQ: When I Click Debug, Why Doesn’t the Debug Operation Start or it Starts but Fails? (AutoLISP/VS Code)

NOTE:Debugging is not available in AutoCAD LT.

There are several reasons why the Debug operation might not start. Here are some of the most common reasons why the Debug
operation might not start:

* *launch.json* file might not have been created or configured correctly
* *launch.json* file is placed in a workspace and not a folder
* Make sure the file you are trying to debug is of the LSP or MNL type; if you created a new file, make sure you save it with
  the appropriate file extension
* Make sure the LISPSYS system variable is set to 1 or 2, if you are running AutoCAD on Windows

If you have a
*launch.json* file in a folder,
launchlisp or
attachlisp might not be configured properly. Here are some of the things to look at:

* Path attribute of
  launchlisp
  + Doesn’t contain or contains an incorrect path to the AutoCAD executable, see
    [To Setup the AutoCAD AutoLISP Extension for Debug](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md)
  + Path isn’t specified as an absolute path to the AutoCAD executable
  + On Mac OS,
    '\\' is being used as a path separator instead of the expected
    '/'
* Process attribute of
  attachlisp
  + Doesn’t contain or contains the incorrect or case-sensitive name of the AutoCAD process

#### Related Information

* [Getting Started with Visual Studio Code (AutoLISP/VS Code)](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*