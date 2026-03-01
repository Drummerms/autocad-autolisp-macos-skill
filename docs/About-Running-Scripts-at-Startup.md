# About Running Scripts at Startup

A script can be ran at startup using the /b (on Windows) or -b (on Mac OS) command line switch.

Suppose that every time you begin a new drawing, you turn on the grid, set the global linetype scale to 3.0, and set layer
0 as your current layer, with red as the color. You can do this using a drawing template, but you could do it instead with
the following script and store it in a text file called
*setup.scr*.

```
grid on
ltscale 3.0
layer set 0 color red 0
```

The first line turns on the grid. The second line sets the global scale for linetypes. The third line sets the current layer
to layer 0 and sets its default color to red. The application assumes that in a script you want to use the command line version
of the LAYER command rather than the palette version. The result is equivalent to entering
*-layer* at the Command prompt. The fourth line is blank, ending LAYER.

You can open a drawing and run a script at startup using one of the following techniques:

Windows
:   * In the Run dialog box, on the Start menu or Start screen, enter the necessary syntax.
    * In a Windows Command Prompt window, enter the necessary syntax.

Mac OS
:   * In a Terminal window, enter the necessary syntax.

## Syntax to Run a Script File

You use the /b (on Windows) or -b (on Mac OS) command line switch to run a script file on a new or existing drawing file when
the application starts up. This is done by using the following syntax:

* On Windows,

  ```
  executable_path drawing_name /b script_name
  ```

  You can also specify the view that is displayed when the drawing opens by using the /v command line switch and the view name.
  The /b command line switch and the script file must be the last parameter listed.
* On Mac OS,

  ```
  executable_path drawing_name -b script_name
  ```

NOTE:File names that contain embedded spaces must be enclosed in double quotes, for example,
"guest house".

Including the file extensions
*.exe/.app*,
*.dwg*,
*.dwt*, and
*.scr* is optional. If the script file cannot be found, the application reports that it cannot open the file.

NOTE:*This note applies to AutoCAD and AutoCAD LT for Windows only.* VBA (in AutoCAD only) and AutoLISP® files that are loaded at startup should check whether the program process is visible or invisible. If the program process
is invisible, the files should not be ran, because the program process may be performing background plotting or publishing
operations. To check for whether the program process is visible or invisible, you can use the
Visible property of the
Application object that is part of the AutoCAD ActiveX Automation API.

## Create a Drawing from a Template and Run a Script File

You can create a new drawing using the /t (on Windows) or -t (on Mac OS) command line switch with a specified drawing template
before running a script file. The following syntax creates a new drawing using the
*MyTemplate.dwt* file and then runs the
*script.scr* script after the drawing is created:

* On Windows,

  ```
  executable_path /t MyTemplate /b setup
  ```
* On Mac OS,

  ```
  executable_path -t MyTemplate -b setup
  ```

If you want to use the default template for the new drawing, you can omit the /t or -t command line switch and the template
file name.

NOTE:You can no longer use this method to start a new drawing and give it a name. Name the drawing when you save it.

#### Topics in this section

* [To Run a Script at Startup](To-Run-a-Script-at-Startup.md)

#### Related Tasks

* [To Run a Script at Startup](To-Run-a-Script-at-Startup.md)

#### Related Concepts

* [About Command Scripts](About-Command-Scripts.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*