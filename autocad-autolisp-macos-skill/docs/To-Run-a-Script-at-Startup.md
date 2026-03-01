# To Run a Script at Startup

Windows
:   1. Click the Windows Start button ![](../images/ac.menuaro.gif) Windows System ![](../images/ac.menuaro.gif) Run.
    2. In the Run dialog box, do one of the following:
       * For AutoCAD, enter
         *acad*  **drawing\_name**  */b*  **script\_name**
       * For AutoCAD LT, enter
         *acadlt*  **drawing\_name**  */b*  **script\_name**

       To start a new file, instead of a drawing file name, enter the /t command line switch and the name of a template file:
       */t
       *template\_drawing**.

       To open a drawing file to a particular view, follow the drawing name with the /v command line switch and the name of the view:
       */v
       *view\_name**.

       The name of the script file must be the last parameter listed. The file extensions are optional.
    3. Click OK.

       The application opens the drawing and executes the commands in the script file. When the script has been completed, the Command
       prompt is displayed.

Mac OS
:   1. Click
       *local drive*![](../images/ac.menuaro.gif) Applications ![](../images/ac.menuaro.gif) Utilities ![](../images/ac.menuaro.gif) Terminal.
    2. In the Terminal window, do one of the following:
       * For AutoCAD, enter
         *AutoCAD
         *drawing\_name* -b
         *script\_name**
       * For AutoCAD LT, enter
         *"AutoCAD LT"
         *drawing\_name* -b
         *script\_name**

       NOTE:By default, the program executables can be located at:
       * *AutoCAD* -
         */Applications/Autodesk/<release>/AutoCAD.app/Contents/MacOS/AutoCAD*
       * *AutoCAD LT* -
         */Applications/Autodesk/AutoCAD LT.app/Contents/MacOS/AutoCAD LT*

       To start a new file, instead of opening an existing drawing file, enter the -t switch and the name of a template file:
       *-t
       *template\_drawing**.

       The name of the script file must be the last parameter listed. The file extensions are optional.
    3. Press Enter.

       The application opens the drawing and executes the commands in the script file. When the script has been completed, the Command
       prompt is displayed.

#### Related Concepts

* [About Running Scripts at Startup](About-Running-Scripts-at-Startup.md)
* [About Command Scripts](About-Command-Scripts.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*