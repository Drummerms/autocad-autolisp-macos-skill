# To Start the Program With Script

1. Click local drive ![](../images/ac.menuaro.gif) Applications ![](../images/ac.menuaro.gif) Utilities ![](../images/ac.menuaro.gif) Terminal.
2. In the Terminal window, enter
   AutoCAD drawing\_name -b script\_name

   NOTE:AutoCAD listed above is the path to the AutoCAD executable. By default it is located at:
   /Applications/Autodesk/AutoCAD <release>/AutoCAD <release>.app/Contents/MacOS/AutoCAD

   To start a new file, instead of a drawing file name, enter the
   -t switch and the name of a template file:
   -t template\_drawing.

   The name of the script file must be the last parameter listed. The file extensions are optional.
3. Press Enter.

   AutoCAD opens the drawing and executes the commands in the script file. When the script has been completed, the Command prompt
   is displayed.

NOTE:When using a switch option, you must follow the switch with a space and then the name of a file. For example, the following
entry starts the program from a folder named AutoCAD 2025 with the drawing template
*arch1.dwt* and executes a script
*filestartup.scr*.
"/Applications/Autodesk/AutoCAD 2025/AutoCAD 2025.app/Contents/MacOS/AutoCAD" -t /templates/arch1.dwt -b startup.scr

#### Related References

* [Command Line Switch Reference](Command-Line-Switch-Reference.md)

#### Related Concepts

* [About Customizing Startup](About-Customizing-Startup.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*